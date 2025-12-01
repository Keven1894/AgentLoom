# AI Agent Setup Protocol V2.0 - PART 2

## Knowledge Graphs and Visualization

---

## Phase 4: Create Knowledge Graphs (V2 ENHANCED)

### Objective

Create all JSON knowledge graphs with **full connectivity** - root nodes, parent links, and cross-graph relationships.

### Actions

#### Action 4.1: Create Master Graph

**V2 Enhancement**: Explicitly list all graph files with descriptions.

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
      "id": "[domain-id]-graph",
      "path": "agents/knowledge-graphs/[domain-id]-graph.json",
      "description": "Domain knowledge and content structure"
    },
    {
      "id": "[role-1-id]-knowledge",
      "path": "agents/knowledge-graphs/[role-1-id]-knowledge-graph.json",
      "description": "[Role 1 Name]'s understanding of system architecture"
    },
    {
      "id": "[role-1-id]-skills",
      "path": "agents/knowledge-graphs/[role-1-id]-skills-graph.json",
      "description": "[Role 1 Name]'s capabilities and skill tree"
    },
    {
      "id": "[role-1-id]-behaviors",
      "path": "agents/knowledge-graphs/[role-1-id]-behaviors-graph.json",
      "description": "[Role 1 Name]'s protocols and rules"
    },
    {
      "id": "[role-2-id]-knowledge",
      "path": "agents/knowledge-graphs/[role-2-id]-knowledge-graph.json",
      "description": "[Role 2 Name]'s understanding of managed domains"
    },
    {
      "id": "[role-2-id]-skills",
      "path": "agents/knowledge-graphs/[role-2-id]-skills-graph.json",
      "description": "[Role 2 Name]'s capabilities"
    },
    {
      "id": "[role-2-id]-behaviors",
      "path": "agents/knowledge-graphs/[role-2-id]-behaviors-graph.json",
      "description": "[Role 2 Name]'s protocols"
    }
  ],
  "roles": [
    {
      "id": "[role-1-id]",
      "name": "[Role 1 Name]",
      "graphs": [
        "[domain-id]-graph",
        "[role-1-id]-knowledge",
        "[role-1-id]-skills",
        "[role-1-id]-behaviors"
      ]
    },
    {
      "id": "[role-2-id]",
      "name": "[Role 2 Name]",
      "graphs": [
        "[domain-id]-graph",
        "[role-2-id]-knowledge",
        "[role-2-id]-skills",
        "[role-2-id]-behaviors"
      ]
    }
  ]
}
```

Execute: `write` tool to create `agents/knowledge-graphs/master-graph.json`

Report:

```
✅ Created master-graph.json with [N] graph references
```

#### Action 4.2: Create Domain/Project Knowledge Graph (V2 FULLY CONNECTED)

**V2 Critical**: Ensure every node has a parent (except root).

Create appropriate domain graph (name depends on domain):

- If managing projects → `project-graph.json`
- If domain knowledge → `[domain]-graph.json`

```json
{
  "graphType": "knowledge",
  "project": "[project name]",
  "generatedAt": "[YYYY-MM-DD]",
  "description": "[Domain] knowledge structure",
  "nodes": [
    {
      "id": "[domain]:root",
      "type": "root",
      "title": "[Domain] Knowledge Base"
    },
    {
      "id": "[domain]:category1",
      "type": "folder",
      "path": "[path if applicable]",
      "title": "[Category 1 Name]",
      "parent": "[domain]:root",
      "description": "[Description]"
    },
    {
      "id": "[domain]:category1:sub1",
      "type": "folder",
      "path": "[path]",
      "title": "[Subcategory Name]",
      "parent": "[domain]:category1",
      "description": "[Description]"
    },
    {
      "id": "[domain]:category1:sub1:doc1",
      "type": "document",
      "path": "[path/to/file.md]",
      "title": "[Document Title]",
      "parent": "[domain]:category1:sub1"
    }
  ]
}
```

**Key V2 Rule**: Every node (except root) MUST have `"parent": "[parent-id]"`

Execute: `write` tool to create graph file.

Report:

```
✅ Created [domain]-graph.json with [N] nodes, all connected via parent links
```

#### Action 4.3: Create Role-Specific Knowledge Graphs (V2 FULLY CONNECTED)

For each role, create knowledge graph with system components/concepts.

**Example for Builder Role**:

```json
{
  "graphType": "knowledge",
  "role": "[role-1-id]",
  "generatedAt": "[YYYY-MM-DD]",
  "description": "[Role 1 Name]'s understanding of system architecture",
  "nodes": [
    {
      "id": "sys:root",
      "type": "root",
      "title": "System Architecture"
    },
    {
      "id": "sys:agents",
      "type": "component",
      "path": "agents/",
      "title": "Agent Logic Hub",
      "parent": "sys:root",
      "description": "Contains skills, behaviors, and knowledge graphs"
    },
    {
      "id": "sys:config",
      "type": "component",
      "path": ".cursor/",
      "title": "Configuration",
      "parent": "sys:root",
      "description": "System identity and behavior definitions"
    },
    {
      "id": "sys:behaviors",
      "type": "component",
      "path": ".cursor/behaviors/",
      "title": "Behavior Library",
      "parent": "sys:config",
      "description": "Native rule definitions for the agent"
    },
    {
      "id": "sys:docs",
      "type": "folder",
      "path": "docs/",
      "title": "Documentation Repository",
      "parent": "sys:root",
      "description": "System documentation organized by role"
    },
    {
      "id": "sys:docs:general",
      "type": "folder",
      "path": "docs/general/",
      "title": "General Documentation",
      "parent": "sys:docs",
      "description": "Cross-role guides and references"
    },
    {
      "id": "sys:docs:general:getting-started",
      "type": "document",
      "path": "docs/general/getting-started.md",
      "title": "Getting Started Guide",
      "parent": "sys:docs:general"
    },
    {
      "id": "sys:docs:[role-1-id]",
      "type": "folder",
      "path": "docs/[role-1-id]/",
      "title": "[Role 1 Name] Documentation",
      "parent": "sys:docs"
    },
    {
      "id": "sys:kg:architecture",
      "type": "concept",
      "title": "Knowledge Graph Architecture",
      "parent": "sys:root",
      "description": "The meta-structure defining how the system remembers"
    },
    {
      "id": "sys:kg:schema",
      "type": "concept",
      "title": "Graph Schema",
      "parent": "sys:kg:architecture",
      "description": "Rules defining valid nodes, types, and relationships"
    }
  ]
}
```

Execute: `write` tool for `[role-1-id]-knowledge-graph.json`

Repeat for Role 2 with appropriate structure.

Report:

```
✅ Created [N] role knowledge graphs, all fully connected
```

#### Action 4.4: Create Role-Specific Skills Graphs (V2 WITH SUB-SKILLS)

**V2 Enhancement**: Support skill trees (parent-child skills for orchestration).

For each role:

```json
{
  "graphType": "skills",
  "role": "[role-id]",
  "generatedAt": "[YYYY-MM-DD]",
  "description": "[Role Name]'s capabilities",
  "skills": [
    {
      "id": "skill:[role-id]:root",
      "type": "root",
      "name": "[Role Name] Capabilities",
      "description": "Root of the skill tree"
    },
    {
      "id": "skill-[skill-1-id]",
      "name": "[Skill 1 Name]",
      "category": "[category]",
      "description": "[Description from Phase 2]",
      "path": "agents/skills/[category]/[skill-1-id].md",
      "parent": "skill:[role-id]:root",
      "implementation": "[rule-based|llm-based-max|llm-based-slm|hybrid]",
      "links": {
        "enforces": ["behavior:[behavior-id]"]
      }
    },
    {
      "id": "skill-[orchestrator-skill-id]",
      "name": "[Orchestrator Skill Name]",
      "category": "system",
      "description": "Orchestration capability with sub-skills",
      "path": "agents/skills/system/[orchestrator-id].md",
      "parent": "skill:[role-id]:root",
      "implementation": "hybrid",
      "links": {
        "implements": ["behavior:[behavior-id]"],
        "sub_skills": ["skill-[sub-1]", "skill-[sub-2]", "skill-[sub-3]"]
      }
    },
    {
      "id": "skill-[sub-1]",
      "name": "[Sub-Skill 1 Name]",
      "category": "system",
      "description": "[Description]",
      "path": "agents/skills/system/[sub-1-id].md",
      "parent": "skill-[orchestrator-skill-id]",
      "implementation": "rule-based",
      "links": {
        "prerequisite_for": ["skill-[sub-2]"]
      }
    },
    {
      "id": "skill-[sub-2]",
      "name": "[Sub-Skill 2 Name]",
      "category": "system",
      "description": "[Description]",
      "path": "agents/skills/system/[sub-2-id].md",
      "parent": "skill-[orchestrator-skill-id]",
      "implementation": "llm-based-max"
    },
    {
      "id": "skill-[sub-3]",
      "name": "[Sub-Skill 3 Name]",
      "category": "system",
      "description": "[Description]",
      "path": "agents/skills/system/[sub-3-id].md",
      "parent": "skill-[orchestrator-skill-id]",
      "implementation": "rule-based"
    }
  ]
}
```

**Critical V2 Rules**:

1. Root node for skills
2. Top-level skills parent to root
3. Sub-skills parent to their orchestrator
4. Cross-links to behaviors via `links.enforces` or `links.implements`

Execute: `write` tool for each role's skills graph.

Report:

```
✅ Created [N] skills graphs with [M] total skills, hierarchically connected
```

#### Action 4.5: Create Role-Specific Behaviors Graphs (V2 WITH CROSS-LINKS)

**V2 Enhancement**: Include cross-links to skills and knowledge.

For each role:

```json
{
  "graphType": "behaviors",
  "role": "[role-id]",
  "generatedAt": "[YYYY-MM-DD]",
  "description": "[Role Name]'s protocols",
  "behaviors": [
    {
      "id": "behavior:[role-id]:root",
      "type": "root",
      "name": "[Role Name] Behaviors",
      "description": "Core protocols for the [Role Name] role"
    },
    {
      "id": "behavior:core:[core-behavior-id]",
      "type": "core",
      "name": "[Core Behavior Name]",
      "description": "[Description from Phase 2]",
      "path": ".cursor/behaviors/core/[core-behavior-id].md",
      "priority": "high",
      "parent": "behavior:[role-id]:root"
    },
    {
      "id": "behavior:[role-id]:[behavior-id]",
      "type": "role-specific",
      "name": "[Role-Specific Behavior Name]",
      "description": "[Description]",
      "path": ".cursor/behaviors/[role-id]/[behavior-id].md",
      "priority": "medium",
      "parent": "behavior:[role-id]:root",
      "links": {
        "enforces": ["skill-[skill-id]"],
        "governs": ["sys:[component-id]"]
      }
    }
  ]
}
```

**V2 Cross-Links**:

- `enforces`: This behavior enforces a skill
- `governs`: This behavior governs a system component
- `constrains`: This behavior constrains a knowledge domain

Execute: `write` tool for each role's behaviors graph.

Report:

```
✅ Created [N] behaviors graphs with cross-links to skills and knowledge
```

### Validation Checkpoint

```
✅ Knowledge Graph system complete:
- master-graph.json (entry point)
- [N] domain/project graphs
- [N]*3 role-specific graphs (knowledge, skills, behaviors)
- All nodes have parent links (V2)
- Cross-graph links established (V2)

