---
type: behavior
category: core
id: behavior:core:git
priority: medium
roles:
  - all
---

# Git Workflow Protocol

## Description
Standards for version control and repository management.

## Rules
1. **Commit Often**: Regular commits with clear messages.
2. **Branching**: Use feature branches for major changes.
3. **Syncing**: Pull before push to avoid conflicts.
4. **Submodules**: Managed projects are separate git repositories; do not nest git roots improperly.

## Commit Message Standard
- `feat`: New capabilities
- `fix`: Bug fixes
- `docs`: Documentation only
- `refactor`: Code restructuring

