# Protocol Document Templates

This directory contains reusable markdown document templates for the AI Agent Setup Protocol V2.0.

## Directory Structure

```
docs-templates/
├── README.md
├── NEW_AGENT_START_HERE.md.template
├── USER_MANUAL.md.template
├── TEST_PROTOCOL.md.template
├── CONTENT_TEMPLATE.md.template
└── behavior-file.md.template
```

## Templates

### `NEW_AGENT_START_HERE.md.template`

**Purpose**: Machine-executable startup script for fresh agent instances
**Used in**: Phase 11, Action 11.1
**Reusability**: Template - Requires customization

**Customization Required**:

1. Replace `[Domain Role Name]` with your domain role name (lines 31, 53, 70, 147)
2. Replace `[domain-role-id]` with your domain role ID (lines 70-72, 147)
3. Replace `[domain]` with your domain graph ID (line 77)

**Size**: ~180 lines

**Features**:

- 7-step initialization process
- Agent Builder + Domain Role architecture
- Operational boundaries
- Reference card with bookmarks
- Emergency procedures

---

### `USER_MANUAL.md.template`

**Purpose**: Comprehensive prompt library for agent users
**Used in**: Phase 11, Action 11.2
**Reusability**: Template - Requires customization

**Customization Required**:

1. Replace `[Agent Name]` with your agent name (lines 1, 12)
2. Replace `[Date]` with creation date (line 4)
3. Replace `[Domain Role Name]` with your domain role name (lines 39, 53, etc.)
4. Replace `[TOPIC]`, `[SKILL_NAME]`, `[BEHAVIOR_NAME]` placeholders with actual values
5. Add domain-specific workflows in section "📋 [Domain Role Name] Workflows"

**Size**: ~280 lines

**Features**:

- Magic activation prompt
- Two-role system explanation
- Comprehensive prompt library
- Agent Builder workflows (KG maintenance)
- Domain Role workflows (customizable)
- Troubleshooting section
- Visualization guide
- Advanced usage examples

---

### `TEST_PROTOCOL.md.template`

**Purpose**: Cold-start testing framework
**Used in**: Phase 11, Action 11.3
**Reusability**: 100% - No customization needed

**Size**: ~120 lines

**Features**:

- Detailed test procedure
- Success criteria checklist
- Failure scenarios
- Test log template
- Pain points documentation
- Improvements tracking

---

### `CONTENT_TEMPLATE.md.template`

**Purpose**: General-purpose documentation template
**Used in**: Phase 5, Action 5.1
**Reusability**: 100% - No customization needed

**Size**: ~60 lines

**Features**:

- YAML frontmatter with metadata
- Standard sections (Overview, Key Concepts, Content, Examples)
- Troubleshooting section
- Related resources
- KG indexing reference

**Usage in Phase 5**:

```bash
# Copy to project (no customization needed)
cp [protocol-path]/docs-templates/CONTENT_TEMPLATE.md.template docs/general/CONTENT_TEMPLATE.md
```

---

### `behavior-file.md.template`

**Purpose**: Standard structure for all behavior files
**Used in**: Phase 5, Actions 5.2 and 5.3
**Reusability**: Template - Requires customization

**Size**: ~70 lines

**Customization Required**:

1. Replace `[behavior-id]`, `[Behavior Name]`, descriptions
2. Set `category` (core | agent-builder | domain-role-id)
3. Set `applies-to` (all-roles | agent-builder | domain-role-id)
4. Add specific rules and examples

**Features**:

- YAML frontmatter with metadata
- Description and context
- Rules with examples
- Good/bad practice examples
- Related components (skills, knowledge)
- Validation checklist

**Usage in Phase 5**:

```bash
# Copy for each behavior
cp [protocol-path]/docs-templates/behavior-file.md.template \
   .cursor/behaviors/[category]/[behavior-id].md

# Then customize placeholders
```

---

## How to Use in Protocol

