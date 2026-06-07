# Phase 11: User Manual & Testing

**AI Agent Setup Protocol V2.0**

---

## 📌 Phase Context

**Prerequisites**: Phases 1-10 complete (all system components built)  
**Input needed from previous phases**:
- All Knowledge Graphs (Phase 4) - referenced in startup script
- All behaviors and skills (Phase 5, 7) - referenced in manual
- Visualization tool (Phase 10) - referenced in manual
- Domain role details (Phase 1) - for customization

**Output**: NEW_AGENT_START_HERE.md + USER_MANUAL.md + TEST_PROTOCOL.md  
**Estimated time**: 30-60 minutes (15-30 with express mode)

**Creates for**: Agent cold-start capability (<5 min operational)

**Success criteria**: Fresh agent becomes operational in < 5 minutes

---

## Objective

Create NEW_AGENT_START_HERE.md, USER_MANUAL.md, and perform cold-start testing to validate < 5 minute operational time.

---

## ⚡ Express Mode (For Experienced Builders)

**If you've created user manuals before and understand cold-start testing**:

1. ✅ Copy and customize `NEW_AGENT_START_HERE.md.template` (required - machine-executable)
2. ✅ Copy and customize `USER_MANUAL.md.template` (recommended - proven structure)
3. ✅ Copy `TEST_PROTOCOL.md.template` (optional - for systematic testing)
4. ✅ Perform quick cold-start validation
5. ✅ Skip to final checkpoint

**Templates recommended here**: NEW_AGENT_START_HERE (critical), USER_MANUAL (helpful)

**Time saved**: ~15-20 minutes

**If this is your first time**: Follow all steps below for comprehensive testing.

---

## Why This Phase Is Last

**Dependencies**:

- Phase 4: Knowledge Graphs must exist
- Phase 5: Behaviors and skills must be defined
- Phase 8: Skills must be implemented
- Phase 9: System must be validated
- Phase 10: Visualization must be available

**This phase creates the user-facing documentation** after everything is built and validated.

---

## Before You Begin

The protocol package includes **reusable document templates** for user-facing documentation.

**Location**: `[protocol-package]/docs-templates/`

- `NEW_AGENT_START_HERE.md.template` - Machine-executable startup script
- `USER_MANUAL.md.template` - Comprehensive prompt library
- `TEST_PROTOCOL.md.template` - Cold-start testing framework

See `[protocol-package]/docs-templates/README.md` for details.

---

## Action 11.1: Create NEW_AGENT_START_HERE.md

This is the **machine-executable startup script** for fresh agent instances.

**Step 1: Copy the template**:

```bash
# Copy from protocol package
cp [protocol-path]/docs-templates/NEW_AGENT_START_HERE.md.template agents/NEW_AGENT_START_HERE.md
```

**Step 2: Customize placeholders**:

Open `agents/NEW_AGENT_START_HERE.md` and replace:

1. **Lines 31, 53, 70, 147**: `[Domain Role Name]` → Your domain role name (e.g., "Project Manager")
2. **Lines 70-72, 147**: `[domain-role-id]` → Your domain role ID (e.g., "project-manager")
3. **Line 77**: `[domain]` → Your domain graph ID (e.g., "project-management")

**Example customization**:

```markdown
<!-- Before -->
### 2. [Domain Role Name] (Domain Role)

<!-- After -->
### 2. Project Manager (Domain Role)
```

**What this file does**:

- 7-step initialization process
- Agent Builder always loaded
- Domain Role optional activation
- Operational boundaries defined
- Reference card with bookmarks
- Emergency procedures

**Report**:

```
✅ Created agents/NEW_AGENT_START_HERE.md (Machine-Executable Startup Script)
```

---

## Action 11.2: Create USER_MANUAL.md

This is a **Prompt Library** for users to interact with the agent.

**Step 1: Copy the template**:

```bash
# Copy from protocol package
cp [protocol-path]/docs-templates/USER_MANUAL.md.template agents/USER_MANUAL.md
```

**Step 2: Customize placeholders**:

Open `agents/USER_MANUAL.md` and replace:

1. **Lines 1, 12**: `[Agent Name]` → Your agent name
2. **Line 4**: `[Date]` → Creation date
3. **Lines 39, 53, etc.**: `[Domain Role Name]` → Your domain role name
4. **Throughout**: `[TOPIC]`, `[SKILL_NAME]`, `[BEHAVIOR_NAME]` → Actual values

**Step 3: Add domain-specific workflows**:

In the section **"📋 [Domain Role Name] Workflows"** (around line 160), add your domain-specific workflows:

```markdown
## 📋 Project Manager Workflows

### Workflow: Create Project Plan

**When**: Starting a new project

**🪄 Prompt**:
\```text
Create a project plan for [PROJECT_NAME].
Include milestones, dependencies, and timeline.
Use the project-planning skill.
\```

### Workflow: Track Progress

**When**: Regular status updates

**🪄 Prompt**:
\```text
Review project progress for [PROJECT_NAME].
Identify blockers and suggest next steps.
\```
```

