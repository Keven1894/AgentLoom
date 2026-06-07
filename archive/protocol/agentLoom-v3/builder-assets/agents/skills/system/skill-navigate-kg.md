# Skill: Navigate Knowledge Graph

**ID**: `skill-navigate-kg`  
**Category**: System  
**Priority**: CRITICAL  
**Created**: 2025-11-30  
**Role**: Builder

---

## Purpose

**CRITICAL INFRASTRUCTURE** for preventing information loss and "lost in the middle" problems in agentic AI systems. Provides reliable KG traversal capabilities to find information without manual JSON parsing.

---

## Problem Statement

### The "Lost in Middle" Problem

LLMs struggle with:

- ❌ Manual JSON parsing (error-prone)
- ❌ Finding information in large KG files
- ❌ Traversing complex relationships
- ❌ Maintaining context across deep structures

### The Solution

✅ **Structured KG navigation** using `kg_navigator.py`
✅ **Programmatic traversal** instead of manual parsing
✅ **Relationship-based search** (find dependencies, linked nodes)
✅ **Type-based filtering** (find all skills, behaviors, docs)

---

## When to Use

**ALWAYS use when**:

- Finding nodes in KG files
- Traversing relationships (uses, references, governed_by)
- Discovering dependencies
- Searching by type or path pattern

**NEVER**:

- Manually parse JSON to find nodes
- Search KG files with grep/text search
- Try to remember node IDs

---

## Usage

### 1. Find Node by ID

```bash
python scripts/json-helper/kg_navigator.py \
  agents/knowledge-graphs/builder-skills-graph.json \
  get skill-validate-kg-links
```

**Output**: Full node details with links

### 2. Find Nodes by Type

```bash
python scripts/json-helper/kg_navigator.py \
  agents/knowledge-graphs/builder-skills-graph.json \
  find --type skill
```

**Output**: List of all skill nodes

### 3. Find Nodes by Path Pattern

```bash
python scripts/json-helper/kg_navigator.py \
  agents/knowledge-graphs/builder-knowledge-graph.json \
  find --path "docs/builder/patterns"
```

**Output**: All nodes matching path pattern

### 4. Get Dependencies

```bash
python scripts/json-helper/kg_navigator.py \
  agents/knowledge-graphs/builder-skills-graph.json \
  deps skill-validate-kg-links
```

**Output**: Categorized dependencies (skills, behaviors, documents, scripts)

### 5. Traverse Relationships

```bash
python scripts/json-helper/kg_navigator.py \
  agents/knowledge-graphs/builder-skills-graph.json \
  traverse skill-extract-universal-patterns \
  --links uses references \
  --depth 3
```

**Output**: All nodes reachable via specified link types

---

## Python API

```python
from scripts.json_helper.kg_navigator import KGNavigator

# Load KG
nav = KGNavigator('agents/knowledge-graphs/builder-skills-graph.json')
nav.load()

# Get node
node = nav.get_node('skill-validate-kg-links')

# Get links
links = nav.get_links('skill-validate-kg-links', 'uses')

# Get linked nodes
scripts = nav.get_linked_nodes('skill-validate-kg-links', 'uses')

# Find by type
all_skills = nav.find_by_type('skill')

# Find by path
patterns = nav.find_by_path('docs/builder/patterns')

# Get dependencies
deps = nav.get_dependencies('skill-extract-universal-patterns')
# Returns: {'skills': [...], 'behaviors': [...], 'documents': [...], 'scripts': [...]}

# Traverse
found = nav.traverse('skill-root', ['uses', 'references'], max_depth=3)
# Returns: {'skill': {ids...}, 'behavior': {ids...}, 'document': {ids...}}
```

---

## Key Features

### 1. Relationship Traversal

- Follow `uses`, `references`, `governed_by`, `depends_on` links
- Multi-hop traversal with depth control
- Cycle detection (visited tracking)

### 2. Type-Based Search

- Find all nodes of specific type
- Categorize results automatically
- Filter by node properties

### 3. Path Pattern Matching

- Search by file path patterns
- Locate documentation by folder
- Find related files

### 4. Dependency Analysis

- Automatic categorization (skills, behaviors, docs, scripts)
- Complete dependency tree
- Impact analysis

---

## Benefits

### ✅ Prevents Information Loss

- Structured access to KG data
- No manual JSON parsing errors
- Reliable node lookup

### ✅ Solves "Lost in Middle"

- Navigate large KGs programmatically
- Find information without context loss
- Traverse complex relationships

### ✅ Improves Agent Reliability

- Consistent KG access patterns
- Reduced hallucination risk
- Verifiable results

### ✅ Enables Complex Queries

- Multi-hop traversal
- Dependency discovery
- Relationship mapping

---

## Integration

### With Other Skills

**skill-validate-kg-links**: Uses navigator to check cross-references
**skill-integrate-knowledge**: Uses navigator to find related nodes
**skill-extract-universal-patterns**: Uses navigator to traverse source KGs

### With Behaviors

**behavior:kg-first-retrieval**: Always use navigator for KG queries
**behavior:builder:consistency**: Verify relationships using navigator

---

## Tools

- **Primary**: `scripts/json-helper/kg_navigator.py`
- **Related**: `scripts/json-helper/validator.py`, `scripts/json-helper/kg_editor.py`

---

## Links

### Uses

- `scripts/json-helper/kg_navigator.py`

### Governed By

- `behavior:kg-first-retrieval` (use KG navigation, not manual parsing)
- `behavior:builder:consistency`

### Validates

- All KG files (builder-skills-graph.json, builder-knowledge-graph.json, etc.)

---

## Examples

### Example 1: Find All Pattern Documentation

```bash
python scripts/json-helper/kg_navigator.py \
  agents/knowledge-graphs/builder-knowledge-graph.json \
  find --path "docs/builder/patterns"
```

### Example 2: Discover Skill Dependencies

```bash
python scripts/json-helper/kg_navigator.py \
  agents/knowledge-graphs/builder-skills-graph.json \
  deps skill-extract-universal-patterns
```

### Example 3: Traverse From Root

```bash
python scripts/json-helper/kg_navigator.py \
  agents/knowledge-graphs/builder-skills-graph.json \
  traverse skill:builder:root \
  --links uses governed_by \
  --depth 2
```

---

## Success Criteria

- ✅ Can find any node in KG without manual parsing
- ✅ Can traverse relationships programmatically
- ✅ Can discover dependencies automatically
- ✅ Zero JSON parsing errors

---

**Remember**: This skill is CRITICAL infrastructure. Always use KG navigator instead of manual JSON parsing. This prevents information loss and ensures reliable KG access.
