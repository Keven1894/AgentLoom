# Phase 4: Knowledge Graphs

**AI Agent Setup Protocol V3.0**

---

## Objective

Generate 7 fully-connected Knowledge Graph JSON files using specs and examples(the 3 builder graphs should be already ready from phase 3, just check and verify). No node content generation (done in Phase 5).

---

## Step 1: Load Context

Read `output/phase-01.md`, `output/phase-02.md`, and `output/phase-03.md`:

```
PROJECT_NAME = [value]
DOMAIN_ROLE_ID = [value]
DOMAIN_ID = [value]

From Phase 2:
- KG structure (categories, hierarchy)
- Skills list (with types)
- Behaviors list (with priorities)

From Phase 3:
- Placeholder files created
```

---

## Step 2: Generate Domain Graphs (3 files)

**These are custom** - based on Phase 2 architecture.

**Read**:

- `specs/knowledge-graph-schema-spec.md` (JSON structure rules)
- `specs/domain-role-graphs.spec.md` (if exists)
- `builder-assets/examples/master-graph.json` (see pattern)
- `output/phase-02.md` (your architecture design)

**Generate** fresh JSON files:

1. `agents/knowledge-graphs/[DOMAIN_ROLE_ID]-knowledge-graph.json`
   - Root: `[DOMAIN_ID]:root`
   - Categories from Phase 2 KG structure
   - Hierarchy matching `docs/[DOMAIN_ROLE_ID]/` folder structure
   - **Nodes reference placeholder files** (paths to .md files created in Phase 3)
   - **No content in nodes** - just metadata (id, type, title, path, parent)

2. `agents/knowledge-graphs/[DOMAIN_ROLE_ID]-skills-graph.json`
   - Root: `skill:[DOMAIN_ROLE_ID]:root`
   - Skills from Phase 2 design
   - Each skill references placeholder file in `agents/skills/[DOMAIN_ROLE_ID]/`
   - Include implementation type (from Phase 2)
   - Organize into tree (parent skills → child skills)

3. `agents/knowledge-graphs/[DOMAIN_ROLE_ID]-behaviors-graph.json`
   - Root: `behavior:[DOMAIN_ROLE_ID]:root`
   - Behaviors from Phase 2 design
   - Each behavior references placeholder file in `.cursor/behaviors/[DOMAIN_ROLE_ID]/`
   - Include priority (from Phase 2)
   - Use `links` to connect behaviors → skills they govern

---

## Step 3: Generate Master Graph (1 file)

**Read**:

- `builder-assets/examples/master-graph.json` (see pattern)
- `specs/master-graph-structure.spec.md` (requirements)
- `output/phase-01.md` (PROJECT_NAME)

**Generate**: `agents/knowledge-graphs/master-graph.json`

**Must include**:

- `project`: PROJECT_NAME
- `graphs`: Array with 6-7 entries (3 builder + 3 domain + optional project-graph)
- `roles`: Array with 2 entries (role-builder + role-[DOMAIN_ROLE_ID])

**Each graph entry** has:

- `id`: Graph identifier
- `path`: Relative path to JSON file
- `description`: What this graph contains

**Each role entry** has:

- `id`: Role identifier
- `name`: Role display name
- `graphs`: Array of graph IDs this role uses

---

## Step 4: Validate Graphs

**Run validation scripts**:scripts/validate_graphs.py

Check structure and connectivity.

**Expected**: All graphs valid JSON, fully connected, no placeholders, no encoding issues.

---

## Step 5: Write Output Summary

**Create**: `output/phase-04.md`

**Follow structure**: Read `specs/phase-04-output.spec.md`

**Generate summary** with:

- All 7 files listed
- Node counts per graph
- Validation results
- Total nodes across all graphs

**Length target**: 20-30 lines

---

## Step 6: Confirm with Human with the following format

```
✅ Knowledge Graphs generated:

Builder: 3 graphs ([X] nodes)
Domain: 3 graphs ([Y] nodes)
Master: 1 graph (references all)

Total: 7 files, [Z] nodes
Validation: ✅ All passed

See: output/phase-04.md

Proceed to Phase 5 (Content Generation)?
```

Wait for approval.

---

## Completion

```
✅ Phase 4 Complete

Graphs: 7 files generated
Connectivity: Fully connected
Validation: Passed
Node content: Deferred to Phase 5

Next: Phase 5 (Content Generation)
```

---

## Important Notes

**Node content**: Don't generate actual content for knowledge nodes. Just create node structure with:

- `id`, `type`, `title`, `path`, `parent`
- Actual content (what goes IN the .md files) → Phase 5

**Placeholder references**: Nodes should reference the placeholder files created in Phase 3, not generate new files.

**Fully connected**: Every node (except roots) must have a `parent` field pointing to valid parent ID.

---

**Next**: [Phase 5: Content Generation](PHASE_05_CONTENT_GENERATION.md)
