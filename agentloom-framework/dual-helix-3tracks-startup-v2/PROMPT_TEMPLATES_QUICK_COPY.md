# Quick Copy-Paste Prompts for V2.0 Protocol

**Purpose**: Ready-to-use prompts for common scenarios  
**Just**: Fill in `[PLACEHOLDERS]` and send to AI  
**Updated**: November 28, 2025

---

## 🆕 Scenario 1: Brand New Project

**Use when**: Starting from scratch

**Prompt**:

```
Read the protocol package index:
@temp/dual-helix-3tracks-startup/AI_AGENT_SETUP_PROTOCOL_V2_INDEX.md

Then navigate to the execution index:
@temp/dual-helix-3tracks-startup/phases/INDEX.md

# Task: Build New Agentic AI System

**Domain**: [YOUR_DOMAIN, e.g., Healthcare, Education, Software Development]
**Purpose**: [ONE_SENTENCE_DESCRIPTION of what the agent will do]
**My role**: [YOUR_ROLE, e.g., Developer, Researcher, Manager]

Follow phases 1-11 from the execution index.

**Start with Phase 1**: Ask discovery questions to gather complete requirements.

**V2.0 Critical Requirements**:
- Fully-connected Knowledge Graphs (mandatory parent links)
- Agent Builder + 1 domain role architecture
- Visualization tool with Unified Brain view
- USER_MANUAL.md for < 5min cold-start
- Skills classified by implementation type
- KG maintenance skill for self-evolution

Use EXPRESS MODE in Phases 5, 7, 9, 11 if you understand the patterns.

Begin with Phase 1.
```

---

## 🔄 Scenario 2: Migrate Existing Project to V2.0

**Use when**: You have an existing agent that needs V2.0 structure

**⚠️ IMPORTANT**: Backup your project first!

**Prompt**:

```
Read the protocol package:
@temp/dual-helix-3tracks-startup/AI_AGENT_SETUP_PROTOCOL_V2_INDEX.md
@temp/dual-helix-3tracks-startup/PROMPT_TEMPLATE_EXISTING_PROJECT.md

# Task: Migrate to V2.0 Architecture

**Project**: [PROJECT_NAME]
**Current state**: [BRIEF_DESCRIPTION - what exists now]
**Backup status**: ✅ I have backed up my project

**Migration Steps**:
1. Audit current state (analyze all files)
2. Design V2.0 architecture
3. Create migration plan
4. **WAIT FOR MY APPROVAL** before executing
5. Execute migration (with safety checks)
6. Validate (visualization + cold-start test)
7. Deliver migration summary

Start with Step 1: Audit existing structure and present findings.

Preserve all existing content. Use safe migration approach.
```

---

## 🧪 Scenario 3: Validate Existing V2.0 System

**Use when**: You want to check if your agent follows V2.0 standards

**Prompt**:

```
# Task: Validate V2.0 Compliance

Check my project against V2.0 protocol standards:

**Structure Validation**:
- Run: python scripts/validate_structure.py
- Run: python scripts/validate_graphs.py

**V2.0 Checklist**:
1. Knowledge Graphs fully connected? (root nodes + parent links)
2. Agent Builder + domain role architecture?
3. Visualization tool exists? (visualization.html)
4. USER_MANUAL.md comprehensive? (test cold-start < 5min)
5. Skills classified by implementation type?
6. KG maintenance skill exists and functional?
7. Behaviors in .cursor/behaviors/?

**Visual Validation**:
- Open agents/knowledge-graphs/visualization.html
- Check Unified Brain view (all graphs merged)
- Verify no orphaned nodes
- Check cross-graph links visible

Generate validation report:
- ✅ What passes V2.0 standards
- ⚠️ What needs fixing
- 💡 Recommended improvements

Begin validation.
```

---

## 🏗️ Scenario 4: Add New Role to Existing V2.0 System

**Use when**: Need to expand capabilities with another role

**Prompt**:

