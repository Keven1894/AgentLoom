# Knowledge Graph JSON Specification

## Purpose

Define the schema and requirements for all Knowledge Graph JSON files.

## Schema Version

2.0 (Fully Connected)

## Common Schema (All Graph Types)

```json
{
  "graphType": "master | knowledge | skills | behaviors",
  "role": "agent-builder | {domain-role-id}",
  "project": "{PROJECT_NAME}",
  "generatedAt": "YYYY-MM-DD",
  "description": "Human-readable description",
  "nodes": [ ... ] 
}
```

## Node Schema

### Required Fields (All Nodes)

```json
{
  "id": "string (unique, kebab-case with colons for namespacing)",
  "type": "root | folder | component | document | concept | skill | behavior | ..."
}
```

### Required for Non-Root Nodes

```json
{
  "parent": "string (must reference existing node id)"
}
```

### Optional Fields

```json
{
  "title": "string (human-readable name)",
  "name": "string (alternative to title)",
  "description": "string",
  "path": "string (file path if applicable)",
  "links": {
    "enforces": ["node-id", ...],
    "implements": ["node-id", ...],
    "governs": ["node-id", ...],
    "tracks": ["node-id", ...]
  }
}
```

## Node ID Conventions

### System Nodes

- `sys:root` - System architecture root
- `sys:{component}` - System components
- `sys:{component}:{sub}` - Nested components

### Role-Specific Nodes

- `{role-id}:root` - Role root
- `{role-id}:{category}` - Role categories
- `{role-id}:{category}:{item}` - Specific items

### Skills

- `skill:{role}:root` - Skills root for role
- `skill-{skill-name}` - Individual skill

### Behaviors  

- `behavior:{role}:root` - Behaviors root for role
- `behavior:{role}:{behavior-name}` - Individual behavior
- `behavior:core:{behavior-name}` - Core behaviors (apply to all)

## V2 Connectivity Rules

### CRITICAL: Parent Requirement

Every node EXCEPT root nodes MUST have a `parent` field pointing to an existing node.

### Graph Hierarchy

```
root
├── category-1 (parent: root)
│   ├── item-1 (parent: category-1)
│   └── item-2 (parent: category-1)
└── category-2 (parent: root)
    └── item-3 (parent: category-2)
```

### Cross-Graph Links

Use `links` object for semantic relationships across graphs:

```json
{
  "id": "behavior:builder:kg-consistency",
  "links": {
    "enforces": ["skill-maintain-kg"]
  }
}
```

## Graph Types

### Master Graph

Entry point listing all other graphs.

```json
{
  "graphType": "master",
  "graphs": [
    { "id": "graph-key", "path": "filename.json", "description": "..." }
  ],
  "roles": [
    { "id": "role-id", "name": "Role Name", "alwaysActive": true|false, "graphs": ["..."] }
  ]
}
```

### Knowledge Graph

Understanding and concepts for a role.

- Nodes represent: folders, documents, concepts, components

### Skills Graph  

Capabilities for a role.

- Nodes represent: skills (with implementation type)
- Include: `implementation: "rule-based | llm-based-max | llm-based-slm | hybrid"`

### Behaviors Graph

Protocols and rules for a role.

- Nodes represent: behaviors with priority
- Include: `priority: "critical | high | medium | low"`

## Required Graphs per Agent

### Agent Builder (System Role) - STANDARD

1. `agent-builder-knowledge-graph.json`
2. `agent-builder-skills-graph.json`
3. `agent-builder-behaviors-graph.json`

### Domain Role (Custom) - GENERATED

1. `{domain-role-id}-knowledge-graph.json`
2. `{domain-role-id}-skills-graph.json`
3. `{domain-role-id}-behaviors-graph.json`

### Master Graph - GENERATED

1. `master-graph.json`

### Optional

1. `{domain}-content-graph.json` (if content folders provided)

## Validation Rules

1. **Valid JSON**: Must parse without errors
2. **Has Root**: Every graph must have exactly one node with `type: "root"`
3. **All Connected**: Every non-root node must have `parent` field
4. **Valid Parents**: Every `parent` value must reference an existing node `id`
5. **No Cycles**: Following parent links must not create loops
6. **Valid Links**: All `links` targets should exist (warning, not error)
