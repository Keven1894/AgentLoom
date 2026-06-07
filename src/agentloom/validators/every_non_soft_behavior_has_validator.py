"""every-non-soft-behavior-has-validator — Tier A validator.

Behavior MD: agents/behaviors/builder/behavior-every-non-soft-behavior-has-validator.md

Checks: every behavior node with enforcement != 'soft' has links.validator
pointing to an existing Python file under the repo.

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

EXEMPT_TYPES = {"root", "category"}


def check_one(node: dict) -> list[str]:
    if node.get("type") in EXEMPT_TYPES:
        return []
    enforcement = node.get("enforcement")
    if enforcement == "soft" or enforcement is None:
        # 'soft' is exempt; missing is a different behavior's job
        return []
    links = node.get("links") or {}
    validators = links.get("validator")
    # Normalize: schema enforces array, but accept str for forward-compat too.
    if isinstance(validators, str):
        validators = [validators]
    if not isinstance(validators, list) or not validators:
        return [
            f"missing links.validator (enforcement={enforcement!r} requires "
            f"a validator path)"
        ]
    out = []
    for v in validators:
        if not isinstance(v, str) or not v.strip():
            out.append(f"links.validator entry is empty or non-string: {v!r}")
            continue
        if not (WORKSPACE / v).exists():
            out.append(f"links.validator points to non-existent file: {v}")
    return out


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
            if (
                node.get("type") in EXEMPT_TYPES
                or node.get("enforcement") == "soft"
            ):
                n_exempt += 1
                continue
            n_checked += 1
            for msg in check_one(node):
                print(f"  [VIOLATION] {f.name} :: {node.get('id', '?')} :: {msg}")
                n_violations += 1
    print(
        f"\nChecked {n_checked} non-soft behavior(s); skipped {n_exempt} "
        f"soft/root/category; {n_violations} violation(s)."
    )
    return 0 if n_violations == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
