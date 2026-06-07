---
type: behavior
category: core
id: behavior:core:safety
priority: critical
roles:
  - all
---

# System Safety Protocol

## Description
The highest priority rule preventing data loss and system corruption.

## Rules
1. **Never Delete Without Confirmation**: Do not delete files in `public/`, `personal/`, or `work/` without explicit user approval.
2. **Backup Before Change**: Ensure critical data is safe before restructuring.
3. **Validate Before Commit**: Run validation scripts before finalizing system-level changes.
