# Prompt Template: Start New Project with V2.0 Protocol

**Use Case**: Starting a brand new agentic AI project from scratch  
**Expected Time**: 3-7 hours (depending on complexity)  
**Last Updated**: November 28, 2025

---

## 🤖 AI Model Requirements

**Recommended** (Best Results):
- **Claude Sonnet 4.5** ⭐ - Optimal for all 11 phases
- **Claude Sonnet 4** - Excellent, slightly cheaper
- **GPT-5+** - Should perform similarly (when available)

**Minimum** (Needs More Review):
- **Claude Sonnet 3.5** - May struggle with Phase 2 architecture design
- **GPT-4 Turbo / GPT-4o** - Needs careful validation

**Why Claude 4.5 recommended**:
- ✅ Excellent at nested KG structures (Phase 4)
- ✅ Strong context retention (long sessions)
- ✅ Reliable file regeneration
- ✅ Can simulate cold-start scenarios (Phase 11)

**Cost**: ~$20-50 for complete setup (one-time)

---

## 📋 Preparation Checklist

Before using this prompt, prepare:

- [ ] Project domain and purpose (clear description)
- [ ] Domain role definition (name, tasks, personality)
- [ ] Key capabilities needed (3-10 skills)
- [ ] Critical workflows or rules (if any)
- [ ] Source materials (optional: existing docs, code, etc.)
- [ ] Confidentiality requirements (if any)

---

## 🚀 The Complete Prompt

Copy this entire block and send to your AI assistant:

```
Read the protocol package structure:
@temp/dual-helix-3tracks-startup/AI_AGENT_SETUP_PROTOCOL_V2_INDEX.md

Then go to the execution index:
@temp/dual-helix-3tracks-startup/phases/INDEX.md

# Task: Build New Agentic AI System Using V2.0 Protocol

## Project Definition

**Domain**: [e.g., Healthcare, Education, Legal, Software Development, Research]
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
[Describe what knowledge the agent needs access to]

**If you have existing content folders**:
@[folder-path-1] - [Brief description]
@[folder-path-2] - [Brief description]
[The agent will analyze and map these to KG structure]

**If starting fresh**:
[Describe what content types will be needed: documentation, policies, code, etc.]

## Skills & Capabilities

The agent should be able to:
- [Capability 1 - be specific]
- [Capability 2 - be specific]
- [Capability 3 - be specific]
- [Add more as needed]

## Workflows & Rules

**Critical workflows** (if any):
[Describe multi-step processes that must be followed, or write "None - design appropriate ones"]

**Safety boundaries** (if any):
[Describe what must never happen, or write "Standard safety protocols"]

**Confidentiality** (if any):
[Describe data separation needs, or write "None"]

---

## Instructions for AI

**Follow the AI Agent Setup Protocol V2.0** (11 phases):

### Phase 1: Information Discovery (30-60 min)
- Ask me all discovery questions
- Gather complete requirements
- Validate understanding with me

### Phase 2: Architecture Design (30-45 min)
- Design behavior taxonomy
- Design fully-connected KG structure  
- Classify all skills by implementation type
- **PRESENT ARCHITECTURE FOR MY APPROVAL** before Phase 3

### Phases 3-11: Execution (2-6 hours)
- Execute all remaining phases sequentially
- Use **EXPRESS MODE** in Phases 5, 7, 9, 11 (if you understand patterns)
- Validate at checkpoints (after Phases 4, 6, 9, 10, 11)

### Final Delivery
- Run both validators (should pass 100%)
- Open visualization.html (show me Unified Brain view)
- Perform cold-start test (< 5 min target)
- Generate comprehensive summary

---

## V2.0 Critical Requirements

**Ensure these are implemented**:

1. ✅ **Two-role architecture**:
   - Agent Builder (system role) - standardized, always active
   - [Your domain role] (custom role) - tailored to domain

2. ✅ **Fully-connected Knowledge Graphs**:
   - Every graph has root node
   - Every non-root node has `parent` field
   - Cross-graph links via `links` field

3. ✅ **Agent Builder templates** (copy, don't generate):
   - agent-builder-knowledge-graph.json
   - agent-builder-skills-graph.json
   - agent-builder-behaviors-graph.json

4. ✅ **Validation tools** (copy from protocol):
   - validate_graphs.py
   - validate_structure.py
   - kg_monitor.py
   - kg_heal.py

5. ✅ **Visualization** (copy and customize):
   - visualization.html
   - Unified Brain view functional

6. ✅ **User manual** (copy and customize):
   - NEW_AGENT_START_HERE.md
   - USER_MANUAL.md
   - Cold-start < 5 minutes

7. ✅ **KG maintenance skill**:
   - Self-evolution capability
   - Monitor, update, heal sub-skills

8. ✅ **Documentation** (generate, don't copy):
   - README.md (custom for project)
   - SETUP_COMPLETE.md (summary of build)

---

## Template vs Generate Guide

**For this build, follow these rules**:

**COPY these templates** (Level 1 - Required):
- Agent Builder JSON graphs (3 files)
- Validation scripts (4 files)
- visualization.html

**COPY AND CUSTOMIZE** (Level 2 - Recommended):
- NEW_AGENT_START_HERE.md
- USER_MANUAL.md
- TEST_PROTOCOL.md

**GENERATE CUSTOM** (Level 3 - Trust AI):
- README.md (requirements provided in Phase 9)
- SETUP_COMPLETE.md (requirements provided in Phase 9)
- Domain role behaviors (adapt template or generate)

**Reference**: See phases/INDEX.md for complete decision framework

---

BEGIN with Phase 1: Information Discovery
```