Total: [count] graph files

Proceed to visualization tool creation?
```

---

## Phase 5: Create Content Templates & Behavior/Skill Files

### Objective

Create standard templates and initial behavior/skill documentation.

### Actions

#### Action 5.1: Create Content Template

Create `docs/general/CONTENT_TEMPLATE.md`:

```markdown
---
type: [concept | resource | workflow | skill | behavior | document]
category: [Category Name]
id: [unique-id-slug]
topics:
  - [topic 1]
  - [topic 2]
related:
  - [related-doc-id]
source: "[Original source if applicable]"
---

# [Title]

## Overview
[Brief 2-3 sentence description]

## Key Concepts
- **[Concept 1]**: [Definition]
- **[Concept 2]**: [Definition]

## Detailed Content

### [Section 1]
[Content...]

### [Section 2]
[Content...]

## Diagrams
> **[Diagram Name]**: [Text-based description or ASCII art]

## Examples

### Example 1: [Name]
```

[Code or example content]

```

**Explanation**: [What this example demonstrates]

## Related Resources
- [Link to related content in KG]
- [External references if applicable]

## Troubleshooting

### Issue: [Problem]
**Solution**: [Fix]

---

**Last Updated**: [Date]
**Indexed in KG**: [yes/no] ([node-id])
```

Execute: `write` tool.

Report:

```
✅ Created docs/general/CONTENT_TEMPLATE.md
```

#### Action 5.2: Create Core Behavior Files

For each core behavior from Phase 2, create file in `.cursor/behaviors/core/[behavior-id].md`:

```markdown
---
type: behavior
category: core
id: [behavior-id]
priority: [high|medium|low]
applies-to:
  - all-roles
