# Validator Authoring Guide

**Node ID**: `knowledge:builder:validator-authoring-guide`
**Type**: guide
**Category**: builder-meta
**Created**: 2026-05-18

---

## What a validator is

A validator is a Python script that checks one specific behavior. It's the **executable** in "executable validator" — the thing that turns a soft instruction ("agents should validate inputs") into a hard contract that fails CI when violated.

Every behavior with `enforcement != 'soft'` ships a validator. The behavior MD describes the rule; the validator script enforces it.

---

## Tier model

| Tier | Where it runs | Enforces | Cost to author |
| --- | --- | --- | --- |
| **A — Hard / AST / regex** | Static analysis on source files or KG JSONs at commit / pre-CI time | Structural invariants — fields exist, IDs are unique, files referenced by `path` exist on disk | Low (tens of LOC) |
| **B — Test-time** | Pytest fixture during test runs | Runtime invariants — function returns valid CRS, parsed timestamps in valid range | Medium (small test suite) |
| **C — Process / DB / git-state** | CI step or pre-commit hook checking external state | Workflow invariants — every PR has linked plan, every accepted proposal has UPDATE_LOG, no schema drift | Higher (orchestration glue) |

For Phase 1 we focus on Tier A only (cheapest, fastest workshop demo). Tiers B and C are introduced in Phase 5.

---

## Anatomy of a Tier-A validator (template)

A working Tier-A validator is < 50 lines. Copy this template:

```python
"""<Behavior name> — Tier A validator.

Behavior MD: agents/behaviors/builder/behavior-<slug>.md

Checks: <one-line invariant statement>.

Exit code 0 iff all targeted nodes/files satisfy the invariant.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent.parent

# Files this validator inspects
TARGETS = [
    WORKSPACE / "agents" / "knowledge-graphs" / "builder-skills-graph.json",
    WORKSPACE / "agents" / "knowledge-graphs" / "domain-skills-graph.json",
]


def check_one(node: dict, source_file: Path) -> list[str]:
    """Return list of violation messages for a single node. Empty list = OK."""
    violations = []
    # ... your actual check logic here ...
    return violations


def main() -> int:
    n_violations = 0
    n_checked = 0
    for f in TARGETS:
        kg = json.loads(f.read_text(encoding="utf-8"))
        # array key auto-detect or hardcode
        nodes = kg.get("skills") or kg.get("nodes") or kg.get("behaviors") or []
        for node in nodes:
            n_checked += 1
            for msg in check_one(node, f):
                print(f"  [VIOLATION] {f.name} :: {node.get('id', '?')} :: {msg}")
                n_violations += 1
    print(f"\nChecked {n_checked} node(s); {n_violations} violation(s).")
    return 0 if n_violations == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
```

---

## Five rules of thumb

1. **One validator, one invariant.** If you find yourself adding `if condition_A: ... elif condition_B: ...`, split into two validators.
2. **Print, don't log.** Validators run in CI / agent shells where stdout is the audit trail. No logging frameworks.
3. **Exit 0 or 1, nothing else.** CI / pre-commit hooks key off exit codes.
4. **Fail loud on missing files.** If a TARGETS file doesn't exist, exit 2 (not 0) — silent skipping hides drift.
5. **Idempotent — running twice is safe.** Validators must not mutate state.

---

## Naming + placement

- Script: `src/agentloom/validators/<slug_with_underscores>.py` — the slug matches the behavior MD's `links.validator` field
- Entry in behavior JSON node: `links.validator` = relative path from repo root
- Pre-commit hook (Phase 5+): adds `python -m agentloom.validators.<slug>` to a per-commit script

---

## How `make kg-validate` interacts with validators

`make kg-validate` runs **only the schema + integrity validators** (the structural ones). It does NOT run the per-behavior validators. Those are a separate layer:

```bash
# Run all per-behavior Tier-A validators
python -m agentloom.validators.run_all
# or: make validate-all
```

Phase 5 will wire this into a single `make validate-behaviors` target. For now, run them individually or in a loop.

---

## See also

- `kg-node-schema.md` — the field shapes validators check
- `governance-tiers.md` — the broader Tier-A/B/C model and when to use which
- Real examples: `src/agentloom/validators/every_skill_must_have_script.py`, `every_behavior_declares_tier.py`, `every_non_soft_behavior_has_validator.py`, `kg_node_ids_are_unique.py`
