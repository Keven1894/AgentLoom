# Phase 8: Skills Implementation

**AI Agent Setup Protocol V2.0**

---

## 📌 Phase Context

**Prerequisites**: Phases 1-7 complete  
**Input needed from previous phases**:
- Skills classification (Phase 2.3) - rule-based/LLM/hybrid
- Skill definitions (Phase 5, 7) - what each skill does
- KG maintenance specs (Phase 7) - critical skills

**Output**: 10-30+ implementation files (scripts + prompts)  
**Estimated time**: 60-120 minutes

**Creates for next phases**:
- Rule-based scripts → Phase 9 (testing)
- LLM prompts → Ongoing agent operations
- KG maintenance tools → Ongoing system evolution

---

## Objective

Based on Phase 2.3 classification, create actual tool implementations for all defined skills.

---

## Before You Begin

**Review Phase 2.3 Classification**: Ensure you understand which skills are:

- **Rule-based**: Python scripts ($0 cost)
- **LLM-based**: Prompt templates (Max tier or SLM tier)
- **Hybrid**: Orchestrators combining both approaches

**Reference Documents**:

- [`guides/SKILL_TEMPLATE_GUIDE.md`](../guides/SKILL_TEMPLATE_GUIDE.md) - Complete skill definition format
- [`guides/SKILLS_CLASSIFICATION_GUIDE.md`](../guides/SKILLS_CLASSIFICATION_GUIDE.md) - Implementation type decision tree
- [`guides/REGENERATIVE_EDITING_PROTOCOL.md`](../guides/REGENERATIVE_EDITING_PROTOCOL.md) - For file modification skills

**Cost Optimization Strategy**:

- Maximize rule-based implementations (free)
- Use SLM tier for simple LLM tasks
- Reserve Max tier for complex reasoning only

---

## Action 8.1: Review Skills Classification

Review all skills from Phase 2 and their implementation types.

**For each skill, confirm**:

1. Implementation type (rule-based / LLM-based / hybrid)
2. If LLM-based: Required tier (Max / SLM)
3. Dependencies on other skills
4. Input/output requirements

**Special Focus**: Phase 7 KG Maintenance Skills

- `skill-kg-monitor` (rule-based)
- `skill-kg-update-node` (hybrid)
- `skill-kg-heal` (rule-based)

These are critical for agent self-evolution and should be prioritized.

---

## Action 8.2: Create Rule-Based Skill Tools

For each `rule-based` skill, create a Python script in `scripts/[skill-id].py`.

### Template Structure

```python
#!/usr/bin/env python3
"""
[Skill Name]
Implementation: Rule-based

[Description from skill markdown]
"""

import os
import sys
from pathlib import Path

def main():
    """
    Main execution function
    """
    print(f"Executing [Skill Name]...")
    
    # [Actual implementation based on skill definition]
    # Example operations:
    # - File operations
    # - JSON validation
    # - Directory scanning
    # - Schema checking
    
    print("✅ Complete")
    return 0

if __name__ == '__main__':
    sys.exit(main())
```

### Priority: KG Maintenance Skills (from Phase 7)

The KG maintenance skills are **critical** and **already implemented** in `scripts/reusable/`.

**Copy the reusable scripts**:

```bash
# These scripts are 100% reusable across all projects
cp [protocol-path]/scripts/reusable/kg_monitor.py scripts/
cp [protocol-path]/scripts/reusable/kg_heal.py scripts/
```

**What's included**:

1. **kg_monitor.py** (rule-based)
   - Extracts paths from all KG JSON files
   - Scans monitored directories for markdown files
   - Compares and generates change report
   - Returns JSON with added/deleted files

2. **kg_heal.py** (rule-based)
   - Checks for orphaned nodes (missing parent)
   - Checks for broken parent references
   - Reports connectivity issues
   - Suggests fixes

**No customization needed** - These scripts work for any Agent Builder system.

**Test them**:

```bash
# Test monitor
python scripts/kg_monitor.py

# Test heal
python scripts/kg_heal.py
```

### Testing Rule-Based Skills

After creating each script:

1. Run `python scripts/[skill-id].py` to test
2. Verify output matches expected behavior
3. Check error handling with invalid inputs
4. Confirm exit codes (0 = success, 1 = failure)