**What this file includes**:

- Magic activation prompt (quick start)
- Two-role system explanation
- Comprehensive prompt library
- Agent Builder workflows (KG maintenance)
- Domain Role workflows (customizable)
- Troubleshooting section
- Visualization guide
- Advanced usage examples

**Report**:

```
✅ Created agents/USER_MANUAL.md (Comprehensive Prompt Library)
```

---

## Action 11.3: Create Testing Protocol

**Step 1: Create testing directory**:

```bash
mkdir -p temp/user_manual_test
```

**Step 2: Copy the template**:

```bash
# Copy from protocol package (no customization needed)
cp [protocol-path]/docs-templates/TEST_PROTOCOL.md.template temp/user_manual_test/TEST_PROTOCOL.md
```

**What this file includes**:

- Detailed test procedure
- Success criteria checklist
- Failure scenarios
- Test log template
- Pain points documentation
- Improvements tracking

**Report**:

```
✅ Created temp/user_manual_test/TEST_PROTOCOL.md
```

---

## Action 11.4: Execute Cold-Start Test

**Present to human**:

```
🧪 Ready to execute cold-start test.

I will simulate a fresh agent with no context and follow only the USER_MANUAL.md.

Options:
1. I can simulate the test and document findings
2. You can test with a real fresh agent instance
3. Skip testing for now (not recommended)

Which would you prefer?
```

**If option 1 (Simulate)**:

1. "Forget" all setup context
2. Read only `agents/USER_MANUAL.md`
3. Follow quick start steps exactly
4. Document experience in `temp/user_manual_test/test_log.md`
5. Document pain points in `temp/user_manual_test/pain_points.md`
6. Document improvements in `temp/user_manual_test/improvements.md`
7. Report findings

**If option 2 (Real test)**:

Instruct human:

```
1. Open a new conversation tab
2. Upload only: agents/USER_MANUAL.md
3. Say: "Follow the quick start guide"
4. Time the process
5. Document any issues in temp/user_manual_test/
```

**If option 3 (Skip)**:

Note in validation checkpoint that testing was skipped.

---

## Action 11.5: Iterate Based on Test Results

**After testing**, review findings and update:

1. **USER_MANUAL.md**: Clarify ambiguous instructions
2. **NEW_AGENT_START_HERE.md**: Add missing steps
3. **Prompts**: Improve prompt templates
4. **Organization**: Restructure sections if needed

**Re-test if significant changes made**.

---

## Validation Checkpoint

```
✅ Phase 11 Complete - Protocol Finished!

Created:
- agents/NEW_AGENT_START_HERE.md (copied and customized from template)
- agents/USER_MANUAL.md (copied and customized from template)
- temp/user_manual_test/TEST_PROTOCOL.md (copied from template)

Cold-Start Test:
- [ ] Executed (or scheduled)
- [ ] Time to operational: < 5 minutes
- [ ] Agent successfully loaded all graphs
- [ ] Agent understood role boundaries
- [ ] No critical issues

🎉 ALL 11 PHASES COMPLETE!

The AI Agent Setup Protocol V2.0 is now fully implemented.
```

---

## Final Summary

**System Status**: ✅ Complete

**Deliverables**:

- ✅ 11 phases executed
- ✅ Knowledge Graphs created (fully connected)
- ✅ Behaviors defined
- ✅ Skills implemented
- ✅ Validation tools created
- ✅ Visualization tool created
- ✅ User manual created
- ✅ Cold-start testing framework created

**Agent Capabilities**:

- ✅ Two-role architecture (Agent Builder + Domain)
- ✅ Self-evolution (KG maintenance)
- ✅ < 5 minute cold-start
- ✅ Visual graph validation
- ✅ Comprehensive documentation

**Next Steps**:

1. Add domain-specific content
2. Test agent with real workflows
3. Iterate based on usage
4. Agent can maintain its own KG!

---

## Notes

**Why use templates?**

- ✅ **Separation of concerns**: Templates separate from phase instructions
- ✅ **Reusability**: Copy tested templates instead of writing from scratch
- ✅ **Consistency**: All projects use same structure
- ✅ **Maintainability**: Improve templates in one place
- ✅ **Clarity**: Phases focus on what to do, not full content

**Template locations**:

- `NEW_AGENT_START_HERE.md.template` - ~180 lines
- `USER_MANUAL.md.template` - ~280 lines
- `TEST_PROTOCOL.md.template` - ~120 lines

**For more details**: See `[protocol-package]/docs-templates/README.md`

---

**Previous Phase**: [Phase 10: Visualization Tool](PHASE_10_VISUALIZATION_TOOL.md)  
**🎉 END OF PROTOCOL - All 11 Phases Complete! 🎉**
