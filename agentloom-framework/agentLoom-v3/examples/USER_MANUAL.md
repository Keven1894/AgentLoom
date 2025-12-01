# Agentic AI Project Manager - User Manual (Antigravity Edition)

**Version**: 2.0 (Antigravity)
**Last Updated**: 2025-11-26
**Purpose**: Enable Antigravity agent instances to become operational in < 5 minutes

---

## Table of Contents

1. [Quick Start Guide](#1-quick-start-guide)
2. [Knowledge Graph Navigation](#2-knowledge-graph-navigation)
3. [Role-Specific Workflows](#3-role-specific-workflows)
4. [Key Behaviors & Protocols](#4-key-behaviors--protocols)
5. [Skills Activation](#5-skills-activation)
6. [Troubleshooting & Common Tasks](#6-troubleshooting--common-tasks)

---

## 1. Quick Start (Copy & Paste This Prompt)

```text
Initialize as the Agentic AI Project Manager.

Start by reading:
@agents/NEW_AGENT_START_HERE.md

Follow every step inside that file:
- Load identity
- Load master knowledge graph
- Ask for role selection
- Load all role-specific knowledge, skills, and behaviors
- Confirm operational state

Do not ask the user to do any manual loading; you must perform all loading steps yourself.
When finished, output: “System Ready”.
```

That’s it. Everything else in this manual is for reference, troubleshooting, and advanced usage.

## 2. Knowledge Graph Navigation

### What is the Knowledge Graph?

The KG is your "Mind GPS" - a network of JSON files organizing all system knowledge, behaviors, and skills into an interconnected structure.

### Graph Types

1. **master-graph.json**: Entry point linking all other graphs
2. **project-graph.json**: All managed projects and their documents
3. **[role]-knowledge-graph.json**: Role-specific understanding of system
4. **[role]-skills-graph.json**: Role capabilities and skill trees
5. **[role]-behaviors-graph.json**: Role protocols and rules

### 🪄 Prompt: Navigate the Graph

To explore the Knowledge Graph, use this prompt:

```text
Summarize the Master Knowledge Graph structure.
Then, find the node for [TOPIC] and explain its relationships.
```

### Visualization Tool

Open `agents/knowledge-graphs/visualization.html` in a browser to see the "Unified Brain" view.

---

## 3. Role-Specific Workflows

### Agent Builder Workflows

**Primary Responsibilities**:

- System validation and health checks
- Knowledge Graph maintenance
- Skill and behavior creation/updates
- Enforcing system integrity

#### Workflow: Validate System Health

**When**: On request, after major changes, weekly check

**🪄 Prompt**:

```text
Run a full system health check using the validation scripts.
Report any structure violations or graph inconsistencies.
```

#### Workflow: Maintain Knowledge Graph

**When**: New files added, files moved/deleted, structure changed

**🪄 Prompt**:

```text
Activate the Knowledge Graph Maintenance skill.
Scan for file system changes and update the JSON graphs accordingly.
Ensure no orphaned nodes remain.
```

#### Workflow: Add New Behavior

**When**: User requests new rule or protocol

**🪄 Prompt**:

```text
I want to add a new behavior for [CATEGORY].
Please guide me through creating the file and indexing it in the Knowledge Graph.
```

### Project Manager Workflows

**Primary Responsibilities**:

- Project tracking and registry maintenance
- Cross-project insight generation
- Respecting confidentiality boundaries
- Status reporting

#### Workflow: Add New Project

**When**: User clones a new project into public/, personal/, or work/

**🪄 Prompt**:

```text
I want to add a new project.
Ask me for the details (name, category, description) and register it in the system.
Then update the project graph.
```

#### Workflow: Generate Cross-Project Insights

**When**: User requests analysis, monthly review, pattern detection

**🪄 Prompt**:

```text
Generate cross-project insights for [CATEGORY] projects.
Analyze documents for patterns and synergies, then create a summary report.
```

**Confidentiality Rule**: NEVER mix work/ data with public/personal insights!

---

## 4. Key Behaviors & Protocols

**🪄 Prompt**:

```text
Review the [PROTOCOL_NAME] protocol and explain how it applies to my current task.
```

### Core Behaviors (All Roles)

- **System Safety**: `behavior:core:safety`
- **Confidentiality**: `behavior:core:confidentiality`
- **Project Structure**: `behavior:core:project-structure`
- **Git Workflow**: `/git_workflow`

### Agent Builder Behaviors

- **Schema Integrity**: `behavior:builder:schema`
- **Graph Consistency**: `behavior:builder:consistency`

### Project Manager Behaviors

- **Project Management**: `behavior:manager:mgmt`
- **Insight Generation**: `behavior:manager:insight`

---

## 5. Skills Activation

**🪄 Prompt**:

```text
List all available skills for my current role.
Then, activate the [SKILL_NAME] skill.
```

### Skill Categories

#### System Skills (Builder)

- `skill-validate-structure`
- `skill-validate-graphs`
- `skill-maintain-kg`

#### Orchestration Skills (Manager)

- `skill-scan-repos`
- `skill-update-registry`

### Antigravity Workflows

**🪄 Prompt**:

```text
Run the Git Workflow to sync my changes.
```

- **Git Workflow**: `/git_workflow`

---

## 6. Troubleshooting & Common Tasks

### Problem: Graph Inconsistency Detected

**🪄 Prompt**:

```text
Diagnose and heal the Knowledge Graph.
Identify any orphaned nodes or broken links and propose fixes.
```

### Problem: Role Confusion

**🪄 Prompt**:

```text
Clarify my current role and responsibilities.

```
