# AI Agent Setup Assistant Guide
## Structured Instructions for AI Agents Building New Agent Systems

**Version**: 1.0  
**Target Audience**: AI Assistants (Claude, GPT, etc.)  
**Purpose**: Execute agent system setup following structured protocols  
**Human Companion Guide**: See `AI_AGENT_STARTUP_GUIDE.md`

---

## How to Use This Guide

When a human asks you to help build a new AI agent system, follow this guide **sequentially**. Each section has:
- **Objective**: What you're accomplishing
- **Required Input**: What you need from the human
- **Actions**: Concrete steps to execute
- **Validation**: How to verify success
- **Output**: What artifacts you create

---

## Phase 1: Information Discovery

### Objective
Gather all necessary information before creating any files.

### Required Input from Human

Ask these questions **in order**. Do not proceed until you have clear answers:

#### Question Set 1: Domain & Purpose
```
I'll help you build a structured AI agent system. First, I need to understand your domain:

1. What domain is your agent working in? (e.g., Education, Healthcare, Legal, Software Development)
2. What is the primary purpose of the agent? What problems will it solve?
3. Who are the end users?
```

Wait for response. Record answers.

#### Question Set 2: Agent Roles
```
How many distinct roles will your agent have? (e.g., 2 roles like "Teaching Assistant" and "Developer")

For each role, I need:
- Role name
- Personality (formal/casual/empathetic/technical)
- 3-5 primary tasks
- Communication style
- Key boundaries (what it won't do)

Let's define role 1 first: [Ask about each attribute]
```

Wait for response. Record answers for each role.

#### Question Set 3: Knowledge Requirements
```
What knowledge will your agent need to access?

1. What content types? (course materials, documentation, policies, etc.)
2. What are the sources? (PDFs, databases, APIs, websites)
3. How is it organized? (by topic, module, feature, etc.)
4. Approximately how much content? (10 documents, 100 pages, etc.)
```

Wait for response. Record answers.

#### Question Set 4: Skills & Tools
```
What capabilities and tools will your agent need?

1. What should it be able to DO? (analyze, explain, generate, review, etc.)
2. Are there existing tools to integrate? (compilers, APIs, databases)
3. Any domain-specific skills? (code review, medical diagnosis, legal research)
```

Wait for response. Record answers.

#### Question Set 5: Workflows & Standards
```
What rules and workflows must your agent follow?

1. Any mandatory workflows? (multi-step processes that must be followed)
2. Any standards to enforce? (style guides, regulations, policies)
3. Any safety boundaries? (what must never happen)
```

Wait for response. Record answers.

### Validation Checkpoint

Before proceeding, confirm:
```
Let me confirm what I've gathered:

**Domain**: [domain]
**Purpose**: [purpose]
**Users**: [users]

**Roles** ([N] total):
1. [Role 1 name]: [brief description]
2. [Role 2 name]: [brief description]

**Knowledge Areas**: [list]
**Key Skills**: [list]
**Critical Workflows**: [list]

Is this correct? Should I proceed with setup?
```

Wait for confirmation.

---

## Phase 2: Architecture Design

### Objective
Design the 3-Track system and knowledge graph structure.

### Actions

#### Action 2.1: Design Behavior Taxonomy
Based on gathered information, create a list:

**Core Behaviors** (apply to all roles):
- [List 5-10 core behaviors based on safety boundaries and standards]

**Role-Specific Behaviors** (for each role):
- Role 1: [List 3-5 behaviors]
- Role 2: [List 3-5 behaviors]

**Workflows**:
- [List key workflows as multi-step processes]

Present to human:
```
I've designed the behavior system:

**Core Behaviors** (all roles):
1. [Behavior 1]
2. [Behavior 2]
...

**[Role 1] Behaviors**:
1. [Behavior 1]
...

**Workflows**:
1. [Workflow name]: [Step 1] → [Step 2] → [Step 3]

Should I proceed with this structure?
```

#### Action 2.2: Design Knowledge Graph Structure
Based on knowledge requirements, design the graph:

