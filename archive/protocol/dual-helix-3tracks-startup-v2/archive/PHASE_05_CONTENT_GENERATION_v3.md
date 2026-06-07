# Phase 5: Content Generation

**AI Agent Setup Protocol V3.0**

---

## Objective

Fill placeholder files with actual content. Auto-generate straightforward content, identify complex tasks for human development.

---

## Step 1: Load Context

Read all previous phase outputs:

```
From Phase 1: PROJECT_NAME, DOMAIN_ROLE_ID, domain concepts
From Phase 2: Architecture design
From Phase 3: File structure
From Phase 4: Knowledge Graphs (7 JSON files)
```

---

## Step 2: Process All Knowledge Graphs

For **each of the 7 Knowledge Graph files**:

1. Load the JSON file
2. For each node in the graph:
   - Check if node has a `path` field (references a .md file)
   - If yes → Process that file (Step 3)

**Order**: Process in this sequence:

1. Builder graphs (should already have content from builder-assets)
2. Domain graphs (need content generation)

---

## Step 3: Process Each Node File

For **each .md file** referenced in KG nodes:

### 3.1: Check File Status

**Does file exist?**

- No → Skip (error, should exist from Phase 3)
- Yes → Continue

**Is file a placeholder?**

- Check for marker: `[Content will be generated in Phase 5]`
- If yes → Need to generate content
- If no → Already has content, skip

### 3.2: Assess Complexity

**Ask yourself**: Can I generate this content automatically?

**Straightforward** (auto-generate):

- Standard behavior descriptions (safety, validation, etc.)
- Simple skill descriptions (what it does, when to use)
- Knowledge nodes with clear definition from Phase 1/2
- Documentation that follows patterns

**Complex** (requires human development):

- Skills needing custom Python/Shell implementation
- Behaviors with domain-specific logic/workflows
- Knowledge nodes requiring synthesis of multiple sources
- Content needing external data/APIs
- Anything requiring domain expertise beyond Phase 1/2 info

### 3.3: Take Action

**If straightforward**:

- Generate full content for the .md file
- Follow CONTENT_TEMPLATE.md structure
- Include frontmatter (already there)
- Add description, purpose, usage, examples
- Mark as ✅ in tracking

**If complex**:

- Leave placeholder as-is
- Add to "Complex Tasks" list
- Note WHY it's complex
- Suggest approach for human developer
- Mark as ⚠️ in tracking

---

## Step 4: Generate Straightforward Content

For files marked as straightforward:

**Read**:

- `docs/general/CONTENT_TEMPLATE.md` (structure pattern)
- Relevant KG node (metadata, relationships)
- Phase 2 architecture (context for this component)

**Generate** full content with:

### For Skills

```markdown
---
[existing frontmatter]
---

# [Skill Name]

## Purpose
[What this skill does]

## When to Use
[Scenarios where this skill applies]

## Process
[Step-by-step how it works]

## Related
- Behaviors: [which behaviors govern this]
- Skills: [parent/child skills]
- Knowledge: [what knowledge it uses]

## Implementation Notes
[For rule-based: algorithm description]
[For LLM-based: prompt strategy]
```

### For Behaviors

```markdown
---
[existing frontmatter]
---

# [Behavior Name]

## Purpose
[What this behavior ensures]

## Rules
[Specific rules to follow]

## Applies To
[Which skills/processes this governs]

## Priority
[Why this matters - from Phase 2]

## Examples
[Good vs bad examples]
```

### For Knowledge Nodes

```markdown
---
[existing frontmatter]
---

# [Topic Name]

## Overview
[What this topic covers]

## Key Concepts
[Main ideas, definitions]

## Details
[In-depth information]

## Related Topics
[Links to other knowledge nodes]

## References
[Sources, if applicable]
```

---

## Step 5: Identify Complex Tasks

For files marked as complex, **document each one**:

**For each complex file**, note:

1. **File path**: Where it is
2. **Node type**: Skill / Behavior / Knowledge / Script
3. **Why complex**: Specific reason
   - "Requires Python implementation with [specific library]"
   - "Needs synthesis of [X] documents from [folder]"
   - "Domain-specific workflow requiring [expertise]"
   - "Integration with [external system/API]"
4. **Suggested approach**: How human should tackle it
   - "Implement using [technology/pattern]"
   - "Review [source documents] and synthesize"
   - "Consult domain expert for [specific aspect]"

---

## Step 6: Write Output Summary

**Create**: `output/phase-05.md`

**Follow structure**: Read `specs/phase-05-output.spec.md`

**Generate** with:

- All auto-generated files listed ✅
- All complex tasks listed ⚠️ with explanations
- Counts and percentages
- Next steps for human

**Be honest**: This is where we identify real development work needed.

---

## Step 7: Confirm with Human

```
✅ Phase 5 Content Generation:

Auto-generated: [X] files
- [breakdown by type]

Requires development: [Y] files
- Skills: [count] (custom implementation needed)
- Behaviors: [count] (domain logic needed)
- Knowledge: [count] (synthesis/research needed)
- Scripts: [count] (coding needed)

Completion: [X/Z] ([percentage]%)

See detailed development plan: output/phase-05.md

Review complex tasks and proceed? I strongly suggest we finish this protocol first. 
```

Wait for human to review development plan.

---

## Completion

```
✅ Phase 5 Complete

Content generated: [X] files
Development plan: [Y] tasks identified
Honesty: ✅ Complex tasks flagged for human

Next: Human reviews and implements complex tasks
Then: Phase 6 (Validation Tools)
```

---

## Important Notes

**Be honest**: Don't try to auto-generate complex content that needs real development. Flag it.

**Try your best**: Also, do not leave everything as future plan.You have strong reasoning skills and also world knowledge, if something you can generate and logical sound, go with it.

**Value of this phase**: Separates "easy automation" from "real development work". This IS the value - knowing what needs human expertise.

**Examples of complex tasks**:

- Skill that needs to parse specific file formats
- Behavior with multi-step domain workflow
- Knowledge node summarizing 50+ documents
- Script integrating with external API
- parse multiple pdfs and generate a summary (take time to prepare scripts and content extraction logic)

**Examples of straightforward tasks**:

- Standard safety behavior descriptions
- Simple skill descriptions (what/when/how)
- Knowledge nodes with clear definitions
- Documentation following patterns
- Simple extact content from 1-2 text based files and summarize the content

---

**Next**: [Phase 6: Validation Tools](PHASE_06_VALIDATION_TOOLS.md)