### Phase 11 (User Manual & Testing)

**Action 11.1: Create NEW_AGENT_START_HERE.md**

```bash
# Copy template
cp [protocol-path]/docs-templates/NEW_AGENT_START_HERE.md.template agents/NEW_AGENT_START_HERE.md

# Customize placeholders
# Edit agents/NEW_AGENT_START_HERE.md
```

**Action 11.2: Create USER_MANUAL.md**

```bash
# Copy template
cp [protocol-path]/docs-templates/USER_MANUAL.md.template agents/USER_MANUAL.md

# Customize placeholders and add domain workflows
# Edit agents/USER_MANUAL.md
```

**Action 11.3: Create TEST_PROTOCOL.md**

```bash
# Copy template (no customization needed)
cp [protocol-path]/docs-templates/TEST_PROTOCOL.md.template temp/user_manual_test/TEST_PROTOCOL.md
```

---

## Template Rigidity Levels

Understanding when to use templates vs generate custom content:

### ⭐⭐⭐⭐ **LEVEL 2: RECOMMENDED (Copy and Adapt)**

**These templates should be copied and customized**:

**Machine-Executable**:
- ✅ `NEW_AGENT_START_HERE.md.template` - Startup script with specific steps
- ✅ `TEST_PROTOCOL.md.template` - Testing framework with checklists

**User-Facing**:
- ✅ `USER_MANUAL.md.template` - Prompt library structure

**Why RECOMMENDED**:
- 📋 **Ensures completeness**: Won't forget important sections
- 📋 **Proven structure**: Battle-tested organization
- 📋 **Consistency**: Similar experience across projects
- 📋 **Time-saving**: Faster than generating from scratch

**When to adapt**:
- ✅ Add domain-specific workflows to USER_MANUAL.md
- ✅ Customize role names and IDs
- ✅ Adjust sections based on project needs

**Agent has flexibility**: High - customize content, keep structure

---

### ⭐⭐⭐ **LEVEL 3: OPTIONAL GUIDE (Use as Reference)**

**These templates show best practices but can be generated**:

- ⚠️ `CONTENT_TEMPLATE.md.template` - Documentation structure guide
- ⚠️ `behavior-file.md.template` - Behavior file structure guide

**Why OPTIONAL**:
- 💡 **Agent is capable**: LLMs excel at markdown documentation
- 💡 **Project-specific**: Different projects need different structures
- 💡 **Guide not constraint**: Shows pattern, agent adapts

**When to use template**:
- ✅ First time building an agent (learn the pattern)
- ✅ Want consistency across many files
- ✅ Prefer structured approach

**When to generate custom**:
- ✅ Experienced with the protocol
- ✅ Need unique structure for complex workflows
- ✅ Agent understands requirements clearly

**Agent decision**: Can choose template or generate based on complexity

---

## Decision Framework

**When should agent use a template vs generate?**

```
START
  ↓
Is it JSON or code? ──YES→ USE TEMPLATE (Level 1 or 2)
  ↓ NO
Is it standardized (Agent Builder)? ──YES→ USE TEMPLATE (Level 1)
  ↓ NO
Is it user-facing docs? ──YES→ RECOMMENDED template (Level 2)
  ↓ NO
Is it summary/report? ──YES→ GENERATE custom (Level 3)
  ↓
DEFAULT: Use template as GUIDE, adapt as needed
```

## Benefits

- ✅ **Separation of concerns**: Templates separate from phase instructions
- ✅ **Reusability**: Copy tested templates instead of writing from scratch
- ✅ **Consistency**: All projects use same structure (where appropriate)
- ✅ **Maintainability**: Improve templates in one place
- ✅ **Clarity**: Phases focus on what to do, not full content
- ✅ **Flexibility**: Agent can adapt templates or generate custom based on needs

---

## Version

**Protocol Version**: 2.0
**Last Updated**: November 28, 2025
