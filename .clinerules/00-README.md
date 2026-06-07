# `.clinerules/` — AgentLoom builder agent for Cline (Layer-3 host #3)

This directory makes Cline (the VSCode AI extension) act as a third Layer-3 host for the AgentLoom builder agent, equivalent in role to:

- **Layer-3 host #1**: `agentloom.builder_agent` (standalone Python package, `scripts/agent/`).
- **Layer-3 host #2**: Cursor IDE (when used with the same KG node as a system prompt).
- **Layer-3 host #3 (this directory)**: Cline (VSCode extension).

All three hosts share the same canonical system prompt (`docs/builder/concepts/builder-agent-system-prompt.md`), the same propose-review CLIs (`scripts/kg/propose_node.py`, `scripts/kg/accept_proposal.py`), and the same JSON output contract.

## Files in this directory

Cline loads every `.md` and `.txt` file here at workspace open and concatenates them into the session system prompt. Numeric prefixes order them; the order is meaningful for humans, not for Cline.

| File | Origin | Role |
|---|---|---|
| `00-README.md` | hand-authored | this file; orientation |
| `01-builder-agent-prompt.md` | **GENERATED** by `scripts/sync_clinerules.py` | canonical system prompt body, derived from the KG node |
| `02-cline-host-adaptation.md` | hand-authored | Cline-specific operational notes (how to invoke CLIs, file layout) |
| `03-workshop-discipline.md` | hand-authored | non-negotiable invariants — paired-commit hard-launch, no agent-side accept, validators must stay green |

## Single source of truth

The canonical prompt lives at `docs/builder/concepts/builder-agent-system-prompt.md` (KG node id: `knowledge:builder:builder-agent-system-prompt`). When that node changes:

```bash
python scripts/sync_clinerules.py        # rewrite 01-builder-agent-prompt.md
```

A Tier-A validator (`scripts/validators/clinerules_must_match_system_prompt_kg_node.py`) fails CI if the two are out of sync. **Do not hand-edit `01-builder-agent-prompt.md`** — your edit will be overwritten on the next sync, and CI will fail in the meantime.

## How Cline interacts with the rest of the framework

- Cline reads KG json files directly via its file-read tool (fallback path) OR via the lightweight MCP server (`scripts/mcp_kg_server.py`, see W2 plan) when installed (preferred path).
- Cline shells out to `python scripts/kg/propose_node.py` to file proposals.
- A human (operator) reviews + accepts via `python scripts/kg/accept_proposal.py`. Cline NEVER accepts its own proposals.
- All Cline runs that produce paper-grade evidence should be reproducible. If you run a paper-relevant flow in Cline, save the chat transcript next to the run log convention used by `agentloom.builder_agent` (`runs/agent/*.kept.jsonl`).

## Compliance test

Cline counts as "an instance of the AgentLoom builder agent" iff:

1. It loads `01-builder-agent-prompt.md` (verbatim KG-node body) as part of its system prompt.
2. It uses `propose_node.py` / `accept_proposal.py` for KG mutations.
3. It produces the same JSON output contract specified in the prompt.

Anything else — provider-specific tool calls, Cline-only macros, custom prompts that diverge from the KG node — does not satisfy compliance.
