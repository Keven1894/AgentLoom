# Phase 2: Architecture Design

**AI Agent Setup Protocol V3.0**

---

## Objective

Design domain role architecture through analysis and mapping. Agent Builder architecture is already complete (in `builder-assets/`).

---

## Step 1: Load Context

Read `output/phase-01.md` to get:

```
PROJECT_NAME = [value]
DOMAIN_ROLE_NAME = [value]
DOMAIN_ROLE_ID = [value]
DOMAIN_ID = [value]
DOMAIN_CONCEPTS = [list]
SKILLS_NEEDED = [list]
BEHAVIORS = [list]
CONTENT_FOLDERS = [paths, if any]
```

---

## Step 2: Analyze Content (If Provided)

**If user shared content folders in Phase 1**, analyze them now:

**For each folder**:
1. Scan structure (file types, organization, depth)
2. Identify natural groupings (what categories emerge?)
3. Extract key concepts (what's actually in the content?)
4. Note cross-references (do files link to each other?)

**Document findings**:
```
Folder: [path]
- Files: ~[count], types: [.md, .pdf, etc.]
- Organization: [flat / by topic / by date / hierarchical]
- Categories: [list what you found]
- Concepts: [main topics from content]
```

**Skip to Step 3** if no folders shared.

---

## Step 3: Design Domain Knowledge Structure

**Think through**: How should domain knowledge be organized in the Knowledge Graph?

### Required in Your Design:

**Hierarchy description**:
- What's the root? (`DOMAIN_ID:root`)
- What are main categories? (3-7 typical)
- How deep? (2-level, 3-level, deeper?)
- What's the natural organization for this domain?

**Example thinking** (adapt to YOUR domain):
- Education: Course → Module → Topic → Content
- Healthcare: Specialty → Condition → Symptom → Treatment
- Legal: Area → Topic → Case → Document

**Content mapping** (if folders provided):
- How do shared folders map to KG categories?
- Which folder becomes which node?

---

## Step 4: Design Domain Skills

**Think through**: What capabilities does this domain role need?

### Required in Your Design:

For **each skill** (3-7 typical):

**Name**: skill-[action]-[object]
- Examples: skill-retrieve-course-info, skill-assist-assignment, skill-analyze-code

**Purpose**: What it does (1 sentence)

**Implementation type**: Choose based on task complexity
- **rule-based**: File operations, validation, deterministic logic
- **llm-based-max**: Complex reasoning, requires Claude 4.5+
- **llm-based-slm**: Simple patterns, can use Llama 3.1 8B
- **hybrid**: Rules for prep/validation + LLM for reasoning

**Links to behaviors**: Which behavior(s) govern this skill?

**Guidance questions**:
- What should the domain role be able to DO?
- Which tasks need LLM reasoning vs rules?
- Any orchestration (parent skill → sub-skills)?

---

## Step 5: Design Domain Behaviors

**Think through**: What protocols ensure quality in this domain?

### Required in Your Design:

For **each behavior** (3-5 typical):

**Name**: behavior:[DOMAIN_ROLE_ID]:[behavior-name]
- Examples: behavior:tutor:guide-not-solve, behavior:curator:data-quality

**Purpose**: What it ensures (1-2 sentences)

**Priority**: critical | high | medium
- Critical: Safety, ethics, core function
- High: Quality, user experience  
- Medium: Optimization, preferences

**Governs**: What does it control?
- Specific skills?
- Knowledge areas?
- Communication style?

**Guidance questions**:
- What must NEVER happen in this domain?
- What makes interactions high-quality?
- Any mandatory workflows?

---

## Step 6: Map Relationships

**Think through**: How do components connect?

### Required in Your Design:

**Internal relationships** (within domain role):
```
Example pattern:
behavior:[domain]:rule-name
  ↓ enforces
skill-capability-name
  ↓ uses  
knowledge:[domain]:category
```

**Cross-links to Agent Builder** (rare, but possible):
```
When might domain role interact with Agent Builder?
- Need custom KG maintenance? Link to skill-maintain-kg
- Domain-specific validation? Reference behavior:builder:schema
```

**Typical**: Most domain roles are independent of Agent Builder

---

## Step 7: Write Architecture Output

**Create**: `output/phase-02.md`

**Follow structure**: Read `specs/phase-02-output.spec.md` for required format

**Generate natural language architecture description** following the spec structure:
- Use context variables from Phase 1
- Be specific to YOUR domain (not generic)
- Include all required sections
- Natural language style (descriptive, not mechanical)

**Length target**: 50-100 lines (detailed enough for Phase 3-5 to implement from)

---

## Step 8: Confirm with Human

Present summary:

```
✅ Architecture designed for [DOMAIN_ROLE_NAME]:

Knowledge Structure:
- [Brief description of hierarchy]
- [Number] main categories

Skills:
- [Number] total ([breakdown by type])
- [Mention any orchestration]

Behaviors:
- [Number] total ([breakdown by priority])
- Key protocols: [list top 2-3]

[If content analyzed]
Content Mapping:
- [Number] folders analyzed
- [Brief mapping plan]

See complete design: output/phase-02.md

Approve and proceed to Phase 3?
```

Wait for human approval.

---

## Completion

```
✅ Phase 2 Complete

Created: output/phase-02.md (architecture design)
Status: Awaiting approval

Human approved? → Proceed to Phase 3
```

---

## Guidance for Agent

### What Makes Good Architecture?

**Knowledge Structure**:
- Mirrors natural domain organization
- Clear hierarchy (2-4 levels typical)
- Logical categories
- All nodes will have parents (plan this now)

**Skills Design**:
- Cover all capabilities from Phase 1
- Realistic about LLM vs rules
- Organized (group related skills)
- Links to governing behaviors clear

**Behaviors Design**:
- Address domain-specific quality/safety
- Communication style defined
- Workflows captured
- Priorities make sense

### What to Avoid

❌ **Generic architecture** - "This could be any domain"  
❌ **Over-complex** - 20 skills, 15 behaviors (too much)  
❌ **Under-specified** - "Some skills needed" (not useful)  
❌ **Missing links** - Behaviors and skills disconnected

### Sweet Spot

✅ **Domain-specific** - Clearly for THIS use case  
✅ **Right-sized** - 3-7 skills, 3-5 behaviors  
✅ **Well-linked** - Clear relationships  
✅ **Detailed enough** - Phase 3-5 can implement from this

---

**Next**: [Phase 3: Project Structure](PHASE_03_PROJECT_STRUCTURE.md)
