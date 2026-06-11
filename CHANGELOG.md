# Changelog

All notable changes to the AgentLoom **executable framework** (code under
`src/agentloom/`). Documentation and research artifacts may evolve on separate
cadences.

## Why v3.0.0 after v1.10?

Version **1.x** on `main` was the **research + protocol** era: dual-helix
architecture docs, 9-phase manuals, and a flat `scripts/` + `server/` layout.

Version **3.0.0** is a **major packaging and scope reset**, not a linear v2:

- **Executable framework only** — KG governance, Tier-A validators,
  propose→review→accept, dashboard (authoring time).
- **`src/agentloom/` installable package** with `pyproject.toml` and CLI entry
  points (`agentloom-validate`, `agentloom-kg-validate`, `agentloom-sync-clinerules`).
- **Historical protocol** moved to `archive/protocol/` (reference, not the product).
- **Runtime memory/retrieval** lives in the sibling repo
  [agentloom-runtime](https://github.com/Keven1894/agentloom-runtime) (run time).
- **MCP server integration** deferred to v4 (preview in the
  [workshop repo](https://github.com/Keven1894/ucgis-agentloom-2026-workshop)).

There is no v2.0.0 tag on this repository; v3 reflects the public four-quadrant
ecosystem split (co-agenticOS → AgentLoom → agentloom-runtime → workshop).

---

## 3.0.0 — 2026-06-11

### Added

- Installable Python package under `src/agentloom/` (`pip install -e .[dev]`).
- Makefile targets: `validate-all`, `kg-validate`, `sync-clinerules`, `dashboard`.
- Pytest wrappers for the governance gate (`tests/test_validators.py`).
- GitHub Actions CI: `make validate-all` + pytest on push/PR.
- `SECURITY.md` vulnerability reporting policy.
- Four-quadrant ecosystem positioning in README (co-agenticOS, AgentLoom,
  agentloom-runtime, workshop).

### Changed

- **Breaking:** framework code moved from flat `scripts/` + `server/` to
  `src/agentloom/{kg,validators,agent,dashboard,viz}`.
- **Breaking:** invoke tools via `python -m agentloom.*` or installed CLI scripts,
  not `python scripts/kg/...`.
- KG JSON schema validator paths updated for the new package layout.
- `.clinerules/` regenerated from builder KG canonical prompt.

### Removed / archived

- Research layer removed from the flagship tree (use `archive/protocol/` for
  historical v1/v3 design docs).
- Workshop-only and MCP scripts excluded from this repo (v4 boundary).

### Migration (v1.10 flat layout → v3)

```bash
pip install -e .[dev]
make validate-all          # expect PASS on all Tier-A validators + KG schemas
python -m agentloom.sync_clinerules --check
```

Old paths such as `scripts/kg/validate_all.py` → `python -m agentloom.kg.validate_all`.

---

## 1.10 and earlier

See git history on `main` before the v3 merge (`release v1.10` and prior tags).
Those releases documented the dual-helix research framework and protocol manuals;
they remain available via tags and `archive/protocol/`.
