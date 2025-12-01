---
type: skill
category: system
id: skill-maintain-kg
roles:
  - role-builder
---

# Maintain Knowledge Graph

## Description

The high-level orchestration skill responsible for the lifecycle of the Knowledge Graph. It acts as the "Brain Surgeon" for the agent, ensuring memory integrity using the **json-helper toolkit** for all KG operations.

## Usage

This skill is triggered by:

1. **Scheduled Health Checks**: Periodic validation
2. **Event Triggers**: Detection of file system changes (via `kg-monitor`)
3. **Manual Request**: "Builder, resync the graph."

## Workflow

### 1. Trigger

`skill-kg-monitor` detects a change in tracked files.

### 2. Analyze

Determine if the change requires an Add, Update, or Delete operation.

### 3. Execute (using json-helper)

Call `skill-kg-update-node` which uses:

- `scripts/json-helper/kg_editor.py` for node operations
- Automatic backup before changes
- Validation before and after

### 4. Verify

- Run `scripts/json-helper/validator.py` for schema validation
- Call `skill-kg-heal` to ensure no broken links remain
- Run `scripts/validate_kg_links.py` for cross-reference validation

### 5. Commit

Persist changes to `agents/knowledge-graphs/*.json` (already saved by json-helper).

### 6. Visualize

Verify the changes appear correctly in `visualization.html`.

## Tools & Sub-Skills

### Primary Tools (json-helper toolkit)

- `scripts/json-helper/kg_editor.py` - High-level KG operations
- `scripts/json-helper/validator.py` - Schema validation
- `scripts/json-helper/updater.py` - Atomic updates
- `scripts/json-helper/generator.py` - Node templates

### Sub-Skills

- `skill-kg-monitor` - Detects file changes
- `skill-kg-update-node` - Executes CRUD operations
- `skill-kg-heal` - Repairs broken links
- `skill-validate-kg-links` - Validates cross-references

## Safety Features

✅ **Atomic Operations**: json-helper ensures all-or-nothing updates  
✅ **Automatic Backups**: Every change creates timestamped backup  
✅ **Validation Gates**: Pre/post validation prevents corruption  
✅ **Rollback Capability**: Restore from backup on failure  
✅ **Zero Corruption Risk**: No manual JSON editing

## Prerequisites

- Access to `agents/knowledge-graphs/`
- Read access to all tracked domains
- json-helper toolkit installed (see `requirements.txt`)

## Related

- Behavior: [graph-consistency](agents/behaviors/builder/graph-consistency.md)
- Uses: `scripts/json-helper/` toolkit
- Coordinates: All KG maintenance sub-skills

---

**Updated**: 2025-11-30 to use json-helper toolkit
