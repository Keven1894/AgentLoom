# NEW_AGENT_START_HERE Specification

## Purpose

The `NEW_AGENT_START_HERE.md` file is the onboarding document for new AI agents working on this project. It explains BOTH roles (Agent Builder + Domain Role), the system architecture, and how to get started.

---

## Structure Requirements

### Required Sections

1. **Welcome Header** - Project introduction
2. **Quick Start** - Immediate action items
3. **System Overview** - Architecture explanation
4. **Role 1: Agent Builder** - Builder role guide (STANDARD)
5. **Role 2: Domain Role** - Domain role guide (CUSTOM)
6. **Knowledge Graphs** - How to use KGs
7. **Key Files** - Important file locations
8. **Workflows** - Common tasks
9. **Validation** - How to verify work

---

## Section Details

### 1. Welcome Header

```markdown
# Welcome to <PROJECT_NAME>

You are an AI agent working on the **<PROJECT_NAME>** project.

**Domain**: <DOMAIN_DESCRIPTION>  
**Your Roles**: Agent Builder + <DOMAIN_ROLE_NAME>
```

**Variables** (from Phase 1):

- `PROJECT_NAME`
- `DOMAIN_DESCRIPTION`
- `DOMAIN_ROLE_NAME`

---

### 2. Quick Start

Standard checklist (mostly reusable):

```markdown
## Quick Start

Before you begin:
1. Read `.cursor/identity.md` to understand your roles
2. Check `agents/knowledge-graphs/master-graph.json` for system structure
3. Review this document for workflows
4. Run validation: `python scripts/validate_graphs.py`
```

---

### 3. System Overview

Explain the dual-role architecture (STANDARD):

```markdown
## System Overview

This project uses a **dual-role agentic architecture**:

- **Agent Builder**: Maintains the system itself (structure, KGs, validation)
- **<DOMAIN_ROLE_NAME>**: Performs domain-specific work

You can switch between roles based on the task.
```

**Variable**: `DOMAIN_ROLE_NAME`

---

### 4. Role 1: Agent Builder (STANDARD)

This section is STANDARD across all projects. Copy from reference example.

**Content**:

- What the builder role does
- When to use it
- Key capabilities (validate, maintain KG, update structure)
- Important files for builder role

---

### 5. Role 2: Domain Role (CUSTOM)

Generate this section based on Phase 1 domain role definition.

```markdown
## Role 2: The <DOMAIN_ROLE_NAME>

### Purpose
<DOMAIN_ROLE_PURPOSE>

### When to Use This Role
- <USE_CASE_1>
- <USE_CASE_2>
- <USE_CASE_3>

### Key Capabilities
- <CAPABILITY_1>
- <CAPABILITY_2>
- <CAPABILITY_3>

### Important Files
- `<DOMAIN_SPECIFIC_FILE_1>`
- `<DOMAIN_SPECIFIC_FILE_2>`
```

**Variables** (from Phase 1):

- `DOMAIN_ROLE_NAME`
- `DOMAIN_ROLE_PURPOSE`
- `USE_CASE_X`: When to use domain role
- `CAPABILITY_X`: Domain skills
- `DOMAIN_SPECIFIC_FILE_X`: Key domain files

---

### 6. Knowledge Graphs

Explain the KG system (HYBRID):

**Standard part** (builder KGs):

```markdown
## Knowledge Graphs

### Builder Graphs
- `builder-knowledge-graph.json` - System architecture
- `builder-skills-graph.json` - Builder capabilities
- `builder-behaviors-graph.json` - Builder protocols
```

**Custom part** (domain KGs):

```markdown
### <DOMAIN_ROLE_NAME> Graphs
- `<DOMAIN_ROLE_ID>-knowledge-graph.json` - <DESCRIPTION>
- `<DOMAIN_ROLE_ID>-skills-graph.json` - <DESCRIPTION>
- `<DOMAIN_ROLE_ID>-behaviors-graph.json` - <DESCRIPTION>
```

---

### 7. Key Files

List important files by category (HYBRID):

**Standard files** (always include):

- `.cursor/identity.md`
- `.cursor/project-registry.json` (if applicable)
- `agents/knowledge-graphs/master-graph.json`
- `scripts/validate_graphs.py`

**Domain files** (custom):

- Domain-specific configuration files
- Domain data files
- Domain documentation

---

### 8. Workflows

Common workflows (HYBRID):

**Standard workflows** (builder):

- How to add a new skill
- How to update a behavior
- How to validate the system

**Domain workflows** (custom):

- Domain-specific tasks
- Domain-specific processes

---

### 9. Validation

How to verify work (STANDARD):

```markdown
## Validation

Always validate your work:

```bash
# Validate structure
python scripts/validate_structure.py

# Validate graphs
python scripts/validate_graphs.py

# Check connectivity
python scripts/kg_heal.py
```

```

---

## Generation Instructions

1. **Read** reference example: `examples/NEW_AGENT_START_HERE.md`
2. **Extract** variables from Phase 1 output
3. **Generate** fresh file with:
   - Welcome header (use Phase 1 data)
   - Quick start (standard)
   - System overview (standard)
   - Role 1 section (copy from reference)
   - Role 2 section (generate from Phase 1)
   - Knowledge graphs (hybrid)
   - Key files (hybrid)
   - Workflows (hybrid)
   - Validation (standard)
4. **Validate**: Check all sections present

---

## Validation Criteria

- [ ] File exists at `agents/NEW_AGENT_START_HERE.md`
- [ ] Contains all 9 required sections
- [ ] Agent Builder role section is complete
- [ ] Domain role section is complete and specific
- [ ] No placeholder text remains
- [ ] Markdown formatting is valid
- [ ] Links to files are correct

---

## Common Mistakes to Avoid

❌ **Don't**: Make domain role section generic  
✅ **Do**: Use specific details from Phase 1

❌ **Don't**: Forget the builder role section  
✅ **Do**: Include complete builder guide

❌ **Don't**: Copy-paste and replace placeholders  
✅ **Do**: Generate fresh content following this spec
