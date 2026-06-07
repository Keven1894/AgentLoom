# AI Agent Setup Protocol V3.0 - Phase Index

**9 phases to build a production-ready AI agent with dual roles (Agent Builder + Domain Role)**

---

## Phase Overview

### [Phase 0: Environment Setup](PHASE_00_ENVIRONMENT_SETUP_v3.md)

**Objective**: Verify prerequisites and prepare workspace  
**Outputs**: Confirmed Python 3.9+ installation, workspace ready  
**Key**: Only Python 3.9+ required (no additional dependencies)

### [Phase 1: Information Discovery](PHASE_01_INFORMATION_DISCOVERY_v3.md)

**Objective**: Gather project context and requirements  
**Outputs**: Context variables, domain concepts, skills list, behaviors list  
**Key**: Check existing files first, then ask human for missing info

### [Phase 2: Architecture Design](PHASE_02_ARCHITECTURE_DESIGN_v3.md)

**Objective**: Design domain role architecture (knowledge, skills, behaviors)  
**Outputs**: Complete architecture specification with relationships  
**Key**: Domain-specific design (3-7 skills, 3-5 behaviors, clear hierarchy)

### [Phase 3: Project Structure](PHASE_03_PROJECT_STRUCTURE_v3.md)

**Objective**: Build complete folder structure and generate hybrid files  
**Outputs**: Full directory tree, placeholders, identity.md, rules.md, NEW_AGENT_START_HERE.md  
**Key**: Copy builder-assets + create domain folders + generate 3 hybrid files

### [Phase 4: Knowledge Graphs](PHASE_04_KNOWLEDGE_GRAPHS_v3.md)

**Objective**: Generate all JSON knowledge graphs  
**Outputs**: master-graph.json + 3 domain graphs (knowledge, skills, behaviors)  
**Key**: Follow schema spec, link all nodes, validate with visualization

### [Phase 5: Knowledge Content](PHASE_05_KNOWLEDGE_CONTENT_v3.md)

**Objective**: Populate domain knowledge in docs/ folder  
**Outputs**: Markdown content files organized by KG structure  
**Key**: Use content templates, maintain KG alignment, link to graphs

### [Phase 6: Skills Implementation](PHASE_06_SKILLS_IMPLEMENTATION_v3.md)

**Objective**: Write complete skill definitions  
**Outputs**: Full skill .md files with implementation details  
**Key**: Follow skill template, specify type (rule-based/llm-based/hybrid), link to behaviors

### [Phase 7: Behaviors Generation](PHASE_07_BEHAVIORS_GENERATION_v3.md)

**Objective**: Write complete behavior protocols  
**Outputs**: Full behavior .md files with rules and workflows  
**Key**: Define priorities, specify enforcement, link to skills and knowledge

### [Phase 8: User Manual](PHASE_08_USER_MANUAL_v3.md)

**Objective**: Generate user documentation  
**Outputs**: USER_MANUAL.md, VIEW_VISUALIZATION.md (optional)  
**Key**: Magic activation prompt for < 5 minute startup, role-specific workflows

---

## Quick Reference

**Total Time**: 2-4 hours (depending on domain complexity)

**Critical Files Generated**:

- `.cursor/identity.md` - Dual role definitions
- `agents/knowledge-graphs/master-graph.json` - KG entry point
- `agents/NEW_AGENT_START_HERE.md` - Agent initialization
- `agents/USER_MANUAL.md` - User reference

**Validation Points**:

- Phase 3: Structure validation
- Phase 4: Graph visualization check
- Phase 8: < 5 minute startup test

**Dependencies**:

- Each phase reads `output/phase-XX.md` from previous phases
- Phases 3-8 reference `specs/` and `examples/` from builder-assets

---

**Start Here**: [Phase 0: Environment Setup](PHASE_00_ENVIRONMENT_SETUP_v3.md)
