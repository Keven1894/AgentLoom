# Phase 3 Output Specification

## Purpose

The `output/phase-03.md` file documents what was created during project structure setup.

---

## Required Sections

### 1. Header

```markdown
# Phase 3: Project Structure

**Created**: [timestamp]
**Project**: [PROJECT_NAME]
**Domain Role**: [DOMAIN_ROLE_ID]
```

### 2. Copied from Builder Assets

List what was copied:

```markdown
## Copied from builder-assets

- Behaviors: [count] files (core + builder)
- Skills: [count] files (system)
- Knowledge Graphs: [count] files (builder-*.json)
- Scripts: [count] files
- Template: CONTENT_TEMPLATE.md
```

### 3. Created Folders

List all folders created:

```markdown
## Created Folders

Domain Role:
- .cursor/behaviors/[DOMAIN_ROLE_ID]/
- agents/skills/[DOMAIN_ROLE_ID]/

Knowledge Structure (from Phase 2):
- docs/[DOMAIN_ROLE_ID]/
  - [subfolder-1]/
  - [subfolder-2]/
  ...

Domain-Specific:
- [folder-1]/ (purpose: [why])
- [folder-2]/ (purpose: [why])
```

### 4. Created Placeholders

List placeholder files:

```markdown
## Created Placeholders

Skills ([count] files in agents/skills/[DOMAIN_ROLE_ID]/):
- [skill-name-1].md
- [skill-name-2].md
...

Behaviors ([count] files in .cursor/behaviors/[DOMAIN_ROLE_ID]/):
- [behavior-name-1].md
- [behavior-name-2].md
...
```

### 5. Generated Files

List hybrid files generated:

```markdown
## Generated Files

- .cursor/identity.md (dual roles defined)
- .cursor/rules.md (project rules)
- agents/NEW_AGENT_START_HERE.md (onboarding)
```

### 6. Status

```markdown
## Status

✅ Structure complete
✅ Placeholders ready for Phase 5
✅ Hybrid files generated
✅ Validation: [Pass/Fail]

Ready for Phase 4 (Knowledge Graphs)
```

---

## Length

**Target**: 30-50 lines (detailed inventory, readable format)

---

## Validation Criteria

- [ ] All sections present
- [ ] Accurate counts
- [ ] All created items listed
- [ ] Clear status
- [ ] No placeholder text like `[PROJECT_NAME]` remains
