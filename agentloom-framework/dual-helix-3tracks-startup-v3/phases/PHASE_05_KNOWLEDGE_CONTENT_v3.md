# Phase 5: Knowledge Content Generation

**AI Agent Setup Protocol V3.0**

---

## Objective

Fill knowledge nodes in `docs/` folder with actual content. Focus on domain knowledge only (builder knowledge already complete).

---

## Step 1: Load Context

Read previous phase outputs (`output/`):

```
From Phase 2 (output/phase-02.md):
- KG structure, knowledge categories
- Get [DOMAIN_ROLE_ID] and save to memory
- From ### Content Analysis section: user-shared content info

From Phase 4 (output/phase-04.md):
- Domain knowledge graph JSON filename
```

---

## Step 2: Categorize All Knowledge Nodes

**Load**: `agents/knowledge-graphs/[DOMAIN_ROLE_ID]-knowledge-graph.json`

**For each node** with a `path` field pointing to `docs/[DOMAIN_ROLE_ID]/`:

### 2.1: Check File Status

- File exists? (should be placeholder from Phase 3)
- Has marker `[Content will be generated in Phase 5]`?

### 2.2: Assess Content Source and Categorize

**Check Phase 2 output** for `### Content Analysis` section.

**If user shared content exists**:

- Check scanned folder structure
- Identify source files for this knowledge node
- Determine if content is directly usable or needs synthesis

**For each knowledge node, categorize as ONE of**:

#### Category A: Straightforward (auto-generate now)

- **Single source file** → Extract and format content from user-shared file
- **Clear definition** from Phase 1/2 context
- **Standard terminology** for this domain
- **Simple explanation** possible from available information

#### Category B: Complex (flag for human - synthesis needed)

- **Multiple source files** → Needs synthesis across different documents
- **Large folder** → Needs summarization of many files in user-shared folders
- **Domain patterns** → Needs expertise to identify and explain patterns
- **Integration** → Needs to combine information from different sources

#### Category C: Very Complex (flag for human - research needed)

- **External sources needed** → Not in shared content, requires research
- **Domain expert required** → Specialized knowledge beyond available info
- **Research required** → Needs investigation beyond current materials

**Create tracking list**:

```
Category A (Straightforward): [list of node IDs]
Category B (Complex): [list of node IDs]
Category C (Very Complex): [list of node IDs]
```

---

## Step 3: Generate Straightforward Content

**For each node in Category A** (straightforward):

### 3.1: Gather Content

**Read**:

- `docs/general/CONTENT_TEMPLATE.md` (structure pattern)
- KG node metadata (title, description, parent)
- Phase 2 architecture (context for this topic)
- **User-shared content** (if available - check Phase 2 Content Analysis)
  - Extract relevant information from source file(s)
  - Use actual content, don't make it up

### 3.2: Generate Content

**Use this structure**:

```markdown
---
[existing frontmatter]
---

# [Topic Title]

## Overview
[What this topic covers - 2-3 sentences]

## Key Concepts
[Main ideas, definitions, terminology]
[Use content from user-shared files if available]

## Details
[In-depth information, explanations]
[Extract from source documents or generate from Phase 1/2 context]

## Examples
[Concrete examples if applicable]

## Related Topics
[Links to parent/child/related nodes from KG]

## References
[Sources - list user-shared files used, if any]
```

### 3.3: Content Quality Guidelines

- **Clear and concise** - Easy to understand
- **Domain-appropriate** - Use correct terminology
- **Useful for agent** - Information agent will actually reference
- **Startup quality** - Good enough to start, will refine through use
- **Honest sourcing** - If from user files, acknowledge; if generated, make it clear

**Mark as generated** ✅ in tracking list.

---

## Step 4: Create Development Plan for Complex Tasks

**For each node in Category B and C** (complex and very complex):

### 4.1: Document Each Complex Task

```markdown
### [node-id]: [file-path]

**Category**: [Complex | Very Complex]

**Why complex**:
- [Specific reason - be detailed]
- Example: "Requires synthesis of 15 lecture PDFs from /course-materials/lectures/"
- Example: "Needs domain expertise to explain advanced [topic]"
- Example: "Requires external research on [subject] not in shared content"

**Source documents** (if user provided):
- [list specific files from Phase 2 Content Analysis]
- [folder paths]

**Suggested approach**:
1. [Step 1 - what human should do first]
2. [Step 2 - how to process/synthesize]
3. [Step 3 - how to validate/complete]

**Estimated effort**: [X hours/days]
```

### 4.2: Organize by Priority

**Critical** (blocks agent function):

- [list nodes]

**High** (important for quality):

- [list nodes]

**Medium** (nice to have):

- [list nodes]

---

## Step 5: Write Output Summary

**Create**: `output/phase-05.md`

**Follow structure**: Read `specs/phase-05-output.spec.md`

**Include**:

### Auto-Generated Content (Category A)

```markdown
Successfully generated: [X] knowledge nodes

- [node-id-1]: [file-path] ✅
- [node-id-2]: [file-path] ✅
...
```

### Development Plan (Category B & C)

```markdown
Requires human development: [Y] knowledge nodes

**Complex (synthesis needed)**: [count]
[list from Step 4.1]

**Very Complex (research needed)**: [count]
[list from Step 4.1]
```

### Summary

```markdown
Total nodes: [Z]
- Auto-generated: [X] ([percentage]%)
- Requires development: [Y] ([percentage]%)

Priority breakdown:
- Critical: [count]
- High: [count]
- Medium: [count]
```

---

## Step 6: Confirm with Human

```
✅ Phase 5 Knowledge Content:

Auto-generated: [X] knowledge nodes
Requires development: [Y] knowledge nodes
- Complex (synthesis): [count]
- Very Complex (research): [count]

Completion: [X/Z] ([percentage]%)

See detailed plan: output/phase-05.md

Review and proceed to Phase 6 (Skills)?
```

---

## Completion

```
✅ Phase 5 Complete

Knowledge content: [X] nodes generated
Development plan: [Y] nodes flagged
Focus: Domain knowledge in docs/ folder

Next: Phase 6 (Skills Implementation)
```

---

## Important Notes

**Focus**: Only `docs/[DOMAIN_ROLE_ID]/` folder - domain knowledge nodes

**Builder knowledge**: Already complete in `docs/general/` and `docs/builder/` (from builder-assets)

**Use shared content**: If user provided folders in Phase 1, USE that content (don't make it up)

**Quality bar**: Good enough for startup agent - will refine through real-world use

**Be honest**: Flag complex synthesis/research tasks for human - this IS the value

**Categorization is key**: Step 2 labels everything, Step 3 generates straightforward, Step 4 plans complex

---

**Next**: [Phase 6: Skills Implementation](PHASE_06_SKILLS_IMPLEMENTATION.md)
