---
type: skill
category: system
id: skill-kg-update-node
roles:
  - role-builder
---

# Update Graph Node

## Description
The surgical capability to modify the JSON structure of a Knowledge Graph. Updates made here are immediately reflected in the `visualization.html` Unified View.

## Usage
Executes precise CRUD operations on graph nodes based on the "Change Set" from `kg-monitor`.

## Operations

### 1. Create Node
- **Input**: File path, category, type.
- **Logic**:
  - If path is in `.cursor/behaviors/`: Create `type: "behavior"`.
  - If path is in `agents/skills/`: Create `type: "skill"`.
  - If path is in `work/`: Create `type: "project"` or `type: "document"`.
- **Action**: Add to `nodes` array in the correct JSON file.

### 2. Update Metadata
- **Input**: Node ID, new metadata.
- **Action**: Merges new data (e.g., updated description from README) into existing node.

### 3. Delete Node
- **Input**: Node ID.
- **Action**: Removes node from `nodes` array AND removes any edges pointing to it in `links`.

## Safety Checks
- Validates JSON syntax before saving.
- Ensures ID uniqueness.
- Verifies that `type` aligns with the visualization schema (e.g., 'concept' gets a Star shape).

## Related
- Sub-skill of: [maintain-kg](agents/skills/system/maintain-kg.md)