**Create or copy each rule-based skill script** (copy from `scripts/reusable/` if available, otherwise generate).

**Confirm to human**:
```
✅ Created/Copied rule-based scripts:
- kg_monitor.py (copied from protocol - 100% reusable)
- kg_heal.py (copied from protocol - 100% reusable)
- [N] custom domain scripts (created based on Phase 2 skills)
```

---

## Action 8.3: Create LLM-Based Skill Prompts

For each `llm-based` skill, create a prompt template in `agents/skills/prompts/[skill-id]-prompt.md`.

### Template Structure

```markdown
# [Skill Name] - LLM Prompt Template

## Required LLM Tier
[Max / SLM tier from classification]

**Cost Estimate**: $[X] per execution

## Context to Provide
[List what context the LLM needs]

## Prompt Template

\```
You are [Agent Name], [Role Name].

**Task**: [Task description from skill definition]

**Context**:
{context_variables}

**Input**:
{input_data}

**Instructions**:
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Output Format**:
[Expected output structure]

**Constraints**:
- [Constraint 1 from behaviors]
- [Constraint 2 from behaviors]
- [Additional constraints]

**Example**:
Input: [example input]
Output: [example output]
\```

## Expected Output Schema

\```json
{
  "field1": "value",
  "field2": ["list"],
  "field3": {
    "nested": "object"
  }
}
\```

## Post-Processing

[Any rule-based processing of LLM output]
- Validation steps
- Format conversion
- Error handling

## Testing

**Test Input**: [Provide test case]
**Expected Output**: [Expected result]
```

### Cost Optimization Tips

**For SLM-tier skills**:

- Keep prompts concise (< 500 tokens)
- Use structured output formats
- Avoid complex reasoning chains

**For Max-tier skills**:

- Justify the need for advanced reasoning
- Consider if hybrid approach could work
- Document why SLM tier is insufficient

**Create each LLM prompt template** in `agents/skills/prompts/` following the structure above.

**Confirm to human**:
```
✅ Created [M] LLM prompt templates in agents/skills/prompts/
```

---

## Action 8.4: Create Hybrid Skill Orchestrators

For each `hybrid` skill, create an orchestration script in `scripts/[skill-id]_orchestrator.py`.

### Template Structure

```python
#!/usr/bin/env python3
"""
[Skill Name] - Hybrid Orchestrator
Implementation: Rule-based preprocessing + LLM + Rule-based validation
"""

import json
from pathlib import Path

def preprocess():
    """
    Rule-based preprocessing
    
    Purpose: Gather data, validate inputs, prepare context
    Cost: $0 (deterministic rules)
    """
    print("Step 1: Preprocessing...")
    
    # Example operations:
    # - Scan files
    # - Extract metadata
    # - Validate input format
    # - Build context
    
    data = {
        "files": [],
        "context": {},
        "metadata": {}
    }
    
    print(f"  Processed {len(data['files'])} files")
    return data

def llm_process(preprocessed_data):
    """
    LLM analysis step
    
    Purpose: Complex reasoning, pattern recognition, decision making
    Cost: $X per call (depends on tier)
    """
    print("Step 2: LLM Analysis...")
    
    # In actual implementation:
    # 1. Load prompt template from agents/skills/prompts/
    # 2. Inject preprocessed_data into template
    # 3. Call LLM API (with tier from classification)
    # 4. Parse and validate response
    
    # Example:
    # prompt = load_prompt_template('[skill-id]-prompt.md')
    # prompt_filled = prompt.format(**preprocessed_data)
    # response = call_llm(prompt_filled, tier='slm')  # or 'max'
    # result = json.loads(response)
    
    result = {
        "analysis": "...",
        "recommendations": [],
        "confidence": 0.95
    }
    
    print(f"  Analysis complete (confidence: {result['confidence']})")
    return result

def validate_and_apply(llm_output):
    """
    Rule-based validation and application
    
    Purpose: Verify LLM output, apply changes safely
    Cost: $0 (deterministic rules)
    """
    print("Step 3: Validation & Application...")
    
    # Validation steps:
    # 1. Check output schema
    # 2. Verify against constraints
    # 3. Validate confidence threshold
    # 4. Apply changes with safeguards
    # 5. Verify results
    
    # Example validation:
    if llm_output.get('confidence', 0) < 0.8:
        print("  ⚠️  Low confidence, requesting human review")
        return False
    
    # Apply changes
    print("  Applying changes...")
    
    # Verify
    print("  Verifying results...")
    
    return True

def main():
    """Main orchestration"""
    print("🔄 [Skill Name] (Hybrid)")
    print("="*50)
    
    # Step 1: Preprocess (Rule-based, $0)
    data = preprocess()
    
    # Step 2: LLM Analysis (LLM, $X)
    result = llm_process(data)
    
    # Step 3: Validate & Apply (Rule-based, $0)
    success = validate_and_apply(result)
    
    print("="*50)
    if success:
        print("✅ Complete")
        return 0
    else:
        print("❌ Failed validation")
        return 1

if __name__ == '__main__':
    import sys
    sys.exit(main())
```