---

## 📝 Example: Filled Prompt

Here's how the prompt looks filled in for a **Medical Diagnosis Agent**:

<details>
<summary>Click to expand example</summary>

```
Read the protocol package structure:
@temp/dual-helix-3tracks-startup/AI_AGENT_SETUP_PROTOCOL_V2_INDEX.md

Then go to the execution index:
@temp/dual-helix-3tracks-startup/phases/INDEX.md

# Task: Build New Agentic AI System Using V2.0 Protocol

## Project Definition

**Domain**: Healthcare / Medical Diagnosis
**Purpose**: Assist doctors with differential diagnosis by analyzing symptoms, medical history, and test results to suggest possible conditions and recommend next steps.
**Primary users**: Medical professionals (doctors, nurses, medical students)

## Domain Role (Custom Role)

**Role name**: Medical Diagnosis Assistant
**Role ID**: medical-diagnosis
**Personality**: Professional, empathetic, evidence-based
**Communication style**: Clear medical terminology, patient-focused, always cites sources

**Primary tasks** this role performs:
1. Analyze patient symptoms and generate differential diagnosis
2. Recommend appropriate diagnostic tests
3. Explain medical concepts in accessible language
4. Track patient history and identify patterns
5. Provide evidence-based treatment options

**Boundaries** (what it won't do):
- Will NOT provide final diagnoses (only assist/suggest)
- Will NOT replace doctor judgment
- Will ALWAYS recommend consulting physician for serious symptoms

## Knowledge Requirements

**Content sources**:
Medical knowledge base including diagnostic criteria, treatment guidelines, drug interactions

**Starting fresh**: Will need
- Medical symptom databases
- Diagnostic criteria documentation
- Treatment protocols
- Drug interaction guides

## Skills & Capabilities

The agent should be able to:
- Analyze symptom patterns and generate differential diagnosis
- Query medical databases for relevant information
- Explain complex medical concepts clearly
- Track patient history across visits
- Recommend evidence-based next steps
- Identify urgent vs non-urgent cases

## Workflows & Rules

**Critical workflows**:
1. Symptom Analysis → Differential Diagnosis → Test Recommendations → Treatment Options
2. Always cite medical sources
3. Flag urgent symptoms immediately

**Safety boundaries**:
- Never provide final diagnosis (assist only)
- Always recommend physician consultation for serious symptoms
- No prescription recommendations (suggest classes only)

**Confidentiality**:
- HIPAA compliance (no patient data in logs)
- Secure handling of medical information

---

[Rest of instructions same as template above]

BEGIN with Phase 1: Information Discovery
```

</details>

---

## ⏱️ Time Estimates

**By project complexity**:

| Complexity | Phase 1-2 | Phases 3-11 | Total |
|------------|-----------|-------------|-------|
| **Simple** | 1 hour | 2-3 hours | **3-4 hours** |
| **Medium** | 1.5 hours | 3.5-5.5 hours | **5-7 hours** |
| **Complex** | 2 hours | 6-10 hours | **8-12 hours** |

**With express mode** (experienced builders):
- Simple: 2.5-3 hours
- Medium: 4-5 hours
- Complex: 6-9 hours

---

## ✅ Post-Build Checklist

After AI completes the build, verify:

- [ ] All validators pass (structure + graphs)
- [ ] Visualization.html opens and shows Unified Brain view
- [ ] No orphaned nodes in visualization
- [ ] Cold-start test < 5 minutes
- [ ] README.md is clear and project-specific
- [ ] Agent Builder has KG maintenance skill tree
- [ ] Domain role has all expected skills
- [ ] Behaviors are documented and indexed

**If all checked**: ✅ Agent system is ready to use!

---

## 🎯 Next Steps After Build

1. **Test domain workflows** - Verify agent can perform primary tasks
2. **Add domain content** - Use CONTENT_TEMPLATE.md as guide
3. **Train team** - Use Scenario 10 to create onboarding
4. **Maintain KG** - Use Scenario 5 when files change
5. **Iterate** - Add skills/behaviors as needs evolve

---

**Version**: 2.0  
**Last Updated**: November 28, 2025  
**Status**: Production Ready
