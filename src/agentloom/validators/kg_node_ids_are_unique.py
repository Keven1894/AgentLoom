"""kg-node-ids-are-unique — Tier A validator.

Behavior MD: agents/behaviors/builder/behavior-kg-node-ids-are-unique.md

Checks: globally across all 6 active KG files, no two nodes share an id.

Exit 0 iff all ids are globally unique. Exit 1 on any duplicate. Exit 2 on
missing KG file.
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

from agentloom import REPO_ROOT as WORKSPACE
KG_DIR = WORKSPACE / "agents" / "knowledge-graphs"

TARGETS = [
    KG_DIR / "builder-skills-graph.json",
    KG_DIR / "builder-knowledge-graph.json",
    KG_DIR / "builder-behaviors-graph.json",
    KG_DIR / "domain-skills-graph.json",
    KG_DIR / "domain-knowledge-graph.json",
    KG_DIR / "domain-behaviors-graph.json",
]

ARRAY_KEYS = ("skills", "behaviors", "nodes", "documents")


def collect_ids(file_path: Path) -> list[tuple[str, str]]:
    """Return list of (id, source_file_name) tuples for every node in this file."""
    kg = json.loads(file_path.read_text(encoding="utf-8"))
    out = []
    for key in ARRAY_KEYS:
        for node in kg.get(key, []):
            nid = node.get("id")
            if isinstance(nid, str) and nid.strip():
                out.append((nid, file_path.name))
    return out


def main() -> int:
    seen: dict[str, list[str]] = defaultdict(list)
    n_total = 0
    for f in TARGETS:
        if not f.exists():
            print(f"[ERROR] target KG file missing: {f.relative_to(WORKSPACE)}")
            return 2
        for nid, source in collect_ids(f):
            seen[nid].append(source)
            n_total += 1

    duplicates = {nid: srcs for nid, srcs in seen.items() if len(srcs) > 1}
    n_violations = len(duplicates)

    if duplicates:
        for nid, srcs in sorted(duplicates.items()):
            print(f"  [VIOLATION] duplicate id {nid!r} appears in: {', '.join(srcs)}")

    print(
        f"\nChecked {n_total} node id(s) across {len(TARGETS)} KG file(s); "
        f"{n_violations} duplicate id(s)."
    )
    return 0 if n_violations == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
