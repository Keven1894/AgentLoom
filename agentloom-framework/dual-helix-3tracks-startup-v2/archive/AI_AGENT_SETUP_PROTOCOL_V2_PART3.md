# AI Agent Setup Protocol V2.0 - PART 3

## Continuation: Content Templates, Skills Analysis, KG Maintenance, Testing

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
```

Report:

✅ Created KG Maintenance skill tree:

- skill:maintain-kg (orchestrator)
- skill:kg-monitor (sub-skill)
- skill:kg-update-node (sub-skill)
- skill:kg-heal (sub-skill)

Agent self-evolution capability defined.

## Phase 8: User Manual Testing Protocol (V2 NEW PHASE)

### Objective

Test the USER_MANUAL.md by simulating a cold-start agent scenario.

### Actions

#### Action 8.1: Create Testing Directory

```bash
mkdir temp/user_manual_test
```

#### Action 3.4: Create NEW_AGENT_START_HERE.md (V2 Enhanced: Machine-Executable)

**V2 Enhancement**: Now a machine-executable script with operational boundaries and agent reference.

Create `agents/NEW_AGENT_START_HERE.md`:

```markdown
# NEW_AGENT_START_HERE.md

# Agent Initialization Script (Executed by the Agent Itself)

Hello Agent — this is your startup script.

Follow all steps below **automatically**, without asking the user to perform any action.

---

## Step 1 — Load Identity
Read:
@.cursor/identity.md

Purpose:
- Understand your name, purpose, boundaries, and the two roles you support.

## Step 2 — Master the Knowledge Graph
Read:
@agents/knowledge-graphs/master-graph.json

Purpose:
- This is your "Mind GPS".
- It links to all other graphs (Domain, Role Knowledge, Skills, Behaviors).
- **Rule**: You must traverse this graph to find files. Do not guess paths.

## Step 3 — Select Your Role
Ask the user:
"I am ready. Which role should I activate? (e.g., [Role 1] or [Role 2])"

Wait for the user's reply.

## Step 4 — Load Role-Specific Graphs
Once the user selects a role, read the 3 graphs for that role ONLY:
1. `agents/knowledge-graphs/[role]-knowledge-graph.json`
2. `agents/knowledge-graphs/[role]-skills-graph.json`
3. `agents/knowledge-graphs/[role]-behaviors-graph.json`

Purpose:
- These give you the specific context, capabilities, and protocols for your chosen role.

## Step 5 — Load Core Behaviors
Read the core behavior index or key files:
@.cursor/rules.md

Purpose:
- Ensure you adhere to safety, communication, and project structure protocols.

## Step 6 — Internalize Operational Boundaries
**CRITICAL**: You must strictly adhere to these file system boundaries.

### What NOT to Touch (Read-Only)
- `.cursor/` (Identity, Rules, Behaviors) — *Never modify unless explicitly instructed by an "Agent Builder" role.*
- `agents/knowledge-graphs/` — *Never modify manually. Use the `skill-maintain-kg` to update these.*
- `agents/NEW_AGENT_START_HERE.md` — *This file is immutable.*

### What You Can Freely Access (Read/Write)
- `docs/` — *Create and update documentation here.*
- `[Content Directories]` — *Manage project files here.*
- `temp/` — *Use for scratchpads and intermediate work.*

### Configuration Files Explained
- `.cursor/identity.md`: Who you are.
- `.cursor/rules.md`: How you behave.
- `agents/knowledge-graphs/*.json`: What you know.

## Step 7 — Confirm Ready
Output exactly:
"System Ready. [Role Name] active. Awaiting instructions."

---

## Appendix: Agent Reference Card

### 5-Minute Cold Start Checklist

- [ ] Load `.cursor/identity.md`
- [ ] Load `agents/knowledge-graphs/master-graph.json`
- [ ] Ask user for role selection
- [ ] Load 3 role-specific graphs
- [ ] Confirm operational with summary

### Key Node IDs (Bookmarks)

**System**:
- `sys:root` - System architecture root
- `sys:docs` - Documentation root

**[Role 1]**:
- `[role-1-root]` - [Role 1] root

**[Role 2]**:
- `[role-2-root]` - [Role 2] root

### Common Commands

**Validation**:
```bash
python scripts/validate_structure.py
python scripts/validate_graphs.py
```

**Visualization**:
Open `agents/knowledge-graphs/visualization.html` in browser

### Emergency: Lost Context

If you're confused about where you are or what to do:

1. Re-read `.cursor/identity.md` (who you are)
2. Ask user: "Which role should I be in? What task?"
3. Load relevant graphs for that role
4. Proceed with clarity

```

Execute: `write` tool to create file.

Report:
```

✅ Created agents/NEW_AGENT_START_HERE.md (Machine-Executable)

```

### Validation Checkpoint
```

✅ Core structure created:

### Actions

