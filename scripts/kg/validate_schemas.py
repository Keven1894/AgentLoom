"""Validate every KG JSON file against its JSON Schema.

Sibling tool to `validate_kg_integrity.py`. The integrity validator does
relational checks (parent/child consistency, orphan detection, cycles) on
knowledge graphs only. This tool does *structural* validation (required
fields, types, ID patterns) on all 6 graph files using jsonschema.

Usage:
    python scripts/kg/validate_schemas.py             # validate all 6
    python scripts/kg/validate_schemas.py --only builder-skills

Exit code 0 iff every targeted graph passes its schema.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

import jsonschema

WORKSPACE = Path(__file__).resolve().parent.parent.parent
KG_DIR = WORKSPACE / "agents" / "knowledge-graphs"
SCHEMAS_DIR = Path(__file__).resolve().parent / "lib" / "schemas"


@dataclass
class Target:
    name: str            # e.g. "builder-skills"
    kg_file: Path
    schema_file: Path


# Mapping: graph file → schema file. The 3 schema files cover both roles.
TARGETS = [
    Target("builder-skills", KG_DIR / "builder-skills-graph.json", SCHEMAS_DIR / "skills-graph.schema.json"),
    Target("builder-knowledge", KG_DIR / "builder-knowledge-graph.json", SCHEMAS_DIR / "knowledge-graph.schema.json"),
    Target("builder-behaviors", KG_DIR / "builder-behaviors-graph.json", SCHEMAS_DIR / "behaviors-graph.schema.json"),
    Target("domain-skills", KG_DIR / "domain-skills-graph.json", SCHEMAS_DIR / "skills-graph.schema.json"),
    Target("domain-knowledge", KG_DIR / "domain-knowledge-graph.json", SCHEMAS_DIR / "knowledge-graph.schema.json"),
    Target("domain-behaviors", KG_DIR / "domain-behaviors-graph.json", SCHEMAS_DIR / "behaviors-graph.schema.json"),
    Target("master", KG_DIR / "master-graph.json", SCHEMAS_DIR / "master-graph.schema.json"),
]


def validate_one(t: Target) -> tuple[bool, list[str]]:
    if not t.kg_file.exists():
        return False, [f"KG file missing: {t.kg_file}"]
    if not t.schema_file.exists():
        return False, [f"Schema file missing: {t.schema_file}"]
    try:
        kg = json.loads(t.kg_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return False, [f"JSON parse error: {e}"]
    try:
        schema = json.loads(t.schema_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return False, [f"Schema parse error: {e}"]
    validator = jsonschema.Draft7Validator(schema)
    errors = sorted(validator.iter_errors(kg), key=lambda e: e.path)
    if not errors:
        return True, []
    msgs = []
    for err in errors:
        path = "/".join(str(p) for p in err.path) or "(root)"
        msgs.append(f"  at {path}: {err.message}")
    return False, msgs


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--only", nargs="*", help="Subset of target names")
    args = p.parse_args()

    targets = TARGETS
    if args.only:
        bad = [n for n in args.only if n not in {t.name for t in TARGETS}]
        if bad:
            print(f"Unknown target(s): {bad}")
            print(f"Valid: {[t.name for t in TARGETS]}")
            return 2
        targets = [t for t in TARGETS if t.name in args.only]

    print(f"\n=== Schema validation — {len(targets)} graph(s) ===\n")
    width = max(len(t.name) for t in targets)
    n_fail = 0
    for t in targets:
        ok, msgs = validate_one(t)
        status = "OK  " if ok else "FAIL"
        print(f"[{status}] {t.name:<{width}}  {t.kg_file.name}")
        if not ok:
            n_fail += 1
            for m in msgs:
                print(m)
    print()
    if n_fail:
        print(f"{n_fail}/{len(targets)} target(s) failed schema validation.")
        return 1
    print(f"All {len(targets)} target(s) passed schema validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