```
@temp/dual-helix-3tracks-startup/phases/PHASE_02_ARCHITECTURE_DESIGN.md
@temp/dual-helix-3tracks-startup/phases/PHASE_04_KNOWLEDGE_GRAPHS.md

# Task: Add New Role to V2.0 System

**New Role**: [ROLE_NAME]
**Purpose**: [What this role will do]
**Key capabilities**: [List 3-5 capabilities]

**Design and create**:
1. Role definition (identity.md update)
2. 3 Knowledge Graphs:
   - [role-id]-knowledge-graph.json
   - [role-id]-skills-graph.json
   - [role-id]-behaviors-graph.json
3. Role-specific behaviors (in .cursor/behaviors/[role-id]/)
4. Role-specific skills (in agents/skills/[role-id]/)
5. Update master-graph.json
6. Update rules.md index

**Ensure**:
- All graphs have root nodes
- All nodes have parent links
- Cross-links to existing graphs where appropriate

**Then validate**:
- Run validate_graphs.py
- Check visualization.html (Unified Brain view)

Begin with role design.
```

---

## 📝 Scenario 5: Update Knowledge Graph

**Use when**: Files changed, KG needs updating

**Prompt**:

```
# Task: Update Knowledge Graph

Activate the Agent Builder role and use the KG maintenance skill.

**Steps**:
1. Run: python scripts/kg_monitor.py (detect changes)
2. Analyze changes and determine which graphs to update
3. Generate metadata for new/modified files
4. Update appropriate JSON graphs
5. Run: python scripts/kg_heal.py (check connectivity)
6. Run: python scripts/validate_graphs.py (full validation)

**Report**:
- Files added/modified/deleted
- Graphs updated
- Nodes added/updated/removed
- Validation status

Begin KG update.
```

---

## 🔍 Scenario 6: Explain My Agent's Architecture

**Use when**: Need to understand how your agent is structured

**Prompt**:

```
# Task: Explain Agent Architecture

Read:
@.cursor/identity.md
@agents/knowledge-graphs/master-graph.json

**Provide**:
1. Overview of agent purpose and roles
2. Explanation of Knowledge Graph structure
3. List of key behaviors and their purposes
4. List of key skills and their implementation types
5. How the two roles interact
6. Visualization guide (how to use visualization.html)

Use simple, clear language. Include diagrams if helpful.
```

---

## 🛠️ Scenario 7: Fix Orphaned Nodes

**Use when**: Validation shows disconnected nodes

**Prompt**:

```
# Task: Fix Knowledge Graph Connectivity

**Problem**: Validation shows orphaned nodes

**Steps**:
1. Run: python scripts/kg_heal.py (identify issues)
2. For each orphaned node:
   - Determine appropriate parent based on path/ID pattern
   - Add "parent": "[parent-id]" field
3. Validate parent IDs exist
4. Run: python scripts/validate_graphs.py (confirm fix)
5. Open visualization.html → Check Unified Brain view

**Success criteria**:
- validate_graphs.py passes 100%
- No orphaned nodes reported
- Unified Brain view shows all nodes connected

Begin healing process.
```

---

## 📚 Scenario 8: Create Documentation for New Feature

**Use when**: Added new behavior/skill, need to document it

**Prompt**:

```
# Task: Document New [Behavior/Skill]

**Feature**: [NAME]
**Type**: [behavior/skill]
**Category**: [agent-builder/domain-role-id/core]

**Create documentation**:
1. Use appropriate template:
   - Behavior: docs-templates/behavior-file.md.template (or generate custom)
   - Skill: Follow guides/SKILL_TEMPLATE_GUIDE.md

2. Include:
   - YAML frontmatter (type, category, id, implementation)
   - Description and purpose
   - Usage instructions
   - Examples
   - Related components (cross-references)

3. Update Knowledge Graph:
   - Add node to appropriate graph
   - Add parent link
   - Add cross-links to related components

4. Validate:
   - Run validate_graphs.py
   - Check visualization.html

Begin documentation.
```

---

## 🧹 Scenario 9: Clean Up and Optimize Existing V2.0 System

**Use when**: System works but needs refinement

**Prompt**:

```
# Task: Optimize V2.0 System

**Audit and optimize**:

**Knowledge Graph**:
- Run kg_heal.py → Fix any issues
- Check for redundant nodes
- Optimize node descriptions
- Verify all cross-links are meaningful

**Documentation**:
- Review all behavior files for completeness
- Review all skill files for accuracy
- Update any outdated documentation
- Apply chunking best practices (250-500 lines per file)

**Code**:
- Review skill implementations
- Check for opportunities to use rule-based instead of LLM
- Optimize hybrid skills for cost

**Generate optimization report**:
- Issues fixed
- Improvements made
- Cost savings achieved
- Recommendations for future

Begin audit.
```

