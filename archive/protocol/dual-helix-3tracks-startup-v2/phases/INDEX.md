# AI Agent Setup Protocol V2.0 - EXECUTION INDEX

**Version**: 2.0  
**Created**: November 27, 2025  
**Last Updated**: November 28, 2025  
**Status**: Production Ready

**📍 You are here**: Phase execution navigation hub  
**🔙 Package overview**: [AI_AGENT_SETUP_PROTOCOL_V2_INDEX.md](../AI_AGENT_SETUP_PROTOCOL_V2_INDEX.md)

---

## Overview

This is your **execution hub** for building an agent system. The protocol has been organized into **11 focused phase documents** that you'll follow sequentially.

## How to Use This Protocol

### For AI Agents

1. **Read this INDEX first** - Understand the overall structure
2. **Check your experience level** - Use Express Mode if experienced
3. **Follow phases sequentially** - Each phase builds on the previous
4. **Use validation checkpoints** - Confirm completion before moving forward
5. **Reference the SUMMARY** - Quick reference for templates and rules

### For Humans

1. **Share the entire `phases/` folder** with your AI assistant
2. **Point to Phase 1** to begin the protocol
3. **Review Phase 2 architecture** before approving
4. **Test the final system** with USER_MANUAL.md

---

## 🎯 Template vs Generate: Decision Framework

Understanding when to use templates vs let agent generate custom content:

### When to USE TEMPLATES (Copy)

✅ **Structural Components** (JSON, HTML, Python):
- Agent Builder JSON graphs → **REQUIRED** (Level 1)
- Validation scripts → **REQUIRED** (Level 1)
- Visualization HTML → **REQUIRED** (Level 1)
- **Why**: Complex, brittle, tested, identical across projects

✅ **User-Facing Documentation** (Machine-executable):
- NEW_AGENT_START_HERE.md → **RECOMMENDED** (Level 2)
- USER_MANUAL.md → **RECOMMENDED** (Level 2)
- **Why**: Critical startup scripts, proven structure

✅ **Structural Guides** (Markdown templates):
- behavior-file.md → **OPTIONAL** (Level 3)
- CONTENT_TEMPLATE.md → **OPTIONAL** (Level 3)
- **Why**: Shows pattern, ensures completeness

### When to GENERATE (Trust Agent)

✅ **Project Documentation**:
- README.md → **Generate with requirements**
- SETUP_COMPLETE.md → **Generate as summary**
- **Why**: Agent excels at summaries, each project is unique

✅ **Domain-Specific Content**:
- Domain role behaviors → **Adapt template or generate**
- Domain role skills → **Use guide as reference**
- **Why**: Diverse content, agent understands context

✅ **Summary/Reports**:
- Architecture documentation → **Generate**
- Implementation notes → **Generate**
- **Why**: Agent's strength, project-specific

### Quick Decision Tree

```
Is it JSON or complex code?
  YES → USE TEMPLATE (Level 1)
  NO ↓

Is it Agent Builder component?
  YES → USE TEMPLATE (Level 1 or 2)
  NO ↓

Is it user-facing startup doc?
  YES → TEMPLATE RECOMMENDED (Level 2)
  NO ↓

Is it summary/documentation?
  YES → GENERATE with requirements (Level 3)
  NO ↓

DEFAULT: Use template as GUIDE, adapt as needed
```

---

## The 11 Phases

### Phase 1: Information Discovery

**File**: [PHASE_01_INFORMATION_DISCOVERY.md](PHASE_01_INFORMATION_DISCOVERY.md)  
**Duration**: 30-60 minutes  
**Purpose**: Gather all requirements before creating any files

**What You'll Do**:

- Ask 5 question sets about domain, roles, knowledge, skills, workflows
- Validate gathered information with human
- Document all requirements for use in Phase 2

**Output**: Complete requirements document

---

### Phase 2: Architecture Design

**File**: [PHASE_02_ARCHITECTURE_DESIGN.md](PHASE_02_ARCHITECTURE_DESIGN.md)  
**Duration**: 30-45 minutes  
**Purpose**: Design complete system architecture with V2 enhancements

