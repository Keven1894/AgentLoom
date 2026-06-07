# Phase 4: Create Knowledge Graphs (V2 ENHANCED)

**AI Agent Setup Protocol V2.0**

---

## 📌 Phase Context

**Prerequisites**: Phases 1-3 complete  
**Input needed from previous phases**:
- Domain role ID and name (Phase 1)
- KG structure design (Phase 2)
- Shared content folders (Phase 1, if any)
- Content mapping (Phase 2, Phase 3)

**Output**: 7-8 fully-connected JSON graph files  
**Estimated time**: 45-90 minutes

**Creates for next phases**:
- master-graph.json → Phase 11 (startup script references)
- All KG files → Phase 5 (node IDs for skills/behaviors)
- Graph structure → Phase 6 (validation)

**Critical**: Every non-root node must have `parent` field

---

## Objective

Create all JSON knowledge graphs with **full connectivity** - root nodes, parent links, and cross-graph relationships.

**Note**: This phase creates graphs for Agent Builder (system role) and Domain Role (custom), and optionally maps shared content from Phase 1.

---

## Action 4.1: Create Master Graph

**V2 Enhancement**: Explicitly list all graph files with descriptions for Agent Builder + Domain Role architecture.

### Quick Start

**Generate** `agents/knowledge-graphs/master-graph.json` with:
- Entry point to all graph files
- Agent Builder graphs (3: knowledge, skills, behaviors)
- Domain Role graphs (3: knowledge, skills, behaviors)
- Optional content graph (if shared folders in Phase 1)
- Role definitions with `alwaysActive` flags

<details>
<summary><b>📋 Expand for Complete Template & Examples</b></summary>

Create `agents/knowledge-graphs/master-graph.json`:

```json
{
  "graphType": "master",
  "project": "[project name from Phase 1]",
  "version": "2.0",
  "generatedAt": "[YYYY-MM-DD]",
  "description": "Entry point to the entire Knowledge Graph system",
  "graphs": [
    {
      "id": "agent-builder-knowledge",
      "path": "agents/knowledge-graphs/agent-builder-knowledge-graph.json",
      "description": "Agent Builder's understanding of system architecture"
    },
    {
      "id": "agent-builder-skills",
      "path": "agents/knowledge-graphs/agent-builder-skills-graph.json",
      "description": "Agent Builder's system maintenance capabilities"
    },
    {
      "id": "agent-builder-behaviors",
      "path": "agents/knowledge-graphs/agent-builder-behaviors-graph.json",
      "description": "Agent Builder's system protocols"
    },
    {
      "id": "[domain-role-id]-knowledge",
      "path": "agents/knowledge-graphs/[domain-role-id]-knowledge-graph.json",
      "description": "[Domain Role Name]'s domain understanding"
    },
    {
      "id": "[domain-role-id]-skills",
      "path": "agents/knowledge-graphs/[domain-role-id]-skills-graph.json",
      "description": "[Domain Role Name]'s domain capabilities"
    },
    {
      "id": "[domain-role-id]-behaviors",
      "path": "agents/knowledge-graphs/[domain-role-id]-behaviors-graph.json",
      "description": "[Domain Role Name]'s domain protocols"
    },
    {
      "id": "[domain]-content",
      "path": "agents/knowledge-graphs/[domain]-content-graph.json",
      "description": "Domain content structure (if shared folders provided in Phase 1)",
      "optional": true
    }
  ],
  "roles": [
    {
      "id": "agent-builder",
      "name": "Agent Builder",
      "alwaysActive": true,
      "graphs": [
        "agent-builder-knowledge",
        "agent-builder-skills",
        "agent-builder-behaviors"
      ]
    },
    {
      "id": "[domain-role-id]",
      "name": "[Domain Role Name]",
      "alwaysActive": false,
      "graphs": [
        "[domain-role-id]-knowledge",
        "[domain-role-id]-skills",
        "[domain-role-id]-behaviors",
        "[domain]-content"
      ]
    }
  ]
}
```

**Create** `agents/knowledge-graphs/master-graph.json` with the structure above.

