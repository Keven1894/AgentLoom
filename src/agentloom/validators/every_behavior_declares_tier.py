"""every-behavior-declares-tier — Tier A validator.

Behavior MD: agents/behaviors/builder/behavior-every-behavior-declares-tier.md

Checks: every node in builder-behaviors.json + domain-behaviors.json whose
'type' is 'rule' has an 'enforcement' field with value in {hard, test,
process, soft}.

Exit 0 iff all pass. Exit 1 on any violation. Exit 2 on missing KG file.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from agentloom import REPO_ROOT as WORKSPACE
TARGETS = [
    WORKSPACE / "agents" / "knowledge-graphs" / "builder-behaviors-graph.json",
    WORKSPACE / "agents" / "knowledge-graphs" / "domain-behaviors-graph.json",
]

VALID_TIERS = {"hard", "test", "process", "soft"}
EXEMPT_TYPES = {"root", "category"}


def check_one(node: dict) -> list[str]:
    if node.get("type") in EXEMPT_TYPES:
        return []
    enforcement = node.get("enforcement")
    if enforcement is None:
        return ["missing 'enforcement' field (must be hard|test|process|soft)"]
    if enforcement not in VALID_TIERS:
        return [
            f"invalid 'enforcement' value: {enforcement!r} "
            f"(must be one of {sorted(VALID_TIERS)})"
        ]
    return []


def main() -> int:
    n_violations = 0
    n_checked = 0
    n_exempt = 0
    for f in TARGETS:
        if not f.exists():
            print(f"[ERROR] target KG file missing: {f.relative_to(WORKSPACE)}")
            return 2
        kg = json.loads(f.read_text(encoding="utf-8"))
        for node in kg.get("behaviors", []):
            if node.get("type") in EXEMPT_TYPES:
                n_exempt += 1
                continue
            n_checked += 1
            for msg in check_one(node):
                print(f"  [VIOLATION] {f.name} :: {node.get('id', '?')} :: {msg}")
                n_violations += 1
    print(
        f"\nChecked {n_checked} behavior node(s); skipped {n_exempt} root/category; "
        f"{n_violations} violation(s)."
    )
    return 0 if n_violations == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
