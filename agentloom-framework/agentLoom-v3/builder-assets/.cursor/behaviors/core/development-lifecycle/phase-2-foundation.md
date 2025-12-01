# Phase 2: Foundation Setup

**Parent**: [AgentLoom Development Lifecycle](./INDEX.md)

---

## Goal

Initialize the standard directory structure and core identity files.

---

## 2.1 Create Directory Structure

Establish the standard AgentLoom folder layout:

```bash
project-root/
├── .cursor/              # Track 1: Behaviors
│   ├── identity.md       # Core identity
│   ├── INDEX.md          # Behavior index
│   ├── rules/            # Rule definitions
│   │   ├── core/         # Universal principles
│   │   └── workflows/    # Process definitions
│   └── behaviors/        # (Optional) Advanced behaviors
├── docs/                 # Track 2: Knowledge
│   └── INDEX.md          # Knowledge index
├── agents/               # Track 3: Skills & Infrastructure
│   ├── skills/           # Skill definitions
│   └── knowledge-graphs/ # JSON graphs
└── shared/               # Shared resources
```

## 2.2 Define Identity

Create `.cursor/identity.md` containing:

- **Name & Role**: The agent's persona.
- **Traits**: Personality keywords (e.g., "Helpful", "Strict").
- **Style**: Communication guidelines.
- **Boundaries**: What the agent will NOT do.

## 2.3 Create Master Indexes

Initialize empty index files to serve as entry points:

- `.cursor/INDEX.md`
- `docs/INDEX.md`
- `agents/skills/INDEX.md`

---

**Output**: A clean, structured project ready for content.