**Confirm to human**:
```
✅ Created master-graph.json with:
- Agent Builder graphs (3)
- [Domain Role Name] graphs (3)
- Content graph (1, if applicable)
- Total: [N] graph references
```

</details>

---

## Action 4.2: Create Content Graph (If Shared Folders Provided in Phase 1)

**If user shared content folders in Phase 1**, create content graph based on Phase 2 Action 2.0 analysis.

**V2 Critical**: Ensure every node has a parent (except root).

### Quick Start

**Generate** `[domain]-content-graph.json` mapping shared folders to KG nodes with proper parent hierarchy.

<details>
<summary><b>📋 Expand for Template & Examples</b></summary>

Create `agents/knowledge-graphs/[domain]-content-graph.json`:

```json
{
  "graphType": "knowledge",
  "project": "[project name]",
  "generatedAt": "[YYYY-MM-DD]",
  "description": "[Domain] content structure from shared folders",
  "source": "Phase 1 shared folders, analyzed in Phase 2 Action 2.0",
  "nodes": [
    {
      "id": "[domain]:content:root",
      "type": "root",
      "title": "[Domain] Content Base"
    },
    {
      "id": "[domain]:content:[category-1]",
      "type": "folder",
      "path": "docs/[domain-role-id]/[category-1]",
      "title": "[Category 1 Name from Phase 2 analysis]",
      "parent": "[domain]:content:root",
      "description": "[Description]",
      "source_folder": "[original shared folder path from Phase 1]"
    },
    {
      "id": "[domain]:content:[category-1]:[subcategory]",
      "type": "folder",
      "path": "docs/[domain-role-id]/[category-1]/[subcategory]",
      "title": "[Subcategory Name]",
      "parent": "[domain]:content:[category-1]",
      "description": "[Description]"
    },
    {
      "id": "[domain]:content:[category-1]:[subcategory]:[doc-1]",
      "type": "document",
      "path": "docs/[domain-role-id]/[category-1]/[subcategory]/[file.md]",
      "title": "[Document Title]",
      "parent": "[domain]:content:[category-1]:[subcategory]"
    }
  ]
}
```

**Key V2 Rule**: Every node (except root) MUST have `"parent": "[parent-id]"`

**Create** `agents/knowledge-graphs/[domain]-content-graph.json` with the structure above.

**Confirm to human**:
```
✅ Created [domain]-content-graph.json with [N] nodes from Phase 1 shared folders
```

</details>

**If no folders shared**: Skip to Action 4.3.

---

## Action 4.3: Create Role-Specific Knowledge Graphs (V2 FULLY CONNECTED)

### Action 4.3a: Agent Builder Knowledge Graph

Agent Builder needs to understand system architecture and components.

**The Agent Builder knowledge graph is 100% reusable across all projects.**

**Copy the template**:

```bash
# Copy from protocol package to your project
cp [protocol-path]/json-templates/agent-builder/agent-builder-knowledge-graph.json.template \
   agents/knowledge-graphs/agent-builder-knowledge-graph.json
```

**No customization needed** - This graph is standardized for all agents.

**What's included**:
- System architecture nodes (sys:root, sys:agents, sys:config, sys:docs)
- Documentation structure (general + builder folders)
- Knowledge Graph meta-concepts
- Fully connected (all nodes have parent links)

**Template location**: `[protocol-package]/json-templates/agent-builder/agent-builder-knowledge-graph.json.template`

**Confirm to human**:
```
✅ Copied agent-builder-knowledge-graph.json (100% reusable, no changes needed)
```

### Action 4.3b: Domain Role Knowledge Graph

Domain Role needs to understand domain-specific content and concepts.

Create `agents/knowledge-graphs/[domain-role-id]-knowledge-graph.json`:

