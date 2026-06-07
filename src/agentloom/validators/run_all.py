"""run_all.py — execute every Tier-A validator under src/agentloom/validators/.

Skips this file itself. Each validator is a standalone Python script that
exits 0 on PASS, non-zero on FAIL. We aggregate and report.

Usage:
    python src/agentloom/validators/run_all.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
THIS = Path(__file__).resolve()


def main() -> int:
    scripts = sorted(p for p in HERE.glob("*.py")
                     if p.resolve() != THIS and not p.name.startswith("_"))
    failures: list[str] = []
    for s in scripts:
        print(f"\n{'#' * 60}\n# {s.name}\n{'#' * 60}")
        result = subprocess.run([sys.executable, str(s)])
        if result.returncode != 0:
            failures.append(s.name)
    print()
    if failures:
        print(f"FAIL — {len(failures)} validator(s) failed: {failures}")
        return 1
    print(f"PASS — all {len(scripts)} Tier-A validator(s) succeeded.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