**Top-level categories**: [List]
**Subcategories**: [List]
**Relationships**: [Prerequisites, related topics]

Present structure:
```
Knowledge Graph Structure:

Root
├── [Category 1]
│   ├── [Subcategory 1.1]
│   └── [Subcategory 1.2]
├── [Category 2]
│   └── [Subcategory 2.1]

Key relationships:
- [Topic A] → prerequisite for → [Topic B]
- [Topic C] → related to → [Topic D]

Proceed with this structure?
```

#### Action 2.3: Design Skills Taxonomy
Based on capabilities needed:

**Skill Categories**:
- [Category 1]: [Skills list]
- [Category 2]: [Skills list]

Present:
```
Skills Structure:

**[Category 1]**:
- [Skill 1]: [Description]
- [Skill 2]: [Description]

**[Category 2]**:
- [Skill 3]: [Description]

Proceed?
```

### Validation Checkpoint
```
Architecture designed. Ready to create project structure. Proceed?
```

---

## Phase 3: Create Project Structure

### Objective
Create the complete folder structure and placeholder files.

### Actions

#### Action 3.1: Create Folder Structure

Execute these file operations:

```python
# Directories to create
directories = [
    ".cursor",
    "agents",
    "agents/behaviors",
    "agents/behaviors/core",
    "agents/knowledge-graphs",
    "agents/skills",
    "docs",
    "docs/developer",
    "docs/developer/plan",
    "docs/developer/plan/todo",
    "docs/developer/plan/completed",
    "scripts",
    "temp"
]

# Add role-specific directories
for role in roles:  # from Phase 1
    directories.append(f"agents/behaviors/{role['id']}")
    directories.append(f"agents/skills/{role['id']}")

# Add domain content directories
for category in knowledge_categories:  # from Phase 2
    directories.append(f"docs/{category['id']}")
```

Use `write` tool to create `.gitkeep` file in each empty directory.

Report:
```
✅ Created [N] directories
```

#### Action 3.2: Create Identity File

Use gathered information to populate `.cursor/identity.md`:

```markdown
# [Agent Name] Identity

## Core Identity
- **Name**: [from Phase 1]
- **Domain**: [from Phase 1]
- **Version**: 1.0
- **Organization**: [from Phase 1]
- **Primary Purpose**: [from Phase 1]

## Roles

[For each role from Phase 1, create section:]
### Role [N]: [Role Name]
- **Personality**: [from Phase 1]
- **Communication Style**: [from Phase 1]
- **Primary Responsibilities**:
  [List tasks from Phase 1]
- **Boundaries**:
  - Will NOT: [from Phase 1]
  - Will ALWAYS: [from Phase 1]

## Core Values
[Based on workflows and standards from Phase 1]

## Safety & Ethics
[Based on boundaries from Phase 1]
```

Execute: `write` tool to create file.

Report:
```
✅ Created .cursor/identity.md
```

#### Action 3.3: Create NEW_AGENT_START_HERE.md

Populate with project-specific information:

```markdown
# Welcome, [Agent Name]!

## Your Identity
You are an AI agent for [domain]. Read your full identity:
- `.cursor/identity.md`

## Your Knowledge
Your knowledge is organized in graphs:
- `agents/knowledge-graphs/master-graph.json` - START HERE

## Your Roles
You have [N] roles:
[For each role:]
1. **[Role Name]**: [Brief description from Phase 1]

## Startup Checklist
When you start a new session:
1. ✅ Read `.cursor/identity.md`
2. ✅ Load `master-graph.json`
3. ✅ Ask user: "Which role should I activate?"
4. ✅ Load role-specific graphs for that role

## Quick Reference
- Behaviors: `agents/behaviors/`
- Skills: `agents/skills/`
- Domain Content: `docs/[categories]/`

## Key Workflows
[List workflows from Phase 1]
```

Execute: `write` tool to create file.

Report:
```
✅ Created agents/NEW_AGENT_START_HERE.md
```

#### Action 3.4: Create USER_MANUAL.md

Create comprehensive user manual with all gathered info.