#### Action 3.5.1: Create USER_MANUAL.md Structure

This is a **Prompt Library**. Instead of manual instructions, provide copy-pasteable prompts.

Create `agents/USER_MANUAL.md`:

```markdown
# [Agent Name] - User Manual

**Version**: 2.0
**Last Updated**: [Date]
**Purpose**: Enable fresh agent instances to become operational in < 5 minutes

---

## 1. Quick Start (Copy & Paste This Prompt)

```text
Initialize as the [Agent Name].

Start by reading:
@agents/NEW_AGENT_START_HERE.md

Follow every step inside that file:
- Load identity
- Load master knowledge graph
- Ask for role selection
- Load all role-specific knowledge, skills, and behaviors
- Confirm operational state

Do not ask the user to do any manual loading; you must perform all loading steps yourself.
When finished, output: “System Ready”.
```

That’s it. Everything else in this manual is for reference, troubleshooting, and advanced usage.

## 2. Knowledge Graph Navigation

### 🪄 Prompt: Navigate the Graph

To explore the Knowledge Graph, use this prompt:

```text
Summarize the Master Knowledge Graph structure.
Then, find the node for [TOPIC] and explain its relationships.
```

### Visualization Tool

Open `agents/knowledge-graphs/visualization.html` in a browser to see the "Unified Brain" view.

## 3. Role-Specific Workflows

[For each role:]

### [Role Name] Workflows

#### Workflow: [Workflow Name]

**When**: [Condition]
**🪄 Prompt**:

```text
[Prompt text to trigger this workflow]
```

## 4. Key Behaviors & Protocols

**🪄 Prompt**:

```text
Review the [PROTOCOL_NAME] protocol and explain how it applies to my current task.
```

## 5. Skills Activation

**🪄 Prompt**:

```text
List all available skills for my current role.
Then, activate the [SKILL_NAME] skill.
```

## 6. Troubleshooting & Common Tasks

### Problem: Graph Inconsistency Detected

**🪄 Prompt**:

```text
Diagnose and heal the Knowledge Graph.
Identify any orphaned nodes or broken links and propose fixes.
```

### Problem: Role Confusion

**🪄 Prompt**:

```text
Clarify my current role and responsibilities.
```

```

Execute: `write` tool to create file.

Report:
```

✅ Created agents/USER_MANUAL.md (Prompt-Driven)

```

### Validation Checkpoint
```

✅ USER_MANUAL.md created:

- Includes Magic Activation Prompt
- Includes Prompt Library for workflows/skills
- References NEW_AGENT_START_HERE.md

#### Action 8.2: Create Test Protocol Document

Create `temp/user_manual_test/TEST_PROTOCOL.md`:

```markdown
# User Manual Cold-Start Test Protocol

## Objective
Verify that a fresh AI agent (new conversation, no prior context) can become operational in < 5 minutes using only the USER_MANUAL.md.

## Test Scenario

**Agent State**:
- New conversation tab
- No conversation history
- No memory of project setup
- Has access to file system only

**Goal**:
- Agent reads USER_MANUAL.md
- Follows instructions
- Becomes operational for chosen role
- Confirms readiness

## Test Procedure

### Setup (Human)
1. Open new conversation tab (fresh agent instance)
2. Provide only: `@agents/USER_MANUAL.md`
3. Say: "Follow the quick start guide"
4. Do NOT provide additional context

### Expected Agent Actions (< 5 minutes)
1. Read USER_MANUAL.md
2. Load identity file
3. Load master graph
4. Ask which role to activate
5. Load role-specific graphs
6. Confirm operational with summary

### Success Criteria
- [ ] Agent completes all steps without asking for clarification
- [ ] Agent correctly identifies available roles
- [ ] Agent loads appropriate graphs for chosen role
- [ ] Agent confirms understanding of key behaviors
- [ ] Agent confirms understanding of available skills
- [ ] Total time < 5 minutes
- [ ] Agent is ready for productive work

### Failure Scenarios
- Agent asks "What project is this?"
- Agent cannot find files referenced in manual
- Agent confused about which graphs to load
- Agent doesn't understand role boundaries
- Takes > 5 minutes

## Test Log Template

Use `test_log.md` to record:
- Timestamp for each step
- Agent's questions/confusions
- Issues encountered
- Time to completion

## Pain Points Document

Use `pain_points.md` to record:
- Sections of manual that were unclear
- Missing information
- Confusing instructions
- Suggested improvements

## Improvements Document

Use `improvements.md` to propose:
- Manual rewrites
- Additional sections
- Better examples
- Clarifications needed
```

Execute: `write` tool.

#### Action 8.3: Execute Test (Simulate)

Present to human:

```
I will now simulate a cold-start agent test.

