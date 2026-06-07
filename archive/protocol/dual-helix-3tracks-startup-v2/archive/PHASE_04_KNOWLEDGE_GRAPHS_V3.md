# Phase 4: Create Knowledge Graphs

**AI Agent Setup Protocol V3.0 - Specification-Based Generation**

---

## Prerequisites

Read and keep in memory from previous phases:

- **Phase 1**: `PROJECT_NAME`, `DOMAIN_ROLE_NAME`, `DOMAIN_ROLE_ID`, `DOMAIN_ID`, domain concepts list
- **Phase 2**: Skills list (with implementation types), Behaviors list (with priorities)
- **Phase 3**: Project structure created

---

## Critical Rule: Generate, Don't Copy

**❌ WRONG**: Copy template → Replace placeholders  
**✅ RIGHT**: Read specification → Generate fresh

LLMs excel at generation, fail at find-and-replace.

---

## Instructions

### Step 1: Read the Generation Pattern

Read: `@specs/generation-pattern.md`

Understand:

- Why templates fail
- How to use specifications
- The 4-step process: Gather context → Read spec → Generate fresh → Validate

### Step 2: Confirm Context Variables

Before generating ANY file, confirm you have:

```
PROJECT_NAME      = "_______________"
DOMAIN_ROLE_NAME  = "_______________"
DOMAIN_ROLE_ID    = "_______________"
DOMAIN_ID         = "_______________"
Domain concepts   = [list from Phase 1]
Skills            = [list with types from Phase 2]
Behaviors         = [list with priorities from Phase 2]
```

If any are missing, STOP and ask the human.

### Step 3: Generate Agent Builder Graphs (Standard)

These are **identical** for all projects.

Read: `@specs/agent-builder-graphs-spec.md`

Generate 3 files following the exact specifications:

1. `agents/knowledge-graphs/agent-builder-knowledge-graph.json` (8 nodes)
2. `agents/knowledge-graphs/agent-builder-skills-graph.json` (6 nodes)
3. `agents/knowledge-graphs/agent-builder-behaviors-graph.json` (7 nodes)

**Remember**: Generate fresh from spec. Do NOT copy templates.

### Step 4: Generate Domain Role Graphs (Custom)

These are **custom** based on Phase 1-2 requirements.

Read: `@specs/domain-role-graphs.spec.md`

Generate 3 files using your context variables:

1. `agents/knowledge-graphs/{DOMAIN_ROLE_ID}-knowledge-graph.json`
2. `agents/knowledge-graphs/{DOMAIN_ROLE_ID}-skills-graph.json`
3. `agents/knowledge-graphs/{DOMAIN_ROLE_ID}-behaviors-graph.json`

Follow the structural patterns in the spec, populate with your Phase 1-2 content.

### Step 5: Generate Master Graph

Read: `@specs/knowledge-graph-schema-spec.md` (Master Graph section)

Generate: `agents/knowledge-graphs/master-graph.json`

This file references all 6-7 graphs and defines the 2 roles.

### Step 6: Validate All Graphs

Run validation:

```bash
python scripts/validate_generation.py agents/knowledge-graphs/
python scripts/validate_graphs.py
```

**Expected output**:

```
validate_generation.py: ✅ All files valid!
validate_graphs.py: ✅ All graphs are fully connected and valid!
```

### Step 7: If Validation Fails

**Analyze the error**:

- "Unreplaced placeholder" → You copied instead of generated. Delete file, regenerate from scratch.
- "Encoding issue" → You copy-pasted. Regenerate fresh.
- "Missing parent" → Add `"parent": "valid-id"` to non-root nodes.
- "Invalid parent reference" → Check spelling, parent must exist.

**Regenerate the problematic file** from its specification.

Repeat validation until all pass.

---

## Good vs Bad Examples

**Bad example** (template copy-paste failure):  
See: `@test-output/bad-master-graph.json`  
Issues: Unreplaced `[Project Name]`, `[domain-role-id]` placeholders

**Good example** (specification-based generation):  
See: `@test-output/good-master-graph.json`  
All variables replaced with actual values, no placeholders

---

## Completion Checklist

- [ ] Context variables confirmed
- [ ] Generation pattern understood
- [ ] Agent Builder graphs generated (3 files, 21 total nodes)
- [ ] Domain Role graphs generated (3 files, custom node count)
- [ ] Master graph generated (1 file)
- [ ] All validation passed (no placeholders, no encoding issues, fully connected)

---

## Output to Human

```
✅ Phase 4 Complete - Knowledge Graph System Generated

Files created: 7 graphs with [X] total nodes
Validation: All passed

Proceed to Phase 5?
```

---

**Next**: [Phase 5: Create Content Templates](PHASE_05_CONTENT_TEMPLATES.md)
