# Knowledge Graph Schema Reference

**Framework**: 3-Track Knowledge Graph System  
**Purpose**: Formal schema definition for all knowledge graphs  
**Last Updated**: 2025-11-15

---

## 📊 Overview

The 3-Track Knowledge Graph system uses three interconnected JSON files to represent relationships between behaviors, knowledge, and skills.

---

## 🔷 Node Types

### 1. Skill Node (skills-graph.json)

**Schema**:
```json
{
  "id": "skill-XXX",
  "name": "Skill Name",
  "category": "category-name",
  "status": "production|development",
  "script": "path/to/script.py",
  "type": "script|procedure|workflow",
  "frequency": "daily|weekly|monthly|as-needed",
  "dependencies": ["skill-YYY"],
  "enables": ["skill-ZZZ"],
  "part_of": ["skill-AAA"],
  "related_to": ["skill-BBB"],
  "implements": ["cursor://path/to/rule.md"],
  "references": ["docs://path/to/doc.md"]
}
```

**Fields**:
- **id**: Unique identifier (skill-001 to skill-025)
- **name**: Human-readable skill name
- **category**: One of: data-operations, metadata-operations, system-operations, documentation, qa-operations, communication, development
- **status**: production (active) or development (in progress)
- **script**: Path to actual script file (optional for procedures)
- **type**: script (executable), procedure (manual), workflow (composite)
- **frequency**: How often the skill is used
- **dependencies**: Skills that must run before this one
- **enables**: Skills that can run after this one
- **part_of**: Workflows this skill belongs to
- **related_to**: Similar or complementary skills
- **implements**: Behavior rules this skill implements
- **references**: Documentation this skill uses

---

### 2. Document Node (docs-graph.json)

**Schema**:
```json
{
  "id": "docs-category-name",
  "path": "docs/category/filename.md",
  "type": "procedure|standard|reference|tracking|architecture|diagram|templates|navigation|documentation|configuration",
  "category": "infrastructure|architecture|procedures|standards|configuration|meetings|project|meta",
  "implements": ["skill-XXX"],
  "references": ["docs-YYY"],
  "referenced_by": ["skill-ZZZ", "docs-AAA", "cursor-BBB"],
  "related_to": ["docs-CCC"],
  "contains": ["item1", "item2"],
  "phases": ["phase1", "phase2"]
}
```

**Fields**:
- **id**: Unique identifier (docs-category-name)
- **path**: Relative path from project root
- **type**: Document classification
- **category**: Documentation category
- **implements**: Skills this doc enables
- **references**: Other docs this one links to
- **referenced_by**: Skills, docs, or behaviors that reference this
- **related_to**: Similar or complementary docs
- **contains**: Sub-items or sections (for directories)
- **phases**: Process phases (for workflow docs)

---

### 3. Behavior Node (cursor-graph.json)

**Schema**:
```json
{
  "id": "cursor-category-name",
  "path": ".cursor/path/to/file.md",
  "type": "identity|context|core_rule|action_rule|workflow_rule|standard_rule",
  "category": "core|actions|workflows|standards",
  "priority": "critical|high|medium|low",
  "implements_skills": ["skill-XXX"],
  "related_skills": ["skill-YYY"],
  "references": ["docs-ZZZ", "skill-AAA"],
  "referenced_by": ["all_behaviors"],
  "triggers": ["trigger phrase 1", "trigger phrase 2"],
  "applies_to": ["all_actions", "all_outputs"],
  "defines": ["property1", "property2"],
  "protocols": ["protocol1", "protocol2"],
  "team_members": ["keven", "jennifer", "taylor"]
}
```

**Fields**:
- **id**: Unique identifier (cursor-category-name)
- **path**: Relative path from project root
- **type**: Behavior classification
- **category**: Behavior grouping
- **priority**: Execution priority
- **implements_skills**: Skills this behavior directly implements
- **related_skills**: Skills loosely related to this behavior
- **references**: Docs or other resources this behavior uses
- **referenced_by**: Other behaviors that depend on this
- **triggers**: Phrases that invoke this behavior
- **applies_to**: Scope of application
- **defines**: Properties or concepts this behavior defines
- **protocols**: Specific protocols this behavior enforces
- **team_members**: Team members this behavior applies to (if specific)

---

## 🔗 Relationship Types

### Primary Relationships

| Relationship | Direction | Meaning | Example |
|-------------|-----------|---------|---------|
| **depends_on** | A → B | A requires B to be completed first | skill-005 depends_on skill-004 |
| **enables** | A → B | A makes B possible | skill-004 enables skill-005 |
| **part_of** | A → B | A is a component of B | skill-004 part_of skill-024 |
| **implements** | A → B | A implements the logic/rule defined in B | skill-022 implements cursor-workflow-git |
| **references** | A → B | A uses information from B | skill-010 references docs-std-quality |
| **related_to** | A ↔ B | A and B are similar or complementary | skill-001 related_to skill-002 |

### Composite Relationships

| Relationship | Meaning | Example |
|-------------|---------|---------|
| **composed_of** | Workflow made of multiple skills | skill-024 composed_of [skill-004, skill-005, ...] |
| **contains** | Directory or doc contains items | docs-config-templates contains template files |
| **illustrates** | Diagram shows a workflow/process | docs-arch-data-flow illustrates skill-024 |