Please confirm:
1. Should I proceed as if I'm a fresh agent with no context?
2. Do you want me to document the process in temp/user_manual_test/?
3. After the test, should I update USER_MANUAL.md based on findings?
```

Wait for confirmation, then:

1. "Forget" all setup context
2. Read only `agents/USER_MANUAL.md`
3. Follow quick start steps
4. Document experience in `temp/user_manual_test/test_log.md`
5. Document pain points in `temp/user_manual_test/pain_points.md`
6. Document improvements in `temp/user_manual_test/improvements.md`

Report findings:

```
🧪 Cold-Start Test Results:

**Time to Operational**: [X minutes]
**Steps Completed**: [N/N]
**Issues Encountered**: [N]

**Critical Findings**:
- [Finding 1]
- [Finding 2]

**Recommended Manual Updates**:
- [Update 1]
- [Update 2]

Should I apply these updates to USER_MANUAL.md?
```

---

## Phase 9: Skills Implementation (V2 NEW PHASE)

### Objective

Based on Phase 2.3 classification, create actual tool implementations for skills.

### Actions

#### Action 9.1: Review Skills Classification

Review all skills from Phase 2 and their implementation types.

#### Action 9.2: Create Rule-Based Skill Tools

For each `rule-based` skill:

Create Python script in `scripts/[skill-id].py`:

```python
#!/usr/bin/env python3
"""
[Skill Name]
Implementation: Rule-based

[Description from skill markdown]
"""

import os
import sys
from pathlib import Path

def main():
    """
    Main execution function
    """
    # Implementation based on skill definition
    print(f"Executing [Skill Name]...")
    
    # [Actual implementation]
    
    print("✅ Complete")

if __name__ == '__main__':
    main()
```

#### Action 9.3: Create LLM-Based Skill Prompts

For each `llm-based` skill:

Create prompt template in `agents/skills/prompts/[skill-id]-prompt.md`:

```markdown
# [Skill Name] - LLM Prompt Template

## Required LLM Tier
[Max / SLM tier from classification]

## Context to Provide
[List what context the LLM needs]

## Prompt Template

\`\`\`
You are [Agent Name], [Role Name].

**Task**: [Task description from skill definition]

**Context**:
{context_variables}

**Input**:
{input_data}

**Instructions**:
1. [Step 1]
2. [Step 2]

**Output Format**:
[Expected output structure]

**Constraints**:
- [Constraint 1 from behaviors]
- [Constraint 2]
\`\`\`

## Expected Output Schema

\`\`\`json
{
  "field1": "value",
  "field2": ["list"]
}
\`\`\`

## Post-Processing

[Any rule-based processing of LLM output]
```

#### Action 9.4: Create Hybrid Skill Orchestrators

For each `hybrid` skill:

Create orchestration script in `scripts/[skill-id]_orchestrator.py`:

```python
#!/usr/bin/env python3
"""
[Skill Name] - Hybrid Orchestrator
Implementation: Rule-based preprocessing + LLM + Rule-based validation
"""

def preprocess():
    """Rule-based preprocessing"""
    # Gather data, validate inputs
    pass

def llm_process(preprocessed_data):
    """LLM analysis step"""
    # Call LLM with prompt template
    # Parse LLM response
    pass

def validate_and_apply(llm_output):
    """Rule-based validation and application"""
    # Validate LLM output against schema
    # Apply changes with safeguards
    pass

def main():
    print("🔄 [Skill Name] (Hybrid)")
    
    print("Step 1: Preprocessing...")
    data = preprocess()
    
    print("Step 2: LLM Analysis...")
    result = llm_process(data)
    
    print("Step 3: Validation & Application...")
    validate_and_apply(result)
    
    print("✅ Complete")

if __name__ == '__main__':
    main()
```

Report:

```
✅ Created skill implementations:
- [N] rule-based scripts
- [M] LLM prompt templates
- [P] hybrid orchestrators

All skills from Phase 2 now have implementation artifacts.
```

---

## Phase 10: Final Validation & Documentation

### Objective

Run all validators, create final documentation, and confirm system is ready.

### Actions

#### Action 10.1: Run Structure Validator

Execute: `run_terminal_cmd`

```bash
python scripts/validate_structure.py
```

Capture output. If failures, fix and re-run.

#### Action 10.2: Run Graph Validator

Execute: `run_terminal_cmd`

```bash
python scripts/validate_graphs.py
```

Capture output. If orphaned nodes or broken links, fix graphs and re-run.

#### Action 10.3: Visual Validation

Instruct human:

```
Please open agents/knowledge-graphs/visualization.html in a browser.

Validation checklist:
1. Click "🧠 Unified Brain (ALL)" - verify all graphs merge
2. Check for floating nodes (disconnected)
3. Verify behaviors (yellow hexagons) are connected
4. Verify skills (pink triangles) are connected
5. Verify cross-graph links (dashed amber lines) are visible

Report any issues.
```

Wait for confirmation or issue report.

#### Action 10.4: Create README.md

Create root `README.md`:

