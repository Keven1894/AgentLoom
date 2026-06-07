---
type: skill
category: system
id: skill-validate-chunking
implementation: rule-based
roles:
  - role-builder
---

# Skill: Validate Document Chunking

## Purpose

Validate that AI-consumed documents follow chunking best practices based on the "Lost in the Middle" research and working memory constraints of modern LLMs.

## Context

Even with 1M-token context windows, LLMs have limited **working memory** for reliable reasoning and editing. Documents should be:

- **250-500 lines** (≈1,500-3,000 tokens) per file
- **One concept per file** (avoid mixing theory, execution, examples)
- **Separated by concern** (concept vs execution)
- **Cross-linked** instead of duplicated

## Implementation Type

**Rule-based** - Deterministic checks, no LLM reasoning required

## Script Execution

**Script**: `scripts/validate_chunking.py`

**Usage**:

```bash
# Validate single file
python scripts/validate_chunking.py docs/manager/orchestration-guide.md

# Validate folder (non-recursive)
python scripts/validate_chunking.py docs/manager/

# Validate folder (recursive)
python scripts/validate_chunking.py docs/ --recursive

# Save output to JSON file
python scripts/validate_chunking.py docs/manager/ --output validation-report.json
```

**Output**: JSON format (see Output Format section below)

**Exit Codes**:

- `0`: All files compliant or acceptable
- `1`: One or more files oversized (need splitting)

## Input

```json
{
  "targetPath": "docs/manager/orchestration-guide.md",
  "recursive": false,
  "includeSubfolders": true
}
```

**Parameters**:

- `targetPath`: File or folder to validate
- `recursive`: Check all subfolders (default: false)
- `includeSubfolders`: Include immediate subfolders (default: true)

## Validation Rules

### Rule 1: File Size Check

**Target**: 250-500 lines per file  
**Tolerance**:

- ✅ **Ideal**: 250-350 lines
- ⚠️ **Acceptable**: 351-500 lines
- ❌ **Oversized**: 501+ lines

**Check**:

```python
line_count = count_lines(file_path)
if line_count > 500:
    status = "oversized"
    recommendation = "Split into smaller files"
elif line_count > 350:
    status = "acceptable"
    recommendation = "Consider splitting if adding more content"
else:
    status = "ideal"
    recommendation = None
```

### Rule 2: Concept Boundary Check

**Target**: One primary concept per file  
**Check**: Frontmatter should have single `category` or `concept` field

**Validation**:

```python
frontmatter = parse_frontmatter(file_path)
if "category" in frontmatter:
    concept_count = 1 if isinstance(frontmatter["category"], str) else len(frontmatter["category"])
elif "concept" in frontmatter:
    concept_count = 1
else:
    concept_count = "unknown"

if concept_count > 1:
    status = "warning"
    recommendation = "File covers multiple concepts, consider splitting"
```

### Rule 3: Concept/Execution Separation

**Target**: Separate "what" (concept) from "how" (execution)  
**Check**: Look for mixed patterns in filename or content structure

**Heuristics**:

- Filename contains both `-concept` and `-execution`: ❌ Invalid
- File has both "## Concept" and "## Execution" sections: ⚠️ Warning
- Large files (>400 lines) without `-concept` or `-execution` suffix: ⚠️ Suggest split

### Rule 4: Cross-Linking Check

**Target**: Files should reference related files, not duplicate content  
**Check**: Look for markdown links to other files in same category

**Validation**:

```python
content = read_file(file_path)
internal_links = find_markdown_links(content)
related_files = [link for link in internal_links if is_relative_path(link)]

if len(related_files) == 0 and file_size > 400:
    status = "warning"
    recommendation = "Large file with no cross-links - may contain duplicated content"
```

### Rule 5: Document Type Classification

**Target**: Only validate AI-consumed documents  
**Check**: Determine if document is for AI or human consumption

**AI-Consumed** (Apply chunking rules):

- `docs/[role]/` - Knowledge content
- `agents/skills/` - Skill definitions
- `.cursor/behaviors/` - Behavior definitions
- `agents/NEW_AGENT_START_HERE.md` - Initialization
- Files with frontmatter containing `type: skill|behavior|knowledge`

**Human-Consumed** (Skip validation):

- `USER_MANUAL*.md`
- `README.md`
- `*_DESIGN_SUMMARY.md`
- Files in `docs/general/` (mixed audience)

## Output Format

### Single File Validation

```json
{
  "file": "docs/manager/orchestration-guide.md",
  "documentType": "ai-consumed",
  "lines": 650,
  "tokens": 3250,
  "status": "oversized",
  "issues": [
    {
      "rule": "file-size",
      "severity": "error",
      "message": "File exceeds 500-line recommendation (650 lines)",
      "recommendation": "Split into orchestration-concept.md and orchestration-execution.md"
    },
    {
      "rule": "cross-linking",
      "severity": "warning",
      "message": "Large file with no cross-links to related files",
      "recommendation": "Consider if content should be split and cross-linked"
    }
  ],
  "suggestions": [
    "Create orchestration-concept.md (≈300 lines) - Framework and principles",
    "Create orchestration-execution.md (≈350 lines) - Step-by-step workflows",
    "Add INDEX.md to link both files"
  ]
}
```

