# AgentLoom

**Executable governance framework for builder agents** — knowledge graphs, propose→review→accept,
Tier-A validators, and a human review dashboard.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17561541.svg)](https://doi.org/10.5281/zenodo.17561541)
![Code: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)
![Docs: CC BY-NC 4.0](https://img.shields.io/badge/Docs-CC%20BY--NC%204.0-lightgrey.svg)

**Author:** Dr. Boyuan (Keven) Guan · FIU Library & GIS Center  
**Version:** 3.0.0 (executable framework sync, June 2026)

---

## What this repo contains

| Layer | Path | Role |
|-------|------|------|
| **Runnable framework (v3)** | `scripts/`, `server/`, `agents/knowledge-graphs/` | KG governance, validators, dashboard, propose-review |
| **Protocol docs (historical v3 package)** | `agentloom-framework/agentLoom-v3/` | 9-phase setup manuals, specs, design docs |
| **Research & positioning** | `docs/`, `research/` | Dual-helix narrative, case studies, publication roadmap |

**License split:** Python/scripts = [MIT](LICENSE). Markdown docs and KG content = [CC BY-NC 4.0](LICENSE-DOCS.md).

---

## Quickstart (5 minutes)

```bash
git clone https://github.com/Keven1894/AgentLoom.git
cd AgentLoom
python -m venv .venv

# Windows
.venv\Scripts\pip install -r requirements.txt
.venv\Scripts\python scripts/validators/run_all.py
.venv\Scripts\python -m uvicorn server.dashboard.app:app --port 8000 --host 127.0.0.1

# macOS/Linux
# source .venv/bin/activate && pip install -r requirements.txt
# python scripts/validators/run_all.py
# python -m uvicorn server.dashboard.app:app --port 8000 --host 127.0.0.1
```

Open **http://127.0.0.1:8000** → Proposals / Graph / Timeline tabs.

Or with Make (if installed):

```bash
make install && make validate-all && make dashboard
```

**Expected:** `PASS — all 8 Tier-A validator(s) succeeded.` and schema validation green for all 6 KG files.

---

## Core workflow

1. **Agent proposes** a KG node → `scripts/kg/propose_node.py` (or your host agent via `.clinerules/`)
2. **Human reviews** on dashboard `:8000` → Proposals tab
3. **Human accepts** → `scripts/kg/accept_proposal.py` (CLI only — governance gate)
4. **Validators enforce** → `make validate-all` (8 Tier-A rules + KG integrity)

Architecture details: [`docs/builder/architecture/agentloom-architecture.md`](docs/builder/architecture/agentloom-architecture.md)  
Propose-review protocol: [`docs/builder/protocols/propose-review-protocol.md`](docs/builder/protocols/propose-review-protocol.md)

---

## Optional: Cline host integration

Regenerate host rules from the canonical builder prompt in the KG:

```bash
python scripts/sync_clinerules.py --check   # expect: in sync
```

See `.clinerules/` for the Cline adaptation layer. **MCP server integration** (read-only KG tools for Cline)
is planned for **v4.0**; v3 ships the governance core only.

---

## Builder knowledge graph (v3)

| Graph | Nodes (approx.) | Purpose |
|-------|-----------------|---------|
| builder-knowledge | 10 | Architecture, propose-review, validator guide, catalog storytelling |
| builder-skills | 7 | KG maintenance, validation, multi-platform emit |
| builder-behaviors | 8 | Tier-A governance rules (executable validators) |

Domain graphs ship as **empty roots** — you populate them for your project via propose-review.

---

## Examples

Worked geospatial catalogs from the UCGIS 2026 workshop land in `examples/` in **v4.0**.
See [`examples/README.md`](examples/README.md).

---

## Ecosystem

- **[co-agenticOS](https://github.com/Keven1894/co-agenticOS)** — governance runtime layer
- **9-phase protocol** — [`agentloom-framework/agentLoom-v3/`](agentloom-framework/agentLoom-v3/) (setup manuals)
- **Research roadmap** — [`docs/START_HERE.md`](docs/START_HERE.md)

---

## Dual-helix architecture (why)

AgentLoom pairs two complementary loops:

- **Learning helix:** Context → Documentation → Indexing → RAG → Fine-Tuning
- **Governance helix:** Rules → Coordination → Memory boundaries → Verification → Adaptation

The v3 executable stack implements the **governance helix** as enforceable Tier-A validators and a
human-in-the-loop propose-review protocol — not just prompt text.

Full narrative: [`docs/dual-helix-clarification.md`](docs/dual-helix-clarification.md)

---

## Citation

```bibtex
@software{guan2026agentloom,
  author = {Guan, Boyuan (Keven)},
  title = {AgentLoom: Building Trustworthy AI Agents Through Dual-Helix Architecture},
  year = {2026},
  version = {3.0.0},
  url = {https://github.com/Keven1894/AgentLoom},
  doi = {10.5281/zenodo.17561541}
}
```

See also [`CITATION.cff`](CITATION.cff).

---

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Framework changes should pass `make validate-all` before PR.
