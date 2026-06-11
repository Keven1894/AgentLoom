# Governance Tiers

**Node ID**: `knowledge:builder:governance-tiers`
**Type**: concept
**Category**: builder-meta
**Created**: 2026-05-18

---

## Why tiers

Not every rule deserves the same level of enforcement. A typo in a comment is not a runtime crash. A missing CRS conversion *is*. Forcing every check through the same gate either:
- Slows everything to the speed of the strictest check (bad), or
- Forces the strictest check down to the laxest level (also bad).

The answer is **tiered governance** — different invariants live at different enforcement levels, and authors choose the right tier when authoring a behavior.

---

## The three tiers

### Tier A — Hard (AST / regex / structural)

**Where it runs**: pre-commit hook, CI lint step, `make kg-validate`, `kg_editor.py` post-save.

**What it catches**:
- Structural invariants: required fields exist, types are correct, IDs are unique
- Filesystem invariants: referenced `path` files exist on disk
- KG referential invariants: every link's target ID resolves
- Schema-level invariants: `graphType` matches the schema's `const`, `priority` is in the enum

**Cost**: Low. Tens of LOC per validator. Fast (sub-second on the full repo).

**Examples**: 
- `every-skill-must-have-script` — every skill node has a non-empty `path` field
- `kg-node-ids-are-unique` — no two nodes share an `id` across all 6 graphs
- The schema validator and integrity validator together implement Tier A for the KG layer.

### Tier B — Test-time (runtime invariants)

**Where it runs**: pytest, in-process during automated testing.

**What it catches**:
- Function-output invariants: parser returns valid CRS, timestamps in valid range
- Inter-skill invariants: skill A's output schema matches skill B's input schema
- Data-shape invariants: returned GeoJSON has `type: 'FeatureCollection'`

**Cost**: Medium. Each behavior gets a small pytest fixture or a dedicated test file.

**Examples**:
- `parser-output-must-be-iso8601` — every parser skill's timestamp output passes `datetime.fromisoformat()`
- `geometry-output-must-have-crs` — every geometry-producing skill emits a `crs` field

Tier B validators are introduced in Phase 5 of the workshop sprint, not in Phase 1.

### Tier C — Process / DB / git-state

**Where it runs**: CI workflow checks, GitHub Actions, scheduled cron, post-merge hook.

**What it catches**:
- Workflow invariants: every PR has a linked plan doc, every accepted proposal has an UPDATE_LOG, every commit modifying a KG passes both validators
- Cross-system invariants: dashboard `/timeline` row count matches `git log agents/knowledge-graphs/UPDATE_LOG_*` count, schema files in repo match the ones referenced by the deployed validator
- Drift invariants: no schema in the repo diverges from the corresponding canonical schema in the upstream `envistor-data` reference

**Cost**: Higher. Often involves orchestration (querying GitHub, running git commands, comparing files across repos).

**Examples**:
- `every-pr-modifying-kg-runs-both-validators` (CI workflow check)
- `every-accepted-proposal-has-update-log` (post-merge hook)
- `schema-drift-from-envistor` (scheduled comparison)

Tier C validators are introduced in Phase 5+ of the workshop sprint.

---

## Choosing a tier

When authoring a behavior, ask:

1. **Can I detect this by reading source files alone?** → **Tier A**
2. **Do I need to run code and inspect outputs?** → **Tier B**
3. **Do I need to compare across systems / commits / PRs?** → **Tier C**
4. **Is this aspirational guidance with no automatic check?** → **`enforcement: soft`** (no validator required; reviewer-judgement only)

---

## What `soft` actually means

`soft` is the escape hatch for genuine guidance that resists automation:
- Style preferences ("agents should respond in formal tone")
- High-level principles ("prefer composition over inheritance")
- Cultural norms ("be honest about uncertainty")

These are real and worth documenting. But pretending to enforce them with a regex is worse than honestly labeling them `soft` and trusting reviewers.

**Test**: if you can write a Python validator for it in <100 LOC, it's NOT soft. Make it Tier A or B.

---

## See also

- `validator-authoring-guide.md` — concrete template for a Tier-A validator
- `propose-review-protocol.md` — Tier-C-style governance for KG mutations
- Workshop reference: the four behaviors in `agents/behaviors/builder/` are all Tier A and ship with their validator scripts in `src/agentloom/validators/`
