# Phase 1: Information Discovery

**AI Agent Setup Protocol V2.0**

---

## 📌 Phase Context

**Prerequisites**: None (starting fresh)  
**Input needed**: Human responses to 5 question sets  
**Output**: Complete requirements document for Phase 2  
**Estimated time**: 30-60 minutes

**Creates for next phases**:
- Domain and role definitions → Phase 2, 3
- Knowledge structure requirements → Phase 2, 4
- Skills inventory → Phase 2, 5
- Workflow requirements → Phase 2

---

## Objective

Gather all necessary information before creating any files.

## Prerequisites

Before starting, ensure you have:

- [ ] Access to file creation tools
- [ ] Ability to run Python scripts
- [ ] Understanding of JSON structure
- [ ] Git repository initialized (recommended)
- [ ] Appropriate AI model (Claude Sonnet 4.5+ or GPT-5+ recommended)

---

## Required Input from Human

Ask these questions **in order**. Do not proceed until you have clear answers:

### Question Set 1: Domain & Purpose

```
I'll help you build a structured AI agent. First, I need to understand your domain:

1. What domain is your agent working in? (e.g., Education, Healthcare, Legal, Software Development)
2. What is the primary purpose of the agent? What problems will it solve?
3. Who are the end users?
```

Wait for response. Record answers.

### Question Set 2: Domain Role Definition

```
This agent will have TWO roles:

1. **Agent Builder** (System Role) - MANDATORY
   - Automatically included in every agent
   - Maintains Knowledge Graphs
   - Updates system configuration  
   - Enables self-evolution

2. **[Your Domain Role]** (Custom Role) - DEFINE THIS
   
Please define your primary domain role:
- What is the role name? (e.g., "Project Manager", "Code Reviewer", "Research Assistant")
- Role ID (lowercase-hyphenated, e.g., "project-manager")
- Personality (formal/casual/empathetic/technical)
- 3-5 primary tasks this role performs
- Communication style
- Key boundaries (what it won't do)

**Best Practice**: We recommend a single domain role per agent for maximum reliability and stability.

**Need multiple domain capabilities?** See the "Multi-Agent Architecture Guidance" section in 
V2_PROTOCOL_COMPLETE_PACKAGE_README.md for best practices on building and coordinating multiple agents.

Let's define your domain role: [Ask about each attribute]
```

Wait for response. Record answers for each role.

### Question Set 3: Knowledge Requirements

```
What knowledge will your agent need to access?

**If you already have content organized in folders:**
Please share the folder(s) using @ mention (e.g., @my-content-folder), and provide:
- Brief description of what's in this folder
- How it's organized (by category, topic, date, etc.)
- Approximate size (number of files/subdirectories)
- Any special structure or naming conventions

**If you're starting fresh or have scattered content:**
1. What content types will you need? (projects, documentation, policies, code, research papers, etc.)
2. What are the sources? (Git repos, PDFs, databases, APIs, websites, local files)
3. How should it be organized? (by category, module, feature, chronologically, etc.)
4. Approximately how much content? (10 projects, 100 documents, 50 code files, etc.)

**Note**: Sharing existing folders now allows me to analyze the structure and content during Phase 2 
architecture design, making the Knowledge Graph more accurate and tailored to your actual content.
```

Wait for response. Record answers.

**If user shared folders**: Scan the provided directories to understand:

- File types and extensions
- Directory structure depth
- Naming patterns
- Content categories
- Total file count

Document findings for use in Phase 2 (KG structure design) and Phase 4 (KG creation).

### Question Set 4: Skills & Tools

```
What capabilities and tools will your agent need?

1. What should it be able to DO? (analyze, validate, generate, orchestrate, etc.)
2. Are there existing tools to integrate? (scripts, APIs, databases)
3. Any domain-specific skills? (code review, project analysis, graph maintenance)
4. Which skills need LLM reasoning vs rule-based execution?
```

Wait for response. Record answers.

### Question Set 5: Workflows & Standards

```
What rules and workflows must your agent follow?

1. Any mandatory workflows? (multi-step processes that must be followed)
2. Any standards to enforce? (style guides, schemas, policies)
3. Any safety boundaries? (what must never happen)
4. Any confidentiality requirements? (data separation rules)
```

Wait for response. Record answers.

---

## Validation Checkpoint

Before proceeding, confirm:

```
Let me confirm what I've gathered:

**Domain**: [domain]
**Purpose**: [purpose]
**Users**: [users]

**Agent Roles** (2 total):
1. Agent Builder (System Role) - MANDATORY
   - Maintains Knowledge Graphs
   - Enables self-evolution
   - Updates system configuration
   
2. [Domain Role ID]: [Domain Role Name]
   - Personality: [personality]
   - Primary tasks: [list 3-5 tasks]
   - Communication style: [style]
   - Boundaries: [what it won't do]

**Knowledge Base**:
[If user shared folders:]
- Analyzed folders: [folder paths]
- Content structure: [description of organization]
- File count: [approximate count]
- Key content types: [list]

[If starting fresh:]
- Content types needed: [list]
- Sources: [list]
- Organization plan: [description]
- Estimated volume: [count]

**Key Skills**: [list from Question Set 4]
**Critical Workflows**: [list from Question Set 5]
**Safety Boundaries**: [list from Question Set 5]

Is this correct? Should I proceed to Phase 2 (Architecture Design)?
```

Wait for confirmation.

---

## Output

Document all gathered information for use in Phase 2:

- Domain definition
- Role specifications (complete for each role)
- Knowledge structure requirements
- Skills inventory
- Workflow & behavior requirements

---

**Next Phase**: [Phase 2: Architecture Design](PHASE_02_ARCHITECTURE_DESIGN.md)
