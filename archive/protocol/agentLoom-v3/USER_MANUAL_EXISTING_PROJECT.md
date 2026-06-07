# User Manual: Validating Existing AgentLoom Projects

**Use Case**: Check status and validate an existing AgentLoom agent build  
**Target Audience**: Advanced users, maintainers, troubleshooters  
**Last Updated**: November 29, 2025

---

## 🎯 Purpose

Quick reference for checking the status and health of an existing AgentLoom project. Each phase has a validation prompt you can copy-paste.

---

## 📋 Quick Status Check

### 🪄 Overall Project Status

```
Check overall AgentLoom project status:

1. List all files in agentLoom/outputs/
2. For each phase-XX.md found, report:
   - Phase number and name
   - Completion status
   - Key outputs mentioned
3. Identify the last completed phase
4. List any missing phase outputs (0-8)
5. Summarize: "Project is at Phase X, [complete/incomplete/has issues]"
```

---

## 🔍 Phase-by-Phase Validation

### Phase 0: Environment Setup

**🪄 Check Environment**

```
Validate Phase 0 environment:

1. Check Python version: python --version
2. Verify project structure exists:
   - content-raw/ folder
   - agentLoom/ folder
3. Test validation script:
   python agentLoom/builder-assets/scripts/validate_structure.py
4. Report: ✅ Environment ready / ❌ Issues found
```

**Expected**: Python 3.9+, correct folder structure

---

### Phase 1: Information Discovery

**🪄 Check Phase 1 Output**

```
Validate Phase 1 completion:

1. Check if agentLoom/outputs/phase-01.md exists
2. If exists, verify it contains:
   - PROJECT_NAME
   - DOMAIN_ROLE_NAME
   - DOMAIN_ROLE_ID
   - DOMAIN_ID
   - Domain concepts list
   - Skills list
   - Behaviors list
3. Report: ✅ Complete / ❌ Missing / ⚠️ Incomplete
```

**Expected**: All context variables defined, lists populated

---

### Phase 2: Architecture Design

**🪄 Check Phase 2 Output**

```
Validate Phase 2 completion:

1. Check if agentLoom/outputs/phase-02.md exists
2. If exists, verify it contains:
   - Knowledge structure design (hierarchy, categories)
   - Skills design (3-7 skills with types)
   - Behaviors design (3-5 behaviors with priorities)
   - Relationship mappings
3. Check if architecture was approved by user
4. Report: ✅ Complete & Approved / ❌ Missing / ⚠️ Not approved
```

**Expected**: Detailed architecture, user approval documented

---

### Phase 3: Project Structure

**🪄 Check Phase 3 Output**

```
Validate Phase 3 completion:

1. Check if agentLoom/outputs/phase-03.md exists
2. Run structure validation:
   python agentLoom/builder-assets/scripts/validate_structure.py
3. Verify key files exist:
   - .cursor/identity.md
   - .cursor/rules.md
   - agents/NEW_AGENT_START_HERE.md
4. Check domain folders created:
   - .cursor/behaviors/[DOMAIN_ROLE_ID]/
   - agents/skills/[DOMAIN_ROLE_ID]/
   - docs/[DOMAIN_ROLE_ID]/
5. Report validation results with file counts
```

**Validation Method**: `validate_structure.py` script

**Expected**: All required folders and hybrid files present

---

### Phase 4: Knowledge Graphs

**🪄 Check Phase 4 Output**

```
Validate Phase 4 completion:

1. Check if agentLoom/outputs/phase-04.md exists
2. Verify all 7 graph files exist:
   - agents/knowledge-graphs/master-graph.json
   - agents/knowledge-graphs/builder-knowledge-graph.json
   - agents/knowledge-graphs/builder-skills-graph.json
   - agents/knowledge-graphs/builder-behaviors-graph.json
   - agents/knowledge-graphs/[DOMAIN_ROLE_ID]-knowledge-graph.json
   - agents/knowledge-graphs/[DOMAIN_ROLE_ID]-skills-graph.json
   - agents/knowledge-graphs/[DOMAIN_ROLE_ID]-behaviors-graph.json
3. Run graph validation:
   python agentLoom/builder-assets/scripts/validate_graphs.py
4. Check visualization:
   - Open agents/knowledge-graphs/visualization-dynamic.html
   - Verify all graphs load
   - Check for orphaned nodes (disconnected)
5. Report: Graph count, validation status, orphan count
```

