---
type: skill
category: system
id: skill-maintain-kg
roles:
  - role-builder
---

# Maintain Knowledge Graph

## Description
The high-level orchestration skill responsible for the lifecycle of the Knowledge Graph. It acts as the "Brain Surgeon" for the agent, ensuring memory integrity.

## Usage
This skill is triggered by:
1.  **Scheduled Health Checks**: Periodic validation.
2.  **Event Triggers**: Detection of file system changes (via `kg-monitor`).
3.  **Manual Request**: "Builder, resync the graph."

## Workflow
1.  **Trigger**: `skill-kg-monitor` detects a change.
2.  **Analyze**: Determine if the change requires an Add, Update, or Delete operation.
3.  **Execute**: Call `skill-kg-update-node` to modify the JSON.
4.  **Verify**: Call `skill-kg-heal` to ensure no broken links remain.
5.  **Commit**: Persist changes to `agents/knowledge-graphs/*.json`.
6.  **Visualize**: Verify the changes appear correctly in `visualization.html`.

## Prerequisites
- Access to `agents/knowledge-graphs/`
- Read access to all tracked domains

## Related
- Behavior: [graph-consistency](agents/behaviors/builder/graph-consistency.md)