### Cost Optimization for Hybrid Skills

**Maximize Rule-Based Components**:

- Preprocessing: Extract all possible data with rules
- Post-processing: Validate and apply with rules
- Only use LLM for tasks requiring reasoning

**Example Cost Breakdown**:

- Preprocessing: $0 (5 seconds)
- LLM call: $0.50 (SLM tier) or $2.00 (Max tier)
- Validation: $0 (2 seconds)
- **Total**: $0.50-2.00 vs $5-10 if fully LLM-based

### Testing Hybrid Skills

1. Test preprocessing independently
2. Mock LLM responses for validation testing
3. Test full pipeline with real LLM
4. Verify cost estimates match actual usage

**Create each hybrid orchestrator script** in `scripts/` following the structure above.

**Confirm to human**:
```
✅ Created [P] hybrid orchestrators in scripts/
```

---

## Action 8.5: Implement KG Update Node (Hybrid - Advanced)

This is a critical skill from Phase 7 that requires LLM integration.

**Note**: This skill is **hybrid** and requires:
1. Rule-based file analysis (preprocess)
2. LLM API integration (for metadata generation)
3. Rule-based JSON update (apply changes)

**Implementation Approaches**:

### Approach 1: Manual Implementation (Phase 8)

Create `scripts/kg_update_node_orchestrator.py` with:
- Preprocessing logic (determine which graph to update)
- LLM API call (generate node metadata)
- Graph update logic (insert/modify/delete nodes)

**Complexity**: High - requires LLM API integration

### Approach 2: Use Agent's Native Capability (Recommended)

**Instead of a standalone script**, leverage the agent's built-in ability to:
1. Read files and understand content (LLM)
2. Modify JSON files (native tools)
3. Validate changes (rule-based scripts)

**When user says**: "Update the knowledge graph"

**Agent executes**:
1. Run `kg_monitor.py` → Get change report
2. For each change, use LLM reasoning to generate node metadata
3. Directly modify JSON graphs using file tools
4. Run `kg_heal.py` → Validate connectivity
5. Run `validate_graphs.py` → Confirm success

**This avoids** creating a complex orchestrator script that duplicates agent capabilities.

**Recommendation**: Document this workflow in the skill definition (Phase 7) rather than implementing as standalone script.

---

## Validation Checkpoint

```
✅ Skill implementations complete:

**Rule-Based Scripts**:
- kg_monitor.py (copied from protocol - 100% reusable)
- kg_heal.py (copied from protocol - 100% reusable)
- [N] custom domain scripts (created based on Phase 2 skills)

**LLM Prompt Templates**:
- [M] prompt templates created in agents/skills/prompts/

**Hybrid Orchestrators**:
- kg_update_node: Uses agent's native capability (no separate script)
- [P] custom domain orchestrators (if needed)

**All skills from Phase 2 now have implementation artifacts.**

**Cost Optimization Achieved**:
- Rule-based: [N] skills × $0 = $0
- SLM-based: [M1] skills × $0.50 = $[X]
- Max-based: [M2] skills × $2.00 = $[Y]
- Hybrid: Agent-native (efficient)
- **Total operational cost**: $[X+Y]/day

Proceed to Phase 9?
```

---

**Previous Phase**: [Phase 7: KG Maintenance](PHASE_07_KG_MAINTENANCE.md)  
**Next Phase**: [Phase 9: Final Validation](PHASE_09_FINAL_VALIDATION.md)