---

## 📋 Metadata Schema

### Graph-Level Metadata

All three graphs include:

```json
{
  "metadata": {
    "version": "1.0",
    "framework": "3-Track Knowledge Graph",
    "last_updated": "YYYY-MM-DD",
    "description": "Brief description of graph purpose",
    "total_nodes": 25,
    "total_relationships": 87
  }
}
```

### Category Summary Schema

**skills-graph.json**:
```json
{
  "categories": {
    "category-name": {
      "skills": 9,
      "production": 7,
      "development": 2
    }
  }
}
```

**docs-graph.json**:
```json
{
  "categories": {
    "category-name": {
      "documents": 4,
      "types": ["procedure", "reference"]
    }
  }
}
```

**cursor-graph.json**:
```json
{
  "rule_hierarchy": {
    "category": {
      "priority": "high",
      "rules": ["cursor-rule-1", "cursor-rule-2"],
      "applies_to": "description"
    }
  }
}
```

---

## 🎯 URI Schemes

### Cross-Track References

**Format**: `track://path/to/resource`

**Examples**:
- `skill://agents/skills/data-operations/web-scraping-basic.md`
- `docs://procedures/data-preparation.md`
- `cursor://rules/actions/documentation.md`

**Usage in JSON**:
```json
{
  "implements": ["cursor://rules/actions/data-preparation.md"],
  "references": ["docs://procedures/data-preparation.md"]
}
```

**Resolution**:
- `skill://` → `agents/skills/`
- `docs://` → `docs/`
- `cursor://` → `.cursor/`

---

## ✅ Validation Rules

### Node Validation

**Required Fields**:
- All nodes: `id`, `path` (except workflows), `type`, `category`
- Skills: `name`, `status`, `frequency`
- Docs: `path`
- Behaviors: `path`, `type`

**ID Conventions**:
- Skills: `skill-NNN` (001-025)
- Docs: `docs-category-name`
- Behaviors: `cursor-category-name`

**Path Validation**:
- Skills: Must exist in `agents/skills/`
- Docs: Must exist in `docs/`
- Behaviors: Must exist in `.cursor/`

### Relationship Validation

**Referential Integrity**:
- All IDs in relationships must exist
- `depends_on` must not create cycles
- `part_of` must reference a workflow-type skill
- `implements` must reference a valid behavior or doc
- `references` must reference a valid doc

**Bi-directional Consistency**:
- If A `enables` B, B should `depends_on` A
- If A `part_of` B, B should `composed_of` A
- If A `implements` B, B should have A in `implements_skills`

---

## 🔄 Graph Evolution

### Adding New Nodes

**New Skill**:
1. Add to `skills-graph.json` with new ID (skill-026)
2. Update category counts
3. Add to relevant workflows if applicable
4. Reference in cursor-graph.json if it implements a behavior
5. Reference in docs-graph.json if documentation references it

**New Document**:
1. Add to `docs-graph.json` with new ID
2. Add references to skills that use it
3. Add to category in docs structure
4. Update cursor-graph.json if behaviors reference it

**New Behavior**:
1. Add to `cursor-graph.json` with new ID
2. Link to skills it implements
3. Link to docs it references
4. Add triggers if applicable
5. Place in appropriate hierarchy level

### Updating Relationships

**When a dependency changes**:
1. Update `dependencies` in skill node
2. Update `enables` in prerequisite skill
3. Verify no circular dependencies
4. Update workflow `composed_of` if needed

**When a doc is reorganized**:
1. Update `path` in doc node
2. Update all `references` to new path
3. Verify all links still resolve

---

## 📊 Statistics Schema

### Usage Patterns (cursor-graph.json)

```json
{
  "usage_patterns": {
    "most_triggered": [
      {
        "id": "cursor-rule-id",
        "frequency": "daily",
        "triggers": 4
      }
    ],
    "workflow_sequences": [
      {
        "name": "Workflow name",
        "sequence": ["cursor-rule-1", "cursor-rule-2"]
      }
    ]
  }
}
```

### Cross-References (docs-graph.json)

```json
{
  "cross_references": {
    "most_referenced": [
      {
        "id": "docs-id",
        "references": 13,
        "reason": "Description"
      }
    ],
    "most_cross_track": [
      {
        "id": "docs-id",
        "skill_references": 9,
        "cursor_references": 1
      }
    ]
  }
}
```

---

## 🛠️ Schema Versioning

**Current Version**: 1.0

**Version History**:
- 1.0 (2025-11-15): Initial schema release

**Future Versions**:
- 1.1: Add performance metrics
- 1.2: Add automatic validation
- 2.0: Add temporal dimensions (change history)

---

## 📚 See Also

- **Usage Examples**: [GRAPH_QUERIES.md](./GRAPH_QUERIES.md)
- **Maintenance Guide**: [MAINTENANCE.md](./MAINTENANCE.md)
- **Knowledge Graph README**: [README.md](./README.md)

---

**Version**: 1.0  
**Last Updated**: 2025-11-15  
**Schema Stability**: Stable