```markdown
# [Project Name]

[One-sentence description from Phase 1]

## Overview

This is a [domain] AI agent system with [N] roles:
- **[Role 1]**: [Description]
- **[Role 2]**: [Description]

Built using the **V2.0 Agentic AI Architecture** with fully-connected Knowledge Graphs.

## Quick Start

### For Users (Starting the Agent)

Use this prompt:
\`\`\`
@agents/NEW_AGENT_START_HERE.md

I'm working with [Agent Name].
Please load your identity and knowledge graphs, then confirm you're ready.
Which role should I activate?
\`\`\`

For detailed instructions, see [`agents/USER_MANUAL.md`](agents/USER_MANUAL.md).

### For Developers

See [`docs/[builder-folder]/`](docs/[builder-folder]/) for architecture and implementation guides.

**Validate the system**:
\`\`\`bash
python scripts/validate_structure.py
python scripts/validate_graphs.py
\`\`\`

**Visualize the Knowledge Graph**:
Open `agents/knowledge-graphs/visualization.html` in a browser.

## Project Structure

\`\`\`
[project-root]/
├── .cursor/               # System configuration (auto-loaded)
│   ├── identity.md        # Agent identity
│   ├── rules.md           # Behavior index
│   ├── behaviors/         # Protocol definitions
│   └── templates/         # Content templates
├── agents/                # Agent logic
│   ├── knowledge-graphs/  # KG JSON files + visualization
│   ├── skills/            # Skill definitions & prompts
│   ├── NEW_AGENT_START_HERE.md
│   └── USER_MANUAL.md
├── docs/                  # Documentation (organized by role)
│   ├── general/           # Cross-role docs
│   ├── [builder-folder]/  # Builder-specific docs
│   └── [manager-folder]/  # Manager-specific docs
├── scripts/               # Automation & validation tools
└── [domain-specific folders]
\`\`\`

## Knowledge Graph System (V2.0)

This project uses **fully-connected** Knowledge Graphs:
- **Master Graph**: Entry point linking all sub-graphs
- **Domain Graphs**: [Domain] knowledge structure
- **Role Graphs**: [N] sets of knowledge/skills/behaviors per role

**V2.0 Features**:
- ✅ Every node has a parent (hierarchical)
- ✅ Cross-graph semantic links (behaviors ↔ skills ↔ knowledge)
- ✅ Interactive visualization tool
- ✅ Self-evolution capability (KG maintenance skill)

## Key Capabilities

### [Role 1 Name] Can:
- [Capability 1]
- [Capability 2]
- [Capability 3]

### [Role 2 Name] Can:
- [Capability 1]
- [Capability 2]
- [Capability 3]

## Validation

Run validation scripts to ensure system integrity:
\`\`\`bash
# Check folder structure
python scripts/validate_structure.py

# Check graph connectivity (V2 includes orphan detection)
python scripts/validate_graphs.py
\`\`\`

## Self-Evolution

This agent can maintain its own Knowledge Graph:
- Detects file system changes
- Updates KG automatically
- Heals broken links
- Validates connectivity

See `agents/skills/system/maintain-kg.md` for details.

## License

[Specify license]

---

**Built with AI Agent Setup Protocol V2.0**
```

Execute: `write` tool to create `README.md`

#### Action 10.5: Create SETUP_COMPLETE.md

Create `SETUP_COMPLETE.md`:

