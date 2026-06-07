# Knowledge Graphs — `ucgis-agentloom-2026`

Two roles × three graph types = **6 KG files**. The split mirrors the
[`envistor-data`](https://github.com/Keven1894/envistor-data) production setup,
adapted to workshop scope.

| Role | Skills graph | Knowledge graph | Behaviors graph |
| --- | --- | --- | --- |
| `role-builder` | `builder-skills-graph.json` | `builder-knowledge-graph.json` | `builder-behaviors-graph.json` |
| `role-domain` | `domain-skills-graph.json` | `domain-knowledge-graph.json` | `domain-behaviors-graph.json` |

## Roles

- **`role-builder`** — meta-knowledge: "what AgentLoom is, how to author a skill / knowledge / behavior, how to propose new nodes." Hand-authored on Day 2 of Phase 1; ~15 nodes total. **Stable**: changes only when the framework itself evolves.
- **`role-domain`** — workshop content: "how to ingest USGS Earthquakes, how to render points on MapLibre, how to publish FAIR metadata." **Grows bottom-up** during Phase 2 (May 22–26): the builder agent walks each of D1/D2/D3/D4 sources, calls `propose_node.py` whenever it hits an uncovered pattern, and a human reviews via PR. Currently empty.

## Graph types

- **Skills** (array key: `skills`) — Executable capabilities. Each skill node has a `path` field pointing at a `.md` file under `agents/skills/{builder,domain}/...` and (typically) a `script` field linking to runnable code.
- **Knowledge** (array key: `nodes`) — Domain facts, schemas, conventions, gotchas. Each node has a `path` field pointing at a `.md` file under `docs/builder/...` or `docs/domain/...`.
- **Behaviors** (array key: `behaviors`) — Rules with executable validators. Each behavior has YAML frontmatter declaring its enforcement tier (`hard | test | process | soft`) + a path to its validator (Tier ≠ soft).

The **Schema reference** is in [`SCHEMA.md`](./SCHEMA.md) (ported verbatim from `envistor-data`; workshop-irrelevant fields like `team_members` are tolerated but unused).

## Validation

Two complementary validators (both ported from `envistor-data`):

```bash
# Cross-platform unified runner — exit 0 iff both pass
python scripts/kg/validate_all.py

# Or individually
python scripts/kg/validate_schemas.py            # JSON Schema for all 6 graphs
python scripts/kg/validate_kg_integrity.py --all # relational integrity (parent/child, orphans, cycles) on knowledge graphs

# With make, if available
make kg-validate
```

The CI / pre-commit hook will run the unified runner.

## Editing safely

Never edit these JSON files by hand for non-trivial changes. Use the editor
ported from Envita:

```python
from scripts.kg.lib.kg_editor import KGEditor
editor = KGEditor("agents/knowledge-graphs/builder-skills-graph.json",
                  auto_backup=True, auto_validate=True)
editor.load()
editor.add_skill(id="skill:builder:propose-node", name="Propose KG node",
                 category="kg-tools", path="agents/skills/builder/propose-node.md")
editor.save()  # auto-validates; auto-rolls-back on failure
```

For agent-driven edits during Phase 2, use `scripts/kg/propose_node.py` (Day 3 deliverable) — it writes a candidate node to `agents/knowledge-graphs/proposals/` for human review via PR, **never** editing the canonical KG directly.

## Proposals (Day 3+ workflow)

The directory `agents/knowledge-graphs/proposals/` holds candidate nodes the builder agent has proposed but a human has not yet reviewed. Workflow:

1. Agent encounters a pattern not in domain-KG → calls `propose_node.py`
2. Tool writes `<timestamp>-<slug>.json` (the proposed node) + `UPDATE_LOG_<date>_proposal_<slug>.md` (justification + source-context) to `proposals/`
3. Agent opens a PR with label `kg-proposal`
4. Human reviews the diff; on accept: `python scripts/kg/accept_proposal.py <slug>` (which delegates to `kg_editor.py` with auto-backup)
5. Accepted proposal is removed from `proposals/`; the `UPDATE_LOG` is committed to git as the audit trail

The `proposals/` directory + `UPDATE_LOG_*` files are the workshop's **provenance trail** — what makes the dual-helix "governance" strand visible and reviewable. See [`docs/plan/todo/2026-05-18-builder-first-envita-reuse-decision.md`](https://github.com/Keven1894/envistor-data/blob/main/docs/plan/todo/2026-05-18-builder-first-envita-reuse-decision.md) (in the planning repo) for the design rationale.

## Status

Phase 1 Day 1 closed 2026-05-18 (ahead of schedule, commit `fcbc647`):

- ✅ KG infrastructure ported from Envita (validator, schema validator, kg_editor, 5 schemas)
- ✅ 6 empty KG skeletons in place
- ✅ `make kg-validate` exits 0
- ✅ Schemas reconciled grade-A clean upstream (8/8 PASS in envistor) and synced here
- ✅ Workshop-scoped `MAINTENANCE.md` written
- ⏳ Builder-KG bootstrap content (15 meta nodes) — Day 2 (May 20, possibly earlier)
- ⏳ `propose_node.py` + dashboard MVP — Day 3 (May 21)
