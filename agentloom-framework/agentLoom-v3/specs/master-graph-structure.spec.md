# Master Graph Specification

## Purpose

The `master-graph.json` file is the central registry that links all Knowledge Graphs and defines the agent's roles. It references BOTH Agent Builder graphs (standard) AND Domain Role graphs (custom).

---

## JSON Structure

```json
{
  "graphType": "master",
  "project": "<PROJECT_NAME>",
  "version": "2.0",
  "generatedAt": "<YYYY-MM-DD>",
  "graphs": [ /* Array of graph references */ ],
  "roles": [ /* Array of role definitions */ ]
}
```

---

## Required Fields

### Top Level

| Field | Type | Value | Source |
|-------|------|-------|--------|
| `graphType` | string | `"master"` | Fixed |
| `project` | string | Project name | Phase 1 |
| `version` | string | `"2.0"` | Fixed |
| `generatedAt` | string | ISO date | Current date |
| `graphs` | array | Graph references | See below |
| `roles` | array | Role definitions | See below |

---

## Graphs Array (BOTH Builder + Domain)

### Standard Builder Graphs (ALWAYS INCLUDE)

```json
{
  "id": "builder-knowledge",
  "path": "agents/knowledge-graphs/builder-knowledge-graph.json",
  "description": "System architecture and validation rules"
},
{
  "id": "builder-skills",
  "path": "agents/knowledge-graphs/builder-skills-graph.json",
  "description": "Capabilities for system modification"
},
{
  "id": "builder-behaviors",
  "path": "agents/knowledge-graphs/builder-behaviors-graph.json",
  "description": "Safety rules and behavior protocols for the Builder"
}
```

**Note**: These 3 entries are STANDARD. Copy from reference example.

### Domain Role Graphs (CUSTOM)

```json
{
  "id": "<DOMAIN_ROLE_ID>-knowledge",
  "path": "agents/knowledge-graphs/<DOMAIN_ROLE_ID>-knowledge-graph.json",
  "description": "<DOMAIN_KNOWLEDGE_DESCRIPTION>"
},
{
  "id": "<DOMAIN_ROLE_ID>-skills",
  "path": "agents/knowledge-graphs/<DOMAIN_ROLE_ID>-skills-graph.json",
  "description": "<DOMAIN_SKILLS_DESCRIPTION>"
},
{
  "id": "<DOMAIN_ROLE_ID>-behaviors",
  "path": "agents/knowledge-graphs/<DOMAIN_ROLE_ID>-behaviors-graph.json",
  "description": "<DOMAIN_BEHAVIORS_DESCRIPTION>"
}
```

**Variables** (from Phase 1):

- `DOMAIN_ROLE_ID`: e.g., "project-manager", "catalog-curator"
- `DOMAIN_KNOWLEDGE_DESCRIPTION`: Brief description of domain knowledge
- `DOMAIN_SKILLS_DESCRIPTION`: Brief description of domain capabilities
- `DOMAIN_BEHAVIORS_DESCRIPTION`: Brief description of domain protocols

### Optional: Project Graph

If the domain manages multiple projects/items:

```json
{
  "id": "project-graph",
  "path": "agents/knowledge-graphs/project-graph.json",
  "description": "Mirror of the Project Registry (All Managed Projects)"
}
```

**Note**: Only include if domain requires project/item tracking.

---

## Roles Array (BOTH Builder + Domain)

### Role 1: Agent Builder (STANDARD)

```json
{
  "id": "role-builder",
  "name": "The Agent Builder",
  "graphs": ["builder-knowledge", "builder-skills", "builder-behaviors"]
}
```

**Note**: This is STANDARD. Always include exactly as shown.

**Optional**: Add `"project-graph"` to graphs array if project graph exists.

### Role 2: Domain Role (CUSTOM)

```json
{
  "id": "role-<DOMAIN_ROLE_ID>",
  "name": "The <DOMAIN_ROLE_NAME>",
  "graphs": [
    "<DOMAIN_ROLE_ID>-knowledge",
    "<DOMAIN_ROLE_ID>-skills",
    "<DOMAIN_ROLE_ID>-behaviors"
  ]
}
```

**Variables** (from Phase 1):

- `DOMAIN_ROLE_ID`: e.g., "project-manager"
- `DOMAIN_ROLE_NAME`: e.g., "Project Manager"

**Optional**: Add `"project-graph"` to graphs array if project graph exists and domain role needs it.

---

## Complete Example Structure

```json
{
  "graphType": "master",
  "project": "GIS Data Catalog Manager",
  "version": "2.0",
  "generatedAt": "2025-11-28",
  "graphs": [
    {
      "id": "builder-knowledge",
      "path": "agents/knowledge-graphs/builder-knowledge-graph.json",
      "description": "System architecture and validation rules"
    },
    {
      "id": "builder-skills",
      "path": "agents/knowledge-graphs/builder-skills-graph.json",
      "description": "Capabilities for system modification"
    },
    {
      "id": "builder-behaviors",
      "path": "agents/knowledge-graphs/builder-behaviors-graph.json",
      "description": "Safety rules and behavior protocols for the Builder"
    },
    {
      "id": "catalog-curator-knowledge",
      "path": "agents/knowledge-graphs/catalog-curator-knowledge-graph.json",
      "description": "GIS dataset metadata and catalog structure"
    },
    {
      "id": "catalog-curator-skills",
      "path": "agents/knowledge-graphs/catalog-curator-skills-graph.json",
      "description": "Capabilities for catalog management"
    },
    {
      "id": "catalog-curator-behaviors",
      "path": "agents/knowledge-graphs/catalog-curator-behaviors-graph.json",
      "description": "Protocols for dataset curation"
    }
  ],
  "roles": [
    {
      "id": "role-builder",
      "name": "The Agent Builder",
      "graphs": ["builder-knowledge", "builder-skills", "builder-behaviors"]
    },
    {
      "id": "role-catalog-curator",
      "name": "The Catalog Curator",
      "graphs": ["catalog-curator-knowledge", "catalog-curator-skills", "catalog-curator-behaviors"]
    }
  ]
}
```

---

## Generation Instructions

1. **Read** reference example: `examples/master-graph.json`
2. **Extract** variables from Phase 1 output
3. **Generate** fresh JSON with:
   - 3 builder graph entries (copy from reference)
   - 3 domain graph entries (generate with domain role ID)
   - 2 role entries (builder standard + domain custom)
4. **Validate**: Run `python scripts/validate_graphs.py`

---

## Validation Criteria

- [ ] File exists at `agents/knowledge-graphs/master-graph.json`
- [ ] Valid JSON syntax
- [ ] Contains `graphType: "master"`
- [ ] Contains exactly 6 graph entries (3 builder + 3 domain)
- [ ] Contains exactly 2 role entries (builder + domain)
- [ ] All graph IDs match the pattern `<role-id>-<type>`
- [ ] All paths point to correct file locations
- [ ] No placeholder text remains

---

## Common Mistakes to Avoid

❌ **Don't**: Forget the builder graphs  
✅ **Do**: Include ALL 6 graphs (3 builder + 3 domain)

❌ **Don't**: Use inconsistent role IDs  
✅ **Do**: Match role IDs across identity.md and master-graph.json

❌ **Don't**: Copy-paste and replace placeholders  
✅ **Do**: Generate fresh JSON following this spec
