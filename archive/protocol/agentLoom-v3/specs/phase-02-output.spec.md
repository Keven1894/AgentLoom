# Phase 2 Output Specification

**Purpose**: Define required structure for `output/phase-02.md`  
**Used by**: Phase 2 (to write output), Phases 3-5 (to read architecture)

---

## Required Structure

```markdown
# Architecture Design

## Domain Role: [DOMAIN_ROLE_NAME] ([DOMAIN_ROLE_ID])

### Content Analysis
[If folders scanned]:
- Folder: [path] - [count] files, organized by [structure]
- Categories found: [list]
- Key concepts: [list]

[If no folders]: Starting fresh

### Knowledge Structure

Root: [DOMAIN_ID]:root

Main categories (hierarchy):
1. [category-1] ([node-id])
   - [subcategory] ([node-id])
   - [subcategory] ([node-id])
2. [category-2] ([node-id])
3. [category-3] ([node-id])

Organization: [Describe: hierarchical by topic? time-based? category-based?]
Depth: [2-level / 3-level / deeper]

[If content shared] Mapping plan:
- [shared-folder-1] → [KG category]
- [shared-folder-2] → [KG category]

### Skills Taxonomy

**Rule-Based Skills**:
1. skill-[name]
   - Purpose: [what it does]
   - Links: [behavior that governs it]

**LLM-Based Skills** (Max tier):
1. skill-[name]
   - Purpose: [what it does]
   - Why max tier: [complex reasoning need]
   - Links: [behavior]

**LLM-Based Skills** (SLM tier):
1. skill-[name]
   - Purpose: [what it does]
   - Why SLM sufficient: [simple task]

**Hybrid Skills**:
1. skill-[name]
   - Purpose: [what it does]
   - Architecture: [rules do X, LLM does Y, rules do Z]
   - Links: [behavior]

**Skill tree** (if any parent-child):
- parent-skill
  - sub-skill-1
  - sub-skill-2

### Behaviors Taxonomy

**Critical Priority**:
1. behavior:[DOMAIN_ROLE_ID]:[name]
   - Purpose: [what it ensures]
   - Governs: [skill or knowledge area]

**High Priority**:
1. behavior:[DOMAIN_ROLE_ID]:[name]
   - Purpose: [what it ensures]
   - Governs: [what it controls]

**Medium Priority**:
1. behavior:[DOMAIN_ROLE_ID]:[name]
   - Purpose: [what it ensures]

### Relationship Map

**Internal connections**:
[Describe key relationships within domain role]

Example:
behavior:[domain]:[name] → enforces → skill-[name] → uses → knowledge:[domain]:[category]

**Cross-links to Agent Builder** (if any):
[Usually minimal - describe if needed]

### Summary

Total designed:
- Knowledge categories: [count]
- Skills: [count] ([X] rule-based, [Y] LLM, [Z] hybrid)
- Behaviors: [count] ([X] critical, [Y] high, [Z] medium)
```

---

## Validation Criteria

**Check that output/phase-02.md has**:

- [ ] All required sections present
- [ ] Domain role clearly identified
- [ ] Knowledge hierarchy described (with node IDs)
- [ ] Skills listed and classified
- [ ] Behaviors listed with priorities
- [ ] Relationships mapped
- [ ] Summary with counts

**Length**: 50-100 lines typical  
**Style**: Natural language, descriptive, domain-specific

---

## Usage in Later Phases

**Phase 3**: Reads architecture to know what directories to create  
**Phase 4**: Reads to generate domain KGs  
**Phase 5**: Reads to create behavior and skill files  

**Critical**: This output drives all domain role implementation

