# Phase 8 Output Specification

## Purpose

The `output/phase-08.md` file documents user manual generation results.

---

## Required Sections

### 1. Header

```markdown
# Phase 8: User Manual Generation

**Created**: [timestamp]
**Project**: [PROJECT_NAME]
```

### 2. Generated Files

```markdown
## Generated Files

- `agents/USER_MANUAL.md` ✅
- `agents/knowledge-graphs/VIEW_VISUALIZATION.md` ✅ (if applicable)
```

### 3. Manual Contents

```markdown
## Manual Contents

### Sections Included
- Magic Activation Prompts
- Quick Start Guide
- Role Descriptions (Builder + Domain)
- Knowledge Graph Visualization
- Skills Reference
- Behaviors Reference
- Workflows
- Troubleshooting

### Customizations
- Project name: [PROJECT_NAME]
- Domain role: [DOMAIN_ROLE_NAME]
- [X] skills documented
- [Y] behaviors documented
```

### 4. Summary

```markdown
## Summary

User manual complete and ready for use.

**Next steps**:
1. Review manual for accuracy
2. Test magic activation prompts
3. Share with users
4. Gather feedback for refinement
```

---

## Length

**Target**: 20-30 lines

---

## Validation Criteria

- [ ] USER_MANUAL.md exists
- [ ] All sections present
- [ ] Project-specific content (not generic)
- [ ] Activation prompts included
- [ ] Visualization instructions included
