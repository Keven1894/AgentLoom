# Phase 5 Output Specification

## Purpose

The `output/phase-05.md` file documents knowledge content generation results and development plan.

---

## Required Sections

### 1. Header

```markdown
# Phase 5: Knowledge Content

**Created**: [timestamp]
**Project**: [PROJECT_NAME]
**Domain Role**: [DOMAIN_ROLE_ID]
```

### 2. Auto-Generated Content

```markdown
## Auto-Generated Content (Category A)

Successfully generated: [X] knowledge nodes

- [node-id]: [file-path] ✅
- [node-id]: [file-path] ✅
...
```

### 3. Development Plan

```markdown
## Development Plan (Category B & C)

Requires human development: [Y] knowledge nodes

### Complex (Synthesis Needed) - [count]

#### [node-id]: [file-path]
**Why complex**: [specific reason]
**Source documents**: [list from user-shared content]
**Suggested approach**: [steps to complete]
**Estimated effort**: [X hours]
**Priority**: [Critical | High | Medium]

### Very Complex (Research Needed) - [count]

#### [node-id]: [file-path]
**Why complex**: [specific reason]
**Research needed**: [what to investigate]
**Suggested approach**: [steps to complete]
**Estimated effort**: [X hours]
**Priority**: [Critical | High | Medium]
```

### 4. Summary

```markdown
## Summary

Total knowledge nodes: [Z]
- Auto-generated (Category A): [X] ([percentage]%) ✅
- Requires development (Category B & C): [Y] ([percentage]%) ⚠️

Priority breakdown:
- Critical: [count]
- High: [count]
- Medium: [count]

Total estimated effort: [hours/days]
```

---

## Length

**Target**: 40-80 lines (depends on number of complex tasks)

---

## Validation Criteria

- [ ] All nodes accounted for
- [ ] Categories clear (A/B/C)
- [ ] Complex tasks well-documented
- [ ] Priorities assigned
- [ ] Effort estimates provided
- [ ] Accurate counts and percentages
