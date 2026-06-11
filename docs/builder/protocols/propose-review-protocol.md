# Propose-Review Protocol

**Node ID**: `knowledge:builder:propose-review-protocol`
**Type**: protocol
**Category**: builder-meta
**Created**: 2026-05-18

---

## Purpose

A safe, auditable mechanism for the builder agent to extend the domain-KG without humans being a per-edit bottleneck — yet without escaping human review entirely.

This is the **operationalization of the dual-helix**: the engineering strand discovers candidate patterns, the governance strand approves which ones become canonical KG content.

---

## When to propose

The builder agent calls `propose_node.py` when, during work on a domain task, it encounters a pattern not represented in the current domain-KG. Concrete triggers:

- **Schema gotcha** — a data source has an idiosyncrasy not documented (e.g. epoch-ms timestamps, sentinel value `-999999`, two-call pagination join). Propose a `knowledge` node.
- **Recurring procedure** — the agent finds itself doing the same multi-step thing across two or more sources. Propose a `skill` node abstracting it.
- **Repeated mistake** — the agent (or a previous agent) made the same error twice. Propose a `behavior` node with a Tier-A validator that catches it.
- **Unhandled corner case** — a known skill applied to a new source surfaces a corner case worth recording. Propose a knowledge node attached to that skill via `links.related`.

The agent does **not** propose:
- Ad-hoc one-time observations (those go in chat / commit messages, not the KG).
- Restatements of existing nodes (would add noise; check the KG first).
- Anything still actively-debugging-but-unverified (proposals should be confident-enough to merit review).

---

## How to propose

```bash
python -m agentloom.kg.propose_node \
  --type knowledge \
  --slug time-format-conventions \
  --justification "USGS GeoJSON uses epoch milliseconds while most JSON-LD/EML expects ISO-8601; need a knowledge node so future ingest skills know to convert." \
  --source-context "encountered while building D1 ingest, see scripts/d1_ingest.py:42"
```

The tool writes two files to `agents/knowledge-graphs/proposals/`:

1. `<timestamp>-<slug>.json` — the proposed node payload (a JSON object matching the schema for that node type)
2. `UPDATE_LOG_<date>_proposal_<slug>.md` — the markdown narrative: justification, source-context, intended links to existing nodes, draft schema fields

**The tool does NOT modify the canonical KG.** That happens at human-approval time.

---

## How to review

The reviewer (Keven during the workshop sprint, attendees during the workshop itself):

1. Opens the PR with label `kg-proposal`
2. Reads the `UPDATE_LOG_*` for context (10-30 seconds)
3. Inspects the proposed JSON for shape (5-10 seconds)
4. **On accept**: comments `/accept` (or merges the PR) → CI runs `python -m agentloom.kg.accept_proposal <slug>` → `kg_editor.add_<type>(...)` → both validators run → both PASS or auto-rollback → proposal file deleted, UPDATE_LOG kept
5. **On reject**: closes the PR with reason → UPDATE_LOG kept anyway as "considered and rejected" record (this is itself audit-worthy)
6. **On request-changes**: comments inline → agent revises proposal → re-pushes

Average review time: 30 seconds for a tightly-scoped proposal. Multiple proposals per day are normal during Phase 2.

---

## Why this beats the markdown-soup pattern

Anthropic Skills, Cursor rules, Cline `.clinerules` — all let any author dump any markdown into a `.skills/` folder. There is no provenance, no diff history bound to the KG mutation, no review gate, no audit trail.

AgentLoom's propose-review protocol gives:

- **Provenance** — every node has an `UPDATE_LOG_*` showing why it was added, by which agent, in response to what task
- **Diff history** — every accept/reject is a git commit; `git log agents/knowledge-graphs/` is the full mutation timeline
- **Review gate** — no node enters the canonical KG without passing both validators AND a human approval
- **Audit trail** — even rejected proposals are kept (in the `UPDATE_LOG` history), so reviewers can see what was considered and why it didn't make it

This is the workshop's headline: *the dashboard timeline replay shows the KG growing one approved proposal at a time, with every decision still scrutinizable months later.*

---

## See also

- `kg-update-log-template.md` — the exact format of `UPDATE_LOG_*.md` files
- `governance-tiers.md` — the deeper governance hierarchy this protocol fits into
- `agents/knowledge-graphs/MAINTENANCE.md` — operational runbook with daily workflow detail
