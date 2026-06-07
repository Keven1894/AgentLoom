.PHONY: help install test kg-validate kg-validate-schemas kg-validate-integrity validate-behaviors validate-all kg-bootstrap dashboard sync-clinerules clean

help:
	@echo "AgentLoom v3 — executable framework targets:"
	@echo "  install              - pip install -e .[dev] (editable, src layout)"
	@echo "  test                 - run the pytest suite (wraps the governance gate)"
	@echo "  kg-validate          - JSON-schema + relational integrity for all KG files"
	@echo "  kg-validate-schemas  - JSON-schema validation only"
	@echo "  kg-validate-integrity - relational integrity for knowledge graphs"
	@echo "  validate-behaviors   - run all Tier-A behavior validators"
	@echo "  validate-all         - kg-validate + validate-behaviors (full governance gate)"
	@echo "  kg-bootstrap         - (re-)populate builder KGs with meta-nodes (idempotent)"
	@echo "  sync-clinerules      - regenerate .clinerules/ from builder-KG canonical prompt"
	@echo "  dashboard            - read-only KG dashboard at http://127.0.0.1:8000"

install:
	pip install -e .[dev]

test:
	python -m pytest

kg-validate:
	python -m agentloom.kg.validate_all

kg-validate-schemas:
	python -m agentloom.kg.validate_schemas

kg-validate-integrity:
	python -m agentloom.kg.validate_kg_integrity --all

validate-behaviors:
	python -m agentloom.validators.run_all

validate-all: kg-validate validate-behaviors

kg-bootstrap:
	python -m agentloom.kg.bootstrap_builder_kg

sync-clinerules:
	python -m agentloom.sync_clinerules

dashboard:
	python -m uvicorn agentloom.dashboard.app:app --reload --port 8000 --host 127.0.0.1

clean:
	rm -rf src/**/__pycache__ .pytest_cache *.egg-info src/*.egg-info
