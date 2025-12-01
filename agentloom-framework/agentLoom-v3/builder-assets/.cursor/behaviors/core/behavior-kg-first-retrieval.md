# Behavior: KG-First Information Retrieval

**ID**: `behavior:kg-first-retrieval`  
**Category**: Core  
**Priority**: high  
**Created**: 2025-11-30  
**Applies To**: All roles

---

## Purpose

**CRITICAL BEHAVIOR** to prevent information loss and "lost in the middle" problems. Enforces KG-based information retrieval instead of manual JSON parsing or text search.

---

## The Problem

### Information Loss in Agentic AI

**Common Failures**:

1. ❌ LLM tries to manually parse JSON → syntax errors
2. ❌ LLM searches large files → loses context ("lost in middle")
3. ❌ LLM guesses node IDs → broken references
4. ❌ LLM forgets relationships → incomplete information

**Result**: Unreliable agents, hallucinations, broken workflows

---

## The Solution: KG-First Retrieval

### Core Principle

> **ALWAYS use KG navigator for information retrieval**
> **NEVER manually parse JSON or guess node IDs**

### Why This Works

✅ **Structured Access**: Programmatic KG traversal
✅ **No Context Loss**: Tools handle complexity
✅ **Verifiable Results**: Actual node data, not guesses
✅ **Relationship Preservation**: Follow links programmatically

---

## Rules

### Rule 1: Use KG Navigator for Node Lookup

**WRONG** ❌:

```
"Let me open builder-skills-graph.json and search for the skill..."
"I'll parse the JSON to find the node..."
```

**RIGHT** ✅:

```bash
python scripts/json-helper/kg_navigator.py \
  agents/knowledge-graphs/builder-skills-graph.json \
  get skill-validate-kg-links
```

### Rule 2: Use Navigator for Relationship Traversal

**WRONG** ❌:

```
"Looking at the JSON, I see this skill uses these scripts..."
"Let me manually check what this node references..."
```

**RIGHT** ✅:

```bash
python scripts/json-helper/kg_navigator.py \
  agents/knowledge-graphs/builder-skills-graph.json \
  deps skill-validate-kg-links
```

### Rule 3: Use Navigator for Discovery

**WRONG** ❌:

```
"Let me grep for all skills in the file..."
"I'll search the JSON for pattern documentation..."
```

**RIGHT** ✅:

```bash
# Find by type
python scripts/json-helper/kg_navigator.py \
  agents/knowledge-graphs/builder-skills-graph.json \
  find --type skill

# Find by path
python scripts/json-helper/kg_navigator.py \
  agents/knowledge-graphs/builder-knowledge-graph.json \
  find --path "docs/builder/patterns"
```

### Rule 4: Use Navigator for Impact Analysis

**WRONG** ❌:

```
"Let me manually trace what depends on this behavior..."
```

**RIGHT** ✅:

```bash
python scripts/json-helper/kg_navigator.py \
  agents/knowledge-graphs/builder-behaviors-graph.json \
  traverse behavior:builder:agentloom-development-life \
  --links governed_by implements \
  --depth 3
```

---

## Workflow

### Step 1: Identify Information Need

**Questions to ask**:

- Do I need to find a node in a KG?
- Do I need to traverse relationships?
- Do I need to discover dependencies?
- Do I need to search by type or path?

**If YES to any** → Use KG navigator

### Step 2: Choose Navigator Command

| Need | Command |
|------|---------|
| Get specific node | `get <node-id>` |
| Find by type | `find --type <type>` |
| Find by path | `find --path <pattern>` |
| Get dependencies | `deps <node-id>` |
| Traverse relationships | `traverse <node-id> --links <types>` |

### Step 3: Execute and Process Results

- Run navigator command
- Process structured output
- Use results in workflow
- **Never guess or manually parse**

---

## Examples

### Example 1: Finding Pattern Documentation

**Task**: Find all pattern documentation in Builder KG

**WRONG** ❌:

```
"Let me open builder-knowledge-graph.json and look for patterns..."
```

**RIGHT** ✅:

```bash
python scripts/json-helper/kg_navigator.py \
  agents/knowledge-graphs/builder-knowledge-graph.json \
  find --path "docs/builder/patterns"
```

### Example 2: Discovering Skill Dependencies

**Task**: Find what scripts a skill uses

**WRONG** ❌:

```
"Looking at the skill node in JSON, I see it uses these scripts..."
```

**RIGHT** ✅:

```bash
python scripts/json-helper/kg_navigator.py \
  agents/knowledge-graphs/builder-skills-graph.json \
  deps skill-extract-universal-patterns
```

### Example 3: Traversing Behavior Relationships

**Task**: Find all skills governed by a behavior

**WRONG** ❌:

```
"Let me search all skill files for references to this behavior..."
```

**RIGHT** ✅:

```bash
python scripts/json-helper/kg_navigator.py \
  agents/knowledge-graphs/builder-skills-graph.json \
  traverse behavior:builder:agentloom-development-life \
  --links governed_by \
  --depth 2
```

---

## Benefits

### 1. Prevents Information Loss

- No context overflow
- No "lost in middle" problems
- Reliable information retrieval

### 2. Reduces Errors

- No JSON parsing mistakes
- No broken references
- No hallucinated node IDs

### 3. Improves Reliability

- Consistent access patterns
- Verifiable results
- Reproducible workflows

### 4. Enables Complexity

- Multi-hop traversal
- Deep relationship analysis
- Complex queries

---

## Integration

### Enforced By

- `skill-navigate-kg` (implements this behavior)
- `skill-validate-kg-links` (uses navigator)
- `skill-integrate-knowledge` (uses navigator)

### Applies To

- **Builder**: Finding skills, behaviors, patterns
- **Manager**: Traversing project graphs
- **All Roles**: Any KG information retrieval

---

## Exceptions

**When manual JSON access is acceptable**:

1. ✅ Using `json-helper` toolkit (validator, updater, editor)
2. ✅ Creating new KG files
3. ✅ Schema validation

**When manual JSON access is NOT acceptable**:

1. ❌ Finding nodes
2. ❌ Traversing relationships
3. ❌ Discovering dependencies
4. ❌ Searching by type/path

---

## Success Criteria

- ✅ Zero manual JSON parsing for node lookup
- ✅ All relationship traversal uses navigator
- ✅ All discovery queries use navigator
- ✅ No "lost in middle" failures

---

## Related

- **Skill**: `skill-navigate-kg`
- **Tools**: `scripts/json-helper/kg_navigator.py`
- **Behaviors**: `behavior:builder:consistency`, `behavior:core:validation`

---

**CRITICAL REMINDER**: This behavior is ESSENTIAL for reliable agentic AI. Always use KG navigator. Never manually parse JSON for information retrieval.
