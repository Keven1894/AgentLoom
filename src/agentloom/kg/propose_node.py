"""propose_node.py — agent CLI for filing a candidate KG node.

Writes two files to agents/knowledge-graphs/proposals/:
  - <YYYYMMDD-HHMMSS>-<slug>.json — the candidate node payload
  - UPDATE_LOG_<YYYYMMDD>_proposal_<slug>.md — narrative + justification

Does NOT modify the canonical KG. Acceptance happens via accept_proposal.py
(after PR review).

Usage:
    python src/agentloom/kg/propose_node.py \
        --type knowledge \
        --slug time-format-conventions \
        --title "Time-format conventions for heterogeneous public data" \
        --justification "USGS GeoJSON uses epoch ms; OpenAQ ISO-8601; need a node so ingest skills know to convert." \
        --source-context "encountered while building D1 ingest, scripts/d1_ingest.py:42" \
        --target-role domain
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

from agentloom import REPO_ROOT as WORKSPACE
PROPOSALS_DIR = WORKSPACE / "agents" / "knowledge-graphs" / "proposals"

VALID_TYPES = {"knowledge", "skill", "behavior"}
VALID_ROLES = {"builder", "domain"}


def build_node_payload(args: argparse.Namespace) -> dict:
    role = args.target_role
    nid = f"{args.type}:{role}:{args.slug}"
    parent = args.parent or f"{args.type}:{role}:root"

    if args.type == "knowledge":
        # Nested data/relationships shape (matches integrity validator).
        return {
            "id": nid,
            "type": args.node_subtype or "concept",
            "data": {
                "title": args.title or args.slug.replace("-", " ").title(),
                "description": args.justification,
                "category": f"{role}-proposed",
                "path": args.path or f"docs/{role}/proposed/{args.slug}.md",
                "tags": [role, "proposed"],
            },
            "relationships": {
                "parent": parent,
                "children": [],
            },
        }

    if args.type == "skill":
        return {
            "id": nid,
            "type": args.node_subtype or "skill",
            "name": args.title or args.slug.replace("-", " ").title(),
            "category": args.category or f"{role}-proposed",
            "description": args.justification,
            "path": args.path or f"agents/skills/{role}/skill-{args.slug}.md",
            "parent": parent,
            "links": json.loads(args.links_json) if args.links_json else {},
        }

    # behavior
    return {
        "id": nid,
        "type": args.node_subtype or "rule",
        "name": args.title or args.slug.replace("-", " ").title(),
        "description": args.justification,
        "path": args.path or f"agents/behaviors/{role}/behavior-{args.slug}.md",
        "category": args.category or f"{role}-proposed",
        "priority": args.priority or "medium",
        "enforcement": args.enforcement or "soft",
        "parent": parent,
        "links": json.loads(args.links_json) if args.links_json else {},
    }


def build_update_log(args: argparse.Namespace, node: dict, ts: str) -> str:
    return f"""# UPDATE_LOG: Proposal — {node.get('name') or node.get('data', {}).get('title') or args.slug}

**Date**: {ts[:10]}
**Author (agent)**: {args.author}
**Slug**: {args.slug}
**Proposed node type**: {args.type}
**Target graph**: {args.target_role}-{args.type}

---

## Justification (the "why")

{args.justification}

## Source context

{args.source_context}

## Proposed node

```json
{json.dumps(node, indent=2, ensure_ascii=False)}
```

## Reviewer notes

{args.reviewer_notes or '_(none)_'}
"""


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--type", required=True, choices=sorted(VALID_TYPES))
    p.add_argument("--slug", required=True,
                   help="kebab-case identifier; the node id becomes <type>:<role>:<slug>")
    p.add_argument("--target-role", default="domain", choices=sorted(VALID_ROLES))
    p.add_argument("--title", help="Human-readable title (defaults to slug-titlecased)")
    p.add_argument("--justification", required=True,
                   help="2-4 sentence rationale: what triggered this, what gap it fills")
    p.add_argument("--source-context", required=True,
                   help="Where this came from: task / file / line / conversation")
    p.add_argument("--parent", help="Override parent id (default: <type>:<role>:root)")
    p.add_argument("--node-subtype",
                   help="The 'type' field of the node (e.g. concept|protocol|skill|rule)")
    p.add_argument("--path", help="Override the path field")
    p.add_argument("--category", help="Skill/behavior category")
    p.add_argument("--priority", choices=["low", "medium", "high", "critical"],
                   help="Behavior priority")
    p.add_argument("--enforcement", choices=["hard", "test", "process", "soft"],
                   help="Behavior enforcement tier")
    p.add_argument("--links-json", default="",
                   help="JSON-encoded links dict, e.g. '{\"related\":[\"id-x\"]}'")
    p.add_argument("--author", default="builder-agent",
                   help="Agent name (or 'human-<who>' for human-filed proposals)")
    p.add_argument("--reviewer-notes", default="",
                   help="Optional notes for the human reviewer")
    args = p.parse_args()

    PROPOSALS_DIR.mkdir(parents=True, exist_ok=True)

    now = datetime.now()
    ts_compact = now.strftime("%Y%m%d-%H%M%S")
    ts_iso = now.strftime("%Y-%m-%d")

    node = build_node_payload(args)
    log = build_update_log(args, node, ts_iso)

    json_path = PROPOSALS_DIR / f"{ts_compact}-{args.slug}.json"
    log_path = PROPOSALS_DIR / f"UPDATE_LOG_{ts_iso.replace('-', '')}_proposal_{args.slug}.md"

    if json_path.exists():
        print(f"[ERROR] Proposal already exists: {json_path.name}")
        return 1

    json_path.write_text(json.dumps(node, indent=2, ensure_ascii=False) + "\n",
                         encoding="utf-8")
    log_path.write_text(log, encoding="utf-8")

    print(f"[OK] Proposal filed:")
    print(f"  payload : {json_path.relative_to(WORKSPACE)}")
    print(f"  log     : {log_path.relative_to(WORKSPACE)}")
    print()
    print(f"Proposed id: {node['id']}")
    print(f"Target graph: agents/knowledge-graphs/{args.target_role}-"
          f"{'knowledge-graph' if args.type == 'knowledge' else args.type + 's-graph'}.json")
    print()
    print("Next steps:")
    print(f"  1. (human) review the JSON + UPDATE_LOG")
    print(f"  2. (human) python src/agentloom/kg/accept_proposal.py "
          f"--proposal {json_path.name}")
    print(f"  3. (human) commit the canonical KG mutation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