**Validation Methods**:

- `validate_graphs.py` script
- `visualization-dynamic.html` visual check

**Expected**: 7 graphs, all valid, fully connected, no orphans

---

### Phase 5: Knowledge Content

**🪄 Check Phase 5 Output**

```
Validate Phase 5 completion:

1. Check if agentLoom/outputs/phase-05.md exists
2. Verify content files exist in docs/[DOMAIN_ROLE_ID]/
3. For each category in Phase 2 KG structure:
   - Check if corresponding folder exists
   - Check if content files (.md) are present
   - Verify files have proper frontmatter
4. Cross-reference with knowledge graph:
   - Each node in [DOMAIN_ROLE_ID]-knowledge-graph.json should have a file
   - Each file should be referenced in the graph
5. Report: File count, coverage %, missing files
```

**Validation Method**: Manual cross-reference with KG

**Expected**: All KG nodes have corresponding content files

---

### Phase 6: Skills Implementation

**🪄 Check Phase 6 Output**

```
Validate Phase 6 completion:

1. Check if agentLoom/outputs/phase-06.md exists
2. Verify skill files in agents/skills/[DOMAIN_ROLE_ID]/
3. For each skill in Phase 2 design:
   - Check if .md file exists
   - Verify file has complete content (not just placeholder)
   - Check frontmatter has: type, category, id, roles
   - Verify implementation type is specified
4. Cross-reference with skills graph:
   - Each skill in [DOMAIN_ROLE_ID]-skills-graph.json should have a file
   - Each file should be referenced in the graph
5. Report: Skill count, implementation types breakdown, missing files
```

**Validation Method**: Manual cross-reference with skills graph

**Expected**: All skills fully documented with implementation details

---

### Phase 7: Behaviors Generation

**🪄 Check Phase 7 Output**

```
Validate Phase 7 completion:

1. Check if agentLoom/outputs/phase-07.md exists
2. Verify behavior files in .cursor/behaviors/[DOMAIN_ROLE_ID]/
3. For each behavior in Phase 2 design:
   - Check if .md file exists
   - Verify file has complete content (not just placeholder)
   - Check frontmatter has: type, category, id, priority, roles
   - Verify priority is set (critical/high/medium)
4. Cross-reference with behaviors graph:
   - Each behavior in [DOMAIN_ROLE_ID]-behaviors-graph.json should have a file
   - Each file should be referenced in the graph
5. Check for links to skills (behaviors should govern skills)
6. Report: Behavior count, priority breakdown, missing files
```

**Validation Method**: Manual cross-reference with behaviors graph

**Expected**: All behaviors documented with priorities and skill links

---

### Phase 8: User Manual

**🪄 Check Phase 8 Output**

```
Validate Phase 8 completion:

1. Check if agentLoom/outputs/phase-08.md exists
2. Verify documentation files:
   - agents/USER_MANUAL.md exists and is complete
   - agents/NEW_AGENT_START_HERE.md exists (should be from Phase 3)
   - agents/knowledge-graphs/VIEW_VISUALIZATION.md (optional)
3. Check USER_MANUAL.md contains:
   - Magic activation prompt
   - Role-specific workflows
   - Visualization instructions
   - Troubleshooting section
4. Test magic activation prompt:
   - Copy prompt from USER_MANUAL.md
   - Start new agent session
   - Paste prompt and verify < 5 min initialization
5. Report: Files present, magic prompt test result
```

**Validation Method**: Magic activation prompt test (< 5 min)

**Expected**: Complete user manual, working magic prompt

---

## 🛠️ Common Issues & Fixes

### Issue: Missing phase output files

**🪄 Regenerate Phase Output**

