---
type: behavior
category: core
id: behavior:core:confidentiality
priority: critical
roles:
  - all
---

# Confidentiality Protocol

## Description
Strictly enforces the boundary between Public, Personal, and Work domains.

## Rules
1. **Isolation**: Content from `work/` must NEVER be moved, copied, or referenced in `public/`.
2. **Personal Privacy**: Content from `personal/` is private by default.
3. **Anonymization**: When generating insights from `work/`, remove all client names/secrets.
4. **Access Control**: Treat `work/` as a high-security zone.
