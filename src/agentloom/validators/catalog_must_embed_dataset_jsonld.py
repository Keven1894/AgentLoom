"""catalog-must-embed-dataset-jsonld — Tier A validator.

Behavior MD: agents/behaviors/builder/behavior-catalog-must-embed-dataset-jsonld.md

Checks: every starter/<app>/index.html contains at least one
<script type="application/ld+json"> block whose JSON parses, has
@context=schema.org and @type=Dataset, and includes the minimum
required Schema.org Dataset fields.

Exempt files: those containing the literal HTML comment
    <!-- jsonld-discovery: bootstrapping -->

Exit 0 iff all targets pass. Exit 1 on violation. Exit 2 on missing-targets
sentinel mismatch.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from agentloom import REPO_ROOT as WORKSPACE
EXEMPT_MARKER = "<!-- jsonld-discovery: bootstrapping -->"

REQUIRED_FIELDS = [
    "name",
    "description",
    "url",
    "license",
    "creator",
    "distribution",
    "dateModified",
]

VALID_CONTEXTS = {"https://schema.org/", "http://schema.org/", "https://schema.org", "http://schema.org"}

JSONLD_PATTERN = re.compile(
    r'<script\b[^>]*\btype\s*=\s*["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.DOTALL | re.IGNORECASE,
)


def _find_dataset(parsed: object) -> dict | None:
    if isinstance(parsed, dict):
        if parsed.get("@type") == "Dataset" and parsed.get("@context") in VALID_CONTEXTS:
            return parsed
        graph = parsed.get("@graph")
        if isinstance(graph, list):
            for item in graph:
                if isinstance(item, dict) and item.get("@type") == "Dataset":
                    item.setdefault("@context", parsed.get("@context"))
                    if item.get("@context") in VALID_CONTEXTS:
                        return item
    elif isinstance(parsed, list):
        for item in parsed:
            ds = _find_dataset(item)
            if ds is not None:
                return ds
    return None


def check_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    if EXEMPT_MARKER in text:
        return []

    blocks = JSONLD_PATTERN.findall(text)
    if not blocks:
        return ['no <script type="application/ld+json"> block found.']

    parse_errors: list[str] = []
    dataset: dict | None = None
    for raw in blocks:
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError as e:
            parse_errors.append(f"JSON-LD block failed to parse: {e}")
            continue
        ds = _find_dataset(parsed)
        if ds is not None:
            dataset = ds
            break

    if dataset is None:
        if parse_errors:
            return parse_errors + [
                'no JSON-LD object with @context=schema.org and @type=Dataset.'
            ]
        return ['no JSON-LD object with @context=schema.org and @type=Dataset.']

    missing: list[str] = []
    for field in REQUIRED_FIELDS:
        v = dataset.get(field)
        if v is None or v == "" or v == [] or v == {}:
            missing.append(field)
    if missing:
        return [f"Dataset missing required fields: {', '.join(missing)}"]

    return []


def main() -> int:
    starter_dir = WORKSPACE / "starter"
    if not starter_dir.exists():
        print(f"[INFO] {starter_dir.relative_to(WORKSPACE)} not found — nothing to check.")
        return 0

    targets = sorted(starter_dir.glob("*/index.html"))
    if not targets:
        if any(starter_dir.iterdir()):
            print(f"[ERROR] starter/ has subdirs but no */index.html files.")
            return 2
        return 0

    n_violations = 0
    n_checked = 0
    n_exempt = 0
    for f in targets:
        rel = f.relative_to(WORKSPACE).as_posix()
        text = f.read_text(encoding="utf-8")
        if EXEMPT_MARKER in text:
            n_exempt += 1
            print(f"  [EXEMPT] {rel} :: bootstrapping marker present")
            continue
        n_checked += 1
        for msg in check_file(f):
            print(f"  [VIOLATION] {rel} :: {msg}")
            n_violations += 1

    print(
        f"\nChecked {n_checked} catalog file(s); skipped {n_exempt} bootstrapping; "
        f"{n_violations} violation(s)."
    )
    return 0 if n_violations == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
