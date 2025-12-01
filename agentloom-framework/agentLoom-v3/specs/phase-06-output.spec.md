# Phase 6 Output Specification

## Purpose

The `output/phase-06.md` file documents skills implementation results.

---

## Required Sections

### 1. Header

```markdown
# Phase 6: Skills Implementation

**Created**: [timestamp]
**Project**: [PROJECT_NAME]
**Domain Role**: [DOMAIN_ROLE_ID]
```

### 2. Skills Implemented

```markdown
## Skills Implemented

All [X] domain skills documented with complete descriptions:

### Rule-Based Skills ([count])
- [skill-id]: [file-path] ✅ (references [script-name].py - placeholder)
- [skill-id]: [file-path] ✅ (references [script-name].py - placeholder)

### LLM-Based Skills ([count])
- [skill-id]: [file-path] ✅ (prompt-based, complete)
- [skill-id]: [file-path] ✅ (prompt-based, complete)

### Hybrid Skills ([count])
- [skill-id]: [file-path] ✅ (references [script-name].py - placeholder)
- [skill-id]: [file-path] ✅ (references [script-name].py - placeholder)
```

### 3. Scripts Needed

```markdown
## Scripts Requiring Development

The following [Y] Python/Shell scripts are referenced but need implementation:

- `scripts/[script-name].py` - Used by: [skill-id-1], [skill-id-2]
  - Purpose: [what it does]
  
- `scripts/[script-name].py` - Used by: [skill-id-3]
  - Purpose: [what it does]

**Note**: All scripts are placeholders. Human developer must implement.
```

### 4. Summary

```markdown
## Summary

Total skills: [X]
- LLM-based (complete): [count] ✅
- Rule-based (need scripts): [count] ⚠️
- Hybrid (need scripts): [count] ⚠️

Scripts to develop: [Y]

Completion:
- Skill descriptions: 100% ✅
- Script implementation: 0% (human developer needed)
```

---

## Length

**Target**: 30-40 lines

---

## Validation Criteria

- [ ] All skills listed
- [ ] Scripts identified
- [ ] Counts accurate
- [ ] Clear what needs development
