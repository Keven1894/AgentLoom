---
type: skill
category: system
id: skill-kg-update-node
roles:
  - role-builder
---

# Update Graph Node

## Description

The surgical capability to modify the JSON structure of a Knowledge Graph using the **json-helper toolkit** for safe, atomic operations. Updates made here are immediately reflected in the `visualization.html` Unified View.

## Usage

Executes precise CRUD operations on graph nodes based on the "Change Set" from `kg-monitor`.

**Primary Tool**: `scripts/json-helper/kg_editor.py`

## Operations

### 1. Create Node

**Using json-helper**:

```bash
python scripts/json-helper/kg_editor.py <kg-file> add-skill \
  --id skill-new \
  --name "New Skill" \
  --category learning
```

- **Input**: Node type, ID, metadata
- **Logic**:
  - If path is in `.cursor/behaviors/`: Create `type: "behavior"`
  - If path is in `agents/skills/`: Create `type: "skill"`
  - If path is in `work/`: Create `type: "project"` or `type: "document"`
- **Action**: Uses `kg_editor.add_node()` with automatic validation

### 2. Update Metadata

**Using json-helper**:

```bash
python scripts/json-helper/kg_editor.py <kg-file> update-field \
  --node-id skill-123 \
  --field description \
  --value "Updated description"
```

- **Input**: Node ID, field name, new value
- **Action**: Uses `kg_editor.update_field()` with validation

### 3. Delete Node

**Using json-helper**:

```python
from json_helper import KGEditor

editor = KGEditor('agents/knowledge-graphs/builder-skills-graph.json')
editor.load()
result = editor.delete_node('skill-old')
if result.success:
    editor.save()
```

- **Input**: Node ID
- **Action**: Removes node AND any edges pointing to it
- **Safety**: Automatic backup before deletion

## Safety Features (via json-helper)

✅ **Atomic Operations**: All-or-nothing updates  
✅ **Automatic Backup**: Timestamped before every change  
✅ **Pre/Post Validation**: Ensures valid JSON and schema compliance  
✅ **Rollback Capability**: Restore from backup on failure  
✅ **ID Uniqueness**: Enforced by validator  
✅ **Type Verification**: Aligns with visualization schema

## Tools

- **Primary**: `scripts/json-helper/kg_editor.py` (high-level wrapper)
- **Advanced**: `scripts/json-helper/updater.py` (JSON Patch operations)
- **Validation**: `scripts/json-helper/validator.py` (schema validation)

## Related

- Sub-skill of: [maintain-kg](agents/skills/system/maintain-kg.md)
- Uses: `scripts/json-helper/` toolkit
- Governed by: `behavior:builder:consistency`

---

**Updated**: 2025-11-30 to use json-helper toolkit