indexed-in-kg: [behavior:core:[behavior-id]]
---

# [Behavior Name]

## Description
[What this behavior ensures - from Phase 2]

## Context
**When**: [When this behavior applies]
**Why**: [Why this rule exists]

## Rules

### Rule 1: [Rule Name]
[Detailed rule description]

**Example**:
```

[Example scenario]

```

### Rule 2: [Rule Name]
[Detailed rule description]

## Examples

### ✅ Good Practice
**Scenario**: [Context]
**Action**: [What agent does]
**Reason**: [Why this is correct]

### ❌ Bad Practice
**Scenario**: [Context]
**Action**: [What NOT to do]
**Reason**: [Why this violates the behavior]

## Related

### Enforced By
- Skills: [List skill-ids that implement this behavior]

### Governs
- Components: [List system components this behavior governs]

### Related Behaviors
- [Other behavior-ids that interact with this]

## Validation

How to verify this behavior is being followed:
1. [Check 1]
2. [Check 2]

---

**Priority**: [high|medium|low]
**Version**: 1.0
**Last Updated**: [Date]
```

Execute: `write` tool for each core behavior from Phase 2.

Report:

```
✅ Created [N] core behavior files in .cursor/behaviors/core/
```

#### Action 5.3: Create Role-Specific Behavior Files

For each role-specific behavior from Phase 2, create file in `.cursor/behaviors/[role-id]/[behavior-id].md`:

Use same template as core behaviors, but:

- Set `applies-to: [role-id]`
- Tailor examples to role context

Execute: `write` tool for each behavior.

Report:

```
✅ Created [N] role-specific behavior files across [M] role directories
```

#### Action 5.4: Create Skill Definition Files

For each skill from Phase 2, create file in `agents/skills/[category]/[skill-id].md`:

```markdown
---
type: skill
category: [category]
id: [skill-id]
implementation: [rule-based|llm-based-max|llm-based-slm|hybrid]
roles:
  - [role-id]