### Folder Validation

```json
{
  "folder": "docs/manager/",
  "totalFiles": 12,
  "aiConsumedFiles": 8,
  "humanConsumedFiles": 4,
  "summary": {
    "compliant": 5,
    "acceptable": 2,
    "oversized": 1,
    "skipped": 4
  },
  "oversizedFiles": [
    {
      "file": "orchestration-guide.md",
      "lines": 650,
      "recommendation": "Split into concept + execution"
    }
  ],
  "recommendations": [
    "Create INDEX.md for orchestration category (3 related files)",
    "Add .meta.json to track chunking status"
  ]
}
```

## Execution Steps

### Step 1: Classify Document Type

```python
def classify_document(file_path):
    # Check path patterns
    if "USER_MANUAL" in file_path or "README" in file_path:
        return "human-consumed"
    
    if file_path.startswith("docs/") or file_path.startswith("agents/skills/"):
        return "ai-consumed"
    
    # Check frontmatter
    frontmatter = parse_frontmatter(file_path)
    if frontmatter.get("type") in ["skill", "behavior", "knowledge"]:
        return "ai-consumed"
    
    return "unknown"
```

### Step 2: Run Validation Rules

```python
def validate_file(file_path):
    doc_type = classify_document(file_path)
    
    if doc_type == "human-consumed":
        return {"status": "skipped", "reason": "Human-consumed document"}
    
    issues = []
    
    # Rule 1: File size
    line_count = count_lines(file_path)
    if line_count > 500:
        issues.append({
            "rule": "file-size",
            "severity": "error",
            "message": f"File exceeds 500-line recommendation ({line_count} lines)"
        })
    
    # Rule 2: Concept boundary
    # Rule 3: Concept/execution separation
    # Rule 4: Cross-linking
    # ... (implement each rule)
    
    return {
        "file": file_path,
        "documentType": doc_type,
        "lines": line_count,
        "status": determine_status(issues),
        "issues": issues
    }
```

### Step 3: Generate Recommendations

```python
def generate_recommendations(validation_result):
    if validation_result["status"] == "oversized":
        # Suggest split pattern based on content
        return suggest_split_pattern(validation_result["file"])
    
    if validation_result["status"] == "acceptable":
        return ["Monitor file size when adding content"]
    
    return []
```

### Step 4: Output Results

Format results according to output specification (single file or folder summary).

## Usage Examples

### Example 1: Validate Single File

**Prompt**:

```
Validate chunking compliance for:
@docs/manager/orchestration-guide.md
```

**Agent Action**:

1. Read file and count lines
2. Check frontmatter for concept classification
3. Look for cross-links
4. Generate validation report

**Output**:

```
❌ Chunking Validation Failed

File: docs/manager/orchestration-guide.md
Lines: 650 (exceeds 500-line limit)
Status: Oversized

Issues:
- File size: 650 lines (recommended: 250-500)
- No cross-links found (may contain duplicated content)

Recommendations:
1. Split into:
   - orchestration-concept.md (≈300 lines) - Framework
   - orchestration-execution.md (≈350 lines) - Workflows
2. Create orchestration-INDEX.md to link both files
3. Update knowledge graph to reference new structure
```

### Example 2: Validate Entire Folder

**Prompt**:

```
Validate chunking compliance for all AI-consumed docs in:
@docs/manager/
```

**Agent Action**:

1. Scan folder for all .md files
2. Classify each as AI-consumed or human-consumed
3. Validate AI-consumed files
4. Generate summary report

**Output**:

```
✅ Chunking Validation Summary

Folder: docs/manager/
Total Files: 12
AI-Consumed: 8
Human-Consumed: 4 (skipped)

Status:
✅ Compliant: 5 files
⚠️ Acceptable: 2 files
❌ Oversized: 1 file

Oversized Files:
- orchestration-guide.md (650 lines) → Split recommended

Recommendations:
- Create INDEX.md for orchestration category
- Add .meta.json to track chunking status
- Consider splitting orchestration-guide.md
```

## Success Criteria

- ✅ Correctly classifies AI-consumed vs human-consumed documents
- ✅ Identifies files exceeding 500-line limit
- ✅ Detects missing cross-links in large files
- ✅ Provides actionable split recommendations
- ✅ Generates clear validation reports

## Related Skills

- `skill-chunk-document` - Auto-split oversized documents
- `skill-maintain-kg` - Update KG after chunking changes
- `skill-generate-index` - Create INDEX.md files

## Related Behaviors

- `behavior:builder:document-chunking` - Enforces chunking rules during content generation

## Notes

- This skill is **read-only** - it validates but doesn't modify files
- Use `skill-chunk-document` to actually split oversized files
- Validation should run before committing new documentation
- Consider adding this to CI/CD pipeline for automated checks