```markdown
# Setup Complete ✅

## Project: [Project Name]
**Created**: [Current Date]
**Domain**: [Domain]
**Roles**: [N]
**Architecture**: V2.0 (Fully-Connected Knowledge Graphs)

## Setup Summary

### ✅ Phase 1: Information Discovery
- Domain defined
- [N] roles identified
- Knowledge requirements gathered
- Skills classified by implementation type

### ✅ Phase 2: Architecture Design
- Behavior taxonomy created
- Fully-connected KG structure designed
- Skills classified (rule-based/LLM/hybrid)

### ✅ Phase 3: Project Structure
- [N] directories created
- Identity file defined
- Rules index created
- Start guide created

### ✅ Phase 3.5: User Manual (V2)
- Comprehensive USER_MANUAL.md created
- Cold-start tested
- Operational time: < 5 minutes

### ✅ Phase 4: Knowledge Graphs
- master-graph.json (entry point)
- [N] domain/project graphs
- [N]*3 role-specific graphs
- All nodes have parent links ✅
- Cross-graph links established ✅

### ✅ Phase 4.5: Visualization Tool (V2)
- visualization.html created
- Unified Brain view
- Role-specific views
- Connectivity validated ✅

### ✅ Phase 5: Content Templates
- [N] behavior files created
- [N] skill definition files created
- Content template created

### ✅ Phase 6: Validation Tools
- Structure validator
- Graph validator (V2 with connectivity checks)

### ✅ Phase 7: KG Maintenance Skill (V2)
- Orchestrator skill: maintain-kg
- Sub-skill: kg-monitor
- Sub-skill: kg-update-node
- Sub-skill: kg-heal
- Self-evolution capability enabled ✅

### ✅ Phase 8: User Manual Testing (V2)
- Cold-start test performed
- Pain points identified and fixed
- Manual validated ✅

### ✅ Phase 9: Skills Implementation (V2)
- [N] rule-based scripts created
- [M] LLM prompt templates created
- [P] hybrid orchestrators created

### ✅ Phase 10: Final Validation
- Structure: ✅ PASS
- Graphs: ✅ PASS ([N] graphs, [M] nodes, fully connected)
- Visualization: ✅ VERIFIED

## Verification Results

### Structure Validation
\`\`\`
[Output from validate_structure.py]
\`\`\`

### Graph Validation
\`\`\`
[Output from validate_graphs.py]
\`\`\`

### Visual Validation
- [x] Unified Brain view shows all graphs merged
- [x] No floating/disconnected nodes
- [x] Cross-graph links visible
- [x] All behaviors connected
- [x] All skills connected

## Project Statistics

- **Directories**: [N]
- **JSON Graphs**: [N] (all fully connected)
- **Behavior Files**: [N]
- **Skill Files**: [N]
- **Documentation Files**: [N]
- **Python Scripts**: [N]
- **Total Nodes in KG**: [N]
- **Total Edges in KG**: [M]

## Next Steps

### 1. Add Domain Content
- Process source materials into appropriate folders
- Use `skill:maintain-kg` to update KG automatically
- Follow template: `docs/general/CONTENT_TEMPLATE.md`

### 2. Test the Agent
- Use startup prompt from README.md
- Test each role
- Verify skill execution
- Test KG maintenance skill

### 3. Iterate & Evolve
- Add new skills as needed
- Expand behaviors
- Refine workflows
- Agent can update its own KG!

## Quick Start (Reminder)

To activate the agent:
\`\`\`
@agents/NEW_AGENT_START_HERE.md

I'm working with [Agent Name].
Load identity and graphs, confirm ready.
Which role should I activate?
\`\`\`

## Support Resources

- **User Manual**: `agents/USER_MANUAL.md`
- **Visualization**: `agents/knowledge-graphs/visualization.html`
- **Architecture Docs**: `docs/[builder-folder]/`
- **Validation Scripts**: `scripts/`

---

🎉 **System is fully operational with self-evolution capability!**

**Built with AI Agent Setup Protocol V2.0**
\`\`\`
```

Execute: `write` tool.

#### Action 10.6: Generate Final Summary

Present to human:

```
🎉 AI Agent System Setup Complete!

**Project**: [Project Name]
**Domain**: [Domain]
**Architecture**: V2.0 (Fully-Connected Knowledge Graphs)
**Roles**: [N] ([list])

**Statistics**:
- [N] directories created
- [N] JSON knowledge graphs (fully connected)
- [N] behavior definitions
- [N] skill definitions
- [N] validation & automation scripts
- [N] documentation files

**V2.0 Enhancements Applied**:
✅ Fully-connected Knowledge Graphs (parent links + cross-links)
✅ Interactive visualization tool with Unified Brain view
✅ Deep content indexing (file-level granularity)
✅ Comprehensive USER_MANUAL.md (< 5min cold-start)
✅ Skills classified by implementation (rule-based/LLM/hybrid)
✅ KG maintenance skill (self-evolution)
✅ Cold-start testing protocol
✅ Native behavior layer (.cursor/ optimization)

**Validation Results**:
- Structure: ✅ PASS
- Graphs: ✅ PASS (all nodes connected, no orphans)
- Visualization: ✅ VERIFIED (Unified Brain shows full connectivity)
- Cold-Start Test: ✅ PASS (operational in < 5 minutes)

**Next Steps**:
1. Add domain-specific content
2. Test agent with startup prompt
3. Verify skill execution
4. Use self-evolution capability to keep KG updated

**Ready to use!** See README.md and SETUP_COMPLETE.md for details.
```

---

## Error Handling Protocols

*[Keep from V1.0, no changes needed]*

---

## Phase 4.5: Create Visualization Tool (V2 NEW PHASE)

### Objective

Create an interactive HTML tool to visualize and validate Knowledge Graph connectivity.

### Why This Matters

Without visualization, you cannot verify:

- Are all nodes connected?
- Do cross-graph links work?
- Are there orphaned nodes?
- Is the graph truly a "Mind GPS"?

### Actions

#### Action 4.5.1: Create visualization.html

This is a large file (~500 lines). Create `agents/knowledge-graphs/visualization.html`:

**Key Features to Include**:

1. Load all JSON graphs
2. Merge nodes (deduplicate by ID)
3. Render with vis-network library
4. Color-code by type (behaviors, skills, knowledge, etc.)
5. Show parent-child edges (solid lines)
6. Show cross-graph links (dashed amber lines)
7. Button navigation (Unified Brain, per-role, per-graph)
8. Statistics overlay (node count, edge count)

