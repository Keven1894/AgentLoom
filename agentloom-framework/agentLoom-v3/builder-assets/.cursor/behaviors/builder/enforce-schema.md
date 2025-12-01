---
type: behavior
category: builder
id: behavior:builder:schema
priority: high
roles:
  - role-builder
---

# Enforce Schema Integrity

## Description
Ensures all files and data structures match their defined templates.

## Rules
1. **Templates**: Use `docs/CONTENT_TEMPLATE.md` for new markdown files.
2. **JSON**: Ensure `project-registry.json` and Graph files are valid JSON.
3. **Frontmatter**: All docs must have YAML frontmatter defining type/category.