**What You'll Do**:

- Design behavior taxonomy (core + role-specific)
- Design fully-connected Knowledge Graph structure
- Classify all skills by implementation type (rule-based/LLM/hybrid)
- Get human approval before proceeding

**Output**: Architecture design document

---

### Phase 3: Create Project Structure

**File**: [PHASE_03_PROJECT_STRUCTURE.md](PHASE_03_PROJECT_STRUCTURE.md)  
**Duration**: 15-30 minutes  
**Purpose**: Create folder structure and core configuration files

**What You'll Do**:

- Create enhanced directory structure
- Create `.cursor/identity.md`
- Create `.cursor/rules.md` (lightweight index)

**Note**: NEW_AGENT_START_HERE.md will be created in Phase 11

**Output**: ~20-30 directories and 3-4 core files

---

### Phase 4: Create Knowledge Graphs

**File**: [PHASE_04_KNOWLEDGE_GRAPHS.md](PHASE_04_KNOWLEDGE_GRAPHS.md)  
**Duration**: 45-90 minutes  
**Purpose**: Create all JSON Knowledge Graphs with full connectivity

**What You'll Do**:

- Create `master-graph.json` (entry point)
- Create domain/project graphs
- Create role-specific knowledge graphs
- Create role-specific skills graphs (with sub-skills)
- Create role-specific behaviors graphs (with cross-links)

**Critical V2 Rules**:

- Every graph has a root node
- Every non-root node has a `parent` field
- Cross-graph links use `links` field

**Output**: 8+ fully-connected JSON graph files

---

### Phase 5: Create Content Templates

**File**: [PHASE_05_CONTENT_TEMPLATES.md](PHASE_05_CONTENT_TEMPLATES.md)  
**Duration**: 60-120 minutes  
**Purpose**: Create standard templates and initial behavior/skill documentation

**What You'll Do**:

- Create `CONTENT_TEMPLATE.md`
- Create core behavior files (`.cursor/behaviors/core/`)
- Create role-specific behavior files
- Create skill definition files (`agents/skills/`)

**Output**: 20-50+ markdown documentation files

---

### Phase 6: Create Validation Tools

**File**: [PHASE_06_VALIDATION_TOOLS.md](PHASE_06_VALIDATION_TOOLS.md)  
**Duration**: 20-30 minutes  
**Purpose**: Create scripts to validate structure and graph integrity

**What You'll Do**:

- Create `scripts/validate_graphs.py` (V2 with connectivity checks)
- Create `scripts/validate_structure.py`

**Output**: 2 Python validation scripts

---

### Phase 7: KG Maintenance Skill Setup

**File**: [PHASE_07_KG_MAINTENANCE.md](PHASE_07_KG_MAINTENANCE.md)  
**Duration**: 30-45 minutes  
**Purpose**: Create the "Maintain Knowledge Graph" skill system (self-evolution)

**What You'll Do**:

- Create orchestrator skill: `maintain-kg.md`
- Create sub-skill: `kg-monitor.md`
- Create sub-skill: `kg-update-node.md`
- Create sub-skill: `kg-heal.md`

**Output**: 4 skill definition files for self-evolution capability

---

### Phase 8: Skills Implementation

**File**: [PHASE_08_SKILLS_IMPLEMENTATION.md](PHASE_08_SKILLS_IMPLEMENTATION.md)  
**Duration**: 60-120 minutes  
**Purpose**: Create actual tool implementations for all skills

**What You'll Do**:

- Create Python scripts for rule-based skills
- Create prompt templates for LLM-based skills
- Create orchestration scripts for hybrid skills
- Implement KG maintenance tools (kg_monitor.py, kg_heal.py)

**Output**: 10-30+ implementation files (scripts + prompts)

---

### Phase 9: Final Validation

**File**: [PHASE_09_FINAL_VALIDATION.md](PHASE_09_FINAL_VALIDATION.md)  
**Duration**: 20-30 minutes  
**Purpose**: Run all validators and create final documentation

**What You'll Do**:

- Run `validate_structure.py`
- Run `validate_graphs.py`
- Create `README.md`
- Create `SETUP_COMPLETE.md`
- Generate final summary

