# AI Agent Setup Protocol V2.0 - PART 1

## Phases 1-3: Discovery, Architecture, Project Structure

**Version**: 2.0  
**Target Audience**: AI Assistants  
**Purpose**: Execute Phases 1-3 of the protocol

---

## Model Requirements

**Recommended**: Claude Sonnet 4.5+, GPT-5+  
**Minimum**: Claude Sonnet 3.5, GPT-4 Turbo

**Note**: See README for detailed model comparisons, costs, and optimization strategies.

---

## Prerequisites

Before starting, ensure you have:

- [ ] Access to file creation tools
- [ ] Ability to run Python scripts
- [ ] Understanding of JSON structure
- [ ] Git repository initialized (recommended)
- [ ] Appropriate AI model (see requirements above)

---

## Phase 1: Information Discovery

*[Keep Phase 1 from V1.0 - no changes needed]*

### Objective

Gather all necessary information before creating any files.

### Required Input from Human

Ask these questions **in order**. Do not proceed until you have clear answers:

#### Question Set 1: Domain & Purpose

```
I'll help you build a structured AI agent system. First, I need to understand your domain:

1. What domain is your agent working in? (e.g., Education, Healthcare, Legal, Software Development)
2. What is the primary purpose of the agent? What problems will it solve?
3. Who are the end users?
```

Wait for response. Record answers.

#### Question Set 2: Agent Roles

```
How many distinct roles will your agent have? (e.g., 2 roles like "Agent Builder" and "Project Manager")

For each role, I need:
- Role ID (lowercase-hyphenated, e.g., "role-builder")
- Role name (display name)
- Personality (formal/casual/empathetic/technical)
- 3-5 primary tasks
- Communication style
- Key boundaries (what it won't do)

Let's define role 1 first: [Ask about each attribute]
```

Wait for response. Record answers for each role.

#### Question Set 3: Knowledge Requirements

```
What knowledge will your agent need to access?

1. What content types? (projects, documentation, policies, etc.)
2. What are the sources? (Git repos, PDFs, databases, APIs, websites)
3. How is it organized? (by category, module, feature, etc.)
4. Approximately how much content? (10 projects, 100 documents, etc.)
```

Wait for response. Record answers.

#### Question Set 4: Skills & Tools

```
What capabilities and tools will your agent need?

1. What should it be able to DO? (analyze, validate, generate, orchestrate, etc.)
2. Are there existing tools to integrate? (scripts, APIs, databases)
3. Any domain-specific skills? (code review, project analysis, graph maintenance)
4. Which skills need LLM reasoning vs rule-based execution?
```

Wait for response. Record answers.

#### Question Set 5: Workflows & Standards

```
What rules and workflows must your agent follow?

1. Any mandatory workflows? (multi-step processes that must be followed)
2. Any standards to enforce? (style guides, schemas, policies)
3. Any safety boundaries? (what must never happen)
4. Any confidentiality requirements? (data separation rules)
```

Wait for response. Record answers.

### Validation Checkpoint

Before proceeding, confirm:

```
Let me confirm what I've gathered:

**Domain**: [domain]
**Purpose**: [purpose]
**Users**: [users]

**Roles** ([N] total):
1. [Role 1 ID]: [Role 1 name] - [brief description]
2. [Role 2 ID]: [Role 2 name] - [brief description]

**Knowledge Areas**: [list]
**Key Skills**: [list]
**Critical Workflows**: [list]

Is this correct? Should I proceed with setup?
```

Wait for confirmation.

---

## Phase 2: Architecture Design

### Objective

Design the complete system architecture including behavior taxonomy, knowledge structure, skills classification, and **KG connectivity patterns**.

### Actions

#### Action 2.1: Design Behavior Taxonomy

Based on gathered information, create a structured list:

**Core Behaviors** (apply to all roles):

- Safety protocols (data protection, destructive action confirmation)
- Communication standards (how agent responds, error handling)
- System integrity (validation before changes)
- [Add 2-5 more based on Phase 1 answers]

**Role-Specific Behaviors** (for each role):

- Role 1 behaviors (3-5 items based on role responsibilities)
- Role 2 behaviors (3-5 items based on role responsibilities)

**Workflow Behaviors**:

- Multi-step processes that must be followed in order
- Orchestration patterns (when to chain behaviors/skills)

Present to human:

```
I've designed the behavior system:

**Core Behaviors** (all roles):
1. System Safety Protocol - Never delete data without confirmation
2. Communication Protocol - Clear, structured responses
3. [Continue with 3-8 more]

**[Role 1 Name] Behaviors**:
1. [Behavior 1] - [Description]
2. [Behavior 2] - [Description]
[Continue with 3-5 total]

**[Role 2 Name] Behaviors**:
1. [Behavior 1] - [Description]
[Continue with 3-5 total]

**Critical Workflows**:
1. [Workflow name]: [Step 1] → [Step 2] → [Step 3]

Should I proceed with this structure?
```

