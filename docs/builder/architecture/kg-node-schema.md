# KG Node Schema Reference

**Node ID**: `knowledge:builder:kg-node-schema`
**Type**: reference
**Category**: builder-meta
**Created**: 2026-05-18

---

## Overview

Every KG node is a JSON object with at least an `id`. Beyond that, the three node types (skill / knowledge / behavior) have conventional fields that authors should fill but the schema validator does **not** strictly enforce (per the design principle — schemas validate STRUCTURE, not TAXONOMY).

The integrity validator + reviewer judgement enforce the rest.

---

## Schema files

Located at `src/agentloom/kg/lib/schemas/`:

| File | Validates `graphType` | Top-level required | Array key |
| --- | --- | --- | --- |
| `skills-graph.schema.json` | `"skills"` | `graphType`, `role`, `generatedAt`, `skills` | `skills` |
| `knowledge-graph.schema.json` | `"knowledge"` | `graphType`, `role`, `generatedAt`, `oneOf(nodes,documents)` | `nodes` or `documents` |
| `behaviors-graph.schema.json` | `"behaviors"` | `graphType`, `role`, `generatedAt`, `behaviors` | `behaviors` |
| `master-graph.schema.json` | `"master"` | `graphType`, `project`, `version`, `generatedAt`, `roles` | `roles[].graphs[]` |

---

## Skill node

```json
{
  "id": "skill:builder:propose-node",
  "type": "skill",
  "name": "Propose KG node",
  "category": "kg-tools",
  "description": "Agent-callable; writes a candidate node JSON + UPDATE_LOG to proposals/",
  "path": "agents/skills/builder/skill-propose-node.md",
  "script": "src/agentloom/kg/propose_node.py",
  "parent": "skill:builder:root",
  "links": {
    "implements": ["behavior:builder:every-skill-must-have-script"],
    "uses": ["knowledge:builder:propose-review-protocol"]
  }
}
```

**Required**: `id`. **Conventional**: `type`, `name`, `category`, `path`, `parent`. **For executable skills**: `script` pointing at runnable code.

`type` values commonly used: `root`, `category`, `skill`, `procedure`, `script`, `workflow`. Not enum-locked.

---

## Knowledge node

```json
{
  "id": "knowledge:builder:agentloom-architecture",
  "type": "architecture",
  "title": "AgentLoom Architecture",
  "path": "docs/builder/architecture/agentloom-architecture.md",
  "category": "builder-meta",
  "parent": "knowledge:builder:root",
  "links": {
    "referenced_by": ["skill:builder:propose-node"]
  }
}
```

**Required**: `id`. **Conventional**: `type`, `title`, `path` (must point at an existing markdown file — integrity validator enforces), `category`, `parent`.

`type` values: `root`, `category`, `concept`, `architecture`, `protocol`, `reference`, `procedure`, `runbook`, `pattern`, `template`. Not enum-locked.

---

## Behavior node

```json
{
  "id": "behavior:builder:every-skill-must-have-script",
  "type": "rule",
  "name": "Every skill must have a script",
  "description": "Tier-A validator: every node in skills-graph with type=skill must have a non-empty path field pointing to an existing file.",
  "path": "agents/behaviors/builder/behavior-every-skill-must-have-script.md",
  "category": "kg-integrity",
  "priority": "high",
  "enforcement": "hard",
  "parent": "behavior:builder:root",
  "links": {
    "validator": "src/agentloom/validators/every_skill_must_have_script.py",
    "related": ["behavior:builder:every-non-soft-behavior-has-validator"]
  }
}
```

**Required**: `id`. **Conventional**: `type`, `name`, `description`, `path`, `category`, `priority` (`low|medium|high|critical`), `enforcement` (`hard|test|process|soft`), `parent`.

**Critical**: if `enforcement != 'soft'`, then `links.validator` must point to an existing Python file. The behavior `every-non-soft-behavior-has-validator` enforces this.

---

## ID conventions (soft, not schema-enforced)

| Prefix | Meaning |
| --- | --- |
| `skill:<role>:<slug>` | Skill node, e.g. `skill:builder:validate-kg` |
| `skill-NNN` | Numeric skill id (domain convention) |
| `knowledge:<role>:<slug>` | Knowledge node |
| `behavior:<role>:<slug>` | Behavior node |
| `<scope>-root` | Root of a tree, e.g. `skill:builder:root`, `knowledge:builder:root` |
| `cat-<name>` | Category grouping node |

The schema accepts any non-empty string. Reviewers enforce the conventions.

---

## See also

- `agentloom-architecture.md` — why the 3-track / 2-role split
- `propose-review-protocol.md` — how new nodes get added safely
- `validator-authoring-guide.md` — how to write a Tier-A validator
- The upstream methodology doc embeds 4 figures explaining all of this: `envistor-data/docs/knowledge-graphs/KG_MEMORY_METHODOLOGY.md`
