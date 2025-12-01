# Phase 7 Output Specification

## Purpose

The `output/phase-07.md` file documents behaviors generation results.

---

## Required Sections

### 1. Header

```markdown
# Phase 7: Behaviors Generation

**Created**: [timestamp]
**Project**: [PROJECT_NAME]
**Domain Role**: [DOMAIN_ROLE_ID]
```

### 2. Behaviors Generated

```markdown
## Behaviors Generated

All [X] domain behaviors generated:

### Critical Priority ([count])
- [behavior-id]: [file-path] ✅
  - Governs: [skill-id-1], [skill-id-2]
  - Purpose: [brief description]

### High Priority ([count])
- [behavior-id]: [file-path] ✅
  - Governs: [skill-id-1], [skill-id-2]
  - Purpose: [brief description]

### Medium Priority ([count])
- [behavior-id]: [file-path] ✅
  - Governs: [skill-id-1]
  - Purpose: [brief description]
```

### 3. Culture Established

```markdown
## Culture Established

**Communication Style**: [description - e.g., professional, friendly, technical]

**Key Principles**:
1. [Principle 1 - from critical behaviors]
2. [Principle 2 - from critical behaviors]
3. [Principle 3 - from high priority behaviors]

**Governed Skills**: [count] skills have governing behaviors
```

### 4. Summary

```markdown
## Summary

Total behaviors: [X]
- Critical: [count] (safety, ethics, core function)
- High: [count] (quality, user experience)
- Medium: [count] (optimization, preferences)

Skills governed: [Y] out of [Z] total skills

Agent personality: [brief characterization based on behaviors]

**Note**: This is a STARTUP agent - behaviors will refine through real-world use.
```

---

## Length

**Target**: 30-50 lines

---

## Validation Criteria

- [ ] All behaviors listed
- [ ] Priorities clear
- [ ] Skills linkage shown
- [ ] Culture/personality defined
- [ ] Accurate counts
