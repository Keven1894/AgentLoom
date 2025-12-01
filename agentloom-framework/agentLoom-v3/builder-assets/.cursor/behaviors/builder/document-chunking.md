---
type: behavior
category: builder
id: behavior:builder:document-chunking
priority: high
roles:
  - role-builder
---

# Behavior: Document Chunking Governance

## Description

Enforces the "Small File / Single Concept" architecture for all AI-consumed documentation. This ensures the system remains maintainable and comprehensible to LLMs with limited working memory.

## Triggers

- **Pre-Commit**: Before finalizing any task involving documentation updates.
- **KG Maintenance**: When `skill-validate-chunking` reports an "oversized" file.
- **Content Generation**: When creating new documentation.

## Rules

### 1. The 500-Line Hard Limit

- **Rule**: No AI-consumed markdown file (`docs/`, `skills/`, `behaviors/`) should exceed **500 lines**.
- **Action**: If a file grows > 500 lines, you MUST trigger `skill-chunk-document` to split it.
- **Exception**: Human-only manuals (`USER_MANUAL.md`) are exempt.

### 2. Separation of Concerns

- **Rule**: Distinctly separate **Concept** (What/Why) from **Execution** (How/Steps).
- **Pattern**:
  - `feature-concept.md`: Theory, rules, architecture.
  - `feature-execution.md`: Scripts, commands, step-by-step guides.
- **Action**: If a file mixes these (e.g., long theory intro followed by code), split it.

### 3. The Index Pattern

- **Rule**: Any folder with > 3 related files MUST have an `INDEX.md`.
- **Content**: The Index must link to all child files and explain their relationship.
- **Benefit**: Allows agents to read *only* the Index to navigate, saving context.

### 4. Metadata Tracking

- **Rule**: Maintain `.meta.json` in documentation folders to track chunking status.
- **Action**: Update this metadata when files are added or split.

## Enforcement Workflow

1. **Check**: Run `python scripts/validate_chunking.py [folder]`.
2. **Detect**: Identify files with `status: oversized`.
3. **Remediate**:
    - **Plan**: Analyze split points (Concept vs Execution).
    - **Execute**: Use `skill-chunk-document` or manual refactoring.
    - **Verify**: Re-run validation to confirm compliance.

## Interaction with Other Skills

- **`skill-validate-chunking`**: The detector. Use this first.
- **`skill-chunk-document`**: The fixer. Use this when validation fails.
- **`skill-maintain-kg`**: The updater. Ensure KG nodes are updated after splitting.
