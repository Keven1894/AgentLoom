# Skill: Emit Claude Code Format

**ID**: `skill:builder:emit-claude-code`
**Category**: transpiler
**Priority**: medium
**Created**: 2026-05-18

---

## Purpose

Compile the canonical AgentLoom KG into Claude Code's native format — `.claude/skills/` + project-level memory files (`AGENTS.md`, `CLAUDE.md`).

This is the second emitter (after `emit-cline`). Both share the same source-of-truth KG; only the output dialect differs. The framework's claim — *write once, ship to every platform* — depends on at least two emitters being live.

---

## When to use

**Required**:
- After every accepted KG proposal that affects skills, knowledge, or behaviors
- Before publishing the workshop's Claude Code variant of the demo
- In CI: emit on every push to `main`

---

## How to run

```bash
python scripts/transpiler/emit_claude_code.py \
    --output dist/claude-code/ \
    --role {builder|domain|both}
```

Outputs:
- `dist/claude-code/.claude/skills/` — one folder per skill, containing the skill MD + a `SKILL.md` index
- `dist/claude-code/AGENTS.md` — project-level rules (compiled from behaviors)
- `dist/claude-code/CLAUDE.md` — orientation doc (compiled from architecture knowledge nodes)

---

## Output mapping

| KG node | Claude Code artifact |
| --- | --- |
| `behavior` (`hard`/`process`) | line in `AGENTS.md` rules section, with link back to repo's behavior MD |
| `behavior` (`test`) | line in `AGENTS.md` testing section |
| `behavior` (`soft`) | line in `AGENTS.md` style section |
| `skill` | `.claude/skills/<slug>/SKILL.md` matching Claude's per-skill format |
| `knowledge` (architecture) | section in `CLAUDE.md` |
| `knowledge` (procedure) | inlined into the skill that uses it |

Claude Code's per-skill folder format is more structured than Cline's flat `.clinerules/`; this emitter exploits that to preserve the multi-file knowledge → skill → behavior relationships that are flattened in the Cline output.

---

## Implementation status

**Stub** as of Phase 1 Day 2. Phase 6 deliverable, paired with `emit-cline`.

---

## Implements behaviors

- (transpiler skills do not directly enforce rules)

## Uses knowledge

- `knowledge:builder:agentloom-architecture`
- `knowledge:builder:kg-node-schema`

## Companion skills

- `skill:builder:emit-cline`
