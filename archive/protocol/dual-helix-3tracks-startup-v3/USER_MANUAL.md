# User Manual: Building Your AI Agent with Protocol V3.0

**Use Case**: Build a production-ready dual-role AI agent from scratch  
**Expected Time**: 2-4 hours (depending on domain complexity)  
**Last Updated**: November 29, 2025

---

## 🎯 What This Manual Is For

This manual guides **YOU** (the project owner) through using the `dual-helix-3tracks-startup-v3` package to build a custom AI agent for your domain.

**This is NOT** the manual for using your finished agent - that will be generated in Phase 8.

---

## 🤖 AI Model Requirements

**Recommended** (Best Results):

- **Claude Sonnet 4.5** ⭐ - Optimal for all 9 phases
- **Claude Sonnet 4** - Excellent, slightly cheaper
- **Cursor/Antigravity** - Designed for complex agentic workflows

**Minimum** (Needs More Review):

- **Claude Sonnet 3.5** - May struggle with Phase 2 architecture design
- **GPT-4 Turbo / GPT-4o** - Needs careful validation

**Why Claude 4.5 recommended**:

- ✅ Excellent at nested KG structures (Phase 4)
- ✅ Strong context retention (long sessions)
- ✅ Reliable file regeneration
- ✅ Can follow complex multi-phase protocols

**Cost**: ~$15-40 for complete setup (one-time)

---

## 📋 Before You Start

### Preparation Checklist

Gather this information before beginning:

- [ ] **Project domain** (e.g., Healthcare, Education, Legal, Project Management)
- [ ] **Domain role name** (e.g., "Medical Assistant", "Code Reviewer", "Data Analyst")
- [ ] **Primary tasks** (3-7 things the agent should do)
- [ ] **Key behaviors** (3-5 rules/protocols it must follow)
- [ ] **Content sources** (optional: existing docs, code, knowledge base)
- [ ] **Confidentiality needs** (if any)

### Setup Your Project

1. **Create project folder**:

   ```bash
   mkdir my-agent-project
   cd my-agent-project
   ```

2. **Create content folder**:

   ```bash
   mkdir content-raw
   ```

3. **Copy protocol package**:
   - Copy entire `dual-helix-3tracks-startup-v3/` folder into `my-agent-project/`

4. **Verify structure**:

   ```
   my-agent-project/
   ├── content-raw/                    (your domain content)
   └── dual-helix-3tracks-startup-v3/  (protocol package)
   ```

---

## 🚀 Magic Activation Prompt

Copy this entire block and send to your AI assistant:

```
# Task: Build Custom AI Agent Using Protocol V3.0

Read the protocol package:
@dual-helix-3tracks-startup-v3/phases/INDEX.md

Start with Phase 0 to verify environment setup.

## My Project Definition

**Domain**: [e.g., Healthcare, Education, Legal, Software Development]
**Purpose**: [1-2 sentence description of what this agent will do]
**Primary users**: [Who will interact with this agent]

## Domain Role (Custom Role)

**Role name**: [e.g., "Project Manager", "Code Reviewer", "Research Assistant"]
**Role ID**: [lowercase-hyphenated, e.g., "project-manager"]
**Personality**: [formal/casual/empathetic/technical]
**Communication style**: [how should agent speak to users]

**Primary tasks** this role performs:
1. [Task 1]
2. [Task 2]
3. [Task 3]
4. [Task 4 - optional]
5. [Task 5 - optional]

**Boundaries** (what it won't do):
- [Boundary 1]
- [Boundary 2]

## Knowledge Requirements

**Content sources**:
[Describe what knowledge the agent needs]

**If you have existing content folders**:
@[folder-path] - [Brief description]
[The agent will analyze and map these to KG structure]

**If starting fresh**:
[Describe what content types will be needed]

## Skills & Capabilities

The agent should be able to:
- [Capability 1 - be specific]
- [Capability 2 - be specific]
- [Capability 3 - be specific]
- [Add more as needed]

## Workflows & Rules

**Critical workflows** (if any):
[Describe multi-step processes, or write "Design appropriate ones"]

**Safety boundaries** (if any):
[Describe what must never happen, or write "Standard safety protocols"]

**Confidentiality** (if any):
[Describe data separation needs, or write "None"]

---

## Instructions for AI

Follow the AI Agent Setup Protocol V3.0 (9 phases):

### Phase 0: Environment Setup (5 min)
- Verify Python 3.9+ installed
- Confirm project structure is correct
- Test validation scripts

### Phase 1: Information Discovery (30-60 min)
- Ask me all discovery questions
- Gather complete requirements
- Validate understanding with me
- Write output/phase-01.md

### Phase 2: Architecture Design (30-45 min)
- Design domain knowledge structure
- Design skills (3-7 typical)
- Design behaviors (3-5 typical)
- **PRESENT ARCHITECTURE FOR MY APPROVAL** before Phase 3
- Write output/phase-02.md

### Phases 3-8: Execution (1.5-3 hours)
- Execute all remaining phases sequentially
- Validate at checkpoints (after Phases 3, 4, 6, 7)
- Generate all documentation

### Final Delivery
- Run validation scripts (should pass 100%)
- Open visualization-dynamic.html (show me the KG)
- Test magic activation prompt (< 5 min target)
- Generate comprehensive summary

---

## V3.0 Critical Requirements

Ensure these are implemented:

1. ✅ **Two-role architecture**:
   - Agent Builder (system role) - standardized, always active
   - [Your domain role] (custom role) - tailored to domain

2. ✅ **Fully-connected Knowledge Graphs** (7 files total):
   - master-graph.json (links all graphs)
   - 3 builder graphs (knowledge, skills, behaviors)
   - 3 domain graphs (knowledge, skills, behaviors)

3. ✅ **Builder assets copied** (Phase 3):
   - All files from builder-assets/ folder
   - Validation scripts functional
   - Visualization tool working

4. ✅ **User documentation** (Phase 8):
   - NEW_AGENT_START_HERE.md (agent initialization)
   - USER_MANUAL.md (user reference)
   - Magic activation prompt for < 5 min startup

5. ✅ **Validation passing**:
   - Structure validation (Phase 3)
   - Graph validation (Phase 4)
   - All nodes connected, no orphans

---

BEGIN with Phase 0: Environment Setup
```