```json
{
  "graphType": "knowledge",
  "role": "[domain-role-id]",
  "generatedAt": "[YYYY-MM-DD]",
  "description": "[Domain Role Name]'s understanding of domain",
  "nodes": [
    {
      "id": "[domain-role-id]:root",
      "type": "root",
      "title": "[Domain] Knowledge"
    },
    {
      "id": "[domain-role-id]:docs",
      "type": "folder",
      "path": "docs/[domain-role-id]/",
      "title": "[Domain] Documentation",
      "parent": "[domain-role-id]:root",
      "description": "Domain-specific documentation and guides"
    },
    {
      "id": "[domain-role-id]:concepts",
      "type": "folder",
      "title": "[Domain] Concepts",
      "parent": "[domain-role-id]:root",
      "description": "Key concepts and terminology"
    },
    {
      "id": "[domain-role-id]:concepts:[concept-1]",
      "type": "concept",
      "title": "[Concept 1 from Phase 1]",
      "parent": "[domain-role-id]:concepts",
      "description": "[Description]"
    }
  ]
}
```

**Create** `agents/knowledge-graphs/[domain-role-id]-knowledge-graph.json` with the structure above.

**Confirm to human**:
```
✅ Created [domain-role-id]-knowledge-graph.json with [N] domain nodes
✅ Total: 2 role knowledge graphs created
```

---

## Action 4.4: Create Role-Specific Skills Graphs (V2 WITH SUB-SKILLS)

**V2 Enhancement**: Support skill trees (parent-child skills for orchestration). Reference Phase 2.3 for skill classifications.

### Action 4.4a: Agent Builder Skills Graph

Agent Builder has standard system skills, especially the KG maintenance skill tree.

**The Agent Builder skills graph is 100% reusable across all projects.**

**Copy the template**:

```bash
# Copy from protocol package to your project
cp [protocol-path]/json-templates/agent-builder/agent-builder-skills-graph.json.template \
   agents/knowledge-graphs/agent-builder-skills-graph.json
```

**No customization needed** - This graph is standardized for all agents.

**What's included**:
- KG Maintenance skill tree (orchestrator + 3 sub-skills):
  - `skill-maintain-kg` (orchestrator, hybrid)
  - `skill-kg-monitor` (rule-based)
  - `skill-kg-update` (hybrid)
  - `skill-kg-heal` (rule-based)
- Structure validation skill
- Full parent-child hierarchy
- Cross-links to behaviors
- Implementation types defined

**Template location**: `[protocol-package]/json-templates/agent-builder/agent-builder-skills-graph.json.template`

**Confirm to human**:
```
✅ Copied agent-builder-skills-graph.json with KG maintenance tree (100% reusable)
```

### Action 4.4b: Domain Role Skills Graph

Domain Role has domain-specific skills from Phase 2.

Create `agents/knowledge-graphs/[domain-role-id]-skills-graph.json`:

```json
{
  "graphType": "skills",
  "role": "[domain-role-id]",
  "generatedAt": "[YYYY-MM-DD]",
  "description": "[Domain Role Name]'s capabilities",
  "skills": [
    {
      "id": "skill:[domain-role-id]:root",
      "type": "root",
      "name": "[Domain Role Name] Capabilities",
      "description": "Root of the [Domain Role Name] skill tree"
    },
    {
      "id": "skill-[skill-1-id]",
      "name": "[Skill 1 Name from Phase 2]",
      "category": "[category]",
      "description": "[Description from Phase 2]",
      "path": "agents/skills/[category]/[skill-1-id].md",
      "parent": "skill:[domain-role-id]:root",
      "implementation": "[rule-based|llm-based-max|llm-based-slm|hybrid from Phase 2.3]",
      "links": {
        "enforces": ["behavior:[domain-role-id]:[behavior-id]"]
      }
    },
    {
      "id": "skill-[skill-2-id]",
      "name": "[Skill 2 Name from Phase 2]",
      "category": "[category]",
      "description": "[Description]",
      "path": "agents/skills/[category]/[skill-2-id].md",
      "parent": "skill:[domain-role-id]:root",
      "implementation": "[classification from Phase 2.3]"
    }
  ]
}
```

**Create** `agents/knowledge-graphs/[domain-role-id]-skills-graph.json` with the structure above.

**Confirm to human**:
```
✅ Created [domain-role-id]-skills-graph.json with [N] domain skills
✅ Total: 2 role skills graphs created
```

**Critical V2 Rules**:

1. Root node for skills
2. Top-level skills parent to root
3. Sub-skills parent to their orchestrator
4. Cross-links to behaviors via `links.enforces` or `links.implements`
5. Implementation type from Phase 2.3 classification

