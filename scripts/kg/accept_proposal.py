"""accept_proposal.py — human CLI for promoting a proposal into the canonical KG.

Reads agents/knowledge-graphs/proposals/<file>.json, derives the target graph
from the node's id (`<type>:<role>:<slug>`), backs up the target file,
inserts the node directly via JSON edit (using the array-key convention
matching schema), then runs both validators (schema + integrity) plus the
Tier-A behavior validators.

On success: deletes the proposal JSON; KEEPS the UPDATE_LOG (audit trail).
On failure: rolls back the canonical file from the backup; leaves proposal
intact so the agent can retry.

Usage:
    python scripts/kg/accept_proposal.py --proposal 20260518-141500-time-format-conventions.json

    # dry-run: show what would happen, don't write
    python scripts/kg/accept_proposal.py --proposal <file> --dry-run

    # reject instead: deletes the proposal JSON, keeps the UPDATE_LOG
    # (you should also write a UPDATE_LOG_<date>_reject_<slug>.md by hand)
    python scripts/kg/accept_proposal.py --proposal <file> --reject "<reason>"
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
KG_DIR = WORKSPACE / "agents" / "knowledge-graphs"
PROPOSALS_DIR = KG_DIR / "proposals"
SCRIPTS_KG = WORKSPACE / "scripts" / "kg"
SCRIPTS_VALIDATORS = WORKSPACE / "scripts" / "validators"


def derive_target(node: dict) -> tuple[Path, str]:
    """From node id like 'knowledge:domain:foo', return (target file, array key)."""
    nid = node.get("id", "")
    parts = nid.split(":")
    if len(parts) < 3:
        raise SystemExit(f"[ERROR] node id {nid!r} not in <type>:<role>:<slug> form")
    ntype, role = parts[0], parts[1]
    if role not in ("builder", "domain"):
        raise SystemExit(f"[ERROR] unknown role {role!r}")
    if ntype == "knowledge":
        return KG_DIR / f"{role}-knowledge-graph.json", "nodes"
    if ntype == "skill":
        return KG_DIR / f"{role}-skills-graph.json", "skills"
    if ntype == "behavior":
        return KG_DIR / f"{role}-behaviors-graph.json", "behaviors"
    raise SystemExit(f"[ERROR] unknown node type {ntype!r}")


def insert_node(target: Path, array_key: str, node: dict) -> None:
    kg = json.loads(target.read_text(encoding="utf-8"))
    items = kg.setdefault(array_key, [])
    if any(n.get("id") == node["id"] for n in items):
        raise SystemExit(f"[ERROR] node id {node['id']!r} already exists in "
                         f"{target.name}")
    items.append(node)
    # Wire the parent's children list (best-effort; skip silently if no parent).
    parent_id = (node.get("relationships", {}).get("parent")
                 if "relationships" in node else node.get("parent"))
    if parent_id:
        for n in items:
            if n.get("id") == parent_id and "relationships" in n:
                children = n["relationships"].setdefault("children", [])
                if node["id"] not in children:
                    children.append(node["id"])
    kg.setdefault("metadata", {})["last_updated"] = datetime.now().strftime("%Y-%m-%d")
    kg["metadata"]["total_nodes"] = len(items)
    target.write_text(json.dumps(kg, indent=2, ensure_ascii=False) + "\n",
                      encoding="utf-8")


def run_validators() -> tuple[bool, str]:
    """Run KG schema+integrity then Tier-A behavior validators. Return (ok, log)."""
    out_lines = []
    for label, cmd in [
        ("KG validators", [sys.executable, str(SCRIPTS_KG / "validate_all.py")]),
        ("Behavior validators", [sys.executable, str(SCRIPTS_VALIDATORS / "run_all.py")]),
    ]:
        out_lines.append(f"--- {label} ---")
        result = subprocess.run(cmd, capture_output=True, text=True)
        out_lines.append(result.stdout[-800:] if result.stdout else "(no stdout)")
        if result.returncode != 0:
            out_lines.append(f"[FAIL] {label} exit={result.returncode}")
            if result.stderr:
                out_lines.append(result.stderr[-400:])
            return False, "\n".join(out_lines)
    return True, "\n".join(out_lines)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--proposal", required=True,
                   help="Filename inside agents/knowledge-graphs/proposals/")
    p.add_argument("--dry-run", action="store_true",
                   help="Show what would happen, do not modify canonical KG")
    p.add_argument("--reject", help="Reject reason (deletes proposal JSON, keeps UPDATE_LOG)")
    args = p.parse_args()

    proposal_path = PROPOSALS_DIR / args.proposal
    if not proposal_path.exists():
        print(f"[ERROR] proposal not found: {proposal_path.relative_to(WORKSPACE)}")
        return 1

    if args.reject:
        print(f"REJECT: {proposal_path.name}")
        print(f"Reason: {args.reject}")
        if not args.dry_run:
            proposal_path.unlink()
            print(f"[OK] Removed proposal JSON. UPDATE_LOG kept (audit trail).")
            print(f"     Recommend writing UPDATE_LOG_<date>_reject_<slug>.md "
                  f"in {PROPOSALS_DIR.relative_to(WORKSPACE)}/.")
        return 0

    node = json.loads(proposal_path.read_text(encoding="utf-8"))
    target, array_key = derive_target(node)
    if not target.exists():
        print(f"[ERROR] target KG missing: {target.relative_to(WORKSPACE)}")
        return 1

    print(f"ACCEPT: {proposal_path.name}")
    print(f"  node id     : {node['id']}")
    print(f"  target file : {target.relative_to(WORKSPACE)}")
    print(f"  array key   : {array_key}")
    if args.dry_run:
        print("[DRY-RUN] No files modified.")
        return 0

    # Backup
    backup = target.with_suffix(target.suffix + ".bak_accept")
    shutil.copy2(target, backup)

    try:
        insert_node(target, array_key, node)
    except SystemExit as e:
        print(str(e))
        shutil.copy2(backup, target)
        backup.unlink()
        return 1

    print(f"  inserted    : OK (backup at {backup.name})")
    print()
    print("Running validators...")
    ok, log = run_validators()
    print(log)

    if not ok:
        print()
        print("[FAIL] Validators rejected the new node. Rolling back canonical KG.")
        shutil.copy2(backup, target)
        backup.unlink()
        print(f"[OK] Rolled back. Proposal kept at {proposal_path.name} for retry.")
        return 1

    backup.unlink()
    proposal_path.unlink()
    print()
    print(f"[OK] Accepted. Proposal JSON deleted.")
    print(f"     UPDATE_LOG kept at: agents/knowledge-graphs/proposals/UPDATE_LOG_*_"
          f"proposal_*.md")
    print(f"     Next: git add -A && git commit -m 'KG: accept {node['id']}'")
    return 0


if __name__ == "__main__":
    sys.exit(main())
