# Phase 7: KG Maintenance Skill Setup

**AI Agent Setup Protocol V2.0**

---

## 📌 Phase Context

**Prerequisites**: Phases 1-6 complete  
**Input needed from previous phases**:
- Agent Builder skills graph (Phase 4) for node IDs
- Behavior IDs (Phase 2, 4) for cross-links

**Output**: 4 Agent Builder skill definition files  
**Estimated time**: 30-45 minutes (15-20 with express mode)

**Creates for next phases**:
- KG maintenance skill definitions → Phase 8 (implementation)
- Self-evolution capability → Ongoing system maintenance

---

## Objective

Create the foundational "Maintain Knowledge Graph" skill system to enable agent self-evolution through user-triggered updates.

---

## ⚡ Express Mode (For Experienced Builders)

**If you understand KG maintenance patterns and skill orchestration**:

1. ✅ Create 4 skill files in `agents/skills/system/`:
   - `maintain-kg.md` (orchestrator, hybrid)
   - `kg-monitor.md` (sub-skill, rule-based)
   - `kg-update.md` (sub-skill, hybrid)
   - `kg-heal.md` (sub-skill, rule-based)
2. ✅ Follow SKILL_TEMPLATE_GUIDE for structure
3. ✅ Reference Phase 4.4a for Agent Builder skills graph (node IDs, relationships)
4. ✅ Ensure sub-skills reference parent skill
5. ✅ Skip to validation checkpoint

**Time saved**: ~20-30 minutes

**If this is your first time**: Follow all steps below to see complete examples.

---

## Why This Matters

Without KG maintenance capability:

- Agent cannot adapt to new files/changes
- Manual KG updates required (error-prone)
- System becomes stale as project evolves

**This phase creates the foundation**. Advanced options (scheduled monitoring, autonomous learning) are available in the [Advanced Evolution Guide](../guides/ADVANCED_EVOLUTION_GUIDE.md) for users who complete the full protocol first.

---

## Action 7.1: Create Orchestrator Skill Definition

Create `agents/skills/system/maintain-kg.md`:

```markdown
---
type: skill
category: system
id: maintain-kg
implementation: hybrid
roles:
  - agent-builder
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
4. **Heal** (Rule-based): Validate connectivity and fix issues

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
- After major project changes

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

## Tracked Directories

This skill monitors:
- `.cursor/behaviors/` → Updates `[role]-behaviors-graph.json`
- `agents/skills/` → Updates `[role]-skills-graph.json`
- `docs/[role]/` → Updates `[role]-knowledge-graph.json`
- `[domain-content-dirs]/` → Updates domain graphs (if applicable)

## Related

### Implements Behaviors
- `behavior:agent-builder:kg-consistency` - Graph must reflect reality
- `behavior:agent-builder:self-evolution` - Agent maintains its own knowledge

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

**Create** `agents/skills/system/maintain-kg.md` with the content above.

**Confirm to human**:
```
✅ Created agents/skills/system/maintain-kg.md
```

---

## Action 7.2: Create Sub-Skill: Monitor

Create `agents/skills/system/kg-monitor.md`:

```markdown
---
type: skill
category: system
id: kg-monitor
implementation: rule-based
parent-skill: maintain-kg
roles:
  - agent-builder
indexed-in-kg: skill-kg-monitor
---

# Monitor File System

## Description
Detects changes in tracked directories by comparing file system state to Knowledge Graph state.

## Implementation Type: Rule-Based

**Tool**: Python script
**Location**: `scripts/kg_monitor.py` (to be created in Phase 9)
**Cost**: $0 (deterministic rules)

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
**Version**: 1.0

```

**Create** `agents/skills/system/kg-monitor.md` with the content above.

**Confirm to human**:
```
✅ Created agents/skills/system/kg-monitor.md
```

---

## Action 7.3: Create Sub-Skill: Update Node

Create `agents/skills/system/kg-update-node.md`:

```markdown
---
type: skill
category: system
id: kg-update-node
implementation: hybrid
parent-skill: maintain-kg
roles:
  - agent-builder
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

**Cost Optimization**: ~$0.50-2/update vs $5-10 if fully LLM-based

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
**Version**: 1.0

```

**Create** `agents/skills/system/kg-update-node.md` with the content above.

**Confirm to human**:
```
✅ Created agents/skills/system/kg-update-node.md
```

---

## Action 7.4: Create Sub-Skill: Heal

Create `agents/skills/system/kg-heal.md`:

```markdown
---
type: skill
category: system
id: kg-heal
implementation: rule-based
parent-skill: maintain-kg
roles:
  - agent-builder
indexed-in-kg: skill-kg-heal
---

# Heal Graph Links

## Description
Detects and fixes orphaned nodes, broken parent links, and connectivity issues in Knowledge Graphs.

## Implementation Type: Rule-Based

**Tool**: Python script
**Location**: `scripts/kg_heal.py` (to be created in Phase 9)
**Cost**: $0 (deterministic validation)

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
**Version**: 1.0

```

**Create** `agents/skills/system/kg-heal.md` with the content above.

**Confirm to human**:
```
✅ Created agents/skills/system/kg-heal.md
```

---

## Optional: Advanced Evolution Options

**For users who have completed Phases 1-11 and want to explore advanced self-evolution capabilities:**

The foundation skills created in this phase support **user-triggered** KG updates. For production agents that need to evolve autonomously, see:

**[Advanced Evolution Guide](../guides/ADVANCED_EVOLUTION_GUIDE.md)**

This guide covers:

- **Tier 2: Scheduled Monitoring** - Periodic automatic KG checks with approval gates
- **Tier 3: Autonomous Self-Learning** - Content watcher with LLM extraction pipeline

**Recommendation**: Complete the full protocol (Phases 1-11) and validate your agent works reliably with manual KG updates before exploring autonomous evolution.

---

## Validation Checkpoint

**Created KG Maintenance skill tree:**

- skill-maintain-kg (orchestrator, hybrid)
- skill-kg-monitor (sub-skill, rule-based)
- skill-kg-update-node (sub-skill, hybrid)
- skill-kg-heal (sub-skill, rule-based)

**Status**: Agent self-evolution capability defined (user-triggered).

**Optional**: Advanced evolution options available in guides/

**Next**: Proceed to Phase 8?

---

**Previous Phase**: [Phase 6: Create Validation Tools](PHASE_06_VALIDATION_TOOLS.md)  
**Next Phase**: [Phase 8: Skills Implementation](PHASE_08_SKILLS_IMPLEMENTATION.md)
