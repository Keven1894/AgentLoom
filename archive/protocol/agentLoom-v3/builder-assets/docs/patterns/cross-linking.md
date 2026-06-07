# Pattern: Cross-Linking

**Category**: Patterns  
**Version**: 1.0

---

## Pattern Overview

How to establish meaningful links between behaviors, knowledge, and skills (across the 3 tracks).

---

## Cross-Track Link Types

### Behaviors → Skills
```
behavior:academic-integrity → invoked_by → skill:guide-problem-solving
```

### Skills → Knowledge
```
skill:answer-concepts → uses_knowledge → docs:ta/course-content
```

### Skills → Behaviors
```
skill:guide-problem-solving → uses_behavior → behavior:pedagogical-approach
```

---

## Discovery Process

1. **Explicit References**: Found in documentation
2. **Semantic Analysis**: Use `intelligent-linking` skill
3. **Usage Patterns**: Observe actual invocations
4. **Manual Review**: Developer verification

---

**Status**: Pattern documented (Phase 3)