**Implementation Template** (abbreviated):

```html
<!DOCTYPE html>
<html>
<head>
    <title>[Project Name] Knowledge Graph Visualization</title>
    <script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
    <style>
        body { margin: 0; font-family: 'Segoe UI', sans-serif; background: #0f172a; color: #f1f5f9; }
        #network { width: 100vw; height: 100vh; }
        .sidebar { position: fixed; left: 20px; top: 20px; background: rgba(15, 23, 42, 0.95); 
                   padding: 20px; border-radius: 12px; max-width: 250px; }
        button { display: block; width: 100%; margin: 5px 0; padding: 10px; border: none; 
                 border-radius: 6px; cursor: pointer; background: #334155; color: #f1f5f9; }
        button.active { background: #3b82f6; }
        .stats-overlay { position: absolute; top: 20px; right: 20px; background: rgba(15, 23, 42, 0.95);
                         padding: 15px; border-radius: 8px; }
        .legend { position: fixed; bottom: 20px; right: 20px; background: rgba(15, 23, 42, 0.95);
                  padding: 15px; border-radius: 8px; }
    </style>
</head>
<body>
    <div class="sidebar">
        <h2>[Project Name]</h2>
        <div class="btn-group-label">System Views</div>
        <button onclick="loadUnifiedGraph()" id="btn-unified">🧠 Unified Brain (ALL)</button>
        <button onclick="loadGraph('master')" class="active" id="btn-master">🌐 Master Graph</button>
        
        <div class="btn-group-label">[Role 1 Name]</div>
        <button onclick="loadGraph('[role-1-id]-knowledge')" id="btn-[role-1-id]-knowledge">🏗️ Knowledge</button>
        <button onclick="loadGraph('[role-1-id]-skills')" id="btn-[role-1-id]-skills">🛠️ Skills</button>
        <button onclick="loadGraph('[role-1-id]-behaviors')" id="btn-[role-1-id]-behaviors">🛡️ Behaviors</button>
        
        <div class="btn-group-label">[Role 2 Name]</div>
        <button onclick="loadGraph('[role-2-id]-knowledge')" id="btn-[role-2-id]-knowledge">📋 Knowledge</button>
        <button onclick="loadGraph('[role-2-id]-skills')" id="btn-[role-2-id]-skills">⚡ Skills</button>
        <button onclick="loadGraph('[role-2-id]-behaviors')" id="btn-[role-2-id]-behaviors">🤝 Behaviors</button>
    </div>

    <div style="position: relative;">
        <div class="stats-overlay">
            <div><strong>Graph:</strong> <span id="stat-name">-</span></div>
            <div><strong>Nodes:</strong> <span id="stat-nodes">0</span></div>
            <div><strong>Links:</strong> <span id="stat-links">0</span></div>
        </div>
        <div id="network"></div>
    </div>

    <div class="legend">
        <div>🟣 Root</div>
        <div>🔵 [Role 1]</div>
        <div>🟢 [Role 2]</div>
        <div>🟡 Behavior</div>
        <div>🟣 Skill</div>
        <div>🟠 Concept</div>
        <div>⚫ File/Doc</div>
    </div>

    <script>
        let network = null;
        const container = document.getElementById('network');

        const allGraphFiles = {
            'master': 'master-graph.json',
            '[domain-id]': '[domain-id]-graph.json',
            '[role-1-id]-knowledge': '[role-1-id]-knowledge-graph.json',
            '[role-1-id]-skills': '[role-1-id]-skills-graph.json',
            '[role-1-id]-behaviors': '[role-1-id]-behaviors-graph.json',
            '[role-2-id]-knowledge': '[role-2-id]-knowledge-graph.json',
            '[role-2-id]-skills': '[role-2-id]-skills-graph.json',
            '[role-2-id]-behaviors': '[role-2-id]-behaviors-graph.json'
        };

        // V2 CRITICAL: Composite Views
        const viewDependencies = {
            'master': ['master-graph.json', '[domain-id]-graph.json'],
            '[role-1-id]-skills': ['[role-1-id]-skills-graph.json', '[role-1-id]-behaviors-graph.json'],
            '[role-1-id]-behaviors': ['[role-1-id]-behaviors-graph.json', '[role-1-id]-skills-graph.json'],
            '[role-2-id]-skills': ['[role-2-id]-skills-graph.json', '[role-2-id]-behaviors-graph.json'],
            '[role-2-id]-behaviors': ['[role-2-id]-behaviors-graph.json', '[role-2-id]-skills-graph.json']
        };

        function getNodeColor(node) {
            const type = node.type || '';
            const id = node.id || '';

            if (type === 'root' || type === 'master') return '#8b5cf6'; // Violet
            if (type === 'project' || type === 'database') return '#f43f5e'; // Rose
            
            // V2: Type checks BEFORE ID checks
            if (type.includes('behavior') || type === 'core' || type === 'role-specific') return '#eab308';
            if (type.includes('skill')) return '#ec4899';
            if (type === 'concept') return '#f97316';
            if (type === 'document' || type === 'component') return '#64748b';
            
            if (id.includes('[role-1-id]') || id.includes('sys:')) return '#3b82f6';
            if (id.includes('[role-2-id]')) return '#10b981';
            
            return '#94a3b8';
        }

        function getNodeShape(node) {
            const type = node.type || '';
            if (type === 'root' || type === 'master') return 'diamond';
            if (type === 'project') return 'box';
            if (type === 'document') return 'ellipse';
            if (type === 'concept') return 'star';
            if (type.includes('behavior')) return 'hexagon';
            if (type.includes('skill')) return 'triangle';
            return 'dot';
        }

        function parseGraph(data, filterDeepNodes = false) {
            const nodes = [];
            const edges = [];

            const rawNodes = data.nodes || data.skills || data.behaviors || data.graphs || [];
            
            rawNodes.forEach(node => {
                if (filterDeepNodes && node.type === 'document') return;

                nodes.push({
                    id: node.id,
                    label: node.name || node.title || node.id,
                    title: `<b>${node.id}</b><br>${node.description || node.path || node.type}`,
                    color: getNodeColor(node),
                    shape: getNodeShape(node),
                    size: node.type === 'root' ? 30 : 20,
                    font: { color: '#f1f5f9' }
                });

                // V2: Parent links (solid edges)
                if (node.parent) {
                    edges.push({ from: node.parent, to: node.id });
                }

                // V2: Cross-graph links (dashed amber edges)
                if (node.links) {
                    Object.keys(node.links).forEach(linkType => {
                        const targets = node.links[linkType];
                        if (Array.isArray(targets)) {
                            targets.forEach(target => {
                                edges.push({
                                    from: node.id,
                                    to: target,
                                    label: linkType,
                                    color: { color: '#fbbf24', opacity: 0.6 },
                                    dashes: true
                                });
                            });
                        }
                    });
                }
            });

            return { nodes, edges };
        }

        function loadFiles(files, isMasterView = false) {
            const promises = files.map(file => fetch(file).then(r => r.json()));
            return Promise.all(promises).then(results => {
                let allNodes = new Map();
                let allEdges = [];

                results.forEach(data => {
                    const { nodes, edges } = parseGraph(data, isMasterView);
                    nodes.forEach(n => allNodes.set(n.id, n));
                    allEdges.push(...edges);
                });

                return { nodes: Array.from(allNodes.values()), edges: allEdges };
            });
        }

        function loadUnifiedGraph() {
            updateUI('unified');
            loadFiles(Object.values(allGraphFiles)).then(({ nodes, edges }) => {
                renderNetwork(nodes, edges);
            }).catch(console.error);
        }

        function loadGraph(key) {
            updateUI(key);
            let filesToLoad = viewDependencies[key] || [allGraphFiles[key]];
            let isMaster = (key === 'master');
            loadFiles(filesToLoad, isMaster).then(({ nodes, edges }) => {
                renderNetwork(nodes, edges);
            }).catch(console.error);
        }

        function updateUI(key) {
            document.querySelectorAll('button').forEach(b => b.classList.remove('active'));
            const btn = document.getElementById(`btn-${key}`);
            if (btn) btn.classList.add('active');
            document.getElementById('stat-name').textContent = key;
        }

        function renderNetwork(nodes, edges) {
            document.getElementById('stat-nodes').textContent = nodes.length;
            document.getElementById('stat-links').textContent = edges.length;

            const data = { nodes: new vis.DataSet(nodes), edges: new vis.DataSet(edges) };
            const options = {
                physics: { barnesHut: { gravitationalConstant: -8000, springLength: 200 } },
                nodes: { font: { size: 14 } },
                edges: { arrows: 'to', smooth: { type: 'cubicBezier' } }
            };

            if (network) network.destroy();
            network = new vis.Network(container, data, options);
        }

        // Load master graph on start
        loadGraph('master');
    </script>
</body>
</html>
```