---

## 📝 Example: Filled Prompt

Here's how the prompt looks filled in for a **Project Manager Agent**:

<details>
<summary>Click to expand example</summary>

```
# Task: Build Custom AI Agent Using Protocol V3.0

Read the protocol package:
@dual-helix-3tracks-startup-v3/phases/INDEX.md

Start with Phase 0 to verify environment setup.

## My Project Definition

**Domain**: Project Management
**Purpose**: Assist project managers with task tracking, team coordination, and project health monitoring across multiple concurrent projects.
**Primary users**: Project managers, team leads, stakeholders

## Domain Role (Custom Role)

**Role name**: Project Manager Assistant
**Role ID**: project-manager
**Personality**: Professional, organized, proactive
**Communication style**: Clear, action-oriented, uses project management terminology

**Primary tasks** this role performs:
1. Track project status and milestones
2. Identify blockers and risks
3. Generate status reports and summaries
4. Coordinate team activities and dependencies
5. Maintain project documentation

**Boundaries** (what it won't do):
- Will NOT make final project decisions (assists only)
- Will NOT replace human project manager judgment
- Will NOT access confidential HR or financial data

## Knowledge Requirements

**Content sources**:
Project management methodologies, templates, best practices

**If you have existing content folders**:
@content-raw/templates - Project templates and workflows
@content-raw/methodologies - Agile, Waterfall, Hybrid guides

## Skills & Capabilities

The agent should be able to:
- Analyze project status and identify risks
- Generate status reports from project data
- Suggest task prioritization based on dependencies
- Track team capacity and workload
- Maintain project knowledge base

## Workflows & Rules

**Critical workflows**:
1. Daily standup summary generation
2. Weekly status report compilation
3. Risk identification and escalation
4. Project health scoring

**Safety boundaries**:
- Never share project data across confidentiality boundaries
- Always flag high-risk items for human review
- Maintain audit trail of all recommendations

**Confidentiality**:
- Separate public, personal, and work project data
- No cross-contamination between client projects

---

[Rest of instructions same as template above]

BEGIN with Phase 0: Environment Setup
```

</details>

---

## 📄 Document Chunking Guidelines

To ensure optimal AI performance, Protocol V3.0 enforces strict document size limits.

### The 500-Line Rule

- **Limit**: No AI-consumed file should exceed **500 lines**.
- **Why**: Large files degrade LLM reasoning and working memory.
- **Solution**: Split large topics into **Concept** (What/Why) and **Execution** (How/Steps).

### Tools Available

- **Validation**: `python scripts/validate_chunking.py [folder]`
- **Auto-Chunking**: Use the `skill-chunk-document` to split oversized files safely.

### Best Practices

1. **One Concept Per File**: Don't mix unrelated topics.
2. **Link, Don't Repeat**: Use `[Link Text](path/to/file.md)` instead of copying content.
3. **Use Indexes**: Every folder with >3 files needs an `INDEX.md`.

---

## 🔄 Resuming After Interruption

If you stop at any point, use these prompts to resume:

### 🪄 Check Current Status

```
Check my current progress in the Protocol V3.0 build:

1. List all files in dual-helix-3tracks-startup-v3/outputs/
2. Read the most recent phase output file
3. Tell me:
   - Which phase was last completed
   - What was generated
   - What the next step should be
   - Any issues found

Then ask if I want to continue from there.
```

### 🪄 Resume from Specific Phase

```
Resume Protocol V3.0 build from Phase [X]:

1. Read dual-helix-3tracks-startup-v3/outputs/phase-0[X-1].md (previous phase)
2. Read dual-helix-3tracks-startup-v3/phases/PHASE_0[X]_*.md (current phase instructions)
3. Summarize what was done and what's next
4. Continue execution from Phase [X]
```

### 🪄 Validate Current State

