.PHONY: help install kg-validate kg-validate-schemas kg-validate-integrity validate-behaviors validate-all kg-bootstrap dashboard sync-clinerules clean

help:
	@echo "AgentLoom v3 — executable framework targets:"
	@echo "  install              - pip install -r requirements.txt"
	@echo "  kg-validate          - JSON-schema + relational integrity for all KG files"
	@echo "  kg-validate-schemas  - JSON-schema validation only"
	@echo "  kg-validate-integrity - relational integrity for knowledge graphs"
	@echo "  validate-behaviors   - run all Tier-A behavior validators"
	@echo "  validate-all         - kg-validate + validate-behaviors (full governance gate)"
	@echo "  kg-bootstrap         - (re-)populate builder KGs with meta-nodes (idempotent)"
	@echo "  sync-clinerules      - regenerate .clinerules/ from builder-KG canonical prompt"
	@echo "  dashboard            - read-only KG dashboard at http://127.0.0.1:8000"

install:
	pip install -r requirements.txt

kg-validate:
	python scripts/kg/validate_all.py

kg-validate-schemas:
	python scripts/kg/validate_schemas.py

kg-validate-integrity:
	python scripts/kg/validate_kg_integrity.py --all

validate-behaviors:
	python scripts/validators/run_all.py

validate-all: kg-validate validate-behaviors

kg-bootstrap:
	python scripts/kg/bootstrap_builder_kg.py

sync-clinerules:
	python scripts/sync_clinerules.py

dashboard:
	python -m uvicorn server.dashboard.app:app --reload --port 8000 --host 127.0.0.1

clean:
	rm -rf __pycache__ */__pycache__ .pytest_cache
