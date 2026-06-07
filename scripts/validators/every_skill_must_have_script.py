"""every-skill-must-have-script — Tier A validator.

Behavior MD: agents/behaviors/builder/behavior-every-skill-must-have-script.md

Checks: every node in builder-skills-graph.json + domain-skills-graph.json
whose 'type' is 'skill' has a non-empty 'path' field, and the file at that
path exists on disk.

Exit 0 iff all targeted nodes pass. Exit 1 if any violation. Exit 2 if a
target KG file is missing (silent skip would hide drift).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]

TARGETS = [
    WORKSPACE / "agents" / "knowledge-graphs" / "builder-skills-graph.json",
    WORKSPACE / "agents" / "knowledge-graphs" / "domain-skills-graph.json",
]

EXEMPT_TYPES = {"root", "category"}


def check_one(node: dict) -> list[str]:
    if node.get("type") in EXEMPT_TYPES:
        return []
    path = node.get("path")
    if not isinstance(path, str) or not path.strip():
        return ["empty or missing 'path' field (type=skill requires path to MD)"]
    abs_path = WORKSPACE / path
    if not abs_path.exists():
        return [f"'path' references non-existent file: {path}"]
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
        for node in kg.get("skills", []):
            if node.get("type") in EXEMPT_TYPES:
                n_exempt += 1
                continue
            n_checked += 1
            for msg in check_one(node):
                print(f"  [VIOLATION] {f.name} :: {node.get('id', '?')} :: {msg}")
                n_violations += 1
    print(
        f"\nChecked {n_checked} skill node(s); skipped {n_exempt} root/category; "
        f"{n_violations} violation(s)."
    )
    return 0 if n_violations == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
