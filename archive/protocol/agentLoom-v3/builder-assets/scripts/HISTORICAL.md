# Historical — pre-v3 executable scripts

**Status:** historical reference only (December 2025 and earlier).

The scripts in this directory (`validate_graphs.py`, `kg_heal.py`, `validate_structure.py`,
`validate-generation.py`, etc.) belong to the **documentation-first** AgentLoom v3 protocol package.
They were used during early framework development before the UCGIS 2026 sprint produced a
**runnable governance stack** at the repository root.

## Use the runnable framework instead

| Need | Location |
|------|----------|
| KG schema + integrity validation | `scripts/kg/validate_schemas.py`, `scripts/kg/validate_kg_integrity.py` |
| Unified KG gate | `scripts/kg/validate_all.py` or `make kg-validate` |
| Tier-A behavior validators | `scripts/validators/run_all.py` or `make validate-all` |
| Propose → review → accept | `scripts/kg/propose_node.py`, `scripts/kg/accept_proposal.py` |
| Human review UI | `make dashboard` → `http://127.0.0.1:8000` |
| Cline host emit | `scripts/sync_clinerules.py` → `.clinerules/` |

**Protocol documentation** (9-phase setup, specs, user manuals) remains in `agentloom-framework/agentLoom-v3/`.
**Executable framework** lives at repo root: `scripts/`, `server/`, `agents/knowledge-graphs/`.

Do not maintain two divergent validator implementations. Changes go to `scripts/kg/` and `scripts/validators/`.