indexed-in-kg: [skill-[skill-id]]
---

# [Skill Name]

## Description
[What this skill enables - from Phase 2]

## Implementation Type: [Type from Phase 2.3]

**Reasoning**: [Why this implementation type was chosen]

[If rule-based:]
**Tool**: Python script / Shell command / MCP tool
**Location**: `scripts/[skill-id].py` (to be created in Phase 7)

[If LLM-based-max:]
**Required LLM**: Claude Sonnet 4.5+ / GPT-5.1+ / Gemini 3 Pro+
**Reasoning**: [Why max-tier LLM needed]

[If LLM-based-slm:]
**Suitable SLM**: Llama 3.1 8B / Mistral 7B
**Reasoning**: [Why SLM sufficient]

[If hybrid:]
**Architecture**:
1. **Preprocessing** (Rule-based): [What rules do]
2. **Analysis** (LLM): [What LLM does]
3. **Validation** (Rule-based): [What validation rules do]

## Usage

### When to Use
[Trigger conditions or scenarios]

### How to Activate
```

User: "[Example user prompt]"
Agent: [How agent invokes this skill]

```

### Input Requirements
- [Input 1]: [Description]
- [Input 2]: [Description]

### Output
- [Output 1]: [Description]
- [Output 2]: [Description]

## Prerequisites

### Knowledge Prerequisites
- Must understand: [List concepts]

### Skill Prerequisites
- Must have completed: [List prerequisite skill-ids]

### System Prerequisites
- [File/component requirements]

## Sub-Skills (if orchestrator skill)

[If this skill has sub-skills:]

This skill orchestrates the following sub-skills:

