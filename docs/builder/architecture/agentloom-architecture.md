# AgentLoom Architecture

**Node ID**: `knowledge:builder:agentloom-architecture`
**Type**: architecture
**Category**: builder-meta
**Created**: 2026-05-18

---

## What AgentLoom is

AgentLoom is a framework for building dual-role AI agents using **three-track knowledge graphs** (skills, knowledge, behaviors) governed by a **dual-helix protocol** (engineering strand auto-extends; governance strand human-reviews).

The framework's deliverable is not a single agent. It's the **methodology** for assembling agents: how to author skills, how to encode knowledge, how to enforce behaviors with executable validators, and how to grow the knowledge graph safely as the agent learns new domains.

---

## Three-track structure

Every AgentLoom-built agent has three KGs per role:

| Track | What it holds | Governs | Array key |
| --- | --- | --- | --- |
| **Skills** | Executable capabilities — Python scripts the agent can call | `skills-graph.schema.json` | `skills` |
| **Knowledge** | Domain facts, schemas, conventions, gotchas — markdown-backed | `knowledge-graph.schema.json` | `nodes` (or `documents`) |
| **Behaviors** | Rules + their executable validators (Tier A/B/C) | `behaviors-graph.schema.json` | `behaviors` |

Tracks are **not orthogonal** — a skill *implements* one or more behaviors, a behavior *references* one or more knowledge nodes, and so on. The cross-track links are first-class graph edges (`implements`, `references`, `related_to`).

---

## Two roles

Each agent built with AgentLoom has at least two roles:

- **`role-builder`** — meta-knowledge: "what AgentLoom is, how to author a skill / knowledge / behavior, how to propose new nodes." Stable; changes only when the framework itself evolves.
- **`role-domain`** — domain-specific knowledge: "how to ingest USGS Earthquakes, how to render points on MapLibre, how to publish FAIR metadata." Grows with the agent's experience.

Roles are physical KG-file separation. Each role has its own `<role>-{skills,knowledge,behaviors}-graph.json`. A `master-graph.json` (the registry) maps roles to their graph files.

---

## Dual-helix protocol

Two strands run in parallel:

- **Engineering strand** (auto): the agent reads memory (graph-RAG via embeddings), proposes new nodes when it hits unhandled patterns, embeds new content, writes operational state. Continuous, autonomous.
- **Governance strand** (human-reviewed): every KG mutation passes through validators (schema + integrity), every proposal is reviewed by a human via PR. Discrete, gated.

Neither strand escapes the other. The engineering strand can't write to the canonical KG without passing the governance gate. The governance strand can't manufacture knowledge without the engineering strand discovering candidate patterns. **Together they make memory grow safely without humans being the bottleneck.**

---

## Why this design

The competing landscape (Anthropic Skills, Cursor rules, Cline `.clinerules`) ships markdown-soup with no provenance, no diff history, no review gate. AgentLoom's structural commitment is the opposite: **every rule ships an executable validator, every KG mutation is reviewable, every memory layer has a known purpose.**

This is the load-bearing claim: *machine-executable protocols, not suggestive instructions.*

---

## See also

- `kg-node-schema.md` — the formal schema for skill / knowledge / behavior nodes
- `propose-review-protocol.md` — how the dual-helix is operationalized day-to-day
- `governance-tiers.md` — the layered enforcement model (Tier A AST/lint, Tier B test-time, Tier C process/git-state)
