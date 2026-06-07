"""Run both KG validators sequentially. Exit 0 iff both pass.

Cross-platform alternative to `make kg-validate`. Useful for Windows
attendees who don't have `make` on PATH.

Usage:
    python scripts/kg/validate_all.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

CHECKS = [
    ("Schema validation", [sys.executable, str(HERE / "validate_schemas.py")]),
    ("Relational integrity (knowledge graphs)", [sys.executable, str(HERE / "validate_kg_integrity.py"), "--all"]),
]


def main() -> int:
    failures = []
    for label, cmd in CHECKS:
        print(f"\n{'#' * 60}")
        print(f"# {label}")
        print(f"{'#' * 60}")
        result = subprocess.run(cmd)
        if result.returncode != 0:
            failures.append(label)
    print()
    if failures:
        print(f"FAIL — {len(failures)} validator(s) failed: {failures}")
        return 1
    print("PASS — all KG validators succeeded.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
