---
type: skill
category: system
id: skill-validate-graphs
roles:
  - role-builder
---

# Validate Knowledge Graphs

## Description
A capability to parse and verify the integrity of all JSON Knowledge Graphs.

## Usage
Run this when modifying graphs or after a bulk update to ensure no broken links.

## Execution
```bash
python scripts/validate_graphs.py
```

## Prerequisites
- Valid JSON syntax in graph files
- All referenced files must exist

## Related
- Behaviors: [enforce-schema](agents/behaviors/builder/enforce-schema.md)

