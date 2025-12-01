# Phase 6: Skills Implementation

**AI Agent Setup Protocol V3.0**

---

## Objective

Implement domain skills - write COMPLETE skill descriptions as if fully developed. Reference placeholder scripts for rule-based/hybrid skills.

---

## Step 1: Load Context

Read previous phase outputs (`output/`):

```
From Phase 2 (output/phase-02.md):
- Get [DOMAIN_ROLE_ID] and save to memory
- Skills list with implementation types

From Phase 5 (output/phase-05.md):
- Knowledge content (for skills to reference)
```

---

## Step 2: Generate Complete Skill Descriptions

**Load**: `agents/knowledge-graphs/[DOMAIN_ROLE_ID]-skills-graph.json`

**For each skill node**, generate COMPLETE content as if skill is fully developed:

### 2.1: For LLM-Based Skills

**Generate complete skill file** with prompt/methodology:

```markdown
---
[existing frontmatter]
implementation: llm-based
---

# [Skill Name]

## Purpose
[What this skill does]

## When to Use
[Scenarios, trigger conditions]

## Methodology

This skill uses LLM reasoning to [accomplish task].

### Prompt Strategy
[Describe the prompt approach]

### Context Provided
- [What context to include]
- [What information to pass]

### Expected Output
[What LLM should return]

## Procedure

1. **Prepare context**: [gather information]
2. **Construct prompt**: [build prompt with context]
3. **Call LLM**: [send to model]
4. **Parse response**: [extract result]
5. **Return**: [formatted output]

## Example

**Input**: [sample input]

**Prompt**: 
```

[Example prompt template]

```

**Output**: [sample output]

## Related
- Governed by: [behavior IDs]
- Uses knowledge: [knowledge node IDs]
```

**This is COMPLETE** - LLM-based skills are fully implemented ✅

### 2.2: For Rule-Based Skills

**Generate complete skill file** referencing placeholder script:

```markdown
---
[existing frontmatter]
implementation: rule-based
---

# [Skill Name]

## Purpose
[What this skill does]

## When to Use
[Scenarios, trigger conditions]

## Methodology

This skill uses deterministic logic implemented in `scripts/[script-name].py`.

### Algorithm
[Describe what the script does - high level]

## Procedure

1. **Validate input**: Check required fields
2. **Execute script**: Run `python scripts/[script-name].py [args]`
3. **Parse output**: Extract result from script
4. **Handle errors**: Check exit code, error messages
5. **Return**: Formatted result

## Script Reference

**File**: `scripts/[script-name].py`  
**Status**: ⚠️ PLACEHOLDER - Human developer must implement

**Expected behavior**:
- Input: [what script receives]
- Processing: [what script does]
- Output: [what script returns]
- Exit codes: 0 (success), 1 (error)

## Example

**Input**: [sample input]

**Command**: `python scripts/[script-name].py [args]`

**Output**: [sample output]

## Related
- Governed by: [behavior IDs]
- Uses knowledge: [knowledge node IDs]
```

**Skill description is COMPLETE**, script is placeholder ⚠️

### 2.3: For Hybrid Skills

**Generate complete skill file** referencing placeholder scripts + LLM:

```markdown
---
[existing frontmatter]
implementation: hybrid
---

# [Skill Name]

## Purpose
[What this skill does]

## When to Use
[Scenarios, trigger conditions]

## Methodology

This skill combines rule-based processing with LLM reasoning.

### Workflow
1. **Prepare** (Script): `scripts/[prep-script].py`
2. **Reason** (LLM): Prompt-based analysis
3. **Validate** (Script): `scripts/[validate-script].py`

## Procedure

### Step 1: Prepare (Rule-based)
- **Script**: `scripts/[prep-script].py`
- **Purpose**: [what prep does]
- **Output**: Structured data for LLM

### Step 2: Reason (LLM)
- **Prompt**: [describe prompt strategy]
- **Context**: Output from Step 1
- **Output**: LLM analysis/decision

### Step 3: Validate (Rule-based)
- **Script**: `scripts/[validate-script].py`
- **Purpose**: [what validation does]
- **Output**: Final result

## Script References

**Prep script**: `scripts/[prep-script].py` ⚠️ PLACEHOLDER  
**Validate script**: `scripts/[validate-script].py` ⚠️ PLACEHOLDER

## Example

[Full workflow example]

## Related
- Governed by: [behavior IDs]
- Uses knowledge: [knowledge node IDs]
```

**Skill description is COMPLETE**, scripts are placeholders ⚠️

---

## Step 3: Track Referenced Scripts

**Create list** of all placeholder scripts referenced:

```
Scripts needing implementation:
- scripts/[script-1].py (used by: [skill-id-1], [skill-id-2])
- scripts/[script-2].py (used by: [skill-id-3])
- scripts/[script-3].py (used by: [skill-id-4])
```

---

## Step 4: Write Output Summary

**Create**: `output/phase-06.md`

**Follow structure**: Read `specs/phase-06-output.spec.md`

**Include**:

- All skills listed (complete descriptions)
- Scripts referenced (placeholders)
- Note: "All scripts are placeholders, human developer must implement"

---

## Step 5: Confirm with Human

```
✅ Phase 6 Skills Implementation:

Skills documented: [X] (all complete)
- LLM-based: [count] (fully implemented) ✅
- Rule-based: [count] (reference placeholder scripts) ⚠️
- Hybrid: [count] (reference placeholder scripts) ⚠️

Scripts to develop: [Y]

See: output/phase-06.md

Note: All scripts are placeholders - human developer needed 🛠️

Proceed to Phase 7 (Behaviors)?
```

---

## Completion

```
✅ Phase 6 Complete

Skills: [X] complete descriptions
Scripts: [Y] placeholders for development
Focus: Domain skills in agents/skills/ folder

Next: Phase 7 (Behaviors Generation)
```

---

## Important Notes

**Skill files are COMPLETE**: Written as if skill is fully developed

**LLM-based skills**: Fully implemented (prompts described) ✅

**Rule-based/Hybrid skills**: Reference placeholder scripts ⚠️

**One note suffices**: "All scripts are placeholders, you need to develop and provide the tools"

**Human value preserved**: Real development work (scripts) still needed

---

**Next**: [Phase 7: Behaviors Generation](PHASE_07_BEHAVIORS_GENERATION.md)
