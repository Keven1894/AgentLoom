# Domain Role Graphs Specification

## Purpose

Domain Role graphs are CUSTOM for each project. Unlike Agent Builder (standard), these must be generated based on the specific domain requirements gathered in Phase 1-2.

## Input Required

Before generating, the agent MUST have collected:

### From Phase 1 (Information Discovery)

- `DOMAIN_ROLE_NAME`: Human-readable name (e.g., "Catalog Curator", "Project Manager")
- `DOMAIN_ROLE_ID`: Kebab-case ID (e.g., "catalog-curator", "project-manager")
- `DOMAIN_ID`: Domain prefix for content (e.g., "gis-catalog", "project-management")
- Domain tasks (3-5 primary responsibilities)
- Domain concepts (key terminology and ideas)
- Domain boundaries (what the role won't do)

### From Phase 2 (Architecture Design)

- Skills list with classifications (rule-based, llm-based-max, llm-based-slm, hybrid)
- Behaviors list with priorities (critical, high, medium, low)
- Knowledge categories (what the role needs to understand)

---

## 1. Domain Knowledge Graph

**File**: `agents/knowledge-graphs/{DOMAIN_ROLE_ID}-knowledge-graph.json`

### Structure

```json
{
  "graphType": "knowledge",
  "role": "{DOMAIN_ROLE_ID}",
  "project": "{PROJECT_NAME}",
  "generatedAt": "YYYY-MM-DD",
  "description": "{DOMAIN_ROLE_NAME}'s understanding of the domain",
  "nodes": [ ... ]
}
```

### Required Nodes

| Node Pattern | Type | Parent | Description |
|--------------|------|--------|-------------|
| `{DOMAIN_ROLE_ID}:root` | root | - | Root of domain knowledge |
| `{DOMAIN_ROLE_ID}:docs` | folder | root | Documentation folder |
| `{DOMAIN_ROLE_ID}:concepts` | folder | root | Key domain concepts |
| `{DOMAIN_ROLE_ID}:concepts:{concept-id}` | concept | concepts | One per key concept from Phase 1 |

### Optional Nodes (Based on Phase 1)

| Node Pattern | Type | Parent | When to Include |
|--------------|------|--------|-----------------|
| `{DOMAIN_ROLE_ID}:workflows` | folder | root | If workflows defined in Phase 1 |
| `{DOMAIN_ROLE_ID}:workflows:{workflow-id}` | concept | workflows | One per workflow |
| `{DOMAIN_ROLE_ID}:resources` | folder | root | If external resources referenced |

### Example Generation

**Given**:

- DOMAIN_ROLE_ID = "catalog-curator"
- DOMAIN_ROLE_NAME = "Catalog Curator"
- Concepts from Phase 1: metadata standards, data quality, spatial indexing

**Generate**:

```json
{
  "graphType": "knowledge",
  "role": "catalog-curator",
  "project": "GIS Data Catalog Manager",
  "generatedAt": "2025-11-28",
  "description": "Catalog Curator's understanding of GIS data management",
  "nodes": [
    {
      "id": "catalog-curator:root",
      "type": "root",
      "title": "Catalog Curator Knowledge"
    },
    {
      "id": "catalog-curator:docs",
      "type": "folder",
      "path": "docs/catalog-curator/",
      "title": "Curator Documentation",
      "parent": "catalog-curator:root",
      "description": "Guides and references for catalog curation"
    },
    {
      "id": "catalog-curator:concepts",
      "type": "folder",
      "title": "Domain Concepts",
      "parent": "catalog-curator:root",
      "description": "Key GIS catalog concepts"
    },
    {
      "id": "catalog-curator:concepts:metadata-standards",
      "type": "concept",
      "title": "Metadata Standards",
      "parent": "catalog-curator:concepts",
      "description": "ISO 19115, FGDC, and Dublin Core metadata standards"
    },
    {
      "id": "catalog-curator:concepts:data-quality",
      "type": "concept",
      "title": "Data Quality",
      "parent": "catalog-curator:concepts",
      "description": "Completeness, accuracy, and consistency metrics"
    },
    {
      "id": "catalog-curator:concepts:spatial-indexing",
      "type": "concept",
      "title": "Spatial Indexing",
      "parent": "catalog-curator:concepts",
      "description": "Geographic extent and coordinate reference systems"
    }
  ]
}
```

---

## 2. Domain Skills Graph

**File**: `agents/knowledge-graphs/{DOMAIN_ROLE_ID}-skills-graph.json`

### Structure

```json
{
  "graphType": "skills",
  "role": "{DOMAIN_ROLE_ID}",
  "project": "{PROJECT_NAME}",
  "generatedAt": "YYYY-MM-DD",
  "description": "{DOMAIN_ROLE_NAME}'s capabilities",
  "nodes": [ ... ]
}
```

### Required Nodes

| Node Pattern | Type | Parent | Fields |
|--------------|------|--------|--------|
| `skill:{DOMAIN_ROLE_ID}:root` | root | - | name, description |
| `skill-{skill-id}` | skill | root or orchestrator | name, description, implementation, path |

### Skill Node Fields

Every skill node MUST have:

- `id`: Unique identifier (skill-{name})
- `type`: "skill"
- `name`: Human-readable name
- `description`: What the skill does
- `parent`: Reference to root or parent skill
- `implementation`: One of:
  - `"rule-based"` - Python/shell script, $0 cost
  - `"llm-based-slm"` - Simple LLM task, low cost
  - `"llm-based-max"` - Complex reasoning, higher cost
  - `"hybrid"` - Rules + LLM + Rules

Optional fields:

- `path`: File path to skill definition
- `links`: Cross-references to behaviors

### Orchestrator Skills (Skill Trees)

If a skill has sub-skills, it's an orchestrator:

```json
{
  "id": "skill-analyze-catalog",
  "type": "skill",
  "name": "Analyze Catalog",
  "parent": "skill:catalog-curator:root",
  "implementation": "hybrid",
  "description": "Orchestrator for catalog analysis"
},
{
  "id": "skill-scan-entries",
  "type": "skill",
  "name": "Scan Entries",
  "parent": "skill-analyze-catalog",  // Parent is orchestrator, not root
  "implementation": "rule-based",
  "description": "Scan catalog for entries"
}
```

### Example Generation

**Given**:

- DOMAIN_ROLE_ID = "catalog-curator"
- Skills from Phase 2:
  - Validate Metadata (rule-based)
  - Generate Description (llm-based-slm)
  - Analyze Quality (hybrid)
  - Suggest Improvements (llm-based-max)

**Generate**:

```json
{
  "graphType": "skills",
  "role": "catalog-curator",
  "project": "GIS Data Catalog Manager",
  "generatedAt": "2025-11-28",
  "description": "Catalog Curator's capabilities",
  "nodes": [
    {
      "id": "skill:catalog-curator:root",
      "type": "root",
      "name": "Catalog Curator Capabilities",
      "description": "Root of Catalog Curator skill tree"
    },
    {
      "id": "skill-validate-metadata",
      "type": "skill",
      "name": "Validate Metadata",
      "description": "Check metadata against standards (ISO 19115, FGDC)",
      "parent": "skill:catalog-curator:root",
      "implementation": "rule-based",
      "path": "agents/skills/catalog-curator/validate-metadata.md",
      "links": {
        "implements": ["behavior:catalog-curator:quality-assurance"]
      }
    },
    {
      "id": "skill-generate-description",
      "type": "skill",
      "name": "Generate Description",
      "description": "Create human-readable descriptions from metadata",
      "parent": "skill:catalog-curator:root",
      "implementation": "llm-based-slm",
      "path": "agents/skills/catalog-curator/generate-description.md"
    },
    {
      "id": "skill-analyze-quality",
      "type": "skill",
      "name": "Analyze Quality",
      "description": "Comprehensive quality analysis orchestrator",
      "parent": "skill:catalog-curator:root",
      "implementation": "hybrid",
      "path": "agents/skills/catalog-curator/analyze-quality.md",
      "links": {
        "implements": ["behavior:catalog-curator:quality-assurance"]
      }
    },
    {
      "id": "skill-suggest-improvements",
      "type": "skill",
      "name": "Suggest Improvements",
      "description": "AI-powered improvement recommendations",
      "parent": "skill:catalog-curator:root",
      "implementation": "llm-based-max",
      "path": "agents/skills/catalog-curator/suggest-improvements.md"
    }
  ]
}
```

---

## 3. Domain Behaviors Graph

**File**: `agents/knowledge-graphs/{DOMAIN_ROLE_ID}-behaviors-graph.json`

### Structure

```json
{
  "graphType": "behaviors",
  "role": "{DOMAIN_ROLE_ID}",
  "project": "{PROJECT_NAME}",
  "generatedAt": "YYYY-MM-DD",
  "description": "{DOMAIN_ROLE_NAME}'s protocols",
  "nodes": [ ... ]
}
```

### Required Nodes

| Node Pattern | Type | Parent | Fields |
|--------------|------|--------|--------|
| `behavior:{DOMAIN_ROLE_ID}:root` | root | - | name, description |
| `behavior:{DOMAIN_ROLE_ID}:{behavior-id}` | role-specific | root | name, description, priority, path |

### Behavior Node Fields

Every behavior node MUST have:

- `id`: Unique identifier
- `type`: "root", "core", or "role-specific"
- `name`: Human-readable name
- `description`: What the behavior ensures
- `parent`: Reference to root
- `priority`: One of "critical", "high", "medium", "low"

Optional fields:

- `path`: File path to behavior definition
- `links`: Cross-references to skills and components

### Priority Guidelines

| Priority | When to Use |
|----------|-------------|
| critical | Safety, data integrity, security |
| high | Core functionality, quality standards |
| medium | Best practices, workflows |
| low | Preferences, nice-to-haves |

### Example Generation

**Given**:

- DOMAIN_ROLE_ID = "catalog-curator"
- Behaviors from Phase 2:
  - Data Integrity (critical)
  - Quality Assurance (high)
  - Documentation Standards (medium)
  - User Communication (medium)

**Generate**:

```json
{
  "graphType": "behaviors",
  "role": "catalog-curator",
  "project": "GIS Data Catalog Manager",
  "generatedAt": "2025-11-28",
  "description": "Catalog Curator's protocols",
  "nodes": [
    {
      "id": "behavior:catalog-curator:root",
      "type": "root",
      "name": "Catalog Curator Behaviors",
      "description": "Core protocols for catalog curation"
    },
    {
      "id": "behavior:catalog-curator:data-integrity",
      "type": "role-specific",
      "name": "Data Integrity",
      "description": "Never modify source data; work on copies only",
      "parent": "behavior:catalog-curator:root",
      "priority": "critical",
      "path": ".cursor/behaviors/catalog-curator/data-integrity.md",
      "links": {
        "governs": ["catalog-curator:concepts:data-quality"]
      }
    },
    {
      "id": "behavior:catalog-curator:quality-assurance",
      "type": "role-specific",
      "name": "Quality Assurance",
      "description": "Validate all metadata before publishing",
      "parent": "behavior:catalog-curator:root",
      "priority": "high",
      "path": ".cursor/behaviors/catalog-curator/quality-assurance.md",
      "links": {
        "enforces": ["skill-validate-metadata", "skill-analyze-quality"]
      }
    },
    {
      "id": "behavior:catalog-curator:documentation-standards",
      "type": "role-specific",
      "name": "Documentation Standards",
      "description": "Follow ISO 19115 and FGDC guidelines",
      "parent": "behavior:catalog-curator:root",
      "priority": "medium",
      "path": ".cursor/behaviors/catalog-curator/documentation-standards.md"
    },
    {
      "id": "behavior:catalog-curator:user-communication",
      "type": "role-specific",
      "name": "User Communication",
      "description": "Explain technical concepts in accessible language",
      "parent": "behavior:catalog-curator:root",
      "priority": "medium",
      "path": ".cursor/behaviors/catalog-curator/user-communication.md"
    }
  ]
}
```

---

## 4. Content Graph (Optional)

**File**: `agents/knowledge-graphs/{DOMAIN_ID}-content-graph.json`

Only generate if content folders were provided in Phase 1.

### Structure

```json
{
  "graphType": "knowledge",
  "role": "{DOMAIN_ROLE_ID}",
  "project": "{PROJECT_NAME}",
  "generatedAt": "YYYY-MM-DD",
  "description": "{DOMAIN_ID} content structure",
  "source": "Phase 1 shared folders",
  "nodes": [ ... ]
}
```

### Node Generation Rules

1. **Root node**: `{DOMAIN_ID}:content:root`
2. **Folder nodes**: One for each directory
   - `id`: `{DOMAIN_ID}:content:{folder-name}`
   - `type`: "folder"
   - `parent`: Parent folder or root
3. **Document nodes**: One for each significant file
   - `id`: `{DOMAIN_ID}:content:{folder}:{filename}`
   - `type`: "document"
   - `parent`: Containing folder

### Example

**Given**: Shared folder with structure:

```
gis-data/
├── metadata/
│   ├── standards.md
│   └── templates/
│       └── iso-template.xml
└── catalogs/
    └── main-catalog.json
```

**Generate**:

```json
{
  "graphType": "knowledge",
  "role": "catalog-curator",
  "project": "GIS Data Catalog Manager",
  "generatedAt": "2025-11-28",
  "description": "GIS catalog content structure",
  "source": "Phase 1 shared folders",
  "nodes": [
    {
      "id": "gis-catalog:content:root",
      "type": "root",
      "title": "GIS Catalog Content"
    },
    {
      "id": "gis-catalog:content:metadata",
      "type": "folder",
      "path": "docs/catalog-curator/metadata/",
      "title": "Metadata",
      "parent": "gis-catalog:content:root"
    },
    {
      "id": "gis-catalog:content:metadata:standards",
      "type": "document",
      "path": "docs/catalog-curator/metadata/standards.md",
      "title": "Standards Guide",
      "parent": "gis-catalog:content:metadata"
    },
    {
      "id": "gis-catalog:content:metadata:templates",
      "type": "folder",
      "path": "docs/catalog-curator/metadata/templates/",
      "title": "Templates",
      "parent": "gis-catalog:content:metadata"
    },
    {
      "id": "gis-catalog:content:metadata:templates:iso",
      "type": "document",
      "path": "docs/catalog-curator/metadata/templates/iso-template.xml",
      "title": "ISO Template",
      "parent": "gis-catalog:content:metadata:templates"
    },
    {
      "id": "gis-catalog:content:catalogs",
      "type": "folder",
      "path": "docs/catalog-curator/catalogs/",
      "title": "Catalogs",
      "parent": "gis-catalog:content:root"
    },
    {
      "id": "gis-catalog:content:catalogs:main",
      "type": "document",
      "path": "docs/catalog-curator/catalogs/main-catalog.json",
      "title": "Main Catalog",
      "parent": "gis-catalog:content:catalogs"
    }
  ]
}
```

---

## Validation Checklist

After generating all domain role graphs, verify:

1. **Valid JSON**: All files parse without errors
2. **Root nodes**: Each graph has exactly one root node
3. **Parent links**: Every non-root node has `parent` field
4. **Valid parents**: Every `parent` references an existing node ID
5. **No placeholders**: No `{DOMAIN_ROLE_ID}` or similar text remains
6. **Cross-links valid**: All `links` targets exist (warning only)
7. **Implementation types**: All skills have valid implementation field
8. **Priority values**: All behaviors have valid priority field

Run:

```bash
python scripts/validate_generation.py agents/knowledge-graphs/
python scripts/validate_graphs.py
```