Execute: `write` tool to create file.

Report:

```
✅ Created visualization.html (~500 lines) with:
- Unified Brain view
- Role-specific views
- Composite loading
- Cross-graph link visualization
- Color-coded node types
```

#### Action 4.5.2: Create Visualization Instructions

Create `agents/knowledge-graphs/VIEW_VISUALIZATION.md`:

```markdown
# Knowledge Graph Visualization Guide

## Quick Start

1. Open `visualization.html` in a web browser
2. The Master Graph loads by default
3. Use sidebar buttons to explore different views

## Views

### 🧠 Unified Brain (ALL)
Shows ALL graphs merged together. Use this to:
- Verify full system connectivity
- See cross-graph relationships
- Validate that no nodes are orphaned

### 🌐 Master Graph
High-level entry point showing roles and graph structure.

### Role-Specific Views

#### [Role 1 Name] Views
- **🏗️ Knowledge**: What [Role 1] knows about the system
- **🛠️ Skills**: What [Role 1] can do (includes related behaviors)
- **🛡️ Behaviors**: Protocols [Role 1] follows (includes related skills)

#### [Role 2 Name] Views
- **📋 Knowledge**: What [Role 2] knows
- **⚡ Skills**: What [Role 2] can do
- **🤝 Behaviors**: Protocols [Role 2] follows

## Node Colors

- 🟣 **Violet**: Root nodes, system entry points
- 🔵 **Blue**: [Role 1]-related nodes
- 🟢 **Green**: [Role 2]-related nodes
- 🟡 **Yellow**: Behavior nodes (hexagons)
- 🟣 **Pink**: Skill nodes (triangles)
- 🟠 **Orange**: Concept nodes (stars)
- ⚫ **Slate**: Document/file nodes (ellipses)

## Edge Types

- **Solid lines**: Parent-child hierarchical relationships
- **Dashed amber lines**: Cross-graph semantic links (labeled with relationship type)

## Validation Checklist

Use this tool to verify:
- [ ] All nodes are connected to the graph (no floating nodes)
- [ ] Each behavior/skill graph has a root node
- [ ] Cross-graph links are visible (e.g., behavior → skill)
- [ ] Document nodes are properly nested under folders
- [ ] Statistics show reasonable counts (not 0 or unexpectedly low)

## Troubleshooting

**Problem**: Graph shows disconnected nodes
- **Cause**: Missing `parent` field in JSON
- **Fix**: Add `"parent": "[parent-id]"` to disconnected nodes

**Problem**: No cross-graph links visible
- **Cause**: Missing `links` field or target node not in view
- **Fix**: Use "Unified Brain" view to see all links, or add composite views

**Problem**: Graph is too cluttered
- **Cause**: Too many deep nodes in one view
- **Fix**: Use role-specific views instead of Unified Brain

## Next Steps

After validating connectivity:
1. Note any disconnected nodes
2. Fix JSON files
3. Refresh visualization
4. Re-validate

```

