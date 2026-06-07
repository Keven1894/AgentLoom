# Phase 5: Build Track 3 (Skills)

**Parent**: [AgentLoom Development Lifecycle](./INDEX.md)

---

## Goal

Implement the executable capabilities (Skills) that allow the agent to interact with the world.

---

## 5.1 Define Skill Categories

Group skills logically in `agents/skills/`:

- `system/`: Infrastructure skills (e.g., file operations, KG navigation).
- `domain/`: Subject-specific skills (e.g., data analysis, code generation).
- `meta/`: Self-management skills (e.g., planning, reflection).

## 5.2 Implement Skills

For each skill:

1. **Create Directory**: `agents/skills/<category>/`
2. **Specification**: Write `<skill-name>.md` defining inputs, outputs, and usage.
3. **Implementation**: Write the code (Python scripts, etc.) if needed.
4. **Testing**: Verify the skill works in isolation.

## 5.3 Organize Skills

- Update `agents/skills/INDEX.md`.
- Ensure skills link to the Behaviors that govern them (`governed_by`).
- Ensure skills link to the Knowledge they use (`references`).

---

**Output**: A library of executable skills in `agents/skills/` ready for use.
