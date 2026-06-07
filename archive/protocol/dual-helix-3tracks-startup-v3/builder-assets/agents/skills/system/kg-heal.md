---
type: skill
category: system
id: skill-kg-heal
roles:
  - role-builder
---

# Heal Graph Links

## Description
The immune system of the Knowledge Graph. It identifies and repairs structural structural inconsistencies.

## Usage
Runs after any update operation or during periodic health checks.

## Capabilities

### 1. Prune Orphans
- Detects nodes that have no incoming or outgoing links (unless they are Roots).
- **Action**: Flag for review or auto-archive.

### 2. Fix Broken Edges
- Detects edges where `source` or `target` ID does not exist.
- **Action**: Delete the broken edge.

### 3. Re-Parenting
- Detects nodes with invalid `parent` IDs.
- **Action**: Attempt to find correct parent or move to `lost+found`.

## Related
- Sub-skill of: [maintain-kg](agents/skills/system/maintain-kg.md)