Execute: `write` tool.

Report:

```
✅ Created VIEW_VISUALIZATION.md (usage guide)
```

### Validation Checkpoint

```
✅ Visualization tool complete:
- visualization.html (interactive graph explorer)
- VIEW_VISUALIZATION.md (usage guide)

Ready to validate graphs visually.

Proceed to behavior/skill file creation?
```

---

## V2.0 Critical Reminders

### Before Declaring "Setup Complete"

Verify these V2.0-specific items:

- [ ] Every graph (except master) has a root node
- [ ] Every node (except roots) has a `parent` field
- [ ] Cross-graph `links` established (behaviors ↔ skills)
- [ ] visualization.html created and tested
- [ ] Unified Brain view shows fully connected graph
- [ ] USER_MANUAL.md cold-start tested (< 5 min)
- [ ] Skills classified by implementation type
- [ ] KG maintenance skill system created (4 files)
- [ ] Validation scripts include connectivity checks
- [ ] All orphaned nodes fixed

### V2.0 Success Criteria

The system is ready when:

1. **Fully Connected**: visualization.html Unified Brain view shows no floating nodes
2. **Navigable**: Any node reachable from root via parent links
3. **Cross-Linked**: Behaviors/skills/knowledge show semantic relationships
4. **Self-Aware**: Agent can find any file via KG navigation
5. **Self-Evolving**: KG maintenance skill can update graphs automatically
6. **Cold-Startable**: Fresh agent operational in < 5 minutes with just USER_MANUAL.md

---

## Appendix: V2.0 vs V1.0 Comparison

| Feature | V1.0 | V2.0 |
|---------|------|------|
| **Graph Connectivity** | Optional parent links | Mandatory parent links |
| **Root Nodes** | Not required | Required per graph |
| **Cross-Graph Links** | Not specified | Explicit `links` field |
| **Visualization** | Not included | Interactive HTML tool |
| **User Manual** | Basic | Comprehensive + tested |
| **Skills Analysis** | Not included | Rule/LLM/hybrid classification |
| **Self-Evolution** | Not included | KG maintenance skill |
| **Cold-Start Time** | Unknown | < 5 minutes (validated) |
| **Validation** | Basic structure | Connectivity + orphan detection |
| **Behavior Loading** | agents/behaviors/ | .cursor/behaviors/ (native) |

---

**END OF AI AGENT SETUP PROTOCOL V2.0**

**Remember**: This protocol is battle-tested. Follow it sequentially. The V2.0 enhancements ensure your agent has a fully-connected "Mind GPS" and can evolve itself.