```
Validate my current Protocol V3.0 build state:

1. Run: python dual-helix-3tracks-startup-v3/builder-assets/scripts/validate_structure.py
2. If graphs exist, run: python dual-helix-3tracks-startup-v3/builder-assets/scripts/validate_graphs.py
3. List any missing files or errors
4. Suggest fixes for any issues found
```

---

## 🛠️ Troubleshooting Guide

### Problem: Agent doesn't understand the protocol

**🪄 Prompt**:

```
Re-read the protocol structure:
@dual-helix-3tracks-startup-v3/phases/INDEX.md

Then read the current phase instructions:
@dual-helix-3tracks-startup-v3/phases/PHASE_0[X]_*.md

Summarize the phase objective and steps, then continue.
```

### Problem: Phase output is missing or incomplete

**🪄 Prompt**:

```
Check if dual-helix-3tracks-startup-v3/outputs/phase-0[X].md exists.

If missing: Regenerate it following the spec at dual-helix-3tracks-startup-v3/specs/phase-0[X]-output.spec.md

If incomplete: Compare against spec and add missing sections.
```

### Problem: Validation scripts fail

**🪄 Prompt**:

```
Run validation and diagnose issues:

1. python dual-helix-3tracks-startup-v3/builder-assets/scripts/validate_structure.py
2. For each missing file/folder, explain why it's needed
3. Suggest which phase should have created it
4. Offer to fix by re-running that phase step
```

### Problem: Knowledge Graph has orphaned nodes

**🪄 Prompt**:

```
Diagnose and heal the Knowledge Graph:

1. Open agents/knowledge-graphs/visualization-dynamic.html in browser
2. Look for disconnected nodes (no parent links)
3. For each orphan, identify its correct parent
4. Update the graph JSON files to fix connections
5. Re-run validation
```

### Problem: Architecture design doesn't match my needs

**🪄 Prompt**:

```
Let's revise the Phase 2 architecture:

Read: dual-helix-3tracks-startup-v3/outputs/phase-02.md

I want to change:
- [Describe what needs to change]

Update the architecture design and regenerate phase-02.md.
Then ask if I want to continue to Phase 3 with the new design.
```

### Problem: Generated files don't follow specs

**🪄 Prompt**:

```
Verify [filename] follows its spec:

1. Read the spec: dual-helix-3tracks-startup-v3/specs/[spec-name].spec.md
2. Read the generated file: [path]
3. List any deviations from spec
4. Regenerate the file correctly
```

---

## ⏱️ Time Estimates

**By project complexity**:

| Complexity | Phases 0-2 | Phases 3-8 | Total |
|------------|------------|------------|-------|
| **Simple** | 45 min | 1.5-2 hours | **2-3 hours** |
| **Medium** | 1 hour | 2.5-3.5 hours | **3.5-4.5 hours** |
| **Complex** | 1.5 hours | 3-5 hours | **4.5-6.5 hours** |

**Simple**: Single domain, 3-5 skills, clear workflows  
**Medium**: Multiple categories, 5-7 skills, some complexity  
**Complex**: Deep hierarchy, 7+ skills, intricate relationships

---

## ✅ Post-Build Checklist

After AI completes the build, verify:

- [ ] All validators pass (structure + graphs)
- [ ] visualization-dynamic.html opens and shows all graphs
- [ ] No orphaned nodes in visualization
- [ ] Magic activation prompt works (< 5 min test)
- [ ] NEW_AGENT_START_HERE.md is clear and complete
- [ ] USER_MANUAL.md has domain-specific workflows
- [ ] All 7 knowledge graphs exist and are valid
- [ ] Domain skills and behaviors are documented

**If all checked**: ✅ Your AI agent system is ready to use!

---

## 🎯 Next Steps After Build

1. **Test the magic prompt** - Use NEW_AGENT_START_HERE.md to initialize
2. **Add domain content** - Populate docs/[domain-role-id]/ folders
3. **Test domain workflows** - Verify agent can perform primary tasks
4. **Iterate** - Add skills/behaviors as needs evolve
5. **Maintain KG** - Use builder skills when structure changes

---

## 📚 Reference Documents

**In the protocol package**:

- `phases/INDEX.md` - Overview of all 9 phases
- `phases/PHASE_0X_*.md` - Detailed instructions for each phase
- `specs/*.spec.md` - Technical specifications for all outputs
- `examples/*.md` - Reference templates
- `V3_DESIGN_SUMMARY.md` - Protocol design philosophy

**Generated during build**:

- `outputs/phase-0X.md` - Output summary for each phase
- `agents/NEW_AGENT_START_HERE.md` - Agent initialization guide
- `agents/USER_MANUAL.md` - End-user reference

---

## 💡 Tips for Success

1. **Be specific in Phase 1** - Clear requirements = better architecture
2. **Review Phase 2 carefully** - Architecture changes are hard later
3. **Use prompts for everything** - Even if you can check manually, let the agent help
4. **Save phase outputs** - They're your build documentation
5. **Test early, test often** - Run validators after each major phase
6. **Don't skip visualization** - Visual check catches issues text can't

---

**Version**: 3.0  
**Last Updated**: November 29, 2025  
**Status**: Production Ready
