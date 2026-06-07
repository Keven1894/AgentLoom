# Skill: Wire Validator

**ID**: `skill:builder:wire-validator`
**Category**: kg-tools
**Priority**: high
**Created**: 2026-05-18

---

## Purpose

Given a behavior MD that declares an enforcement tier, scaffold its companion validator script using the Tier-A template, and link the two via the behavior node's `links.validator` field.

This skill closes the loop between *declaring* a rule (`behavior-*.md`) and *enforcing* a rule (`src/agentloom/validators/*.py`). It exists because manual wiring is error-prone and `every-non-soft-behavior-has-validator` will fail CI if the wiring is incomplete.

---

## When to use

**Required** when:
- A new behavior with `enforcement` ∈ {hard, test, process} is being authored
- An existing soft behavior is being upgraded to a non-soft tier

**Do not use** when:
- The behavior is genuinely `enforcement: soft` — no validator needed

---

## How to run

```bash
python src/agentloom/kg/wire_validator.py \
    --behavior-id <behavior:role:slug> \
    --tier {A|B|C}
```

The script:
1. Locates the behavior MD by id
2. Scaffolds `src/agentloom/validators/<slug_with_underscores>.py` from the appropriate tier template (Tier A is the default; B/C templates added in Phase 5)
3. Updates the behavior node's `links.validator` field via `kg_editor`
4. Runs `make kg-validate` to confirm wiring is consistent
5. Prints next steps: "fill in the `check_one()` function body, run the script, commit"

---

## Implementation status

**Stub** as of Phase 1 Day 2. The script will be authored in Phase 5 alongside the broader validator-tooling sweep. For Phase 1–4 the four bootstrap behaviors and their validators are wired by hand.

---

## Implements behaviors

- `behavior:builder:every-non-soft-behavior-has-validator` (mechanizes compliance)
- `behavior:builder:every-skill-must-have-script` (the scaffolded script counts as the skill's body)

## Uses knowledge

- `knowledge:builder:validator-authoring-guide`
- `knowledge:builder:governance-tiers`