#### Action 2.2: Design Knowledge Graph Structure (V2: FULLY CONNECTED)

**Critical V2 Addition**: Design for full connectivity from the start.

Based on knowledge requirements, design the graph with:

**Root Node Strategy**:

- Each graph MUST have a root node
- All top-level nodes MUST have `parent` field pointing to root
- All child nodes MUST have `parent` field pointing to their parent

**Cross-Graph Links Strategy**:

- Identify semantic relationships between tracks (Behaviors ↔ Skills ↔ Knowledge)
- Use `links` field with relationship types: `governs`, `enforces`, `implements`, `tracks`, etc.

**Example Structure**:

```
Master Graph (Entry Point)
├── Role 1 (Builder)
│   ├── Builder Knowledge Graph
│   │   ├── sys:root (ROOT NODE)
│   │   ├── sys:agents (parent: sys:root)
│   │   ├── sys:config (parent: sys:root)
│   │   ├── sys:docs (parent: sys:root)
│   │   │   ├── sys:docs:general (parent: sys:docs)
│   │   │   └── sys:docs:builder (parent: sys:docs)
│   │   │       ├── sys:docs:builder:arch (parent: sys:docs:builder)
│   │   │       │   └── [document nodes] (parent: sys:docs:builder:arch)
│   │   └── [concepts]
│   ├── Builder Skills Graph
│   │   ├── skill:builder:root (ROOT NODE)
│   │   ├── skill-validate-structure (parent: skill:builder:root)
│   │   └── skill-maintain-kg (parent: skill:builder:root)
│   │       ├── skill-kg-monitor (parent: skill-maintain-kg)
│   │       ├── skill-kg-update (parent: skill-maintain-kg)
│   │       └── skill-kg-heal (parent: skill-maintain-kg)
│   └── Builder Behaviors Graph
│       ├── behavior:builder:root (ROOT NODE)
│       ├── behavior:core:safety (parent: behavior:builder:root)
│       └── behavior:builder:consistency (parent: behavior:builder:root, links: {enforces: [skill-maintain-kg]})
└── Role 2 (Manager)
    └── [Similar structure]
```

Present structure:

```
Knowledge Graph Architecture (V2 - Fully Connected):

**Connectivity Rules**:
1. Every graph has a root node
2. Every node (except root) has a parent
3. Cross-graph relationships use 'links' field

**Structure**:
Root
├── [Domain Knowledge]
│   ├── [Category 1] (parent: root)
│   │   ├── [Subcategory 1.1] (parent: Category 1)
│   │   │   └── [Document 1.1.1] (parent: Subcategory 1.1)
│   └── [Category 2] (parent: root)
├── [Role 1 Knowledge] (parent: root)
│   ├── [Component 1] (parent: Role 1 Knowledge)
│   └── [Concept 1] (parent: Role 1 Knowledge)

**Cross-Graph Links** (dashed amber lines in visualization):
- Behavior:consistency --enforces--> Skill:maintain-kg
- Skill:validate --implements--> Behavior:schema
- Knowledge:docs --tracked_by--> Knowledge:registry

Proceed with this architecture?
```

#### Action 2.3: Design Skills Taxonomy with Implementation Classification (V2 NEW)

**V2 Addition**: Classify each skill by implementation type upfront.

For each skill identified in Phase 1, determine:

1. **Rule-Based**: Deterministic, file operations, schema validation
   - Tool: Python script, shell command, MCP tool
   - Example: File validation, JSON parsing, directory scanning

2. **LLM-Based**: Natural language, reasoning, context interpretation
   - **Tier 1 (Max)**: Complex reasoning, architecture decisions (Claude Sonnet 4.5+)
   - **Tier 2 (SLM)**: Pattern recognition, simple summarization (Llama 3.1 8B)
   - Example: Insight generation, cross-project analysis

3. **Hybrid**: Rule preprocessing → LLM reasoning → Rule validation
   - Tools: Orchestration script + LLM API + validation script
   - Example: KG update (scan files → LLM interprets → rules validate JSON)

Present:

```
Skills Architecture with Implementation Strategy:

**Rule-Based Skills** (Fast, deterministic, no LLM cost):
1. [Skill 1]: [Description]
   - Tool: Python script
   - Input: [file paths]
   - Output: [validation report]

**LLM-Based Skills (Max Tier)**:
1. [Skill 2]: [Description]
   - Requires: Claude Sonnet 4.5+ level
   - Reason: [complex reasoning need]

**LLM-Based Skills (SLM Tier)**:
1. [Skill 3]: [Description]
   - Can use: Llama 3.1 8B
   - Reason: [simple pattern matching]

**Hybrid Skills**:
1. [Skill 4]: [Description]
   - Step 1: Rule-based file scan
   - Step 2: LLM analysis
   - Step 3: Rule-based validation

Proceed with this classification?
```

