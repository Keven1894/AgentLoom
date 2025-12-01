# Phase 1: Information Discovery

**AI Agent Setup Protocol V3.0**

---

## Objective

Gather project context by checking existing files first, then asking human for missing information.

---

## Instructions

### Step 1: Check for Existing Project

**This might be a V1/V2 upgrade.** Check these locations for existing information:

```
.cursor/identity.md          → Project name, roles, purpose
.cursor/project-registry.json → Domain info (if manager role)
agents/knowledge-graphs/*.json → Existing graphs
docs/                        → Content structure
```

**If files exist**: Extract and use existing information. Note what you found.

**If files don't exist**: This is a fresh build. Proceed to Step 2.

### Step 2: Gather Missing Information

Ask the human for any information NOT found in existing files.

**Required context variables**:

- `PROJECT_NAME`: What is this agent called?
- `DOMAIN_ROLE_NAME`: Primary role name (e.g., "Project Manager", "Code Reviewer")
- `DOMAIN_ROLE_ID`: Kebab-case ID (e.g., "project-manager", "code-reviewer")
- `DOMAIN_ID`: Domain prefix (e.g., "project-mgmt", "code-review")

**Required lists**:

- **Domain concepts**: 3-5 key concepts the agent needs to understand
- **Skills needed**: What should the agent DO? (analyze, validate, generate, etc.)
- **Behaviors/rules**: What protocols must it follow? (safety, confidentiality, workflows)

**Optional**:

- Existing content folders to analyze (use @ mention)
- Integration requirements (APIs, tools, scripts)

### Step 3: Confirm with Human

Present what you gathered/found:

```
Found existing project: [Yes/No]

Context Variables:
- PROJECT_NAME: [value]
- DOMAIN_ROLE_NAME: [value]
- DOMAIN_ROLE_ID: [value]
- DOMAIN_ID: [value]

Domain Concepts: [list]
Skills: [list]
Behaviors: [list]

[If content folders provided]
Content Analysis:
- Folders: [paths]
- Structure: [description]
- File count: ~[number]

Is this correct? Proceed to Phase 2?
```

Wait for confirmation.

### Step 4: Write Output Summary

Create `output/phase-01.md` with gathered information (10-20 lines, readable format).

Include:

- All context variables
- Domain concepts list
- Skills list
- Behaviors list
- Content folder info (if any)
- Source (existing files vs human input)

---

## Completion

```
✅ Phase 1 Complete
See output/phase-01.md for context variables and requirements.
Proceed to Phase 2?
```

---

**Next**: [Phase 2: Architecture Design](PHASE_02_ARCHITECTURE_DESIGN.md)
