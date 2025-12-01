# Skill: Validate Knowledge Graph Links

**ID**: `skill-validate-kg-links`  
**Category**: System Validation  
**Priority**: High  
**Created**: 2025-11-30

---

## Purpose

Validates cross-references and connectivity across all knowledge graphs to ensure:

- All link references point to existing nodes
- All skills have proper `governed_by` links
- Master graph is complete and accurate
- No broken links or critical orphaned nodes

---

## When to Use

**Required After**:

- ✅ Adding new skills/behaviors to any KG
- ✅ Updating cross-references between KGs
- ✅ Learning from other agents (extracting patterns)
- ✅ Major KG restructuring

**Recommended**:

- Before committing KG changes
- Weekly validation runs
- After merging changes from other projects

---

## How to Run

### Validation Only (Report Issues)

```bash
python scripts/validate_kg_links.py
```

### With Detailed Output

```bash
python scripts/validate_kg_links.py --verbose
```

### Save Report to File

```bash
python scripts/validate_kg_links.py --output validation-report.json
```

### Auto-Fix (Simple Issues Only)

```bash
python scripts/validate_kg_links.py --fix
```

> ⚠️ **Note**: Auto-fix only removes broken links. It does NOT intelligently fix them.

---

## Validation Checks

### 1. Cross-Reference Validation

Checks all link types:

- `governed_by` → behaviors
- `guides` → skills
- `depends_on` → skills
- `enforces` → skills/behaviors
- `implements` → behaviors
- `extends` → behaviors
- `synergizes_with` → behaviors
- `applies_to` → categories/skills
- And more...

### 2. Connectivity Validation

- All skills MUST have at least one `governed_by` link
- Identifies orphaned nodes (no links)
- Flags missing critical connections

### 3. Master Graph Validation

- All listed graph files exist
- All roles reference valid graphs
- No missing graphs

---

## Interpreting Results

### Exit Codes

- `0` = PASS (no critical issues)
- `1` = FAIL (broken links or master issues found)

### Issue Severity

- **ERROR**: Broken cross-references, missing files
- **WARNING**: Orphaned nodes, missing optional links

### Report Structure

```json
{
  "summary": {
    "total_nodes": 78,
    "total_links": 51,
    "broken_links": 7,
    "orphaned_nodes": 54,
    "status": "PASS" | "FAIL"
  },
  "broken_links": [...],
  "orphaned_nodes": [...],
  "master_issues": [...],
  "suggestions": [...]
}
```

---

## Fixing Issues

### 🤖 Automated Fix (Limited)

The `--fix` flag performs **simple, safe fixes only**:

- ✅ Removes broken links to non-existent nodes
- ✅ Cleans up empty link sections

**Does NOT**:

- ❌ Intelligently determine correct target
- ❌ Create missing nodes
- ❌ Resolve ambiguous references

### 🧠 LLM-Assisted Fix (Recommended)

**For complex issues, use a high-capability LLM agent** (Sonnet 3.5+, GPT-4+, Gemini 2.0+):

1. **Run validation** to get report
2. **Review broken links** in report
3. **LLM analyzes context**:
   - Examines node purpose
   - Checks related nodes
   - Determines correct target
4. **LLM proposes fix** with reasoning
5. **Human approves** before applying

**Instructions for LLM**:
> When fixing KG link issues, you MUST:
>
> 1. Understand the semantic meaning of both source and target
> 2. Check if target should exist (create it) or reference is wrong (remove it)
> 3. For format issues (e.g., `skill:builder:X` vs `skill-X`), fix the format
> 4. For missing nodes, determine if they should be created or reference removed
> 5. If information is missing or ambiguous, STOP and report - do not guess
> 6. Document your reasoning for each fix

**Example LLM Fix Process**:

```
Issue: behavior:core:planning-workflow → all-skills (doesn't exist)

Analysis:
- Source: Universal planning behavior
- Intent: Apply to all skills
- Problem: "all-skills" is not a valid node ID

Options:
1. Create wildcard pattern support (complex)
2. Remove link (loses intent)
3. Change to applies_to: ["skill:*"] (pattern)

Decision: This is a design question - STOP and report to user
```

### 🛠️ Manual Fix (Always Works)

For any issue:

1. Open the graph file mentioned in report
2. Find the node with broken link
3. Fix or remove the link
4. Re-run validation to confirm

---

## Common Issues

### Issue: `skill:builder:maintain-kg` not found

**Cause**: Wrong ID format  
**Fix**: Change to `skill-maintain-kg` (no role prefix for skills)

### Issue: `all-skills` not found

**Cause**: Pseudo-target doesn't exist  
**Fix**: LLM decision - create pattern support or remove

### Issue: Missing `governed_by` link

**Cause**: Skill not linked to any behavior  
**Fix**: Add appropriate behavior link (requires understanding skill purpose)

### Issue: Orphaned knowledge nodes

**Severity**: WARNING (usually OK)  
**Cause**: Documentation nodes don't need links  
**Fix**: No action needed unless node should be linked

---

## Integration

### Pre-Commit Hook

Add to `.git/hooks/pre-commit`:

```bash
#!/bin/bash
python scripts/validate_kg_links.py
if [ $? -ne 0 ]; then
    echo "❌ KG validation failed. Fix issues before committing."
    exit 1
fi
```

### CI/CD Pipeline

```yaml
- name: Validate KGs
  run: python scripts/validate_kg_links.py --output kg-report.json
```

---

## Governed By

- `behavior:builder:consistency` - Ensures KG reflects reality

---

## Uses

- `scripts/validate_kg_links.py` - Validation script

---

## Validates

- `builder-skills-graph.json`
- `builder-behaviors-graph.json`
- `builder-knowledge-graph.json`
- `manager-skills-graph.json`
- `manager-behaviors-graph.json`
- `manager-knowledge-graph.json`
- `master-graph.json`

---

**Remember**: Validation is cheap, fixing is expensive. Run often, fix carefully.
