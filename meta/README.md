# Metadata Overview

This directory consolidates project-level metadata, indexing manifests, and cross-reference tables so collaborators and automated agents can discover authoritative context quickly.

## Contents

- `directory-index.yaml` — Canonical enumeration of every top-level folder and key files, including ownership notes and primary references.
- `search-manifest.json` — Machine-readable mapping of document categories to file paths to assist retrieval-augmented systems.

## Usage

1. **Human readers** should start with `directory-index.yaml` to understand where the framework package, governed KG data, docs, and archives live.
2. **Automation** (RAG pipelines, lint bots, orchestrators) can ingest `search-manifest.json` to narrow lookup scope without scanning the whole repo.
3. Update both files whenever a new folder is added or retired, or when a major document moves.

## Maintenance Policy

- Keep entries synchronized with the repository structure.
- Reference stable relative paths (e.g., `docs/guides/START_HERE.md`, `src/agentloom/kg/validate_all.py`).
- Note if a directory is archived or actively maintained.

_Last updated: 2026-06-07_
