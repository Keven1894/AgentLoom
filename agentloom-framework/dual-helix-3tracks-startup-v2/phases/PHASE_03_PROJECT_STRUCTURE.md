# Phase 3: Create Project Structure

**AI Agent Setup Protocol V2.0**

---

## 📌 Phase Context

**Prerequisites**: Phases 1-2 complete  
**Input needed from previous phases**:
- Domain role ID and name (Phase 1)
- Behavior taxonomy (Phase 2)
- Shared content folders (Phase 1, if any)
- Content mapping plan (Phase 2)

**Output**: Complete folder structure + core config files  
**Estimated time**: 15-30 minutes

**Creates for next phases**:
- Directory structure → All phases
- `.cursor/identity.md` → Phase 11 (startup)
- `.cursor/rules.md` → Phase 5 (behavior index)

---

## Objective

Create the complete folder structure and core configuration files including V2 additions.

**Note**: This phase uses the Agent Builder + Domain Role architecture from Phase 1 & 2, and maps any shared content folders to the appropriate structure.

---

## Action 3.1: Map Shared Content (If Provided in Phase 1)

**If user shared content folders in Phase 1**, map them to the directory structure first.

### Review Phase 1 & Phase 2 Analysis

From Phase 1, you gathered:

- Shared folder paths (if any)
- Content organization
- File types and structure

From Phase 2 Action 2.0, you analyzed:

- Suggested KG mapping
- Content categories
- Cross-references

### Create Mapping Plan

Present to human:

```
Content Folder Mapping Plan:

**Shared Folders** (from Phase 1):
- [folder-path-1] → docs/[domain-role-id]/[category-1]
- [folder-path-2] → docs/[domain-role-id]/[category-2]
- [folder-path-3] → docs/general/[category-3]

**Rationale**:
- [Explain why each folder maps to its destination]

Should I proceed with this mapping?
```

Wait for confirmation.

**If no folders shared**: Skip to Action 3.2.

---

## Action 3.2: Create Enhanced Folder Structure

Execute these file operations:

```python
# V2 Enhanced Directory Structure
# Core system directories
directories = [
    ".cursor",
    ".cursor/behaviors",
    ".cursor/behaviors/core",
    ".cursor/templates",
    "agents",
    "agents/skills",
    "agents/knowledge-graphs",
    "docs",
    "docs/general",
    "scripts",
    "temp"
]

# Agent Builder (System Role - MANDATORY)
directories.extend([
    ".cursor/behaviors/agent-builder",
    "agents/skills/system",  # Agent Builder skills
    "docs/builder",
    "docs/builder/architecture",
    "docs/builder/implementation",
    "docs/builder/plan"
])

# Domain Role (Custom - from Phase 1)
domain_role_id = "[domain-role-id from Phase 1]"
directories.extend([
    f".cursor/behaviors/{domain_role_id}",
    f"agents/skills/{domain_role_id}",
    f"docs/{domain_role_id}"
])

# Add domain content categories (from Phase 1/2 analysis)
if has_shared_content:
    for category in content_categories:
        directories.append(f"docs/{domain_role_id}/{category['id']}")

# Add skill categories (from Phase 2.3 classification)
for skill_category in skill_categories:
    if skill_category not in ['system', domain_role_id]:
        directories.append(f"agents/skills/{skill_category}")
```

**Confirm to human**:
```
✅ Created directory structure:
- Core system: [N] directories
- Agent Builder role: [M] directories
- [Domain Role Name]: [P] directories
- Total: [N+M+P] directories
```

---

## Action 3.3: Create Identity File

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

This system operates through 2 distinct roles:

### Role 1: Agent Builder (System Role - MANDATORY)

- **ID**: `agent-builder`
- **Purpose**: System maintenance, Knowledge Graph evolution, self-improvement
- **Always Active**: Yes (runs in background)
- **Personality**: Technical, precise, systematic
- **Communication Style**: Structured, validation-focused
- **Primary Responsibilities**:
  - Maintain Knowledge Graphs (monitor, update, heal)
  - Validate system structure and integrity
  - Update `.cursor/` configuration when instructed
  - Enable agent self-evolution
- **Boundaries**:
  - **Will NOT**: Modify `.cursor/` or KG files without explicit instruction
  - **Will ALWAYS**: Validate changes before committing
  - **Will ALWAYS**: Maintain graph connectivity

### Role 2: [Domain Role Name] (Custom Role)

- **ID**: `[domain-role-id]` (from Phase 1)
- **Purpose**: [Primary purpose from Phase 1]
- **Always Active**: No (activated on user request)
- **Personality**: [from Phase 1]
- **Communication Style**: [from Phase 1]
- **Primary Responsibilities**:
  - [Task 1 from Phase 1]
  - [Task 2 from Phase 1]
  - [Task 3 from Phase 1]
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

**Create** `.cursor/identity.md` with the structure above.

**Confirm to human**:
```
✅ Created .cursor/identity.md
```

---

## Action 3.4: Create Rules Index (V2: Lightweight Index)

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

## Agent Builder Behaviors (System Role - Standard)
- [KG Consistency](behaviors/agent-builder/kg-consistency.md)
- [System Integrity](behaviors/agent-builder/system-integrity.md)
- [Validation Protocol](behaviors/agent-builder/validation-protocol.md)
- [Self-Evolution](behaviors/agent-builder/self-evolution.md)
- [Continue with behaviors from Phase 2]

## [Domain Role Name] Behaviors (Custom)
- [Behavior 1](behaviors/[domain-role-id]/[behavior-1-id].md)
- [Behavior 2](behaviors/[domain-role-id]/[behavior-2-id].md)
- [Continue with behaviors from Phase 2]

---
*Refer to the individual markdown files for detailed rule definitions.*
```

**Create** `.cursor/rules.md` with the structure above.

**Confirm to human**:
```
✅ Created .cursor/rules.md (index mode)
```

---

## Note: NEW_AGENT_START_HERE.md Creation

**NEW_AGENT_START_HERE.md will be created in Phase 11** (User Manual & Testing) because:

1. **Dependencies**: It references Knowledge Graphs that are created in Phase 4
2. **Testing**: It should be tested alongside the User Manual in Phase 11
3. **Completeness**: By Phase 11, all behaviors, skills, and KGs exist

The file will include:

- Identity loading
- KG loading (master + role-specific)
- Role architecture explanation
- Operational boundaries
- Agent reference card

See Phase 11 for the complete NEW_AGENT_START_HERE.md creation.

---

## Validation Checkpoint

```
✅ Core structure created:
- [N] directories (Agent Builder + Domain Role)
- .cursor/identity.md (2-role architecture)
- .cursor/rules.md (index mode)

Ready to proceed to Phase 4 (Knowledge Graphs)?
```

---

**Previous Phase**: [Phase 2: Architecture Design](PHASE_02_ARCHITECTURE_DESIGN.md)  
**Next Phase**: [Phase 4: Create Knowledge Graphs](PHASE_04_KNOWLEDGE_GRAPHS.md)
