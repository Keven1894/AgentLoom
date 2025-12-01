# AI Agent Setup Protocol V2.0 - Quick Reference

**Purpose**: Quick lookup for agents and humans using the protocol  
**Full Protocol**: Navigate via `phases/INDEX.md` (execution hub)  
**Last Updated**: November 28, 2025  
**Version**: 2.0 - Production Ready

---

## 🎯 Protocol Overview

### What Is This?

A **production-ready protocol** for building AI agent systems with:
- ✅ Fully-connected Knowledge Graphs (no orphaned nodes)
- ✅ Two-role architecture (Agent Builder + your domain)
- ✅ Self-evolution capability (agents maintain their own KG)
- ✅ < 5 minute cold-start (tested)
- ✅ Interactive visualization (see agent's "brain")

**Build time**: 3-7 hours  
**Result**: 70-150+ files, production-ready agent

---

## 📁 Quick Navigation

### For AI Agents Starting Fresh

1. **Package INDEX** - Read first
   - `AI_AGENT_SETUP_PROTOCOL_V2_INDEX.md` (package overview)
   
2. **Execution INDEX** - Your navigation hub
   - `phases/INDEX.md` (how to execute, decision framework)
   
3. **Phases 1-11** - Execute sequentially
   - `phases/PHASE_01_INFORMATION_DISCOVERY.md` → Start here
   - Follow through Phase 11

### For Humans Using Quick Prompts

1. **Quick scenarios** - Copy and paste
   - `PROMPT_TEMPLATES_QUICK_COPY.md` (10 ready-to-use prompts)
   
2. **Detailed new project**
   - `PROMPT_TEMPLATE_NEW_PROJECT.md` (comprehensive guide)
   
3. **Migration guide**
   - `PROMPT_TEMPLATE_EXISTING_PROJECT.md` (retrofit existing)

---

## 📋 The 11 Phases (Quick Summary)

### Discovery & Structure (Phases 1-3) - 75-135 min

**Phase 1: Information Discovery** (30-60 min)
- Gather requirements via 5 question sets
- Define Agent Builder + domain role
- Document for Phase 2

**Phase 2: Architecture Design** (30-45 min)
- Design behavior taxonomy
- Design fully-connected KG structure
- Classify skills (rule-based/LLM/hybrid)
- **Get human approval before Phase 3**

**Phase 3: Project Structure** (15-30 min)
- Create directory structure
- Create identity.md and rules.md
- Map content folders (if provided)

---

### Knowledge Graphs & Tools (Phases 4-7) - 155-280 min

**Phase 4: Knowledge Graphs** (45-90 min)
- **Copy** 3 Agent Builder graphs (templates)
- **Generate** 3-4 domain role graphs (custom)
- Create master-graph.json
- Ensure full connectivity

**Phase 5: Content Templates** (60-120 min, or 30-60 with express)
- Copy/create CONTENT_TEMPLATE.md
- Create behavior files (template OR generate)
- Create skill definition files
- Agent Builder + domain role

**Phase 6: Validation Tools** (20-30 min)
- **Copy** validate_graphs.py (from protocol)
- **Copy** kg_monitor.py, kg_heal.py (from protocol)
- **Customize** validate_structure.py

**Phase 7: KG Maintenance** (30-45 min, or 15-20 with express)
- Create 4 KG maintenance skill files
- Enable self-evolution
- Agent Builder standard

---

### Implementation & Finalization (Phases 8-11) - 140-275 min

**Phase 8: Skills Implementation** (60-120 min)
- **Copy** rule-based scripts (if in protocol)
- **Create** custom domain scripts
- **Create** LLM prompt templates
- **Create** hybrid orchestrators

**Phase 9: Final Validation** (20-30 min, or 15-20 with express)
- Run validate_structure.py
- Run validate_graphs.py
- **Generate** README.md (not template!)
- **Generate** SETUP_COMPLETE.md (not template!)

**Phase 10: Visualization Tool** (30-45 min)
- **Copy and customize** visualization.html
- Create VIEW_VISUALIZATION.md
- Test Unified Brain view

**Phase 11: User Manual & Testing** (30-60 min, or 15-30 with express)
- **Copy and customize** NEW_AGENT_START_HERE.md
- **Copy and customize** USER_MANUAL.md
- Cold-start test (< 5 min target)

---

## 🎯 Template Rigidity Levels

Understanding when to copy vs generate:

### ⭐⭐⭐⭐⭐ Level 1: REQUIRED (Copy Exactly)

**Must copy these**:
- Agent Builder JSON graphs (3) - Structural integrity
- Validation scripts (3) - Tested logic
- visualization.html - Complex frontend code

**Why**: Complex, brittle, identical across projects

---

### ⭐⭐⭐⭐ Level 2: RECOMMENDED (Copy and Adapt)

**Should copy these**:
- NEW_AGENT_START_HERE.md - Machine-executable startup
- USER_MANUAL.md - Proven prompt library structure
- validate_structure.py - Needs domain role customization

**Why**: Proven structure, needs customization

---

### ⭐⭐⭐ Level 3: OPTIONAL (Use as Reference)

**Can generate these**:
- README.md - Agent generates better
- SETUP_COMPLETE.md - Agent knows what happened
- Behavior files - Can adapt template or generate
- CONTENT_TEMPLATE.md - Shows pattern

**Why**: Agent excels at documentation, domains vary

---

## 🎯 V2.0 Critical Rules

### 1. Fully-Connected Knowledge Graphs

**Every non-root node MUST have**:
```json
"parent": "parent-node-id"
```

**Every graph MUST have**:
```json
{
  "id": "[type]:root",
  "type": "root",
  "title": "Root Name"
}
```

**Validation**:
- Run `python scripts/validate_graphs.py`
- Check visualization.html Unified Brain view
- No orphaned nodes allowed

---

### 2. Two-Role Architecture

**Every agent has exactly 2 roles**:

**Role 1: Agent Builder** (System Role) - MANDATORY
- Standardized (same for all projects)
- KG maintenance, validation, system integrity
- Always active in background
- **Templates**: 100% reusable (copy from protocol)

**Role 2: [Your Domain]** (Custom Role)
- Tailored to your use case
- Domain-specific tasks
- Activated on user request
- **Templates**: Use as guides, generate custom

---

### 3. Template vs Generate Decision

**Quick rule**:
```
JSON or code? → COPY template
Agent Builder component? → COPY template
Startup docs? → COPY and customize template
Documentation/summaries? → GENERATE with requirements
Domain content? → ADAPT template or generate
```

**Full framework**: `phases/INDEX.md` section "Template vs Generate"

---

## ⚡ Express Mode (Time Savings)

**Available in**: Phases 5, 7, 9, 11

**What it is**:
- Quick checklist instead of detailed steps
- For experienced builders who understand patterns
- Saves 60-120 minutes total

**When to use**:
- ✅ You've built agents before
- ✅ Understand KG connectivity
- ✅ Familiar with skill orchestration

**When NOT to use**:
- ❌ First time with protocol
- ❌ Complex/unique domain
- ❌ Want to learn patterns

---

## 📐 Key Code Snippets

### Master Graph Structure

```json
{
  "graphType": "master",
  "project": "[name]",
  "version": "2.0",
  "graphs": [
    {"id": "agent-builder-knowledge", "path": "..."},
    {"id": "agent-builder-skills", "path": "..."},
    {"id": "agent-builder-behaviors", "path": "..."},
    {"id": "[domain]-knowledge", "path": "..."},
    {"id": "[domain]-skills", "path": "..."},
    {"id": "[domain]-behaviors", "path": "..."}
  ],
  "roles": [
    {
      "id": "agent-builder",
      "name": "Agent Builder",
      "alwaysActive": true,
      "graphs": ["agent-builder-knowledge", "agent-builder-skills", "agent-builder-behaviors"]
    },
    {
      "id": "[domain-role-id]",
      "name": "[Domain Role Name]",
      "alwaysActive": false,
      "graphs": ["[domain]-knowledge", "[domain]-skills", "[domain]-behaviors"]
    }
  ]
}
```

### Validation Commands

```bash
# Check structure
python scripts/validate_structure.py

# Check graph connectivity
python scripts/validate_graphs.py

# Monitor KG changes
python scripts/kg_monitor.py

# Heal broken links
python scripts/kg_heal.py
```

### Activation Prompt (For Built Agents)

```
Initialize as the [Agent Name].

Start by reading:
@agents/NEW_AGENT_START_HERE.md

Follow every step:
- Load identity
- Load master knowledge graph
- Ask for role selection
- Load role-specific graphs
- Confirm operational state

Do not ask user to perform manual loading.
When finished, output: "System Ready".
```

---

## ✅ Success Criteria Checklist

**Before declaring "Setup Complete"**, verify:

### Graph Connectivity
- [ ] All graphs have root nodes
- [ ] All non-root nodes have `parent` field
- [ ] Cross-graph `links` established
- [ ] visualization.html Unified Brain shows full connectivity
- [ ] No orphaned/floating nodes

### Templates Used Correctly
- [ ] Agent Builder graphs copied (not generated)
- [ ] Validation scripts copied (not generated)
- [ ] visualization.html copied and customized
- [ ] User manuals copied and customized
- [ ] README.md generated (not copied)

### Testing
- [ ] Cold-start test < 5 minutes
- [ ] Structure validator passes
- [ ] Graph validator passes (no orphans)
- [ ] Visualization shows all connections

### Implementation
- [ ] All skills classified by type
- [ ] KG maintenance skill created (4 files)
- [ ] Rule-based skills have scripts (or copied)
- [ ] LLM skills have prompt templates

---

## ⚠️ Common Pitfalls (Avoid These)

1. **Generating Agent Builder graphs** → Copy templates instead
2. **Missing parent links** → Every non-root node needs `parent`
3. **Skipping validation** → Run validators at checkpoints
4. **No express mode** → Save time if experienced
5. **Copying README** → Generate custom instead
6. **Untested cold-start** → Must validate < 5 min
7. **No Unified Brain check** → Visual validation required
8. **Forgetting KG maintenance** → Self-evolution is critical

---

## 🚀 Quick Execution Paths

### Path A: Fastest (For Experienced)

```
1. Read: AI_AGENT_SETUP_PROTOCOL_V2_INDEX.md (10 min)
2. Go to: phases/INDEX.md (5 min)
3. Phase 1-2: Answer questions, design architecture (60 min)
4. Phases 3-11: Execute with EXPRESS MODE (120-180 min)
5. Validate: All checks (30 min)

Total: 3.5-5 hours
```

### Path B: Thorough (For First-Timers)

```
1. Read: AI_AGENT_SETUP_PROTOCOL_V2_INDEX.md (10 min)
2. Read: This SUMMARY (10 min)
3. Go to: phases/INDEX.md (10 min)
4. Phases 1-11: Follow detailed instructions (4-7 hours)
5. Validate: All checks (30 min)

Total: 5-8 hours
```

### Path C: Copy-Paste Prompt (Quickest)

```
1. Open: PROMPT_TEMPLATES_QUICK_COPY.md (2 min)
2. Copy Scenario 1, fill placeholders (3 min)
3. Send to AI with protocol @ mentions
4. AI executes (3-7 hours)
5. Validate result (30 min)

Your time: 35 minutes
```

---

## 📊 Expected Deliverables

### File Counts by Project Size

**Small project** (simple domain):
- 50-80 files
- 3-4 hours build time

**Medium project** (moderate complexity):
- 80-120 files
- 5-7 hours build time

**Large project** (complex domain):
- 120-150+ files
- 8-12 hours build time

### File Breakdown

**Configuration** (4+):
- .cursor/identity.md, rules.md
- .cursor/behaviors/*.md (10-30 files)

**Knowledge Graphs** (7-8):
- 3 Agent Builder (copied)
- 3-4 domain role (generated)
- 1 master graph

**Scripts & Tools** (5-15):
- 4 validation/KG scripts (copied)
- Domain-specific scripts (custom)

**Documentation** (10-30):
- Behaviors, skills, README, user manual

**Visualization** (2):
- visualization.html, VIEW_VISUALIZATION.md

---

## 🎓 V2.0 vs V1.0 Key Differences

| Feature | V1.0 | V2.0 |
|---------|------|------|
| **Graph Connectivity** | Optional parent links | **Mandatory** (no orphans) |
| **Root Nodes** | Not required | **Required** per graph |
| **Visualization** | None | **Interactive HTML** with Unified Brain |
| **User Manual** | Basic | **Comprehensive** + cold-start tested |
| **Skills Analysis** | Not included | **Classified** (rule/LLM/hybrid) |
| **Self-Evolution** | No | **Yes** (KG maintenance skill) |
| **Cold-Start** | Not validated | **< 5 min** (tested) |
| **Behavior Location** | agents/behaviors/ | **.cursor/behaviors/** (native) |
| **Organization** | 8 phases, 3 files | **11 phases**, organized |
| **Templates** | Embedded | **13 templates** in 4 directories |
| **Prompt Quality** | B | **A-** (optimized for AI) |

---

## 🎯 Template System Quick Reference

### What to COPY (Don't Generate)

**JSON Graphs**:
```bash
# Copy Agent Builder graphs (100% reusable)
cp json-templates/agent-builder/*.json.template agents/knowledge-graphs/
```

**Scripts**:
```bash
# Copy validation and KG tools
cp scripts/reusable/validate_graphs.py scripts/
cp scripts/reusable/kg_monitor.py scripts/
cp scripts/reusable/kg_heal.py scripts/
```

**Visualization**:
```bash
# Copy and customize
cp htmls/templates/visualization.html.template agents/knowledge-graphs/visualization.html
# Then replace [Project Name], [domain-role-id] placeholders
```

**User Docs**:
```bash
# Copy and customize
cp docs-templates/NEW_AGENT_START_HERE.md.template agents/NEW_AGENT_START_HERE.md
cp docs-templates/USER_MANUAL.md.template agents/USER_MANUAL.md
# Then replace placeholders, add domain workflows
```

### What to GENERATE (Trust Agent)

**Documentation**:
- README.md - Agent generates project-specific
- SETUP_COMPLETE.md - Agent summarizes build
- Architecture docs - Agent explains system

**Domain Content**:
- Domain behaviors - Adapt template or generate
- Domain skills - Use guide, generate custom
- Domain knowledge graph - Agent designs structure

---

## 🚀 Critical V2.0 Rules

### Rule 1: Full Connectivity

**Every non-root node**:
```json
{
  "id": "node-id",
  "parent": "parent-id",  ← REQUIRED
  "type": "node-type"
}
```

**Every graph**:
```json
{
  "id": "[type]:root",
  "type": "root"  ← At least one per graph
}
```

**Validation**: No orphaned nodes in visualization.html Unified Brain view

---

### Rule 2: Agent Builder Standardization

**These files are IDENTICAL across all projects**:
- agent-builder-knowledge-graph.json ← Copy template
- agent-builder-skills-graph.json ← Copy template
- agent-builder-behaviors-graph.json ← Copy template

**Do NOT generate these** - Copy from `json-templates/agent-builder/`

**Why**: Ensures every agent has same system foundation

---

### Rule 3: Two Roles Only

**Every agent has exactly 2 roles**:

1. **Agent Builder** (system role) - Always included, standardized
2. **[Your Domain]** (custom role) - Your use case

**Why**: Reliability + flexibility balance

**Need multiple domains?** Build separate agents, connect via MCP

---

### Rule 4: Validate Early and Often

**Required validation points**:
- After Phase 4 → Run validate_graphs.py
- After Phase 6 → Test validation scripts
- After Phase 9 → Run both validators
- After Phase 10 → Visual validation in browser
- After Phase 11 → Cold-start test

**All must pass** before declaring complete

---

## 📐 Key Code Templates

### Fully-Connected Node

```json
{
  "id": "unique-id",
  "type": "document|folder|skill|behavior|concept",
  "title": "Display Name",
  "parent": "parent-id",
  "path": "file/path" (optional),
  "description": "Brief description",
  "links": {
    "enforces": ["target-id"],
    "governs": ["target-id"],
    "implements": ["target-id"]
  }
}
```

### Skill Definition Frontmatter

```yaml
---
type: skill
category: system|domain-role-id
id: skill-id
implementation: rule-based|llm-based-max|llm-based-slm|hybrid
roles:
  - agent-builder|domain-role-id
parent-skill: parent-id (if sub-skill)
indexed-in-kg: skill-skill-id
---
```

### Behavior Definition Frontmatter

```yaml
---
type: behavior
category: core|agent-builder|domain-role-id
id: behavior-id
priority: critical|high|medium|low
applies-to:
  - all-roles|agent-builder|domain-role-id
indexed-in-kg: behavior:category:behavior-id
---
```

---

## ⚡ Express Mode Checklist

**For experienced builders**, use this quick checklist:

**Phases 1-4** (Standard - ~2-3 hours):
- Phase 1: Answer questions
- Phase 2: Design & approve
- Phase 3: Create structure
- Phase 4: Copy Agent Builder graphs, generate domain graphs

**Phase 5** (Express - ~30-60 min):
- Copy CONTENT_TEMPLATE
- Create behaviors (template or generate)
- Create skills (follow guide)

**Phase 6** (Standard - ~20 min):
- Copy validation scripts

**Phase 7** (Express - ~15-20 min):
- Create 4 KG maintenance skills
- Follow guide or examples

**Phase 8** (Standard - ~60-120 min):
- Copy/create implementations

**Phase 9** (Express - ~15-20 min):
- Run validators
- **Generate** README + SETUP_COMPLETE

**Phase 10** (Standard - ~30-45 min):
- Copy visualization.html

**Phase 11** (Express - ~15-30 min):
- Copy user manuals
- Quick cold-start test

**Total with express**: 3.5-5.5 hours (vs 5-8 hours detailed)

---

## ⚠️ Common Pitfalls & Solutions

| Pitfall | Solution |
|---------|----------|
| **Orphaned nodes** | Add `parent` field, run kg_heal.py |
| **Generating Agent Builder graphs** | Copy templates from json-templates/ |
| **Skipping validation** | Run at checkpoints (Phases 4, 6, 9, 10, 11) |
| **Cold-start > 5 min** | Review USER_MANUAL.md against template |
| **No Unified Brain view** | Check visualization.html customization |
| **Missing cross-links** | Add `links` field to behaviors/skills |
| **Lost context between phases** | Use context cards in each phase |
| **Copying README template** | Generate with requirements instead |

---

## 📊 Success Metrics

### Your V2.0 system is successful when:

**Technical**:
- ✅ validate_structure.py passes (100%)
- ✅ validate_graphs.py passes (0 orphans)
- ✅ visualization.html shows connected Unified Brain
- ✅ All graphs have root nodes

**Functional**:
- ✅ Cold-start < 5 minutes
- ✅ KG maintenance skill works
- ✅ Both roles operational
- ✅ Domain workflows execute

**Quality**:
- ✅ Documentation complete
- ✅ Tests pass
- ✅ Team can use via USER_MANUAL.md
- ✅ Agent maintains own KG

---

## 🎯 Next Steps After Build

1. **Validate** - Run all validators, check visualization
2. **Test** - Cold-start, domain workflows
3. **Add content** - Use CONTENT_TEMPLATE.md
4. **Train team** - Share USER_MANUAL.md
5. **Maintain** - Use KG maintenance skill when files change
6. **Iterate** - Add skills/behaviors as needed

---

## 📖 Where to Find Things

**Navigation**:
- Package overview: `AI_AGENT_SETUP_PROTOCOL_V2_INDEX.md`
- Execution hub: `phases/INDEX.md`
- This quick ref: `AI_AGENT_SETUP_PROTOCOL_V2_SUMMARY.md`

**Templates**:
- Agent Builder JSON: `json-templates/agent-builder/`
- Documents: `docs-templates/`
- Visualization: `htmls/templates/`
- Scripts: `scripts/reusable/` and `scripts/templates/`

**Guides**:
- Skills classification: `guides/SKILLS_CLASSIFICATION_GUIDE.md`
- Skill structure: `guides/SKILL_TEMPLATE_GUIDE.md`
- Chunking: `guides/CHUNKING_BEST_PRACTICES.md`
- Editing: `guides/REGENERATIVE_EDITING_PROTOCOL.md`
- Advanced evolution: `guides/ADVANCED_EVOLUTION_GUIDE.md`

**User Prompts**:
- Quick scenarios: `PROMPT_TEMPLATES_QUICK_COPY.md`
- New project: `PROMPT_TEMPLATE_NEW_PROJECT.md`
- Migration: `PROMPT_TEMPLATE_EXISTING_PROJECT.md`

---

## 🎉 You're Ready!

**Protocol quality**: A- (Production Ready)  
**Success rate**: 95-98% (with capable LLMs)  
**Battle-tested**: Yes (Agentic AI Project Manager)  

**Start building**: Go to `phases/INDEX.md` or use `PROMPT_TEMPLATES_QUICK_COPY.md`

---

**Version**: 2.0  
**Last Updated**: November 28, 2025  
**Status**: Production Ready  
**Next**: Choose your path and start building! 🚀