Execute: `write` tool to create file following template from human guide.

Report:
```
✅ Created agents/USER_MANUAL.md
```

### Validation Checkpoint
```
✅ Core structure created:
- [N] directories
- Identity file
- Agent start guide
- User manual

Proceed to knowledge graphs?
```

---

## Phase 4: Create Knowledge Graphs

### Objective
Create all JSON knowledge graphs with proper structure.

### Actions

#### Action 4.1: Create Master Graph

```json
{
  "graphType": "master",
  "project": "[project name]",
  "generatedAt": "[current date]",
  "graphs": [
    {
      "id": "docs-graph",
      "path": "agents/knowledge-graphs/docs-graph.json",
      "description": "Domain knowledge and content"
    },
    [For each role, add 3 graphs:]
    {
      "id": "[role-id]-knowledge",
      "path": "agents/knowledge-graphs/[role-id]-knowledge-graph.json",
      "description": "Knowledge specific to [role-name]"
    },
    {
      "id": "[role-id]-skills",
      "path": "agents/knowledge-graphs/[role-id]-skills-graph.json",
      "description": "Skills available to [role-name]"
    },
    {
      "id": "[role-id]-behaviors",
      "path": "agents/knowledge-graphs/[role-id]-behaviors-graph.json",
      "description": "Behaviors for [role-name]"
    }
  ],
  "roles": [
    [For each role:]
    {
      "id": "[role-id]",
      "name": "[role-name]",
      "graphs": ["docs-graph", "[role-id]-knowledge", "[role-id]-skills", "[role-id]-behaviors"]
    }
  ]
}
```

Execute: `write` tool to create `agents/knowledge-graphs/master-graph.json`

#### Action 4.2: Create Domain Knowledge Graph

Using structure from Phase 2:

```json
{
  "graphType": "domain",
  "project": "[project name]",
  "generatedAt": "[current date]",
  "nodes": [
    {
      "id": "docs:root",
      "type": "root",
      "title": "[Domain] Knowledge Base"
    },
    [For each category from Phase 2:]
    {
      "id": "docs:[category-id]",
      "type": "folder-index",
      "path": "docs/[category-id]",
      "title": "[Category Name]",
      "parentFolder": "docs:root"
    }
  ],
  "links": [
    [For each category:]
    {
      "source": "docs:root",
      "target": "docs:[category-id]",
      "relationship": "contains"
    }
  ],
  "metadata": {
    "totalNodes": [count],
    "totalLinks": [count]
  }
}
```

Execute: `write` tool to create `agents/knowledge-graphs/docs-graph.json`

#### Action 4.3: Create Role-Specific Graphs

For each role, create 3 graphs (knowledge, skills, behaviors).

**Skills Graph** (`[role-id]-skills-graph.json`):
```json
{
  "graphType": "skills",
  "role": "[role-id]",
  "generatedAt": "[current date]",
  "skills": [
    [For each skill from Phase 2:]
    {
      "id": "skill-[###]",
      "name": "[Skill Name]",
      "category": "[Category]",
      "description": "[Description]",
      "path": "agents/skills/[category]/[skill-id].md",
      "prerequisites": [],
      "relatedBehaviors": []
    }
  ]
}
```

**Behaviors Graph** (`[role-id]-behaviors-graph.json`):
```json
{
  "graphType": "behaviors",
  "role": "[role-id]",
  "generatedAt": "[current date]",
  "behaviors": [
    [For each behavior from Phase 2:]
    {
      "id": "behavior:[type]:[id]",
      "type": "[core|role-specific|workflow]",
      "name": "[Behavior Name]",
      "description": "[Description]",
      "path": "agents/behaviors/[type]/[id].md",
      "priority": "[high|medium|low]"
    }
  ]
}
```

Execute: `write` tool for each graph file.

Report:
```
✅ Created knowledge graphs:
- master-graph.json
- docs-graph.json
- [N] role-specific graphs ([N]*3 files)

Total: [count] graph files
```

### Validation Checkpoint
```
Knowledge graph structure complete. Proceed to content templates?
```

