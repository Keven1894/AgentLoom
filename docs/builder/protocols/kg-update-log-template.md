# UPDATE_LOG Template

**Node ID**: `knowledge:builder:kg-update-log-template`
**Type**: template
**Category**: builder-meta
**Created**: 2026-05-18

---

## Purpose

`UPDATE_LOG_*.md` files are the human-readable narrative half of every KG mutation. The JSON delta says *what* changed; the UPDATE_LOG says *why*.

Together they form the audit trail. The dashboard `/timeline` page renders the chronological list of UPDATE_LOG headers as the workshop's "watch the KG learn" moment.

---

## File naming

```
UPDATE_LOG_<YYYYMMDD>_<kind>_<slug>.md
```

| Field | Values |
| --- | --- |
| `YYYYMMDD` | Calendar date, e.g. `20260522` |
| `kind` | One of: `proposal`, `accept`, `reject`, `migration`, `archive` |
| `slug` | Short kebab-case identifier matching the proposed node's slug |

Examples:
- `UPDATE_LOG_20260522_proposal_time-format-conventions.md` — proposal filed
- `UPDATE_LOG_20260522_accept_time-format-conventions.md` — proposal accepted (created at accept time, not at propose time)
- `UPDATE_LOG_20260518_migration_kg-schema-drift-reconciliation.md` — bulk migration

Files live at: `agents/knowledge-graphs/UPDATE_LOG_*.md` (committed to git; never deleted).

---

## Template — proposal

```markdown
# UPDATE_LOG: Proposal — <Node Title>

**Date**: 2026-MM-DD
**Author (agent)**: <agent name or "human-keven">
**Slug**: <kebab-case-slug>
**Proposed node type**: skill | knowledge | behavior
**Target graph**: builder-skills | domain-knowledge | ...

---

## Justification (the "why")

<2-4 sentences: what triggered this proposal? what gap does it fill? what would happen if we didn't add it?>

## Source context

<Where did this come from? Cite the task, file, line, conversation. Reviewers should be able to navigate to the original cause.>

- Task: <task slug or PR>
- File(s): <paths>
- Trigger: <one-line description>

## Proposed node

```json
{
  "id": "...",
  "type": "...",
  ...
}
```

## Intended links

- `parent`: <existing node id>
- `links.related`: [<existing node ids>]
- `links.implements`: [<existing behavior ids>]

## Reviewer notes

<Anything the reviewer should know that's not obvious from the JSON above. E.g. "this overlaps slightly with knowledge:domain:source-pagination but is more general — propose to consolidate post-Phase-2.">
```

---

## Template — accept

```markdown
# UPDATE_LOG: Accept — <Node Title>

**Date**: 2026-MM-DD
**Reviewer (human)**: <name>
**Original proposal**: UPDATE_LOG_<date>_proposal_<slug>.md
**PR**: <link>

---

## Decision

ACCEPTED with <no changes | minor edits | one substantive edit>.

## Edits made (if any)

- <field>: <before> → <after>, reason: <one line>

## Validators run

- `make kg-validate` → PASS
- `python -m agentloom.validators.run_all` → PASS

## Visual confirmation

- Cytoscape visualizer renders the new node
- Dashboard timeline shows the new entry
```

---

## Template — reject

```markdown
# UPDATE_LOG: Reject — <Node Title>

**Date**: 2026-MM-DD
**Reviewer (human)**: <name>
**Original proposal**: UPDATE_LOG_<date>_proposal_<slug>.md
**PR**: <link>

---

## Decision

REJECTED.

## Reason

<2-3 sentences: what was wrong with the proposal? duplicate of an existing node? premature? wrong abstraction level? out of scope?>

## What to do instead

<Optional: if the agent should retry with a different framing, say so.>
```

---

## Template — migration (bulk operations)

For changes that affect many nodes at once (schema reconciliation, axis-confusion fixes, etc.), one UPDATE_LOG covers all of them:

```markdown
# UPDATE_LOG: Migration — <Migration Title>

**Date**: 2026-MM-DD
**Author (human)**: <name>
**Migration script**: scripts/migrations/<filename>.py
**Backup suffix**: *.bak_drift_<date>

---

## Scope

- N node(s) affected across <list of KG files>
- <one-line summary of the structural change>

## Why now

<Why this migration was needed; what triggered it; what would break without it>

## Per-file changes

| File | Before | After |
| --- | --- | --- |
| ... | ... | ... |

## Validators run

- `make kg-validate` → PASS
- All per-behavior validators → PASS

## Rollback

`python -m agentloom.kg.rollback_kg <file>` restores from `.bak_drift_<date>`.
```

---

## See also

- `propose-review-protocol.md` — when and how to propose
- `governance-tiers.md` — bigger picture of governance layers
- Real example: `Scripts/migrations/2026-05-18-kg-schema-drift-reconciliation.py` (upstream `envistor-data` repo) and its companion completion doc
