# Phase 4 Output Specification

## Purpose

The `output/phase-04.md` file documents the Knowledge Graphs generated.

---

## Required Sections

### 1. Header

```markdown
# Phase 4: Knowledge Graphs

**Created**: [timestamp]
**Project**: [PROJECT_NAME]
```

### 2. Generated Graphs

```markdown
## Generated Graphs (7 files)

### Builder Graphs (3 files, standard)
- builder-knowledge-graph.json ([X] nodes)
- builder-skills-graph.json ([Y] nodes)
- builder-behaviors-graph.json ([Z] nodes)

### Domain Graphs (3 files, custom)
- [DOMAIN_ROLE_ID]-knowledge-graph.json ([X] nodes)
- [DOMAIN_ROLE_ID]-skills-graph.json ([Y] nodes)
- [DOMAIN_ROLE_ID]-behaviors-graph.json ([Z] nodes)

### Master Graph (1 file)
- master-graph.json (references all 6 graphs, defines 2 roles)
```

### 3. Validation Results

```markdown
## Validation

Structure: ✅ All JSON valid
Connectivity: ✅ All graphs fully connected
Placeholders: ✅ None found
Encoding: ✅ No issues

Total nodes: [count across all graphs]
```

### 4. Status

```markdown
## Status

✅ All 7 graphs generated
✅ Validation passed
✅ Ready for Phase 5 (Content Generation)
```

---

## Length

**Target**: 20-30 lines (concise inventory)

---

## Validation Criteria

- [ ] All 7 files listed
- [ ] Node counts accurate
- [ ] Validation results clear
- [ ] No placeholder text remains
