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
| **Runnable framework (v3)** | `src/agentloom/` | KG governance, validators, dashboard, propose-review (installable package) |
| **Governed data** | `agents/knowledge-graphs/`, `agents/skills/` | Knowledge graphs, skills, and behaviors the framework enforces |
| **Docs** | `docs/` | Guides, builder concepts, release notes |
| **Historical protocol** | `archive/protocol/` | Earlier v1/v2/v3 design docs and 9-phase manuals (reference only) |

**License split:** Python/scripts = [MIT](LICENSE). Markdown docs and KG content = [CC BY-NC 4.0](LICENSE-DOCS.md).

---

## Quickstart (5 minutes)

```bash
git clone https://github.com/Keven1894/AgentLoom.git
cd AgentLoom
python -m venv .venv

# Windows
.venv\Scripts\pip install -e .[dev]
.venv\Scripts\python -m agentloom.validators.run_all
.venv\Scripts\python -m uvicorn agentloom.dashboard.app:app --port 8000 --host 127.0.0.1

# macOS/Linux
# source .venv/bin/activate && pip install -e .[dev]
# python -m agentloom.validators.run_all
# python -m uvicorn agentloom.dashboard.app:app --port 8000 --host 127.0.0.1
```

Open **http://127.0.0.1:8000** → Proposals / Graph / Timeline tabs.

Or with Make (if installed):

```bash
make install && make validate-all && make dashboard
```

**Expected:** `PASS — all 8 Tier-A validator(s) succeeded.` and schema validation green for all 6 KG files.

---

## How to use this repo

Two consumption modes:

1. **As a scaffold (primary).** Clone it as the starting point for your own
   governed agent. The builder graphs ship populated (governance rules,
   validators, skills); the **domain graphs ship empty** — you fill them with
   your project's knowledge through the propose-review workflow below.
2. **As a tool.** `pip install -e .` gives you the governance CLI anywhere:
   `agentloom-validate` (Tier-A behavior validators), `agentloom-kg-validate`
   (KG schema + integrity), and `agentloom-sync-clinerules` (host-rule sync).

For a worked, forkable instance built this way, see the
[UCGIS 2026 workshop repo](https://github.com/Keven1894/ucgis-agentloom-2026-workshop).

---

## Core workflow

1. **Agent proposes** a KG node → `python -m agentloom.kg.propose_node` (or your host agent via `.clinerules/`)
2. **Human reviews** on dashboard `:8000` → Proposals tab
3. **Human accepts** → `python -m agentloom.kg.accept_proposal` (CLI only — governance gate)
4. **Validators enforce** → `make validate-all` (8 Tier-A rules + KG integrity)

Architecture details: [`docs/builder/architecture/agentloom-architecture.md`](docs/builder/architecture/agentloom-architecture.md)  
Propose-review protocol: [`docs/builder/protocols/propose-review-protocol.md`](docs/builder/protocols/propose-review-protocol.md)

---

## Optional: Cline host integration

Regenerate host rules from the canonical builder prompt in the KG:

```bash
python -m agentloom.sync_clinerules --check   # expect: in sync
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

Four repos, four roles — split by *what they are* and by *agent lifecycle phase*:

| Repo | Role | Lifecycle phase |
|------|------|-----------------|
| [**co-agenticOS**](https://github.com/Keven1894/co-agenticOS) | Governance **spec** — rules, coordination, memory boundaries, verification | sets the rules |
| **AgentLoom** (this repo) | Build **framework** — KG governance, validators, propose-review-accept | **authoring time** (build & govern the agent) |
| **AgentLoom Runtime** | Runtime **library** — layered memory, graph-first retrieval, file→DB sync | **run time** (the deployed agent remembers & retrieves) |
| [**ucgis-agentloom-2026-workshop**](https://github.com/Keven1894/ucgis-agentloom-2026-workshop) | A concrete **instance** — a worked, forkable example | a use of all of the above |

> co-agenticOS sets the rules → AgentLoom is the framework you build and govern
> an agent with (authoring time) → AgentLoom Runtime is the library the deployed
> agent uses to remember and retrieve (run time) → the workshop repo is one
> concrete instance that puts all of them to work.

Historical protocol manuals (v1–v3 design docs) live in
[`archive/protocol/`](archive/protocol/). New readers start at
[`docs/guides/START_HERE.md`](docs/guides/START_HERE.md).

---

## Dual-helix architecture (why)

AgentLoom pairs two complementary loops:

- **Learning helix:** Context → Documentation → Indexing → RAG → Fine-Tuning
- **Governance helix:** Rules → Coordination → Memory boundaries → Verification → Adaptation

The v3 executable stack implements the **governance helix** as enforceable Tier-A validators and a
human-in-the-loop propose-review protocol — not just prompt text.

Full narrative: [co-agenticOS](https://github.com/Keven1894/co-agenticOS) (governance spec) and the design docs under [`archive/protocol/agentLoom-v3/`](archive/protocol/agentLoom-v3/).

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