---

## Action 4.5: Create Role-Specific Behaviors Graphs (V2 WITH CROSS-LINKS)

**V2 Enhancement**: Include cross-links to skills and knowledge.

### Action 4.5a: Agent Builder Behaviors Graph

**The Agent Builder behaviors graph is 100% reusable across all projects.**

**Copy the template**:

```bash
# Copy from protocol package to your project
cp [protocol-path]/json-templates/agent-builder/agent-builder-behaviors-graph.json.template \
   agents/knowledge-graphs/agent-builder-behaviors-graph.json
```

**No customization needed** - This graph is standardized for all agents.

**What's included**:
- Core behaviors (system safety)
- Agent Builder-specific behaviors:
  - `behavior:agent-builder:kg-consistency` (enforces skill-maintain-kg)
  - `behavior:agent-builder:system-integrity` (enforces skill-validate-structure)
- Cross-links to skills
- Cross-links to system components
- Priority levels defined

**Template location**: `[protocol-package]/json-templates/agent-builder/agent-builder-behaviors-graph.json.template`

**Confirm to human**:
```
✅ Copied agent-builder-behaviors-graph.json (100% reusable)
```

### Action 4.5b: Domain Role Behaviors Graph

Create `agents/knowledge-graphs/[domain-role-id]-behaviors-graph.json`:

```json
{
  "graphType": "behaviors",
  "role": "[domain-role-id]",
  "generatedAt": "[YYYY-MM-DD]",
  "description": "[Domain Role Name]'s protocols",
  "behaviors": [
    {
      "id": "behavior:[domain-role-id]:root",
      "type": "root",
      "name": "[Domain Role Name] Behaviors",
      "description": "Core protocols for the [Domain Role Name] role"
    },
    {
      "id": "behavior:core:communication",
      "type": "core",
      "name": "Communication Protocol",
      "description": "Clear, structured responses",
      "path": ".cursor/behaviors/core/communication-protocol.md",
      "priority": "medium",
      "parent": "behavior:[domain-role-id]:root"
    },
    {
      "id": "behavior:[domain-role-id]:[behavior-1-id]",
      "type": "role-specific",
      "name": "[Behavior 1 Name from Phase 2]",
      "description": "[Description]",
      "path": ".cursor/behaviors/[domain-role-id]/[behavior-1-id].md",
      "priority": "medium",
      "parent": "behavior:[domain-role-id]:root",
      "links": {
        "enforces": ["skill-[skill-id]"],
        "governs": ["[domain-role-id]:[component-id]"]
      }
    }
  ]
}
```

**Create** `agents/knowledge-graphs/[domain-role-id]-behaviors-graph.json` with the structure above.

**Confirm to human**:
```
✅ Created [domain-role-id]-behaviors-graph.json with [N] behaviors
✅ Total: 2 role behaviors graphs created
```

**V2 Cross-Links**:

- `enforces`: This behavior enforces a skill
- `governs`: This behavior governs a system component
- `constrains`: This behavior constrains a knowledge domain

---

## Validation Checkpoint

```
✅ Knowledge Graph system complete:
- master-graph.json (created - entry point with Agent Builder + Domain Role)
- [domain]-content-graph.json (created if shared folders provided)
- agent-builder-knowledge-graph.json (copied from template - 100% reusable)
- agent-builder-skills-graph.json (copied from template - 100% reusable)
- agent-builder-behaviors-graph.json (copied from template - 100% reusable)
- [domain-role-id]-knowledge-graph.json (created - custom)
- [domain-role-id]-skills-graph.json (created - custom)
- [domain-role-id]-behaviors-graph.json (created - custom)
- All nodes have parent links (V2)
- Cross-graph links established (V2)

Total: 7-8 graph files (3 copied, 4-5 created)

Proceed to Phase 5?
```

---

**Previous Phase**: [Phase 3: Create Project Structure](PHASE_03_PROJECT_STRUCTURE.md)  
**Next Phase**: [Phase 5: Create Content Templates](PHASE_05_CONTENT_TEMPLATES.md)