1. **[Sub-Skill 1]** (`skill-[sub-1-id]`)
   - **Purpose**: [What it does]
   - **When**: [When it's triggered]

2. **[Sub-Skill 2]** (`skill-[sub-2-id]`)
   - **Purpose**: [What it does]
   - **When**: [When it's triggered]

**Execution Flow**:
```

skill-[orchestrator-id]
├─> skill-[sub-1-id] (Step 1)
├─> skill-[sub-2-id] (Step 2)
└─> skill-[sub-3-id] (Step 3)

```

## Workflow

### Step-by-Step Execution

1. **[Step 1 Name]**
   - Action: [What happens]
   - Validation: [How to verify]

2. **[Step 2 Name]**
   - Action: [What happens]
   - Validation: [How to verify]

[Continue for all steps]

## Error Handling

### Error: [Error Type]
**Cause**: [Why this error occurs]
**Recovery**: [How to fix]

## Related

### Implements Behaviors
- [List behavior-ids this skill implements]

### Uses Knowledge
- [List knowledge node-ids this skill accesses]

### Related Skills
- [List related skill-ids]

## Examples

### Example 1: [Scenario]
**Input**: [Example input]
**Process**: [What skill does]
**Output**: [Example output]

---

**Implementation**: [Type]
**Status**: [Defined | Implemented | Tested]
**Version**: 1.0
**Last Updated**: [Date]
```

Execute: `write` tool for each skill from Phase 2.

Report:

```
✅ Created [N] skill definition files across [M] categories
```

### Validation Checkpoint

```
✅ Documentation created:
- Content template
- [N] core behavior files
- [N] role-specific behavior files  
- [N] skill definition files

Total: [count] markdown files

Proceed to validation tools?
```

---

## Phase 6: Create Validation Tools

### Objective

Create scripts to validate structure and graph integrity.

### Actions

#### Action 6.1: Create Graph Validator

Create `scripts/validate_graphs.py`:

```python
import json
import os
from pathlib import Path

def validate_graph(graph_path):
    """Validates JSON graph structure and file references"""
    print(f"\n🔍 Validating {graph_path}...")
    
    try:
        with open(graph_path, 'r', encoding='utf-8') as f:
            graph = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        return False
    
    # Check required fields
    required_fields = {
        'master': ['graphType', 'project', 'graphs', 'roles'],
        'knowledge': ['graphType', 'nodes'],
        'skills': ['graphType', 'role', 'skills'],
        'behaviors': ['graphType', 'role', 'behaviors']
    }
    
    graph_type = graph.get('graphType', 'unknown')
    required = required_fields.get(graph_type, ['graphType'])
    
    for field in required:
        if field not in graph:
            print(f"❌ Missing required field: {field}")
            return False
    
    # V2: Validate connectivity (parent links)
    orphaned_nodes = []
    root_nodes = []
    
    nodes = graph.get('nodes', []) or graph.get('skills', []) or graph.get('behaviors', [])
    
    for node in nodes:
        node_id = node.get('id', 'unknown')
        node_type = node.get('type', '')
        
        # Root nodes don't need parents
        if node_type == 'root':
            root_nodes.append(node_id)
        # All other nodes MUST have parent
        elif 'parent' not in node:
            orphaned_nodes.append(node_id)
    
    if orphaned_nodes:
        print(f"⚠️  Found {len(orphaned_nodes)} orphaned nodes (missing parent):")
        for node_id in orphaned_nodes[:5]:  # Show first 5
            print(f"   - {node_id}")
        if len(orphaned_nodes) > 5:
            print(f"   ... and {len(orphaned_nodes) - 5} more")
    
    if not root_nodes and nodes:
        print(f"⚠️  No root node found! Graph should have at least one root.")
    
    # Validate file references
    files_checked = 0
    files_missing = 0
    
    for node in nodes:
        if 'path' in node:
            files_checked += 1
            if not os.path.exists(node['path']):
                print(f"⚠️  Missing file: {node['path']}")
                files_missing += 1
    
    # Report
    if files_missing > 0:
        print(f"⚠️  {files_missing}/{files_checked} referenced files missing")
    elif files_checked > 0:
        print(f"✅ All {files_checked} referenced files exist")
    
    if orphaned_nodes:
        print(f"⚠️  {len(orphaned_nodes)} orphaned nodes detected")
        print(f"✅ {graph_path} structure valid but connectivity issues found")
        return False
    else:
        print(f"✅ {graph_path} fully connected and valid")
        return True

def main():
    print("=" * 60)
    print("Knowledge Graph Validation (V2 - Connectivity Check)")
    print("=" * 60)
    
    graphs_dir = Path('agents/knowledge-graphs')
    if not graphs_dir.exists():
        print("❌ knowledge-graphs directory not found!")
        return
    
    graphs = list(graphs_dir.glob('*.json'))
    if not graphs:
        print("❌ No graph files found!")
        return
    
    results = []
    for graph_path in graphs:
        if graph_path.name == 'visualization.html':
            continue
        results.append(validate_graph(str(graph_path)))
    
    print("\n" + "=" * 60)
    if all(results):
        print(f"✅ All {len(results)} graphs are fully connected and valid!")
    else:
        print(f"⚠️  {sum(results)}/{len(results)} graphs passed")
        print("Fix orphaned nodes by adding 'parent' fields.")
    print("=" * 60)

if __name__ == '__main__':
    main()
```

Execute: `write` tool.

Report:

```
✅ Created scripts/validate_graphs.py (V2 with connectivity checks)
```

#### Action 6.2: Create Structure Validator

Create `scripts/validate_structure.py`:

```python
import os
from pathlib import Path

def check_structure():
    """Validates project folder structure"""
    print("🔍 Validating project structure (V2)...\n")
    
    required_dirs = [
        '.cursor',
        '.cursor/behaviors',
        '.cursor/behaviors/core',
        'agents',
        'agents/knowledge-graphs',
        'agents/skills',
        'docs',
        'docs/general',
        'scripts',
        'temp'
    ]
    
    required_files = [
        '.cursor/identity.md',
        '.cursor/rules.md',
        'agents/NEW_AGENT_START_HERE.md',
        'agents/USER_MANUAL.md',
        'agents/knowledge-graphs/master-graph.json',
        'agents/knowledge-graphs/visualization.html',
        'agents/knowledge-graphs/VIEW_VISUALIZATION.md',
        'docs/general/CONTENT_TEMPLATE.md'
    ]
    
    print("Directories:")
    dirs_ok = 0
    for dir_path in required_dirs:
        exists = os.path.isdir(dir_path)
        status = "✅" if exists else "❌"
        print(f"  {status} {dir_path}")
        if exists:
            dirs_ok += 1
    
    print(f"\n{dirs_ok}/{len(required_dirs)} required directories present\n")
    
    print("Core Files:")
    files_ok = 0
    for file_path in required_files:
        exists = os.path.isfile(file_path)
        status = "✅" if exists else "❌"
        print(f"  {status} {file_path}")
        if exists:
            files_ok += 1
    
    print(f"\n{files_ok}/{len(required_files)} required files present\n")
    
    # V2: Check for behavior files
    behavior_files = list(Path('.cursor/behaviors').rglob('*.md')) if Path('.cursor/behaviors').exists() else []
    skill_files = list(Path('agents/skills').rglob('*.md')) if Path('agents/skills').exists() else []
    
    print(f"Content Files:")
    print(f"  ✅ {len(behavior_files)} behavior files")
    print(f"  ✅ {len(skill_files)} skill files")
    
    all_ok = (dirs_ok == len(required_dirs)) and (files_ok == len(required_files))
    
    print()
    if all_ok and behavior_files and skill_files:
        print("✅ Project structure is complete and valid!")
    elif all_ok:
        print("⚠️  Structure valid but missing behavior/skill content")
    else:
        print("⚠️  Project structure is incomplete")
    
    return all_ok

if __name__ == '__main__':
    check_structure()
```

Execute: `write` tool.

Report:

```
✅ Created scripts/validate_structure.py
```

### Validation Checkpoint

```
✅ Created validation scripts:
- scripts/validate_graphs.py (V2 with connectivity validation)
- scripts/validate_structure.py

Proceed to KG maintenance skill setup?
```

---

## Phase 7: KG Maintenance Skill Setup (V2 NEW PHASE)

### Objective

Create the "Maintain Knowledge Graph" skill system to enable agent self-evolution.

### Why This Matters

Without KG maintenance capability:

- Agent cannot adapt to new files/changes
- Manual KG updates required (error-prone)
- System becomes stale as project evolves

### Actions

#### Action 7.1: Create Orchestrator Skill Definition

Create `agents/skills/system/maintain-kg.md`:

```markdown
---
type: skill
category: system
id: maintain-kg
implementation: hybrid
roles:
  - [builder-role-id]
indexed-in-kg: skill-maintain-kg
---

# Maintain Knowledge Graph

## Description
Orchestration capability to keep the Knowledge Graph in sync with the file system state. This is the agent's "self-evolution" mechanism.

## Implementation Type: Hybrid

**Architecture**:
1. **Monitor** (Rule-based): Detect file system changes
2. **Interpret** (LLM): Understand what changed and why
3. **Update** (Rule-based): Modify JSON graphs with validation
4. **Visualize** (Rule-based): Update visualization if needed

## Sub-Skills

This orchestrator skill chains three sub-skills:

1. **Monitor File System** (`skill-kg-monitor`)
   - Scans tracked directories for changes
   - Compares current state to KG state
   - Reports additions, modifications, deletions

2. **Update Graph Node** (`skill-kg-update-node`)
   - Adds new nodes to appropriate graphs
   - Updates existing node metadata
   - Removes nodes for deleted files
   - Validates JSON schema after changes

3. **Heal Graph Links** (`skill-kg-heal`)
   - Detects orphaned nodes (missing parent)
   - Identifies broken cross-links
   - Suggests relationship repairs
   - Validates full connectivity

## Usage

### When to Use

**Trigger Scenarios**:
- New files added to tracked directories
- Files moved or renamed
- Documentation structure changed
- New behaviors/skills created
- Periodic maintenance (weekly)

### How to Activate

```

User: "Update the knowledge graph"
Agent:

  1. Activating skill-kg-monitor...
  2. Changes detected: [list]
  3. Activating skill-kg-update-node...
  4. Nodes updated: [count]
  5. Activating skill-kg-heal...
  6. Graph validated: [status]
  7. ✅ Knowledge Graph updated and validated

```

## Workflow

### Step 1: Monitor (skill-kg-monitor)
- Scan `.cursor/behaviors/`, `agents/skills/`, `docs/`
- Compare to nodes in KG JSON files
- Generate change report

### Step 2: Interpret Changes (LLM)
- Analyze change report
- Determine which graph(s) to update
- Generate node metadata (titles, descriptions)
- Determine parent relationships

### Step 3: Update Graphs (skill-kg-update-node)
- Modify JSON files
- Add/update/remove nodes
- Preserve cross-links
- Validate JSON syntax

### Step 4: Heal (skill-kg-heal)
- Check for orphaned nodes
- Validate parent links exist
- Suggest missing cross-links
- Report connectivity status

### Step 5: Visualize (Optional)
- Update visualization.html if graph structure changed
- Notify user to refresh browser

## Tracked Directories

This skill monitors:
- `.cursor/behaviors/` → Updates `[role]-behaviors-graph.json`
- `agents/skills/` → Updates `[role]-skills-graph.json`
- `docs/[role]/` → Updates `[role]-knowledge-graph.json`
- `[domain-content-dirs]/` → Updates domain graphs

## Related

### Implements Behaviors
- `behavior:builder:consistency` - Graph must reflect reality

### Uses Sub-Skills
- `skill-kg-monitor`
- `skill-kg-update-node`
- `skill-kg-heal`

## Error Handling

### Error: JSON Syntax Invalid After Update
**Recovery**: Rollback to previous version, re-apply with validation

### Error: Circular Parent References
**Recovery**: skill-kg-heal detects and breaks cycles

---

**Implementation**: Hybrid (Rule + LLM + Rule)
**Status**: Defined
**Version**: 1.0
```

Execute: `write` tool.

#### Action 7.2: Create Sub-Skill: Monitor

Create `agents/skills/system/kg-monitor.md`:

```markdown
---
type: skill
category: system
id: kg-monitor
implementation: rule-based
parent-skill: maintain-kg
indexed-in-kg: skill-kg-monitor
---

# Monitor File System

## Description
Detects changes in tracked directories by comparing file system state to Knowledge Graph state.

## Implementation Type: Rule-Based

**Tool**: Python script
**Location**: `scripts/kg_monitor.py` (to be created)

## Usage

**Input**:
- List of directories to monitor
- Current KG JSON files

**Output**:
- Change report (JSON)
  - `added`: Files not in KG
  - `modified`: Files with updated timestamps
  - `deleted`: KG nodes with missing files

## Workflow

1. Read KG JSON files
2. Extract all `path` fields → current_kg_files
3. Scan monitored directories → actual_files
4. Compare: `added = actual_files - current_kg_files`
5. Compare: `deleted = current_kg_files - actual_files`
6. Check timestamps for `modified`
7. Return change report

## Implementation Pseudocode

```python
def monitor_changes(monitored_dirs, kg_files):
    kg_paths = extract_paths_from_graphs(kg_files)
    actual_paths = scan_directories(monitored_dirs)
    
    added = actual_paths - kg_paths
    deleted = kg_paths - actual_paths
    modified = check_timestamps(kg_paths, actual_paths)
    
    return {
        "added": list(added),
        "deleted": list(deleted),
        "modified": list(modified)
    }
```

## Related

### Parent Skill

- `skill-maintain-kg` (orchestrator)

### Next Skill in Chain

- `skill-kg-update-node` (processes this output)

---

**Implementation**: Rule-based (Python)
**Status**: Defined

```

Execute: `write` tool.

#### Action 7.3: Create Sub-Skill: Update Node

Create `agents/skills/system/kg-update-node.md`:

```markdown
---
type: skill
category: system
id: kg-update-node
implementation: hybrid
parent-skill: maintain-kg
indexed-in-kg: skill-kg-update-node
---

# Update Graph Node

## Description
Adds, modifies, or removes nodes in JSON Knowledge Graph files.

## Implementation Type: Hybrid

**Architecture**:
1. **Rule-based**: Read JSON, validate schema
2. **LLM**: Generate node metadata (title, description, determine parent)
3. **Rule-based**: Write JSON, validate syntax

## Usage

**Input**:
- Change report from `skill-kg-monitor`
- Graph file to modify

**Process**:
1. For `added` files:
   - LLM generates: title, description, node type
   - LLM determines: parent node ID
   - Rules: Insert node, validate, save
   
2. For `modified` files:
   - LLM updates: description if content changed
   - Rules: Update node, validate, save
   
3. For `deleted` files:
   - Rules: Remove node, check for orphaned children, save

**Output**:
- Updated JSON file
- Validation report

## Workflow

### Adding a Node

```python
# Step 1: LLM generates metadata
metadata = llm_analyze_file(file_path)
# Returns: {title, description, type, suggested_parent}

# Step 2: Rules create node
new_node = {
    "id": generate_id(file_path),
    "type": metadata["type"],
    "path": file_path,
    "title": metadata["title"],
    "parent": metadata["suggested_parent"],
    "description": metadata["description"]
}

# Step 3: Rules insert and validate
graph = load_json(graph_file)
graph["nodes"].append(new_node)
validate_schema(graph)
save_json(graph_file, graph)
```

## Related

### Parent Skill

- `skill-maintain-kg`

### Follows

- `skill-kg-monitor` (provides input)

### Followed By

- `skill-kg-heal` (validates result)

---

**Implementation**: Hybrid (Rules + LLM + Rules)
**Status**: Defined

```
Execute: `write` tool.
```

#### Action 7.4: Create Sub-Skill: Heal

Create `agents/skills/system/kg-heal.md`:

```markdown
---
type: skill
category: system
id: kg-heal
implementation: rule-based
parent-skill: maintain-kg
indexed-in-kg: skill-kg-heal
---

# Heal Graph Links

## Description
Detects and fixes orphaned nodes, broken parent links, and connectivity issues in Knowledge Graphs.

## Implementation Type: Rule-Based

**Tool**: Python script
**Location**: `scripts/kg_heal.py` (to be created)

## Usage

**Input**:
- All KG JSON files

**Output**:
- Validation report
- List of issues found
- Suggested fixes

## Checks Performed

### 1. Orphaned Nodes
- **Check**: All non-root nodes have `parent` field
- **Fix**: Suggest parent based on file path or node ID pattern

### 2. Broken Parent References
- **Check**: All `parent` values reference existing node IDs
- **Fix**: Remove invalid parent or suggest correct parent

### 3. Circular References
- **Check**: Following parent links doesn't create loops
- **Fix**: Break cycle by identifying and removing one link

### 4. Missing Root Nodes
- **Check**: Each graph has at least one root node
- **Fix**: Create root node for graph type

### 5. Disconnected Subgraphs
- **Check**: All nodes reachable from root
- **Fix**: Create intermediate nodes to connect subgraphs

## Workflow

```python
def heal_graph(graph_file):
    graph = load_json(graph_file)
    issues = []
    
    # Check 1: Orphaned nodes
    for node in graph["nodes"]:
        if node.get("type") != "root" and "parent" not in node:
            issues.append({
                "type": "orphaned",
                "node": node["id"],
                "suggested_parent": infer_parent(node)
            })
    
    # Check 2: Broken references
    all_ids = {n["id"] for n in graph["nodes"]}
    for node in graph["nodes"]:
        if "parent" in node and node["parent"] not in all_ids:
            issues.append({
                "type": "broken_parent",
                "node": node["id"],
                "invalid_parent": node["parent"]
            })
    
    # Check 3: Cycles
    cycles = detect_cycles(graph)
    issues.extend(cycles)
    
    return issues
```

## Related

### Parent Skill

- `skill-maintain-kg`

### Follows

- `skill-kg-update-node`

---

**Implementation**: Rule-based (Python)
**Status**: Defined

```
Execute: `write` tool.

Report:

✅ Created KG Maintenance skill tree:
- skill:maintain-kg (orchestrator)
- skill:kg-monitor (sub-skill)
- skill:kg-update-node (sub-skill)
- skill:kg-heal (sub-skill)

Agent self-evolution capability defined.
```

---

**[Continue to PART 3 for remaining phases...]**
