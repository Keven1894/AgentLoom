---
type: skill
category: system
id: skill-chunk-document
implementation: hybrid-llm
roles:
  - role-builder
---

# Skill: Auto-Chunk Document

## Purpose

Automatically split oversized documentation files (>500 lines) into smaller, focused files (Concept vs Execution) to optimize for LLM working memory.

## Implementation Strategy: "The Surgeon"

To ensure data integrity, this skill uses a **Hybrid** approach:

1. **LLM (Analysis)**: Analyzes the file and generates a **Split Plan** (JSON).
2. **Script (Execution)**: deterministic Python script cuts and moves text blocks based on the plan.
3. **LLM (Synthesis)**: Generates the `INDEX.md` file to link the new chunks.

**Why this approach?**

- Prevents "hallucination" or data loss during rewriting.
- Allows use of smaller, faster models (e.g., Llama 3.1 8B) for analysis.
- Ensures code blocks and formatting are preserved exactly.

## Input

```json
{
  "targetFile": "docs/builder/implementation/MONITORING-UPDATE-STRATEGY.md",
  "strategy": "concept-execution",
  "model": "local-8b" 
}
```

## Process Flow

### Step 1: Analyze & Plan (LLM)

**Prompt**:
> "Analyze this markdown file. Identify sections that represent high-level 'Concepts' (theory, why, what) vs 'Execution' (steps, code, how). Return a JSON Split Plan mapping line ranges or headers to target files."

**Output (JSON)**:

```json
{
  "originalFile": "MONITORING-UPDATE-STRATEGY.md",
  "chunks": [
    {
      "targetName": "monitoring-concept.md",
      "type": "concept",
      "sections": ["# Overview", "## Strategy", "## Architecture"]
    },
    {
      "targetName": "monitoring-execution.md",
      "type": "execution",
      "sections": ["## Implementation Steps", "## Code Examples", "## Rollback"]
    }
  ]
}
```

### Step 2: Execute Split (Python Script)

The script `scripts/chunk_document.py`:

1. Reads the original file.
2. Parses the JSON Plan.
3. Extracts text blocks by header/section.
4. Writes new files (`*-concept.md`, `*-execution.md`).
5. **Verifies** total line count matches original (sanity check).

### Step 3: Generate Index (LLM)

**Prompt**:
> "Create an INDEX.md file that links to these two new files: [list]. Add a brief summary for each."

## Usage

```bash
# Dry Run (Generate Plan only)
python scripts/chunk_document.py docs/file.md --plan-only

# Execute Split
python scripts/chunk_document.py docs/file.md --execute
```

## Success Criteria

- [ ] Original file is replaced by 2+ smaller files + INDEX.md.
- [ ] No text is lost (line count verification).
- [ ] New files are < 500 lines.
- [ ] `skill-validate-chunking` passes on the new folder.
