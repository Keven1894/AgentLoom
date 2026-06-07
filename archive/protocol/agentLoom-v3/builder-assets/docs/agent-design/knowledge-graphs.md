# Knowledge Graphs - Design & Best Practices

**Category**: Agent Design  
**Audience**: AI Agent Developers  
**Version**: 1.0

---

## Overview

Knowledge Graphs (KGs) are the **intelligence backbone** of 3-Track AI agents. They map relationships between behaviors, knowledge, and skills, enabling:
- **Discoverability**: Find relevant information quickly
- **Connectivity**: Understand relationships
- **Self-Evolution**: Agent can modify its own knowledge
- **Validation**: Ensure system integrity

---

## Why Knowledge Graphs?

###Traditional Approach (Files Only)
```
Problem: Files exist, but relationships are implicit
- Hard to discover related content
- Manual maintenance required
- No validation of completeness
- Cannot programmatically navigate

Example:
  skill.md mentions "uses academic-integrity rule"
  → But how to FIND that rule programmatically?
  → How to know what ELSE uses that rule?
```

### Knowledge Graph Approach
```
Solution: Explicit relationships in structured format
- Programmatically navigable
- Self-validating
- Enables automation
- Supports visualization

Example:
  {
    "id": "skill:guide-problem-solving",
    "links": {
      "uses_behavior": ["behavior:academic-integrity"],
      "uses_knowledge": ["docs:ta/assessments/guidelines"]
    }
  }
  
  → Agent can find rule: graph.get_node("behavior:academic-integrity")
  → Agent can find all users: graph.find_uses("behavior:academic-integrity")
```

---

## 3-Track Knowledge Graph Architecture

```
┌─────────────────────────────────────────────┐
│         Master Knowledge Graph               │
│   (Links all 3 tracks together)             │
└─────────────────────────────────────────────┘
         │              │              │
         ▼              ▼              ▼
┌───────────────┐ ┌──────────────┐ ┌──────────────┐
│ Behaviors     │ │ Knowledge    │ │ Skills       │
│ Graph         │ │ Graph        │ │ Graph        │
│               │ │              │ │              │
│ (Track 1:     │ │ (Track 2:    │ │ (Track 3:    │
│  HOW agent    │ │  WHAT agent  │ │  WHAT agent  │
│  behaves)     │ │  knows)      │ │  can DO)     │
└───────────────┘ └──────────────┘ └──────────────┘
```

### Individual Graphs
Each track has its own graph:
- **behaviors-graph.json**: Maps identity, rules, workflows
- **knowledge-graph.json**: Maps docs, content, references
- **skills-graph.json**: Maps capabilities, tools, procedures

### Master Graph
- Links nodes across all 3 tracks
- Enables cross-track navigation
- Validates system completeness
- Serves as single source of truth

---

## Node Structure

### Basic Node Format
```json
{
  "id": "unique-identifier",
  "type": "node-type",
  "path": "file/path/to/resource.md",
  "metadata": {
    "title": "Human-readable name",
    "description": "Brief description",
    "created": "2025-11-18",
    "updated": "2025-11-18"
  },
  "links": {
    "link_type": ["target-node-id"]
  }
}
```

### Node Types

**Track 1: Behaviors**
```json
{
  "id": "behavior:core/academic-integrity",
  "type": "behavior_rule",
  "path": ".cursor/rules/core/ta/academic-integrity.md",
  "metadata": {
    "title": "Academic Integrity",
    "priority": "critical",
    "scope": "ta"
  },
  "links": {
    "invoked_by": ["skill:guide-problem-solving"],
    "related_to": ["behavior:pedagogical-approach"]
  }
}
```

**Track 2: Knowledge**
```json
{
  "id": "docs:ta/module-01/intro",
  "type": "knowledge_content",
  "path": "docs/ta/course-content/module-01/intro.md",
  "metadata": {
    "title": "Introduction to Software Design",
    "module": "01",
    "topics": ["design", "architecture"]
  },
  "links": {
    "referenced_by": ["skill:answer-concepts"],
    "prerequisite_for": ["docs:ta/module-02/uml"],
    "parent": ["docs:ta/module-01"]
  }
}
```

**Track 3: Skills**
```json
{
  "id": "skill:ta/teaching/answer-concepts",
  "type": "skill",
  "path": "agents/skills/ta/teaching/answer-concepts/skill.md",
  "metadata": {
    "title": "Answer Conceptual Questions",
    "category": "teaching",
    "role": "ta"
  },
  "links": {
    "uses_behavior": ["behavior:pedagogical-approach"],
    "uses_knowledge": ["docs:ta/course-content"],
    "related_skills": ["skill:explain-with-examples"],
    "parent": ["skill:ta/teaching"]
  }
}
```

---

## Link Types

### Hierarchical Links
Parent-child relationships:
```json
"parent": ["parent-node-id"],
"children": ["child1-id", "child2-id"]
```

**Example**: Module → Topics, Category → Skills

### Sequential Links
Ordered progression:
```json
"next": ["next-node-id"],
"previous": ["previous-node-id"]
```

**Example**: Module 1 → Module 2, Topic A → Topic B

### Semantic Links
Meaning-based relationships:
```json
"related_to": ["related-node-id"],
"requires": ["prerequisite-node-id"],
"referenced_by": ["referencer-node-id"]
```

**Example**: Concept A relates to Concept B, Advanced topic requires basic topic

### Cross-Track Links
Connections between tracks:
```json
"uses_behavior": ["behavior-node-id"],
"uses_knowledge": ["docs-node-id"],
"uses_skill": ["skill-node-id"],
"invoked_by": ["invoker-node-id"]
```

