# Phase 8: Generate User Manual

**AI Agent Setup Protocol V3.0**

---

## Objective

Generate two paired documentation files:

1. **NEW_AGENT_START_HERE.md** - Agent reads this to initialize (agent-facing)
2. **USER_MANUAL.md** - User reads this for reference (human-facing)

Together they enable < 5 minutes startup.

---

## Step 1: Load Context

Read all previous phase outputs (`output/`):

```
From Phase 1 (output/phase-01.md):
- Get [PROJECT_NAME], [DOMAIN_ROLE_NAME], [DOMAIN_ROLE_ID]

From Phase 2 (output/phase-02.md):
- Architecture overview

From Phase 5 (output/phase-05.md):
- Knowledge content summary

From Phase 6 (output/phase-06.md):
- Skills summary

From Phase 7 (output/phase-07.md):
- Behaviors summary
- Culture/communication style
```

---

## Step 2: Generate NEW_AGENT_START_HERE.md

**Read**:

- `specs/start-here-structure.spec.md`
- `examples/NEW_AGENT_START_HERE.md`
- All phase outputs (context)

**Generate**: `agents/NEW_AGENT_START_HERE.md`

**Key Points**:

- Follow the 9-section structure from spec
- Customize with Phase 1 variables ([PROJECT_NAME], [DOMAIN_ROLE_NAME], [DOMAIN_ROLE_ID])
- Include clear initialization steps for the agent

---

## Step 3: Generate USER_MANUAL.md

**Read**:

- `examples/USER_MANUAL.md` (see pattern)
- `specs/user-manual-structure.spec.md` (requirements)
- All phase outputs (context)

**Generate**: `agents/USER_MANUAL.md`

**Key Points**:

- **Magic activation prompt**: The most important part - enables < 5 minutes startup
- **Workflow prompts**: Use 🪄 emoji to mark copy-paste prompts
- **Domain-specific**: Customize workflows based on Phase 6 skills and Phase 7 behaviors
- **Visualization**: Include simple instructions (python -m http.server)
- **Reference structure**: Follow `specs/user-manual-structure.spec.md` for all required sections

---

## Step 4: Generate VIEW_VISUALIZATION.md (Optional)

**If domain has complex KG**, create visualization guide:

**Create**: `agents/knowledge-graphs/VIEW_VISUALIZATION.md`

**Content**:

- How to start local server based on user's OS (python -m http.server 8000 is recommended)
- How to use visualization tool
- What each view shows
- Node colors and shapes legend
- Validation checklist

**If domain is simple**, skip this file.

---

## Step 5: Write Output Summary

**Create**: `output/phase-08.md`

Document what was generated:

- Path to NEW_AGENT_START_HERE.md
- Path to USER_MANUAL.md
- Path to VIEW_VISUALIZATION.md (if created)
- Confirmation that agent is ready for use

---

## Success Criteria

- [ ] NEW_AGENT_START_HERE.md exists with all 9 sections
- [ ] USER_MANUAL.md exists with magic activation prompt
- [ ] Both files reference correct paths and variables
- [ ] Visualization instructions are clear and OS-appropriate
- [ ] Agent can initialize in < 5 minutes using the magic prompt

---

**Next**: Agent is ready! Deploy and gather feedback for refinement.
