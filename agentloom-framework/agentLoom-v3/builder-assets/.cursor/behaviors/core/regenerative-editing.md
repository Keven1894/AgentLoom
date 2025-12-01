---
type: behavior
category: core
id: behavior:core:regenerative-editing
priority: critical
roles:
  - role-builder
  - role-manager
---

# Behavior: Regenerative Editing Protocol

## Description

Enforces the foundational rule for file modification: **Always regenerate entire files instead of performing inline edits**. This leverages LLM generative strengths while avoiding precision-editing weaknesses.

## The Core Rule

When modifying any file, you MUST:

1. Load the entire file into context
2. Understand the requested changes fully
3. **Regenerate the complete file from scratch** with modifications applied
4. Ensure all unrelated parts are preserved exactly
5. Output the new complete file

## Prohibited Actions

**NEVER**:

- ❌ Apply inline patches or diffs
- ❌ Use positional edits (line numbers, character offsets)
- ❌ Modify only specific sections
- ❌ Assume context from previous edits
- ❌ Show only changed lines with ellipsis (...)

## Rationale

### LLM Strengths (Leverage These)

✅ Generate complete, coherent text from scratch
✅ Maintain consistent structure and style
✅ Understand and preserve context holistically

### LLM Weaknesses (Avoid These)

❌ Precise positional edits (line 47, column 23)
❌ Maintaining attention across long documents
❌ Applying patches without context drift

## Workflow

### For Every File Modification

1. **Load**: Read complete file into context
2. **Analyze**: Understand structure, dependencies, and requested change
3. **Regenerate**: Create entire file from scratch with changes
4. **Validate**: Ensure completeness and correctness
5. **Output**: Provide full file to user

## Synergy with Chunking

**Combined Power**:

- Chunking keeps files small (250-500 lines)
- Small files regenerate quickly and reliably
- Result: Optimal reliability + performance

**Example**:

```
Instead of: giant-file.py (2000 lines) → Hard to regenerate
Use:        component-a.py (300 lines) → Easy to regenerate ✅
```

## Validation Checklist

Before outputting, verify:

- [ ] Entire file regenerated (no truncation)
- [ ] All imports preserved
- [ ] All functions/classes preserved
- [ ] Requested changes applied correctly
- [ ] Formatting matches original style
- [ ] Full file provided to user

## Exceptions

Only perform inline edits when user **explicitly** instructs:

- "Apply this diff patch exactly as shown"
- "Do not regenerate the whole file"
- "Only show me the changed lines"

**Even then**: Warn about potential reliability issues.

## Edge Cases

### Very Large Files (>500 lines)

**Solution**: Should be chunked first (see `behavior:builder:document-chunking`)

### Binary Files

**Solution**: This protocol applies only to text files

### Generated Code

**Solution**: Modify the generator/template, not the output