---

## Phase 5: Create Content Templates

### Objective
Create standard templates and initial behavior/skill documentation.

### Actions

#### Action 5.1: Create Content Template

Create `docs/CONTENT_TEMPLATE.md`:

```markdown
---
type: [concept | resource | workflow | skill | behavior]
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

## Diagrams
> **[Diagram Name]**: [Text-based description]

## Related Resources
- [Link to related content]
```

Execute: `write` tool.

#### Action 5.2: Create Core Behavior Files

For each core behavior from Phase 2, create file:

`agents/behaviors/core/[behavior-id].md`:
```markdown
---
type: behavior
category: core
id: [behavior-id]
priority: high
applies-to:
  - all-roles
---

# [Behavior Name]

## Description
[What this behavior ensures]

## Rules
1. [Rule 1]
2. [Rule 2]

## Examples

### ✅ Good
[Example]

### ❌ Bad
[Example]

## Related
- Workflows: [list]
- Skills: [list]
```

Execute: `write` tool for each core behavior.

#### Action 5.3: Create Role-Specific Behavior Files

For each role-specific behavior from Phase 2, create file in:
`agents/behaviors/[role-id]/[behavior-id].md`

Use same template as core behaviors.

Execute: `write` tool for each behavior.

#### Action 5.4: Create Skill Definition Files

For each skill from Phase 2, create file in:
`agents/skills/[category]/[skill-id].md`

```markdown
---
type: skill
category: [category]
id: [skill-id]
roles:
  - [role-id]
---

# [Skill Name]

## Description
[What this skill enables]

## Usage
[When and how to use this skill]

## Prerequisites
- [Prerequisite 1]

## Related
- Behaviors: [list]
- Tools: [list]
```

Execute: `write` tool for each skill.

Report:
```
✅ Created documentation:
- Content template
- [N] core behaviors
- [N] role-specific behaviors
- [N] skill definitions

Total: [count] markdown files
```

### Validation Checkpoint
```
Documentation created. Proceed to validation tools?
```

---

## Phase 6: Create Validation Tools

### Objective
Create scripts to validate the structure.

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
        'domain': ['graphType', 'project', 'nodes', 'links'],
        'skills': ['graphType', 'role', 'skills'],
        'behaviors': ['graphType', 'role', 'behaviors']
    }
    
    graph_type = graph.get('graphType', 'unknown')
    required = required_fields.get(graph_type, ['graphType', 'project'])
    
    for field in required:
        if field not in graph:
            print(f"❌ Missing required field: {field}")
            return False
    
    # Validate file references
    files_checked = 0
    files_missing = 0
    
    if 'nodes' in graph:
        for node in graph['nodes']:
            if 'path' in node:
                files_checked += 1
                if not os.path.exists(node['path']):
                    print(f"⚠️  Missing file: {node['path']}")
                    files_missing += 1
    
    if 'skills' in graph:
        for skill in graph['skills']:
            if 'path' in skill:
                files_checked += 1
                if not os.path.exists(skill['path']):
                    print(f"⚠️  Missing file: {skill['path']}")
                    files_missing += 1
    
    if 'behaviors' in graph:
        for behavior in graph['behaviors']:
            if 'path' in behavior:
                files_checked += 1
                if not os.path.exists(behavior['path']):
                    print(f"⚠️  Missing file: {behavior['path']}")
                    files_missing += 1
    
    if files_missing > 0:
        print(f"⚠️  {files_missing}/{files_checked} referenced files missing")
    else:
        print(f"✅ All {files_checked} referenced files exist")
    
    print(f"✅ {graph_path} structure is valid")
    return True

def main():
    print("=" * 60)
    print("Knowledge Graph Validation")
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
        results.append(validate_graph(str(graph_path)))
    
    print("\n" + "=" * 60)
    print(f"Validation Complete: {sum(results)}/{len(results)} graphs valid")
    print("=" * 60)

if __name__ == '__main__':
    main()
