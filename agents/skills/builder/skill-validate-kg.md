# Skill: Validate KG

**ID**: `skill:builder:validate-kg`
**Category**: kg-tools
**Priority**: critical
**Created**: 2026-05-18

---

## Purpose

Run both KG validators (schema + integrity) over all 6 active graphs in one command. This is the gate every KG mutation must pass.

The skill is a thin wrapper over `scripts/kg/validate_all.py`, which itself orchestrates `validate_kg_schemas.py` and `validate_kg_integrity.py`.

---

## When to use

**Required**:
- Before committing any change to `agents/knowledge-graphs/`
- After merging a KG-mutating PR (post-merge sanity check)
- As part of CI for any branch

**Recommended**:
- Daily during Phase 2 builder agent work — frequent runs catch drift early
- After running any migration script (`scripts/migrations/*.py`)

---

## How to run

```bash
# Repo root
python scripts/kg/validate_all.py
# or
make kg-validate
```

Exit codes:
- `0` — all 6 graphs pass schema + integrity
- `1` — at least one violation (output details which file + which check)

The two validators run in sequence. If schema fails, integrity is skipped (because integrity assumes schema-valid input).

---

## What's checked

### Schema validator (`validate_kg_schemas.py`)
- `graphType` matches the schema's `const`
- Required top-level fields exist (`role`, `generatedAt`, the array key)
- Each node has required structural fields per type
- Field types are correct

### Integrity validator (`validate_kg_integrity.py`)
- For knowledge graphs: every node's `path` resolves to an existing file
- Parent/child relationships are coherent (no orphans, no cycles)
- Cross-node references resolve

The two validators **do not** check taxonomic correctness (id-prefix conventions, exhaustive type enums). Those are the per-behavior Tier-A validators' job.

---

## Implementation status

**Functional**. `scripts/kg/validate_all.py` is in place from Phase 1 Day 1. Confirmed clean against the 6 empty/seeded graphs. Will continue to be the gate as the KG grows.

---

## Implements behaviors

- (this skill is the runtime that lets all KG-related behaviors actually be checked)

## Uses knowledge

- `knowledge:builder:kg-node-schema`
- `knowledge:builder:governance-tiers` (Tier A category)
