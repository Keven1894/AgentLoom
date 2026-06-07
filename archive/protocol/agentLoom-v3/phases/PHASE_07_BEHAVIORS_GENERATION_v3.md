# Phase 7: Behaviors Generation

**AI Agent Setup Protocol V3.0**

---

## Objective

Generate domain behaviors - the culture and rules that govern how the agent operates. LLM-driven based on knowledge and skills context.

---

## Step 1: Load Context

Read previous phase outputs:

```
From Phase 2 (output/phase-02.md):
- Get [DOMAIN_ROLE_ID] and save to memory
- Skills list with implementation types
From Phase 4 (output/phase-04.md): Domain behaviors graph JSON
From Phase 5 (output/phase-05.md): Knowledge content (domain understanding)
From Phase 6 (output/phase-06.md): Skills implementation (what agent can do)
```

---

## Step 2: Understand the Domain Culture

**Think**: Based on knowledge and skills, what culture/rules should govern this agent?

**Read**:

- Phase 5 knowledge nodes (domain concepts)
- Phase 6 skills (capabilities)
- Phase 2 architecture (initial behavior ideas)

**Consider**:

- What makes interactions high-quality in this domain?
- What must NEVER happen?
- What workflows are critical?
- What communication style fits this domain?

---

## Step 3: Process Domain Behaviors Graph

**Load**: `agents/knowledge-graphs/[DOMAIN_ROLE_ID]-behaviors-graph.json`

**For each behavior node** with a `path` field pointing to `.cursor/behaviors/[DOMAIN_ROLE_ID]/`:

### 3.1: Check File Status

- File exists? (should be placeholder from Phase 3)
- Has frontmatter with priority?

### 3.2: Generate Behavior Content

**For each behavior**, generate based on:

**Priority** (from Phase 2):

- **Critical**: Safety, ethics, core function
- **High**: Quality, user experience
- **Medium**: Optimization, preferences

**Context**:

- Related skills (what does this behavior govern?)
- Domain knowledge (what domain rules apply?)
- Use cases (when does this matter?)

---

## Step 4: Generate Behavior Descriptions

**Read**:

- `builder-assets/.cursor/behaviors/` (see pattern from builder behaviors)
- Phase 2 behavior definitions
- Phase 6 skills (to link behaviors → skills)

**Generate** using this structure:

```markdown
---
[existing frontmatter with priority]
---

# [Behavior Name]

## Purpose
[What this behavior ensures - 1-2 sentences]

## Priority: [Critical | High | Medium]

[Why this priority level]

## Rules

### Rule 1: [Rule Name]
**What**: [Specific rule]
**Why**: [Reasoning]
**Applies to**: [Which skills/situations]

### Rule 2: [Rule Name]
[Continue for 2-5 rules per behavior]

## Governs

**Skills**:
- [skill-id]: [How this behavior governs this skill]
- [skill-id]: [How this behavior governs this skill]

**Processes**:
- [Process name]: [How this behavior applies]

## Examples

### ✅ Good Example
[Scenario showing behavior followed]

### ❌ Bad Example
[Scenario showing behavior violated]

## Related Behaviors
- [behavior-id]: [Relationship]
```

**Content approach**:

- **Be specific** to the domain (not generic)
- **Be practical** (rules agent can actually follow)
- **Be cultural** (define the "personality" of this agent)
- **Link to skills** (behaviors govern skills)

---

## Step 5: Generate Based on Knowledge + Skills

**LLM reasoning**:

For each behavior, think:

1. **What knowledge** from Phase 5 informs this behavior?
   - Domain concepts → Rules
   - Best practices → Guidelines
   - Constraints → Boundaries

2. **What skills** from Phase 6 does this govern?
   - Skill X needs behavior Y to ensure quality
   - Workflow A requires behavior B for safety

3. **What culture** fits this domain?
   - Professional? Friendly? Technical? Educational?
   - Formal? Casual? Precise? Creative?

**Generate behaviors** that create the right culture for this domain.

---

## Step 6: Write Output Summary

**Create**: `output/phase-07.md`

**Follow structure**: Read `specs/phase-07-output.spec.md`

**Include**:

- Behaviors generated ✅
- Priority breakdown (critical/high/medium)
- Skills governed by each behavior
- Culture/tone established

---

## Step 7: Confirm with Human

```
✅ Phase 7 Behaviors Generated:

Total behaviors: [X]
- Critical: [count] (safety, ethics, core function)
- High: [count] (quality, user experience)
- Medium: [count] (optimization, preferences)

Culture established:
- Communication style: [description]
- Key principles: [list top 3]
- Governed skills: [count]

See: output/phase-07.md

This is a STARTUP agent - behaviors will refine through real-world use.

Approve and proceed to Phase 8 (Final Validation)?
```

---

## Completion

```
✅ Phase 7 Complete

Behaviors: [X] generated
Culture: Defined for domain
Focus: Domain behaviors in .cursor/behaviors/ folder

Next: Phase 8 (Final Validation & Testing)
```

---

## Important Notes

**Focus**: Only `.cursor/behaviors/[DOMAIN_ROLE_ID]/` - domain behaviors

**Builder behaviors**: Already complete in `.cursor/behaviors/core/` and `.cursor/behaviors/builder/` (from builder-assets)

**LLM-driven**: Aggressively use LLM to generate culture/rules based on context

**Startup quality**: Good enough to start - will refine through real-world experience

**Culture matters**: Behaviors define the "personality" and "professionalism" of the agent

**Link to skills**: Every behavior should govern specific skills (use `links` field in KG)

---

**Next**: [Phase 8: Final Validation](PHASE_08_FINAL_VALIDATION.md)
