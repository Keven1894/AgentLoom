# Implementation Guide: Markdown Conventions

**Category**: Implementation  
**Version**: 1.0

---

## Standard Markdown Format

All knowledge base content should follow these conventions for consistency.

---

## File Structure

```markdown
---
title: "Document Title"
date: 2025-11-18
topics: [topic1, topic2]
---

# Document Title

## Overview
Brief introduction

## Main Content
Detailed content with subsections

## Examples
Practical examples

## Related
Links to related content
```

---

## Headings

- `#` H1 - Document title (only one per file)
- `##` H2 - Major sections
- `###` H3 - Subsections
- `####` H4 - Minor subsections (avoid H5, H6)

---

## Lists

**Unordered**:
```markdown
- Item 1
- Item 2
  - Nested item
```

**Ordered**:
```markdown
1. Step 1
2. Step 2
3. Step 3
```

---

## Code Blocks

With language specification:
````markdown
```python
def example():
    return "code"
```
````

---

## Links

**Internal**: `[Text](../path/to/file.md)`  
**External**: `[Text](https://example.com)`

---

## Images

```markdown
![Alt text](./images/diagram.png)
```

Store images in `images/` subdirectory.

---

## Tables

```markdown
| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |
```

---

**Status**: Standard conventions (Phase 3)

