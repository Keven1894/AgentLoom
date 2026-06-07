# Skill: Emit Cline Format

**ID**: `skill:builder:emit-cline`
**Category**: transpiler
**Priority**: medium
**Created**: 2026-05-18

---

## Purpose

Compile the canonical AgentLoom KG (skills + knowledge + behaviors) into the platform-native format consumed by **Cline** (`.clinerules/` + workspace settings).

This is one half of the "AgentLoom as transpiler" pivot — KG is the source of truth, platform-native files are build artifacts. Authoring once and emitting many times is the framework's value-multiplier story.

---

## When to use

**Required**:
- After every accepted KG proposal that affects skills, knowledge, or behaviors
- Before each workshop attendee opens VSCode + Cline (so they get the latest distilled rules)
- In CI: emit on every push to `main`, commit artifacts to a `dist/cline/` branch

**Recommended**:
- Locally during development — re-emit after each KG edit so VSCode picks up changes immediately

---

## How to run

```bash
python scripts/transpiler/emit_cline.py \
    --output dist/cline/ \
    --role {builder|domain|both}
```

Outputs:
- `dist/cline/.clinerules/` — one MD per behavior + per high-priority skill
- `dist/cline/cline-settings.json` — model preferences, token budgets, MCP wiring
- `dist/cline/MANIFEST.md` — diff against previous emit (proposed for Phase 6)

---

## Output mapping

| KG node type | Cline artifact |
| --- | --- |
| `behavior` (any tier) | `.clinerules/<slug>.md` (the rule statement + rationale; validator is referenced but cannot run inside Cline — Cline rules are advisory, the canonical enforcement is in CI) |
| `skill` (with `script`) | listed in `cline-settings.json` as a tool entry; markdown body is preview only |
| `knowledge` | not emitted directly; instead, references appear inside behavior/skill MDs |

The transpiler **does not** preserve KG IDs in the output (Cline doesn't understand them); it preserves human-readable names + paths.

---

## Implementation status

**Stub** as of Phase 1 Day 2. Phase 6 deliverable. The MD here documents the contract so Phase 2–5 KG growth happens with this consumer in mind.

---

## Implements behaviors

- (transpiler skills do not directly enforce rules — they propagate them to platforms)

## Uses knowledge

- `knowledge:builder:agentloom-architecture` (3-track structure being compiled)
- `knowledge:builder:kg-node-schema` (input shape)

## Companion skills

- `skill:builder:emit-claude-code` — analogous emitter for Claude Code
- (future) `skill:builder:emit-cursor`, `skill:builder:emit-windsurf`
