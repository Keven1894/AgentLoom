# Knowledge Graph Maintenance — `ucgis-agentloom-2026`

**Last Updated**: 2026-05-18
**Audience**: workshop attendees authoring KG nodes, agents calling the editor, reviewers approving proposals

This is the **operational runbook** for keeping the workshop KGs healthy. For the conceptual overview (memory layers, retrieval routing, the dual-validator architecture), read [`README.md`](README.md) and the source-of-truth methodology doc in the upstream `envistor-data` repo: [`docs/knowledge-graphs/KG_MEMORY_METHODOLOGY.md`](https://github.com/Keven1894/envistor-data/blob/keven/docs/knowledge-graphs/KG_MEMORY_METHODOLOGY.md).

---

## TL;DR

Two validators, both must PASS:

```bash
make kg-validate            # both, exit 0 iff clean
make kg-validate-schemas    # JSON-Schema (structure)
make kg-validate-integrity  # taxonomy + relations on knowledge graphs
```

Three editing channels, ranked by safety:

1. **For agents during Phase 2**: `python src/agentloom/kg/propose_node.py` → human reviews via PR → `python src/agentloom/kg/accept_proposal.py`
2. **For humans authoring meta-content**: `src/agentloom/kg/lib/kg_editor.py` Python API (auto-backup + auto-validate)
3. **For emergencies only**: hand-edit JSON, then `make kg-validate` (and pray)

---

## What's where

| File | Role | Schema | Array key |
| --- | --- | --- | --- |
| `builder-skills-graph.json` | Meta capabilities (propose, validate, emit) | skills | `skills` |
| `builder-knowledge-graph.json` | Meta knowledge (architecture, conventions) | knowledge | `nodes` |
| `builder-behaviors-graph.json` | Meta rules + validators | behaviors | `behaviors` |
| `domain-skills-graph.json` | Workshop content skills (D1–D4 ingest, viz) | skills | `skills` |
| `domain-knowledge-graph.json` | Workshop content knowledge (source schemas, gotchas) | knowledge | `nodes` |
| `domain-behaviors-graph.json` | Workshop content rules + validators | behaviors | `behaviors` |

Schemas in `src/agentloom/kg/lib/schemas/`. The **schemas validate STRUCTURE, not TAXONOMY** — they check required fields, types, and the `const graphType`, but do NOT enforce id patterns, exhaustive type enums, or path patterns. Taxonomy is the integrity validator's job, with reviewer judgement as the third rail. (Full rationale in [`KG_VALIDATION_ARCHITECTURE.md`](https://github.com/Keven1894/envistor-data/blob/keven/docs/knowledge-graphs/KG_VALIDATION_ARCHITECTURE.md) upstream.)

---

## Daily workflow during Phase 2 (May 22–26)

The builder agent is the primary KG author during Phase 2. The workflow is:

1. Agent walks the D-N pipeline (ingest → process → publish → visualize)
2. Agent hits a pattern not in domain-KG → calls `python src/agentloom/kg/propose_node.py`
3. Tool writes:
   - `agents/knowledge-graphs/proposals/<timestamp>-<slug>.json` — proposed node payload
   - `agents/knowledge-graphs/UPDATE_LOG_<date>_proposal_<slug>.md` — justification + source-context
4. Agent opens a PR with label `kg-proposal`
5. Reviewer (Keven) reviews diff in PR
6. **On accept** → `python src/agentloom/kg/accept_proposal.py <slug>` → `kg_editor.add_<type>(...)` → both validators run → both PASS or auto-rollback → proposal file deleted, UPDATE_LOG kept as audit trail
7. **On reject** → close PR with reason; UPDATE_LOG kept anyway as "considered and rejected" record

The accepted-and-rejected UPDATE_LOG history IS the workshop's provenance trail. By Phase 3 demo, the dashboard `/timeline` page replays this history one row per accept/reject, with link to source PR.

---

## Editing safely (humans, off the propose-review path)

For meta-layer edits where the propose-review process is overkill (e.g. authoring the initial 15-node builder-KG in Phase 1 Day 2):

```python
from scripts.kg.lib.kg_editor import KGEditor

editor = KGEditor(
    "agents/knowledge-graphs/builder-skills-graph.json",
    auto_backup=True,    # writes *.bak_<timestamp> next to the file
    auto_validate=True,  # runs both validators after save; rolls back on FAIL
)
editor.load()
editor.add_skill(
    id="skill:builder:propose-node",
    name="Propose KG node",
    category="kg-tools",
    path="agents/skills/builder/propose-node.md",
    description="Agent-callable; writes a candidate node JSON + UPDATE_LOG to proposals/",
)
editor.save()
```

Auto-rollback means: if the post-save validator FAILs, the editor restores from backup. Your in-progress JSON edit is lost; the canonical file stays clean.

---

## Validator coverage matrix

| KG file | Schema validator | Integrity validator |
| --- | --- | --- |
| `builder-skills-graph.json` | ✅ | ❌ (key=`skills`, ignored — known limitation) |
| `builder-knowledge-graph.json` | ✅ | ✅ |
| `builder-behaviors-graph.json` | ✅ | ❌ (key=`behaviors`, ignored — known limitation) |
| `domain-skills-graph.json` | ✅ | ❌ (key=`skills`, ignored) |
| `domain-knowledge-graph.json` | ✅ | ✅ |
| `domain-behaviors-graph.json` | ✅ | ❌ (key=`behaviors`, ignored) |

**Schema validation covers all 6.** Integrity validation only covers the 2 knowledge graphs (it's keyed on `nodes`/`documents` array names; skills + behaviors graphs use different keys). Skills + behaviors get their structural checks from the schema validator, and their ID/relation checks from `kg_editor.py`'s post-save hooks during the edit.

---

## When validators fail

```text
$ make kg-validate
[FAIL] domain-skills      domain-skills-graph.json
  at skills/12/path: 'foo/bar' is not of type 'string'
```

Diagnosis order:

1. **Read the path** (`skills/12/path` = the 13th skill node's `path` field)
2. **Inspect the offending node** — `python -c "import json; print(json.load(open('agents/knowledge-graphs/domain-skills-graph.json'))['skills'][12])"`
3. **Decide schema-fix vs KG-fix**:
   - If the schema is wrong (the field is legitimately not a string here, or `null` should be allowed) → relax the schema
   - If the KG is wrong (typo, wrong type, missed required field) → fix the KG
4. **If you backed up before the edit**: `python src/agentloom/kg/rollback_kg.py <kg-file>` restores from the most recent `.bak_*`
5. **Re-run validator** until PASS

> Full reconciliation methodology: [`docs/plan/completed/2026-05-18-kg-schema-drift-reconciliation-COMPLETE.md`](https://github.com/Keven1894/envistor-data/blob/keven/docs/plan/completed/2026-05-18-kg-schema-drift-reconciliation-COMPLETE.md) (real-world case from upstream).

---

## Pre-commit hook (Phase 5+)

Once the workshop infrastructure stabilizes, add `make kg-validate` to a pre-commit hook so no commit can land with broken KGs. Skipped during the workshop sprint to avoid friction during high-velocity authoring.

---

## See also

- [`README.md`](README.md) — orientation, role + graph-type explanation
- [`SCHEMA.md`](SCHEMA.md) — node-shape conventions (note: ported verbatim from envistor-data; some fields like `team_members` are tolerated but unused in workshop scope)
- Upstream methodology: [`docs/knowledge-graphs/KG_MEMORY_METHODOLOGY.md`](https://github.com/Keven1894/envistor-data/blob/keven/docs/knowledge-graphs/KG_MEMORY_METHODOLOGY.md) (4-figure narrative tour)
- Upstream architecture: [`docs/knowledge-graphs/KG_VALIDATION_ARCHITECTURE.md`](https://github.com/Keven1894/envistor-data/blob/keven/docs/knowledge-graphs/KG_VALIDATION_ARCHITECTURE.md) (dual-validator deep-dive)
