# USER_MANUAL Specification

## Purpose

The `USER_MANUAL.md` file is the comprehensive guide for humans working with the AI agent. It explains how to use BOTH roles, activate them, and execute common workflows.

---

## Structure Requirements

### Required Sections

1. **Title & Introduction** - What this manual covers
2. **Magic Activation Prompts** - Quick role activation
3. **Role 1: Agent Builder** - How to use builder (STANDARD)
4. **Role 2: Domain Role** - How to use domain role (CUSTOM)
5. **Common Workflows** - Step-by-step guides (HYBRID)
6. **Troubleshooting** - Common issues (HYBRID)
7. **Advanced Topics** - Deep dives (OPTIONAL)

---

## Section Details

### 1. Title & Introduction

```markdown
# <PROJECT_NAME> User Manual

## Introduction

This manual explains how to work with the AI agent for **<PROJECT_NAME>**.

**Roles Available**:
- **Agent Builder**: System maintenance and validation
- **<DOMAIN_ROLE_NAME>**: <DOMAIN_PURPOSE>
```

**Variables** (from Phase 1):

- `PROJECT_NAME`
- `DOMAIN_ROLE_NAME`
- `DOMAIN_PURPOSE`

---

### 2. Magic Activation Prompts (HYBRID)

Quick prompts to activate each role.

**Builder Activation** (STANDARD):

```markdown
## Magic Activation Prompts

### Activate Agent Builder

> "Switch to Agent Builder role. Validate the system structure and check all Knowledge Graphs for consistency."
```

**Domain Activation** (CUSTOM):

```markdown
### Activate <DOMAIN_ROLE_NAME>

> "Switch to <DOMAIN_ROLE_NAME> role. <DOMAIN_ACTIVATION_INSTRUCTION>"
```

**Variables**:

- `DOMAIN_ROLE_NAME`
- `DOMAIN_ACTIVATION_INSTRUCTION`: What to do when activating domain role

---

### 3. Role 1: Agent Builder (STANDARD)

This section is STANDARD. Copy from reference example.

**Content**:

- What the builder does
- When to use it
- Common builder tasks:
  - Validate system
  - Update Knowledge Graphs
  - Add new skills/behaviors
  - Run health checks

---

### 4. Role 2: Domain Role (CUSTOM)

Generate this section based on Phase 1.

```markdown
## Role 2: The <DOMAIN_ROLE_NAME>

### What It Does
<DOMAIN_ROLE_DESCRIPTION>

### When to Use
- <USE_CASE_1>
- <USE_CASE_2>
- <USE_CASE_3>

### Common Tasks

#### Task 1: <TASK_NAME>
<TASK_DESCRIPTION>

**Steps**:
1. <STEP_1>
2. <STEP_2>
3. <STEP_3>

#### Task 2: <TASK_NAME>
...
```

**Variables** (from Phase 1):

- `DOMAIN_ROLE_NAME`
- `DOMAIN_ROLE_DESCRIPTION`
- `USE_CASE_X`
- `TASK_NAME`, `TASK_DESCRIPTION`, `STEP_X`: Domain-specific workflows

---

### 5. Common Workflows (HYBRID)

Step-by-step guides for common tasks.

**Standard Workflows** (builder):

- How to add a new skill
- How to update a behavior
- How to fix a broken Knowledge Graph
- How to validate the system

**Domain Workflows** (custom):

- Domain-specific processes
- Domain-specific tasks

**Format**:

```markdown
### Workflow: <WORKFLOW_NAME>

**When to use**: <WHEN>

**Steps**:
1. <STEP_1>
2. <STEP_2>
3. <STEP_3>

**Validation**: <HOW_TO_VERIFY>
```

---

### 6. Troubleshooting (HYBRID)

Common issues and solutions.

**Standard Issues** (builder):

- "Validation fails" → Run kg_heal.py
- "Graph not connected" → Check for orphaned nodes
- "File not found" → Check paths in KG

**Domain Issues** (custom):

- Domain-specific problems
- Domain-specific solutions

**Format**:

```markdown
### Problem: <PROBLEM_DESCRIPTION>

**Symptoms**: <WHAT_YOU_SEE>

**Solution**:
1. <SOLUTION_STEP_1>
2. <SOLUTION_STEP_2>
```

---

### 7. Advanced Topics (OPTIONAL)

Deep dives into complex topics:

- Knowledge Graph architecture
- Multi-agent coordination (if applicable)
- Custom skill development
- Domain-specific advanced features

---

## Generation Instructions

1. **Read** reference example: `examples/USER_MANUAL.md`
2. **Extract** variables from Phase 1 output
3. **Generate** fresh file with:
   - Title & intro (use Phase 1 data)
   - Magic prompts (hybrid: standard builder + custom domain)
   - Role 1 section (copy from reference)
   - Role 2 section (generate from Phase 1)
   - Common workflows (hybrid)
   - Troubleshooting (hybrid)
   - Advanced topics (optional)
4. **Validate**: Check all sections present and specific

---

## Validation Criteria

- [ ] File exists at `agents/USER_MANUAL.md` or `agents/USER_MANUAL_<PLATFORM>.md`
- [ ] Contains all required sections
- [ ] Magic activation prompts for BOTH roles
- [ ] Agent Builder section is complete
- [ ] Domain role section is complete and specific
- [ ] At least 3 workflows documented
- [ ] No placeholder text remains
- [ ] Markdown formatting is valid

---

## Common Mistakes to Avoid

❌ **Don't**: Make domain workflows generic  
✅ **Do**: Provide specific, actionable steps

❌ **Don't**: Forget builder workflows  
✅ **Do**: Include standard builder tasks

❌ **Don't**: Copy-paste and replace placeholders  
✅ **Do**: Generate fresh content following this spec

❌ **Don't**: Write for AI agents  
✅ **Do**: Write for HUMANS using the AI agent
