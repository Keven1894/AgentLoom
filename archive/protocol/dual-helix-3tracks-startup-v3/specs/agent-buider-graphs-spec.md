# Agent Builder Graphs Specification

## Purpose

Agent Builder is the SYSTEM ROLE that handles KG maintenance and self-evolution.
Its graphs are STANDARD across all projects (no customization needed).

## Why Standard?

Agent Builder always does the same things:

- Maintain Knowledge Graphs
- Validate system structure  
- Enable self-evolution
- Enforce system integrity

Therefore, its graphs should be IDENTICAL for every agent built with this protocol.

## Generation Instructions

When generating Agent Builder graphs, use these EXACT specifications.

---

## 1. Agent Builder Knowledge Graph

**File**: `agent-builder-knowledge-graph.json`

**Generate with these exact nodes**:

| id | type | title | parent | description |
|----|------|-------|--------|-------------|
| sys:root | root | System Architecture | - | Root of system knowledge |
| sys:agents | component | Agent Logic Hub | sys:root | Contains skills, behaviors, and knowledge graphs |
| sys:config | component | Configuration | sys:root | System identity and behavior definitions |
| sys:behaviors | component | Behavior Library | sys:config | Native rule definitions |
| sys:docs | folder | Documentation Repository | sys:root | System documentation organized by role |
| sys:docs:general | folder | General Documentation | sys:docs | Cross-role guides and references |
| sys:docs:builder | folder | Agent Builder Documentation | sys:docs | System architecture and maintenance guides |
| sys:kg:architecture | concept | Knowledge Graph Architecture | sys:root | Meta-structure defining how system remembers |

---

## 2. Agent Builder Skills Graph

**File**: `agent-builder-skills-graph.json`

**Generate with these exact nodes**:

| id | type | name | parent | implementation | description |
|----|------|------|--------|----------------|-------------|
| skill:builder:root | root | Agent Builder Capabilities | - | - | Root of Agent Builder skills |
| skill-maintain-kg | skill | Maintain Knowledge Graph | skill:builder:root | hybrid | Orchestrator for KG self-evolution |
| skill-kg-monitor | skill | Monitor File System | skill-maintain-kg | rule-based | Detect changes in tracked directories |
| skill-kg-update | skill | Update Graph Node | skill-maintain-kg | hybrid | Add/modify/remove KG nodes |
| skill-kg-heal | skill | Heal Graph Links | skill-maintain-kg | rule-based | Fix orphans and broken links |
| skill-validate-structure | skill | Validate Project Structure | skill:builder:root | rule-based | Check directories and required files |

**Cross-links to add**:

- `skill-maintain-kg` → `links.implements: ["behavior:builder:kg-consistency"]`
- `skill-validate-structure` → `links.implements: ["behavior:builder:system-integrity"]`

---

## 3. Agent Builder Behaviors Graph

**File**: `agent-builder-behaviors-graph.json`

**Generate with these exact nodes**:

| id | type | name | parent | priority | description |
|----|------|------|--------|----------|-------------|
| behavior:builder:root | root | Agent Builder Behaviors | - | - | Core protocols for system role |
| behavior:core:safety | core | System Safety Protocol | behavior:builder:root | critical | Never delete without confirmation |
| behavior:core:communication | core | Communication Protocol | behavior:builder:root | medium | Clear, structured responses |
| behavior:builder:kg-consistency | role-specific | KG Consistency | behavior:builder:root | high | Graph must reflect file system reality |
| behavior:builder:system-integrity | role-specific | System Integrity | behavior:builder:root | high | Never modify .cursor/ without instruction |
| behavior:builder:validation | role-specific | Validation Protocol | behavior:builder:root | medium | Always validate after changes |
| behavior:builder:self-evolution | role-specific | Self-Evolution | behavior:builder:root | medium | Maintain KG when files change |

**Cross-links to add**:

- `behavior:builder:kg-consistency` → `links.enforces: ["skill-maintain-kg"]`
- `behavior:builder:system-integrity` → `links.enforces: ["skill-validate-structure"]`

---

## Validation

After generating, verify:

1. All 3 files are valid JSON
2. Each has exactly one root node
3. Every non-root node has `parent` field
4. All parent references are valid
5. Cross-links reference valid node IDs