---

## 🎓 Scenario 10: Train Team Member on Agent

**Use when**: Someone needs to learn how to use your agent

**Prompt**:

```
# Task: Create Onboarding Guide

**For**: New team member learning to use this agent

**Create**:

1. **Quick Start Guide** (separate from USER_MANUAL.md)
   - 5-minute orientation
   - What this agent does
   - Basic prompts to try
   - How to activate each role

2. **Common Workflows**
   - Top 5 use cases
   - Example prompts for each
   - Expected outputs

3. **Troubleshooting**
   - Common issues
   - How to check agent status
   - When to use which role

4. **Advanced Features**
   - Knowledge Graph navigation
   - Using visualization.html
   - KG maintenance skill

Save as: docs/general/TEAM_ONBOARDING.md

Use clear, simple language. Include examples.
```

---

## 💡 Tips for Using These Prompts

### General Tips

1. **Fill ALL placeholders** - Don't leave `[BRACKETS]`
2. **Be specific** - "Healthcare diagnosis" > "Healthcare"
3. **Attach files as shown** - Use @ mentions for protocol files
4. **Wait for approval** - Review architecture before building

### Scenario-Specific Tips

**Scenario 1 (New Project)**:
- Answer all Phase 1 questions thoroughly
- Review Phase 2 architecture carefully
- Use express mode to save time (if experienced)

**Scenario 2 (Migration)**:
- BACKUP FIRST (cannot stress this enough!)
- Review audit report carefully
- Approve migration plan before execution
- Test thoroughly after migration

**Scenario 3-10 (Specific Tasks)**:
- Reference existing V2.0 structure
- Validate after changes
- Update KG when files change

---

## 🚨 Common Issues & Solutions

### "AI didn't follow the protocol"

**Solution**: Point to specific phase
```
Follow phases/PHASE_01_INFORMATION_DISCOVERY.md exactly.
Don't skip any question sets.
```

### "Graphs are disconnected"

**Solution**: Use Scenario 7 (Fix Orphaned Nodes)
```
Every node except root must have "parent": "[parent-id]"
```

### "Cold-start takes too long"

**Solution**: Test USER_MANUAL.md
```
Use Scenario 3 to validate.
Check if NEW_AGENT_START_HERE.md follows template.
```

### "Not sure which scenario to use"

**Solution**:
- Starting fresh → Scenario 1
- Have existing project → Scenario 2
- Need validation → Scenario 3
- Specific task → Scenarios 4-10

---

## 📊 Expected Results

### After Scenario 1 (New Project)

**Time**: 3-7 hours  
**Files created**: 70-150+  
**Quality**: Production-ready  
**Validation**: Should pass 100%

### After Scenario 2 (Migration)

**Time**: 1-4 hours  
**Files modified**: 10-50+  
**Files created**: 30-80+  
**Validation**: Existing content preserved + V2.0 structure

### After Scenarios 3-10 (Tasks)

**Time**: 30 min - 2 hours  
**Changes**: Focused on specific area  
**Validation**: Targeted to task

---

## 🎯 Best Practices

1. **Always backup** before migrations or major changes
2. **Review architectures** before approving (Phase 2 especially)
3. **Use express mode** to save time (if experienced)
4. **Validate frequently** (after phases 4, 6, 9, 10, 11)
5. **Test cold-start** (must be < 5 minutes)
6. **Use visualization** (Unified Brain view shows everything)
7. **Trust the agent** for documentation (README, summaries)
8. **Use templates** for structure (JSON, code, validation)

---

## 📖 Related Files

- **Protocol execution**: `phases/INDEX.md`
- **Package overview**: `AI_AGENT_SETUP_PROTOCOL_V2_INDEX.md`
- **Quick reference**: `AI_AGENT_SETUP_PROTOCOL_V2_SUMMARY.md`
- **Detailed new project**: `PROMPT_TEMPLATE_NEW_PROJECT.md`
- **Detailed migration**: `PROMPT_TEMPLATE_EXISTING_PROJECT.md`

---

**Version**: 2.0  
**Last Updated**: November 28, 2025  
**Status**: Production Ready