**Output**: README.md + SETUP_COMPLETE.md + validation reports

---

### Phase 10: Visualization Tool

**File**: [PHASE_10_VISUALIZATION_TOOL.md](PHASE_10_VISUALIZATION_TOOL.md)  
**Duration**: 30-45 minutes  
**Purpose**: Create interactive HTML tool for graph visualization

**What You'll Do**:

- Create `visualization.html` (~500 lines)
- Create `VIEW_VISUALIZATION.md` (usage guide)
- Implement Unified Brain view
- Implement role-specific views
- Enable connectivity validation

**Output**: visualization.html + VIEW_VISUALIZATION.md

---

### Phase 11: User Manual & Testing

**File**: [PHASE_11_USER_MANUAL_TESTING.md](PHASE_11_USER_MANUAL_TESTING.md)  
**Duration**: 30-60 minutes  
**Purpose**: Create comprehensive USER_MANUAL.md and perform cold-start testing

**What You'll Do**:

- Create `agents/NEW_AGENT_START_HERE.md` (machine-executable)
- Create `agents/USER_MANUAL.md` (prompt library)
- Create test protocol
- Perform cold-start simulation
- Document pain points and improvements
- Iterate based on findings

**Success Criteria**: Fresh agent operational in < 5 minutes

**Output**: NEW_AGENT_START_HERE.md + USER_MANUAL.md + testing documentation

---

## Quick Reference

### Total Time Estimate

- **Small project** (1-2 roles, simple domain): 3-4 hours
- **Medium project** (2-3 roles, moderate complexity): 5-7 hours
- **Large project** (3+ roles, complex domain): 9-12 hours

### Files Created

- **Directories**: 20-50+
- **JSON Graphs**: 8-12 (fully connected)
- **Behavior Files**: 10-30
- **Skill Files**: 10-30
- **Python Scripts**: 5-15
- **Documentation**: 10-20+
- **Total**: 70-150+ files

### V2.0 Critical Features

- ✅ Fully-connected Knowledge Graphs (mandatory parent links)
- ✅ Interactive visualization with Unified Brain view
- ✅ < 5 minute cold-start (tested)
- ✅ Self-evolution capability (KG maintenance)
- ✅ Skills classified by implementation type
- ✅ Native behavior layer (.cursor/ auto-loaded)

---

## Additional Resources

### Quick Reference Documents

- **AI_AGENT_SETUP_PROTOCOL_V2_SUMMARY.md** - Templates, checklists, common pitfalls
- **V2_PROTOCOL_COMPLETE_PACKAGE_README.md** - Package overview and usage guide

### Original Files (For Reference)

- `AI_AGENT_SETUP_PROTOCOL_V2_PART1.md` - Phases 1-3 (legacy)
- `AI_AGENT_SETUP_PROTOCOL_V2_PART2.md` - Phases 4-7 (legacy)
- `AI_AGENT_SETUP_PROTOCOL_V2_PART3.md` - Phases 8-11 (legacy)

**Note**: The original 3-part files are kept for reference but should be replaced by the new phase-specific documents.

---

## Navigation

**🚀 Start Building**: [Phase 1: Information Discovery](PHASE_01_INFORMATION_DISCOVERY.md)  
**🔙 Package Overview**: [AI_AGENT_SETUP_PROTOCOL_V2_INDEX.md](../AI_AGENT_SETUP_PROTOCOL_V2_INDEX.md)  
**📦 Main README**: [V2_PROTOCOL_COMPLETE_PACKAGE_README.md](../V2_PROTOCOL_COMPLETE_PACKAGE_README.md)

---

## File Relationships

```
Protocol Package Structure:

AI_AGENT_SETUP_PROTOCOL_V2_INDEX.md  ← Package entry point (you start here)
    ↓ (points to)
phases/INDEX.md  ← Execution hub (YOU ARE HERE)
    ↓ (guides through)
phases/PHASE_01-11.md  ← Step-by-step execution
```

---

**Protocol Status**: Production Ready  
**Version**: 2.0  
**Last Updated**: November 28, 2025
