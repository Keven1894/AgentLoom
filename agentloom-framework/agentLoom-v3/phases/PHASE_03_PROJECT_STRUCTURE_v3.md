# Phase 3: Project Structure

**AI Agent Setup Protocol V3.0**

---

## Objective

Build complete project structure: copy builder-assets, create domain folders, generate placeholders, generate hybrid files.

---

## Step 1: Load Context

Read `output/phase-01.md` and `output/phase-02.md`:

```
PROJECT_NAME = [value]
DOMAIN_ROLE_ID = [value]
DOMAIN_ID = [value]

From Phase 2:
- Skills list (names and types)
- Behaviors list (names and priorities)
- KG structure (categories and hierarchy)
- Content folders analyzed (if any)
```

---

## Step 2: Copy Builder Assets

**Copy all files** from `builder-assets/` to project root, maintaining folder structure:

**From** `builder-assets/.cursor/behaviors/` **to** `.cursor/behaviors/`
**From** `builder-assets/agents/skills/system/` **to** `agents/skills/system/`
**From** `builder-assets/agents/knowledge-graphs/` **to** `agents/knowledge-graphs/` (only builder-*.json files)
**From** `builder-assets/agents/visualization-dynamic.html` **to** `agents/visualization-dynamic.html`
**From** `builder-assets/docs/general/` **to** `docs/general/`
**From** `builder-assets/scripts/` **to** `scripts/`

**Result**: Creates foundation structure with all Agent Builder components.

---

## Step 3: Create Domain Role Folders

Based on `DOMAIN_ROLE_ID` from Phase 1, **create these folders**:

- `.cursor/behaviors/[DOMAIN_ROLE_ID]/` (for domain behaviors)
- `agents/skills/[DOMAIN_ROLE_ID]/` (for domain skills)
- `docs/[DOMAIN_ROLE_ID]/` (for domain knowledge)

---

## Step 4: Create Knowledge Subfolders

**Think**: Based on Phase 2 KG structure, what knowledge categories exist?

**For each main category** in Phase 2 KG design, **create subfolder** under `docs/[DOMAIN_ROLE_ID]/`:

**Example thinking** (adapt to YOUR Phase 2):

- Phase 2 has "Course Materials" category → Create `docs/tutor/course-materials/`
- Phase 2 has "Standards" category → Create `docs/curator/standards/`
- Phase 2 has "Projects" category → Create `docs/manager/projects/`

**Create subfolders** matching Phase 2 hierarchy (2-3 levels typical).

---

## Step 5: Create Domain-Specific Folders

**Think**: Does this domain need special folders for content organization?

**Ask yourself**:

- Does domain manage different types of items? (projects, datasets, cases, courses, etc.)
- Are there confidentiality boundaries? (public vs private content)
- Any workflow stages? (drafts, published, archived)

**Create folders** based on domain needs.

**Examples by domain type**:

- Project Manager: `public/`, `personal/`, `work/` (project categories)
- Tutor: `courses/`, `students/` (educational content)
- Legal: `cases/`, `contracts/` (legal documents)
- Curator: `datasets/`, `metadata/` (data management)

**Note**: Only create folders that make sense for THIS domain. Don't copy generic patterns.

---

## Step 6: Create Skill Placeholders

For **each skill** from Phase 2 architecture:

**Create file**: `agents/skills/[DOMAIN_ROLE_ID]/[skill-name].md`

**Content** (frontmatter only):

```markdown
---
type: skill
category: [DOMAIN_ROLE_ID]
id: [skill-id]
roles:
  - role-[DOMAIN_ROLE_ID]
---

# [Skill Name]

[Content will be generated in Phase 5]
```

**Repeat** for all skills in Phase 2 design.

---

## Step 7: Create Behavior Placeholders

For **each behavior** from Phase 2 architecture:

**Create file**: `.cursor/behaviors/[DOMAIN_ROLE_ID]/[behavior-name].md`

**Content** (frontmatter only):

```markdown
---
type: behavior
category: [DOMAIN_ROLE_ID]
id: [behavior-id]
priority: [critical|high|medium]
roles:
  - role-[DOMAIN_ROLE_ID]
---

# [Behavior Name]

[Content will be generated in Phase 5]
```

**Repeat** for all behaviors in Phase 2 design.

---

## Step 8: Generate Hybrid Files

**Generate these 3 files** using specs + examples + context:

### 8.1: Generate `.cursor/identity.md`

**Read**:

- `builder-assets/examples/identity.md` (see pattern)
- `specs/identity-structure.spec.md` (requirements)
- `output/phase-01.md` (context variables)

**Generate** fresh file with:

- Role 1 (Agent Builder): Use description from example
- Role 2 (Domain Role): Generate from Phase 1 data
- All required sections

### 8.2: Generate `.cursor/rules.md`

**Read**:

- `specs/rules-structure.spec.md` (if exists, or use simple structure)
- `output/phase-01.md` and `output/phase-02.md`

**Generate** with project-specific rules.

### 8.3: Generate `agents/NEW_AGENT_START_HERE.md`

**Read**:

- `builder-assets/examples/NEW_AGENT_START_HERE.md` (see pattern)
- `specs/start-here-structure.spec.md` (requirements)
- `output/phase-01.md` and `output/phase-02.md`

**Generate** fresh file with:

- Welcome with PROJECT_NAME
- Quick start checklist
- Role 1 guide (from example)
- Role 2 guide (from Phase 1/2)
- File locations

---

## Step 9: Write Output Summary

**Create**: `output/phase-03.md`

**Follow structure**: Read `specs/phase-03-output.spec.md` for required format

**Generate natural language summary** following the spec:

- What was copied (from builder-assets)
- What folders were created (with reasoning)
- What placeholders were created (counts and names)
- What files were generated
- Validation status

**Length target**: 30-50 lines

---

## Step 10: Validate Structure

**Run validation script** in scripts/buildervalidate_structure.py to check structure is complete.

**Expected**: All required folders and files present.

---

## Step 11: Confirm with Human

Present summary:

```
✅ Project structure created:

Copied: builder-assets ([X] files)
Created: [Y] domain folders
Created: [Z] skill placeholders
Created: [W] behavior placeholders
Generated: 3 hybrid files

Structure validated: [✅ Pass / ❌ Issues]

See: output/phase-03.md

Proceed to Phase 4 (Knowledge Graphs)?
```

Wait for approval.

---

## Completion

```
✅ Phase 3 Complete

Structure: 100% built
Placeholders: Ready for Phase 5
Hybrid files: Generated
Validation: Passed

Next: Phase 4 (Knowledge Graph Generation)
```

---

**Next**: [Phase 4: Knowledge Graphs](PHASE_04_KNOWLEDGE_GRAPHS.md)