```

Execute: `write` tool.

#### Action 6.2: Create Structure Validator

Create `scripts/validate_structure.py`:

```python
import os
from pathlib import Path

def check_structure():
    """Validates project folder structure"""
    print("🔍 Validating project structure...\n")
    
    required_dirs = [
        '.cursor',
        'agents',
        'agents/behaviors',
        'agents/behaviors/core',
        'agents/knowledge-graphs',
        'agents/skills',
        'docs',
        'docs/developer',
        'scripts',
        'temp'
    ]
    
    required_files = [
        '.cursor/identity.md',
        'agents/NEW_AGENT_START_HERE.md',
        'agents/USER_MANUAL.md',
        'agents/knowledge-graphs/master-graph.json',
        'agents/knowledge-graphs/docs-graph.json',
        'docs/CONTENT_TEMPLATE.md'
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
    
    all_ok = (dirs_ok == len(required_dirs)) and (files_ok == len(required_files))
    
    if all_ok:
        print("✅ Project structure is valid!")
    else:
        print("⚠️  Project structure is incomplete")
    
    return all_ok

if __name__ == '__main__':
    check_structure()
```

Execute: `write` tool.

Report:
```
✅ Created validation scripts:
- scripts/validate_graphs.py
- scripts/validate_structure.py
```

---

## Phase 7: Create README and Documentation

### Objective
Create top-level documentation.

### Actions

#### Action 7.1: Create README.md

```markdown
# [Project Name]

[One sentence description based on Phase 1]

## Overview

This is a [domain] AI agent system with [N] roles:
- **[Role 1]**: [Description from Phase 1]
- **[Role 2]**: [Description from Phase 1]

## Quick Start

### For Users
See [`agents/USER_MANUAL.md`](agents/USER_MANUAL.md) for complete instructions.

**Quick Start Prompt**:
\`\`\`
@NEW_AGENT_START_HERE.md

I'm working with the [Agent Name].
Please load your identity and knowledge graphs, then confirm you're ready.
Which role should I activate?
\`\`\`

### For Developers
- See [`docs/developer/`](docs/developer/) for development guides
- Run validation: `python scripts/validate_structure.py`

### For the Agent
Start here: [`agents/NEW_AGENT_START_HERE.md`](agents/NEW_AGENT_START_HERE.md)

## Project Structure

\`\`\`
[Project tree based on created structure]
\`\`\`

## Knowledge Graph System

This project uses interconnected JSON knowledge graphs:
- **Master Graph**: `agents/knowledge-graphs/master-graph.json` (entry point)
- **Domain Graph**: `docs-graph.json` (all domain content)
- **Role Graphs**: [N] sets of knowledge/skills/behaviors graphs

## Validation

Run validation scripts:
\`\`\`bash
python scripts/validate_structure.py
python scripts/validate_graphs.py
\`\`\`

## License

[Specify license]
```

Execute: `write` tool.

#### Action 7.2: Create SETUP_COMPLETE.md

```markdown
# Setup Complete ✅

## Project: [Project Name]
**Created**: [Current Date]
**Domain**: [Domain]
**Roles**: [N]

## Setup Summary

### ✅ Completed

1. **Project Structure**
   - [N] directories created
   - Core files in place
   
2. **Knowledge Graphs**
   - Master graph linking [N] graphs
   - Domain graph with [N] categories
   - [N] role-specific graph sets
   
3. **Documentation**
   - Identity defined
   - User manual created
   - Agent start guide created
   - [N] behaviors documented
   - [N] skills documented

4. **Validation**
   - Structure validator created
   - Graph validator created

## Verification Results

### Structure Validation
Run: `python scripts/validate_structure.py`

### Graph Validation
Run: `python scripts/validate_graphs.py`

## Next Steps

1. **Add Domain Content**
   - Process source materials into `docs/[categories]/`
   - Update `docs-graph.json` for each addition
   - Follow template in `docs/CONTENT_TEMPLATE.md`

2. **Test the Agent**
   - Use startup prompt from README.md
   - Test each role
   - Verify knowledge retrieval

3. **Iterate**
   - Add more behaviors as needed
   - Expand skills
   - Refine workflows

## Quick Start

To activate the agent, use:
\`\`\`
@NEW_AGENT_START_HERE.md
\`\`\`
```

Execute: `write` tool.

Report:
```
✅ Created documentation:
- README.md
- SETUP_COMPLETE.md
```

---

## Phase 8: Final Validation

### Objective
Run all validators and confirm setup is complete.

### Actions

#### Action 8.1: Run Structure Validator

Execute: `run_terminal_cmd`
```bash
python scripts/validate_structure.py
```

Capture output. Report results.

#### Action 8.2: Run Graph Validator

Execute: `run_terminal_cmd`
```bash
python scripts/validate_graphs.py
```

Capture output. Report results.

#### Action 8.3: Generate Summary

```
🎉 Setup Complete!

**Project**: [Project Name]
**Domain**: [Domain]
**Roles**: [N] ([list])

**Created**:
- [N] directories
- [N] JSON knowledge graphs
- [N] behavior definitions
- [N] skill definitions
- [N] core documentation files
- [N] validation scripts

**Validation Results**:
- Structure: [PASS/FAIL]
- Graphs: [PASS/FAIL]

**Next Steps**:
1. Add domain content to docs/[categories]/
2. Test agent with startup prompt
3. Iterate based on usage

**Ready to use!** See README.md for quick start.
```

---

## Error Handling Protocols

### If Human Provides Incomplete Information

Response:
```
I need more information to proceed. Specifically:

[List missing items]

Could you provide these details?
```

Wait for response. Do not guess or make assumptions.

### If Validation Fails

Response:
```
⚠️ Validation failed:

[List issues]

I can:
1. Fix these issues automatically
2. Explain what went wrong
3. Create the missing files

What would you like me to do?
```

### If Human Requests Changes Mid-Setup

Response:
```
I can make those changes. This will affect:
- [List affected files/graphs]

Should I:
1. Make the changes now (will update [N] files)
2. Finish setup first, then make changes
3. Cancel and restart with new parameters

What's your preference?
```

---

## Quick Reference: Command Sequences

### Minimal Setup (Fast)
1. Phase 1: Discovery (required)
2. Phase 3: Create structure
3. Phase 4: Create graphs (minimal)
4. Phase 7: Create README
5. Phase 8: Validate

### Complete Setup (Recommended)
Execute all phases 1-8 sequentially.

### Add Content Later
After initial setup:
1. Create markdown files in `docs/[category]/`
2. Update `docs-graph.json` with new nodes
3. Run `python scripts/validate_graphs.py`

---

## Success Criteria

Before declaring "Setup Complete", verify:

- [ ] All Phase 1 questions answered
- [ ] All required directories created
- [ ] All 3 core files created (identity, start guide, user manual)
- [ ] Master graph exists and is valid JSON
- [ ] At least one behavior file created
- [ ] At least one skill file created
- [ ] README.md exists
- [ ] Both validation scripts run without errors
- [ ] SETUP_COMPLETE.md created with summary

---

## Tips for Efficiency

1. **Batch Operations**: Create all files in a phase before moving to next
2. **Use Variables**: Store project name, roles, etc. to avoid repetition
3. **Validate Early**: Run validators after Phase 4 and Phase 6
4. **Clear Communication**: Show progress after each phase
5. **Confirm Before Large Operations**: Ask before creating >20 files

---

## Example Session Flow

```
Human: Help me build an AI agent for medical diagnosis

AI: [Execute Phase 1: Ask all discovery questions]
AI: [Wait for answers]
AI: [Confirm gathered information]
AI: [Execute Phase 2: Design architecture]
AI: [Show architecture, get confirmation]
AI: [Execute Phase 3-7: Create all files]
AI: [Execute Phase 8: Validate]
AI: [Show summary]

✅ Setup complete! 42 files created. See SETUP_COMPLETE.md
```

---

**Remember**: This is a structured protocol. Follow it sequentially. Ask for clarification when needed. Validate at checkpoints. Report progress clearly.

