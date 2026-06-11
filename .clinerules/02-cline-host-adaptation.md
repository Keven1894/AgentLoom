# 02 — Cline Host Adaptation

Operational notes specific to running the AgentLoom builder agent inside Cline. The canonical system prompt (file `01-builder-agent-prompt.md` in this directory) is host-agnostic; this file fills in the Cline-specific glue.

## File layout you should know about

- `agents/knowledge-graphs/*-graph.json` — the live knowledge graphs. Six files: `builder-knowledge-graph.json`, `builder-skills-graph.json`, `builder-behaviors-graph.json` and the matching three under `domain-…`. **Read these before proposing.**
- `agents/knowledge-graphs/proposals/` — pending proposal JSON files plus `UPDATE_LOG_*` audit artifacts from accepted/rejected past proposals.
- `docs/{builder,domain}/concepts/`, `docs/{builder,domain}/proposed/` — markdown bodies for KG nodes (one file per node).
- `data/snapshots/` — vendored data snapshots for the four workshop sources (D1 quakes, D2 OpenAQ air, D3 NWIS streamflow, D4 Natural Earth admin0).
- `python -m agentloom.kg.propose_node` — the **only** way to file a proposal. Do not edit graph json directly.
- `python -m agentloom.kg.accept_proposal` — human-only. **Do not call this yourself.**
- `python -m agentloom.validators.run_all` — runs all Tier-A validators. Run after any change.
- `runs/agent/` — JSONL run logs. Files matching `*.kept.jsonl` are paper-grade evidence and not auto-cleaned.
- **Dashboard** (`make dashboard` → `http://127.0.0.1:8000`) — **human review surface**. Proposals tab shows pending queue in plain language; Graph/Timeline show accepted history. Read-only — accept stays CLI.

## How humans review proposals (not json)

1. Cline files proposals via `python -m agentloom.kg.propose_node`.
2. Human opens dashboard → **Proposals** tab — reads title + justification.
3. If satisfied: `python -m agentloom.kg.accept_proposal --proposal agents/knowledge-graphs/proposals/<file>.json`
4. Refresh dashboard — node appears on Graph tab; Timeline updates.

W2 adds a welcome HTML page linking Cline + this dashboard. See `docs/workshop/kg-access-and-human-review.md`.

## How to file a proposal (the only allowed mutation path)

1. Read existing KG json + relevant proposed/accepted markdown.
2. Inspect the data snapshot (typically the first 8 KB is enough for a clean shape read; do not load 14 MB GeoJSONs into context).
3. Compose your JSON output per the contract in `01-builder-agent-prompt.md`.
4. For each proposal, run the equivalent of:

   ```bash
   python -m agentloom.kg.propose_node \
     --type knowledge \
     --target-role domain \
     --slug <kebab-case-slug> \
     --title "<title>" \
     --justification "<2-5 sentences citing concrete observations>" \
     --source-context "<task / branch / snapshot>" \
     --priority high \
     --author cline-builder-agent \
     [--links-json '{"uses": ["existing-node-id-1"]}']
   ```

5. Tell the human operator the proposals are filed and where (proposal filenames). The human decides accept/reject.

## Reading the KG

**Preferred (W2 — MCP connected):** use MCP tools instead of loading graph json into context:

- `kg_search "iso 3166"` — find nodes by topic (includes pending proposals)
- `kg_get_node knowledge:domain:…` — fetch one node + markdown body
- `kg_list_proposals` — pending queue (same as dashboard Proposals tab)

See `docs/workshop/cline-mcp-tools.md` for Cline configuration.

**Fallback (MCP unavailable):** read KG json files directly via file-read. Be selective:

- Read only the json files relevant to the current `target-role` (domain proposal? read `agents/knowledge-graphs/domain-*-graph.json`).
- Skim node ids + titles first; fetch full markdown bodies only for the few nodes whose ids/titles look related.
- Do NOT dump every json file into context. Even the largest one (a few hundred kB) will burn your context budget.

When MCP is unavailable, use the fallback above. Do not load all six `*-graph.json` files at once.

## Snapshot reading quirks

- D2 OpenAQ snapshots can be 100+ KB; sample the first 8 KB only.
- D4 Natural Earth admin0 is 14 MB; never read in full. The first 8 KB contains top-level envelope + `crs` + the first feature (Indonesia, MultiPolygon). **Do not generalize per-feature claims from the first feature alone** — there is a meta-pattern node for this; consult `behavior:builder:sample-multiple-features-when-claiming-shape-uniformity` if it exists at the time you read this.

## Permission to run shell commands

The first time you propose a node in Cline, the user will be prompted to allow `python -m agentloom.kg.propose_node`. Approve once; subsequent invocations are seamless.

## Reproducibility note for paper-grade runs

If the operator marks a Cline session as paper-grade (e.g. for the cross-model matrix), they will:

1. Save the Cline chat transcript.
2. Pin the Cline model + version + your output verbatim.
3. Cross-link to whatever `runs/agent/*.kept.jsonl` were produced by the propose_node.py invocations.

Do not produce nondeterministic helper output between the JSON contract response and the propose_node.py call. The runtime is a parser, not a chatbot.