**Example**: Skill uses behavior, behavior references knowledge

---

## Design Principles

### 1. 100% Connectivity ⚡ CRITICAL
```
Every node MUST be reachable from a root node
No orphaned nodes allowed
```

**Why**: Unreachable nodes = Dead content that can't be used

**Validation**:
```python
def validate_connectivity(graph, root_id):
    reachable = set()
    queue = [root_id]
    
    while queue:
        node_id = queue.pop(0)
        if node_id in reachable:
            continue
        reachable.add(node_id)
        node = graph.get_node(node_id)
        queue.extend(get_all_links(node))
    
    all_nodes = set(graph.all_node_ids())
    orphaned = all_nodes - reachable
    
    return len(orphaned) == 0, orphaned
```

### 2. Explicit Relationships
```
Don't rely on implicit connections
Document all relationships explicitly
```

**Bad**:
```markdown
<!-- In skill.md -->
This skill uses the academic integrity rule.
```

**Good**:
```json
{
  "id": "skill:guide-problem-solving",
  "links": {
    "uses_behavior": ["behavior:academic-integrity"]
  }
}
```

### 3. Bidirectional Links
```
Relationships should be navigable both ways
A → B implies B knows about A
```

**Example**:
```json
// Skill node
{
  "id": "skill:answer-concepts",
  "links": {
    "uses_knowledge": ["docs:ta/module-01"]
  }
}

// Knowledge node
{
  "id": "docs:ta/module-01",
  "links": {
    "referenced_by": ["skill:answer-concepts"]
  }
}
```

### 4. Semantic Clarity
```
Link types should be self-explanatory
Use consistent naming conventions
```

**Conventions**:
- `parent` / `children` - Hierarchy
- `next` / `previous` - Sequence
- `uses_*` - Dependencies
- `referenced_by` - Reverse reference
- `related_to` - Semantic similarity
- `requires` - Prerequisites

### 5. Metadata Richness
```
Include enough metadata for intelligent queries
Enable filtering, searching, categorization
```

**Useful Metadata**:
- `type`, `category`, `role` - Classification
- `priority`, `criticality` - Importance
- `topics`, `keywords` - Searchability
- `created`, `updated` - Temporal tracking
- `author`, `maintainer` - Ownership

---

## Best Practices

### ✅ DO

1. **Validate After Every Change**
   ```bash
   # After modifying any graph
   python scripts/validate_kg.py agents/knowledge-graphs/
   ```

2. **Keep Graphs Synchronized with Filesystem**
   ```
   If file moves: Update path in KG
   If file deleted: Remove node from KG
   If file added: Add node to KG
   ```

3. **Use Automation**
   ```
   Use `auto-integrate` skill for new content
   Use `sync-filesystem` skill for consistency
   ```

4. **Document Relationships**
   ```
   When creating a skill, document what it uses
   When creating content, document dependencies
   ```

5. **Visualize Regularly**
   ```
   Open visualization.html to inspect graph
   Look for isolated clusters
   Check for missing cross-track links
   ```

### ❌ DON'T

1. **Don't Create Orphaned Nodes**
   ```
   Every node must connect to the graph
   ```

2. **Don't Use Arbitrary IDs**
   ```
   Bad: "node-123"
   Good: "skill:ta/teaching/answer-concepts"
   ```

3. **Don't Forget Reverse Links**
   ```
   If A links to B, B should link back to A
   ```

4. **Don't Skip Validation**
   ```
   Always validate before committing
   ```

5. **Don't Manually Edit If Automation Exists**
   ```
   Use KG management skills instead of manual edits
   ```

---

## Schema

### Graph Structure
```json
{
  "metadata": {
    "version": "1.0",
    "created": "2025-11-18",
    "updated": "2025-11-18",
    "track": "behaviors|knowledge|skills|master",
    "root_node": "root-node-id"
  },
  "nodes": [
    {
      "id": "unique-id",
      "type": "node-type",
      "path": "file-path",
      "metadata": {},
      "links": {}
    }
  ]
}
```

### Required Fields
- `metadata.version` - Schema version
- `metadata.track` - Which track this graph represents
- `metadata.root_node` - Starting point for validation
- `nodes[].id` - Unique identifier
- `nodes[].type` - Node classification
- `nodes[].path` - File system path (if applicable)

---

## Tools & Skills

### KG Management Skills (Phase 3)
- `auto-integrate` - Automatically add new content to KG
- `intelligent-linking` - Discover relationships
- `verify-integrity` - Validate 100% connectivity
- `sync-filesystem` - Keep KG and files in sync

### Visualization
```bash
# Open visualization
open agents/knowledge-graphs/visualization.html

# Or use provided scripts
./agents/knowledge-graphs/start-visualization.sh
```

### Validation Scripts
```bash
# Validate all graphs
python shared/tools/kg-core/validate.py

# Check specific graph
python shared/tools/kg-core/validate.py agents/knowledge-graphs/ta-skills-graph.json
```

---

## Related Documentation
- [3-Track Architecture](./3-track-architecture.md)
- [KG Management System Design](../../developer/plan/todo/KG-MANAGEMENT-DESIGN.md)
- [KG Skills Reference](../../developer/plan/todo/KG-SKILLS-REFERENCE.md)

## Related Rules
- [Knowledge Graph Integrity](../../../.cursor/rules/core/developer/knowledge-graph-integrity.md) ⚡ CRITICAL

---

**Last Updated**: November 18, 2025  
**Status**: Core documentation  
**Priority**: CRITICAL - Foundation of agent intelligence

