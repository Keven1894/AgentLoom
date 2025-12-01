---
type: behavior
category: core
id: behavior:core:structure
priority: high
roles:
  - all
---

# Project Structure Protocol

## Description
Defines the strict folder organization for the workspace.

## Rules
1. **Public (`public/`)**: Open-source, shareable code.
2. **Personal (`personal/`)**: Private research and experiments.
3. **Work (`work/`)**: Professional, confidential projects.
4. **System (`agents/`, `.cursor/`)**: The agent's own logic and configuration.
5. **Docs (`docs/`)**: Shared documentation and indices.

## Constraints
- Do not create projects in the root directory.
- Do not cross-contaminate contents (e.g., work code in public folder).

