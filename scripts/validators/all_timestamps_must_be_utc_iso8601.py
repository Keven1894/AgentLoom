"""all-timestamps-must-be-utc-iso8601 — Tier B validator (test-time).

Behavior MD: agents/behaviors/domain/behavior-all-timestamps-must-be-utc-iso8601.md

Walks every JSON file under dist/ (ingest skill outputs) plus committed
snapshots already known to be normalized, and verifies that any value
whose key looks like a timestamp matches the strict UTC ISO-8601 pattern
^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?Z$.

Tier B (test-time) — runs against ingest *outputs*, not source files. If
no normalized output files exist yet (Phase 2 hasn't run any ingest), the
validator exits 0 (no work to do). When ingest skills start emitting
output, every timestamp must conform.

Exit codes:
  0 — all timestamps OK (or no output files to check)
  1 — at least one violation
  2 — internal error
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

WORKSPACE = Path(__file__).resolve().parents[2]

# Globs of files to inspect. Limit to known ingest outputs so we don't
# false-positive on raw upstream snapshots whose dialects we accept on input.
INSPECT_GLOBS = [
    "dist/*-normalized.iso.json",  # final post-conversion output
    "dist/d?-normalized.iso.json",
]

TS_KEY_PATTERN = re.compile(
    r"^(time|updated|fetched_at|generated|timestamp|datetime|date_time|"
    r"last_updated|.*_at|.*_time)$",
    re.IGNORECASE,
)
ISO_UTC_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z$")


def _walk(obj: Any, path: str, violations: list[str]) -> None:
    if isinstance(obj, dict):
        for k, v in obj.items():
            here = f"{path}.{k}" if path else k
            if isinstance(k, str) and TS_KEY_PATTERN.match(k):
                if v is None:
                    continue  # null is allowed
                if not isinstance(v, str):
                    violations.append(
                        f"{here}: value is non-string ({type(v).__name__}), "
                        f"expected ISO-8601 UTC string. Got: {v!r}"
                    )
                elif not ISO_UTC_PATTERN.match(v):
                    violations.append(
                        f"{here}: {v!r} does not match ^\\d{{4}}-\\d{{2}}-\\d{{2}}T"
                        f"\\d{{2}}:\\d{{2}}:\\d{{2}}(\\.\\d+)?Z$"
                    )
            _walk(v, here, violations)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            _walk(item, f"{path}[{i}]", violations)


def main() -> int:
    files = []
    for glob in INSPECT_GLOBS:
        files.extend(WORKSPACE.glob(glob))

    if not files:
        print(
            "[OK] No normalized ingest output found under dist/. "
            "Tier-B check is vacuously satisfied (no timestamps emitted yet)."
        )
        return 0

    n_violations = 0
    for f in files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except Exception as exc:
            print(f"  [ERROR] {f.relative_to(WORKSPACE)}: {exc}")
            return 2
        violations: list[str] = []
        _walk(data, "", violations)
        for v in violations:
            print(f"  [VIOLATION] {f.relative_to(WORKSPACE)} :: {v}")
            n_violations += 1

    print(
        f"\nChecked {len(files)} normalized output file(s); "
        f"{n_violations} violation(s)."
    )
    return 0 if n_violations == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