### Validation Checkpoint

```
Architecture designed with V2 enhancements:
✅ Behavior taxonomy complete
✅ Fully-connected KG structure designed
✅ Skills classified by implementation type

Ready to create project structure. Proceed?
```

---

## Phase 3: Create Project Structure

*[Enhanced from V1.0]*

### Objective

Create the complete folder structure including V2 additions.

### Actions

#### Action 3.1: Create Enhanced Folder Structure

Execute these file operations:

```python
# V2 Enhanced Directory Structure
directories = [
    ".cursor",
    ".cursor/behaviors",
    ".cursor/behaviors/core",
    ".cursor/templates",
    "agents",
    "agents/skills",
    "agents/skills/system",
    "agents/knowledge-graphs",
    "docs",
    "docs/general",
    "docs/builder",
    "docs/builder/architecture",
    "docs/builder/implementation",
    "docs/builder/plan",
    "docs/manager",
    "scripts",
    "temp"
]

# Add role-specific behavior directories in .cursor
for role in roles:
    directories.append(f".cursor/behaviors/{role['id']}")

# Add role-specific skill directories
for role in roles:
    for category in skill_categories:
        directories.append(f"agents/skills/{category}")

# Add domain content directories (if applicable)
if has_domain_content_categories:
    for category in content_categories:
        directories.append(f"[content_root]/{category['id']}")
```

Report:

```
✅ Created [N] directories with V2 structure
```

#### Action 3.2: Create Identity File

Use gathered information to populate `.cursor/identity.md`:

```markdown
# [Agent Name] Identity

## Core Identity
- **Name**: [from Phase 1]
- **Domain**: [from Phase 1]
- **Version**: 2.0 (Agentic Architecture)
- **Organization**: [from Phase 1]
- **Primary Purpose**: [from Phase 1]

## Mission
[Expanded description from Phase 1]

## Roles

This system operates through [N] distinct agent personas.

[For each role from Phase 1:]
### Role [N]: [Role Name] ([Role Title])
- **ID**: `[role-id]`
- **Personality**: [from Phase 1]
- **Communication Style**: [from Phase 1]
- **Primary Responsibilities**:
  - [Task 1 from Phase 1]
  - [Task 2 from Phase 1]
  - [Continue...]
- **Boundaries**:
  - **Will NOT**: [from Phase 1]
  - **Will ALWAYS**: [from Phase 1]

## Operating Principles

1. **Clarity**: [Describe]
2. **Organization**: [Describe]
3. **Integration**: [Describe]
4. **Adaptability**: [Describe]
5. **Efficiency**: [Describe]

## Core Values
1. **Integrity**: [Based on Phase 1]
2. **Separation**: [Based on confidentiality from Phase 1]
3. **Evolution**: [Self-improvement capability]
4. **Clarity**: [Documentation as truth]

## Evolution Path

### Current Phase: Foundation & [Primary Mode from Phase 1]
- [List current phase activities]

### Future Phases
- **Phase 2**: [Next evolution step]
- **Phase 3**: [Advanced capabilities]
- **Phase 4**: [Ultimate goal]

## Safety & Ethics
- [Safety boundaries from Phase 1]
- [Confidentiality rules from Phase 1]
- [Validation requirements from Phase 1]
```

Execute: `write` tool to create `.cursor/identity.md`

Report:

```
✅ Created .cursor/identity.md
```

#### Action 3.3: Create Rules Index (V2: Lightweight Index)

**V2 Change**: `rules.md` becomes an index, not a monolithic file.

Create `.cursor/rules.md`:

```markdown
# [Agent Name] - Core Rules Index

This document serves as the central index for the AI agent's core operational rules and protocols.
These rules are implemented as granular behaviors, organized by category and role.

## Core Behaviors (Apply to all roles)
- [Project Structure Protocol](behaviors/core/project-structure.md)
- [System Safety Protocol](behaviors/core/system-safety.md)
- [Communication Protocol](behaviors/core/communication-protocol.md)
- [Continue with all core behaviors from Phase 2]

## [Role 1 Name] Role Behaviors (System Architecture & Maintenance)
- [Behavior 1](behaviors/[role-1-id]/[behavior-1-id].md)
- [Behavior 2](behaviors/[role-1-id]/[behavior-2-id].md)
- [Continue...]

## [Role 2 Name] Role Behaviors (Operational Tasks)
- [Behavior 1](behaviors/[role-2-id]/[behavior-1-id].md)
- [Continue...]

---
*Refer to the individual markdown files for detailed rule definitions.*
```

Execute: `write` tool to create `.cursor/rules.md`

Report:

```
✅ Created .cursor/rules.md (index mode)
```

Ready to proceed to Phase 4?
