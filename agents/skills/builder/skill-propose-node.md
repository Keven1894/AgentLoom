# Skill: Propose KG Node

**ID**: `skill:builder:propose-node`
**Category**: kg-tools
**Priority**: critical
**Created**: 2026-05-18

---

## Purpose

Allow the agent to safely add a candidate node to the KG without bypassing human review. This is the engineering-strand entry point of the propose-review protocol.

The skill writes two files to `agents/knowledge-graphs/proposals/`:
1. `<timestamp>-<slug>.json` — the candidate node payload
2. `UPDATE_LOG_<date>_proposal_<slug>.md` — narrative + justification

It does **not** mutate the canonical KG. Acceptance happens via PR review and `accept_proposal.py` (Phase 2 deliverable).

---

## When to use

**Required** when the agent encounters one of:
- A schema gotcha not yet documented (data source quirk)
- A recurring procedure used across ≥2 contexts (abstract into a skill)
- A repeated mistake (encode as a behavior + Tier-A validator)
- An unhandled corner case worth recording

**Do NOT use** when:
- Restating an existing node (check the KG first via `make kg-validate` or visualizer)
- Filing a one-time observation (use commit message instead)
- The pattern is still actively-debugging-but-unverified

See: `docs/builder/protocols/propose-review-protocol.md`

---

## How to run

```bash
python scripts/kg/propose_node.py \
    --type {skill|knowledge|behavior} \
    --slug <kebab-case-id> \
    --justification "<2-4 sentence rationale>" \
    --source-context "<task/file/line that triggered this>"
```

Optional flags:
- `--parent <existing-id>` — set `parent` of proposed node (defaults: type-specific root)
- `--links '{"related": ["..."]}'` — JSON-encoded links dict

The script:
1. Validates `--type` against the schemas
2. Generates a candidate node with required structural fields
3. Writes proposal JSON + UPDATE_LOG to `proposals/`
4. Prints next-step instructions (open PR, request review)

---

## Implementation status

**Stub** as of Phase 1 Day 2. Functional implementation is Phase 2 Day 1 (see `PLAN.md`). The MD here is the contract; the script will be authored to match.

When implemented, the script lives at `scripts/kg/propose_node.py` and shells out to `kg_editor.py` for node generation but keeps writes restricted to `proposals/`.

---

## Implements behaviors

- `behavior:builder:every-skill-must-have-script` (when implemented, the script must exist)
- `behavior:builder:kg-node-ids-are-unique` (the proposal staging avoids id-collision risk)

## Uses knowledge

- `knowledge:builder:propose-review-protocol`
- `knowledge:builder:kg-update-log-template`
- `knowledge:builder:kg-node-schema`
