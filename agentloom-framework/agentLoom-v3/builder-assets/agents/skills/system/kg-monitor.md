---
type: skill
category: system
id: skill-kg-monitor
roles:
  - role-builder
---

# Monitor File System

## Description
The sensory capability to detect changes in the file system and map them to specific Knowledge Graph updates.

## Usage
Scans tracked directories to identify new, modified, or deleted files.

## Domain-to-Graph Mapping

| Change Location | Target Graph | Action Type |
|----------------|--------------|-------------|
| `agents/skills/` | `*-skills-graph.json` | Update Skill Nodes |
| `.cursor/behaviors/` | `*-behaviors-graph.json` | Update Behavior Nodes |
| `.cursor/rules.md` | `*-behaviors-graph.json` | Update Core Rules |
| `public/*`, `personal/*`, `work/*` | `project-graph.json` | Update Project/Doc Nodes |
| `docs/` | `manager-knowledge-graph.json` | Update Shared Documentation |
| `presentation/` | `manager-knowledge-graph.json` | Update Assets |
| `agents/knowledge-graphs/` | `master-graph.json` | Update System Meta-State |

## Implementation Details
- **Diffing**: Compares current file listing against paths stored in the target JSON graphs.
- **Filtering**: Ignores `.git`, `node_modules`, `temp/`.

## Output
Returns a "Change Set" categorized by target graph:
```json
{
  "project-graph": { "added": [...], "modified": [...] },
  "builder-behaviors-graph": { "added": [...] }
}
```

## Related
- Sub-skill of: [maintain-kg](agents/skills/system/maintain-kg.md)
