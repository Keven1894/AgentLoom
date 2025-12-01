# Implementation Guide: JSON Schemas

**Category**: Implementation  
**Version**: 1.0

---

## Knowledge Graph JSON Schema

### Graph Structure
```json
{
  "metadata": {
    "version": "string",
    "created": "ISO date",
    "updated": "ISO date",
    "track": "behaviors|knowledge|skills|master",
    "root_node": "node-id"
  },
  "nodes": [
    {
      "id": "string (unique)",
      "type": "string",
      "path": "string (file path)",
      "metadata": {},
      "links": {}
    }
  ]
}
```

### Node Schema
```json
{
  "id": "skill:ta/teaching/answer-concepts",
  "type": "skill",
  "path": "agents/skills/ta/teaching/answer-concepts/skill.md",
  "metadata": {
    "title": "Answer Conceptual Questions",
    "category": "teaching",
    "role": "ta",
    "priority": "high"
  },
  "links": {
    "parent": ["skill:ta/teaching"],
    "uses_behavior": ["behavior:pedagogical-approach"],
    "uses_knowledge": ["docs:ta/course-content"],
    "related_skills": ["skill:explain-with-examples"]
  }
}
```

### Link Types
- `parent` / `children` - Hierarchical
- `next` / `previous` - Sequential
- `uses_behavior` / `uses_knowledge` / `uses_skill` - Dependencies
- `related_to` / `referenced_by` - Semantic

---

## Validation

Use JSON schema validation libraries:
```python
import jsonschema

schema = load_schema("kg-schema.json")
graph = load_graph("ta-skills-graph.json")

jsonschema.validate(graph, schema)
```

---

**Status**: Schema definitions (Phase 3)  
**Next**: Implement validation in verify-integrity skill