```
Regenerate missing phase-0X.md:

1. Read the phase instructions:
   @agentLoom/phases/PHASE_0X_*.md
2. Read the output spec:
   @agentLoom/specs/phase-0X-output.spec.md
3. Analyze what was actually created in that phase
4. Generate the phase-0X.md summary following the spec
5. Save to agentLoom/outputs/phase-0X.md
```

---

### Issue: Validation scripts fail

**🪄 Diagnose Validation Failures**

```
Diagnose and fix validation failures:

1. Run: python agentLoom/builder-assets/scripts/validate_structure.py
2. For each ❌ error:
   - Identify which phase should have created it
   - Check if that phase was completed
   - Suggest: Re-run that phase step OR create missing item
3. Provide fix commands or prompts
```

---

### Issue: Graphs have orphaned nodes

**🪄 Fix Orphaned Nodes**

```
Find and fix orphaned nodes in Knowledge Graphs:

1. Open agents/knowledge-graphs/visualization-dynamic.html
2. Visually identify disconnected nodes
3. For each orphan:
   - Determine its logical parent based on content
   - Update the JSON graph file to add parent field
   - Verify the parent node exists
4. Re-run validation:
   python agentLoom/builder-assets/scripts/validate_graphs.py
5. Refresh visualization to confirm fix
```

---

### Issue: Files don't match graph references

**🪄 Sync Files and Graphs**

```
Synchronize file system with Knowledge Graphs:

1. For each graph JSON file in agents/knowledge-graphs/:
   - List all path references
   - Check if each file exists
   - Report missing files
2. For each missing file:
   - Determine which phase should have created it
   - Suggest: Re-run phase OR create placeholder
3. For orphaned files (exist but not in graph):
   - Suggest: Add to graph OR remove file
```

---

## 📊 Health Score

**🪄 Calculate Project Health**

```
Calculate AgentLoom project health score:

1. Phase completion: Count completed phases (0-8) = X/8
2. Structure validation: Pass/Fail
3. Graph validation: Pass/Fail
4. File coverage: (files with content) / (total files) = Y%
5. Magic prompt test: Pass/Fail

Health Score:
- Phase completion: X/8 (weight: 30%)
- Validations: 2/2 pass (weight: 30%)
- File coverage: Y% (weight: 20%)
- Magic prompt: Pass (weight: 20%)

Overall: [Excellent 90-100% / Good 70-89% / Fair 50-69% / Poor <50%]
```

---

## 🔄 Maintenance Prompts

### Update After Content Changes

**🪄 Sync KG After Content Changes**

```
Update Knowledge Graphs after content changes:

1. Scan docs/[DOMAIN_ROLE_ID]/ for new/modified/deleted files
2. Compare with [DOMAIN_ROLE_ID]-knowledge-graph.json
3. For new files: Add nodes to graph
4. For deleted files: Remove nodes from graph
5. For moved files: Update paths in graph
6. Regenerate phase-05.md summary
7. Run validation to confirm
```

---

### Update After Skill Changes

**🪄 Sync KG After Skill Changes**

```
Update Skills Graph after skill changes:

1. Scan agents/skills/[DOMAIN_ROLE_ID]/ for new/modified/deleted files
2. Compare with [DOMAIN_ROLE_ID]-skills-graph.json
3. Update graph to match current files
4. Regenerate phase-06.md summary
5. Run validation to confirm
```

---

## 📚 Quick Reference

**Validation Scripts**:

- Structure: `python dual-helix-3tracks-startup-v3/builder-assets/scripts/validate_structure.py`
- Graphs: `python dual-helix-3tracks-startup-v3/builder-assets/scripts/validate_graphs.py`

**Visualization**:

- Open: `agents/knowledge-graphs/visualization-dynamic.html`
- Check: No disconnected nodes, all graphs load

**Key Files**:

- Phase outputs: `dual-helix-3tracks-startup-v3/outputs/phase-0X.md`
- Master graph: `agents/knowledge-graphs/master-graph.json`
- User manual: `agents/USER_MANUAL.md`

---

**Version**: 3.0  
**Last Updated**: November 29, 2025  
**Status**: Production Ready
