# Prompt Template: Migrate Existing Project to V2.0

**Use Case**: Retrofit existing agent project with V2.0 structure  
**Expected Time**: 1-4 hours (depending on project size)  
**Risk Level**: Medium (reorganizes files, creates new structure)  
**Last Updated**: November 28, 2025

---

## ⚠️ CRITICAL: Before Starting

### BACKUP YOUR PROJECT FIRST

**Required**:
```bash
# Option A: Git commit
git add -A
git commit -m "Pre-V2.0 migration backup"

# Option B: Folder copy
cp -r [project-folder] [project-folder]-backup-[date]
```

**Why critical**: Migration reorganizes files and structure. You need ability to rollback.

---

## 🤖 AI Model Requirements

**Recommended**:
- **Claude Sonnet 4.5** ⭐ - Best at analyzing existing code structure
- **Claude Sonnet 4** - Excellent for migrations

**Minimum**:
- **Claude Sonnet 3.5** - OK, may need to break into chunks
- **GPT-4 Turbo** - OK, needs careful validation

**Why better models help**:
- ✅ Infer relationships from existing patterns
- ✅ Better context retention for large codebases
- ✅ More accurate at identifying implicit roles/behaviors
- ✅ Better at designing coherent migration plans

**Cost**: ~$10-30 for migration (one-time)

---

## 🔍 Pre-Migration Assessment

Answer these questions to determine migration approach:

### Current State Questions

1. **Do you have agent identity defined?**
   - [ ] Yes (have `.cursor/identity.md` or similar)
   - [ ] Partial (scattered in comments/docs)
   - [ ] No

2. **Do you have Knowledge Graphs?**
   - [ ] Yes - How many? _____
   - [ ] Yes, but not connected (missing parent links)
   - [ ] No

3. **Are behaviors/rules organized?**
   - [ ] Yes (in separate files)
   - [ ] Partial (scattered across files)
   - [ ] No (monolithic `.cursorrules` or similar)

4. **Do you have documented skills?**
   - [ ] Yes (defined with types/categories)
   - [ ] Partial (some documented)
   - [ ] No

5. **Is documentation organized?**
   - [ ] Yes (structured folders)
   - [ ] No (scattered files)
   - [ ] None

6. **How many roles do you currently have?**
   - [ ] 1 role
   - [ ] 2 roles
   - [ ] 3+ roles (consider splitting into multiple agents)
   - [ ] Unclear/undefined

### Migration Complexity

**Answers mostly "Yes"**: **Enhancement migration** (1-2 hours)
- Add missing V2.0 features
- Improve existing structure
- Skip some phases

**Answers mixed**: **Standard migration** (2-4 hours)
- Restructure and enhance
- Follow most phases
- Preserve existing content

**Answers mostly "No"**: **Consider fresh start** (3-7 hours)
- Use PROMPT_TEMPLATE_NEW_PROJECT.md instead
- Easier than migration
- Better long-term structure

---

## 🚀 The Migration Prompt

Copy and send to AI (adjust based on your assessment):

```
Read the protocol:
@temp/dual-helix-3tracks-startup/AI_AGENT_SETUP_PROTOCOL_V2_INDEX.md
@temp/dual-helix-3tracks-startup/phases/INDEX.md

# Task: Migrate Existing Project to V2.0 Architecture

## Current Project

**Project name**: [YOUR_PROJECT_NAME]
**Domain**: [e.g., Software Development, Research, etc.]
**Current state**: [Brief description of what exists now]
**Git status**: ✅ I have committed/backed up my project

## Current Structure

### Roles
**Current roles**: [List current roles, or "Undefined - need to identify"]
**Target**: Agent Builder (system) + 1 domain role

### Behaviors/Rules
**Location**: [e.g., .cursorrules file, .cursor/behaviors/, scattered]
**Organization**: [Monolithic file / Separate files / None]
**Count**: [Approximate number]

### Skills
**Documented**: [Yes/No/Partial]
**Location**: [File paths or "None"]
**Implementation**: [Scripts exist? / Just descriptions? / None]

### Knowledge Graphs
**Exist**: [Yes/No]
**If Yes**:
- Files: [List JSON files]
- Connected?: [Yes/No/Unknown]
- Have parent links?: [Yes/No/Unknown]

### Documentation
**Organization**: [Structured / Scattered / None]
**Location**: [Folder paths]

---

## Migration Instructions

**Follow 6-step migration process**:

### Step 1: AUDIT (30-60 min)
- Analyze all existing files
- Identify implicit roles
- Extract behaviors and skills
- Map current knowledge organization
- Present audit report with:
  - What exists (inventory)
  - What's missing for V2.0
  - Recommended role architecture
  - Migration complexity assessment

**WAIT FOR MY APPROVAL** before Step 2

---

### Step 2: DESIGN V2.0 Architecture (30-45 min)
- Design two-role structure (Agent Builder + domain role)
- Map existing behaviors to new organization
- Design fully-connected KG structure
- Classify existing/new skills by implementation type
- Present architecture design

**WAIT FOR MY APPROVAL** before Step 3

---

### Step 3: MIGRATION PLAN (15-30 min)
- Create detailed migration plan
- File move/create/modify operations
- Data preservation strategy
- Rollback plan
- Risk assessment
- Present plan with timeline

**WAIT FOR MY APPROVAL** before Step 4

---

### Step 4: EXECUTE MIGRATION (1-2 hours)
- Create V2.0 directory structure
- Migrate existing content (preserve all data)
- Create Agent Builder graphs (copy templates)
- Generate domain role graphs
- Organize behaviors into .cursor/behaviors/
- Create/update skill definitions
- Copy validation scripts
- Create visualization.html

**Safety measures**:
- Preserve all existing files
- Create in parallel where possible
- Validate incrementally

---

### Step 5: VALIDATE (30 min)
- Run: python scripts/validate_structure.py
- Run: python scripts/validate_graphs.py
- Open: visualization.html (check Unified Brain)
- Verify: All existing functionality preserved
- Test: Cold-start with USER_MANUAL.md

**Fix any issues** before Step 6

---

### Step 6: DELIVER MIGRATION SUMMARY
- What was migrated
- What was created new
- Validation results
- Before/after comparison
- Rollback instructions (if needed)
- Next steps

---

## V2.0 Requirements

**Your migration MUST include**:

1. ✅ **Agent Builder templates** (copy from protocol):
   - json-templates/agent-builder/*.json.template

2. ✅ **Validation scripts** (copy from protocol):
   - scripts/reusable/validate_graphs.py
   - scripts/reusable/kg_monitor.py
   - scripts/reusable/kg_heal.py

3. ✅ **Fully-connected graphs**:
   - All nodes have parent links
   - Root nodes defined
   - Cross-graph links established

4. ✅ **User manual** (copy and customize):
   - NEW_AGENT_START_HERE.md (from docs-templates)
   - USER_MANUAL.md (from docs-templates)

5. ✅ **Visualization**:
   - visualization.html (from htmls/templates)
   - Unified Brain view functional

6. ✅ **Behaviors in .cursor/behaviors/**:
   - Core behaviors
   - Agent Builder behaviors
   - Domain behaviors

**Reference**: phases/INDEX.md decision framework for template vs generate

---

BEGIN with Step 1: Audit existing project structure
```

---

## 💡 Migration Tips

### For Simple Migrations (Enhancement Only)

**If you already have**:
- Good file organization
- Some behaviors defined
- Basic documentation

**You can**:
- Skip to specific phases (e.g., Phase 4 for KG creation)
- Focus on adding V2.0 features
- Use express mode throughout

---

### For Complex Migrations

**If you have**:
- Monolithic configuration files
- Scattered documentation
- Unclear role boundaries

**You should**:
- Follow full 6-step process
- Take time in Steps 1-3 (audit, design, plan)
- Get approval at each step
- Consider fresh start if too complex

---

## 🚨 Common Migration Issues

### "Can't identify clear roles"

**Solution**: 
- Agent Builder is always one role (standard)
- Identify your domain's primary purpose → That's domain role
- If multiple purposes → Consider multiple agents

### "Existing Knowledge Graph isn't connected"

**Solution**:
- Audit existing graph in Step 1
- Design V2.0 structure in Step 2
- Use kg_heal.py to identify what needs parent links
- Regenerate if easier than fixing

### "Behaviors scattered everywhere"

**Solution**:
- Extract all behaviors in Step 1 (audit)
- Categorize in Step 2 (design)
- Organize in Step 4 (execution)
- Follow behavior-file.md.template for structure

### "Not sure if migration is worth it"

**Solution**: Ask yourself:
- Do I need fully-connected KG? (navigation, evolution)
- Do I need self-evolution? (KG maintenance)
- Do I need visualization? (debugging, understanding)
- Do I need < 5 min cold-start? (team adoption)

**If 3+ yes**: Migration worth it  
**If mostly no**: Maybe not needed

---

## 📊 Migration Success Criteria

### Your migration is successful when:

**Structure**:
- [ ] Two-role architecture (Agent Builder + domain)
- [ ] .cursor/behaviors/ organization
- [ ] agents/skills/ organization
- [ ] docs/ organized by role

**Knowledge Graphs**:
- [ ] 7-8 graphs created (6 role graphs + master + optional content)
- [ ] All fully connected (no orphans)
- [ ] visualization.html shows Unified Brain
- [ ] Agent Builder graphs copied from templates

**Functionality**:
- [ ] All existing features still work
- [ ] New features added (KG maintenance, visualization)
- [ ] Cold-start < 5 minutes
- [ ] Both validators pass

**Documentation**:
- [ ] USER_MANUAL.md comprehensive
- [ ] NEW_AGENT_START_HERE.md functional
- [ ] README.md updated
- [ ] Migration documented

---

## 🔄 Rollback Plan

If migration doesn't work:

```bash
# Option A: Git reset
git reset --hard HEAD~1  # Undo last commit

# Option B: Restore backup folder
rm -rf [project-folder]
mv [project-folder]-backup-[date] [project-folder]
```

**When to rollback**:
- Validation fails repeatedly
- Existing functionality broken
- Migration too complex
- Time exceeds estimate significantly

**Alternative**: Pause migration, fix issues, resume later

---

## 📈 Post-Migration Tasks

After successful migration:

1. **Test all existing workflows** - Ensure nothing broke
2. **Test new features** - KG maintenance, visualization
3. **Update team documentation** - New startup process
4. **Train team** - How to use new structure
5. **Iterate** - Improve based on usage

---

## 📞 Getting Help

**If AI gets stuck**:
- Point to specific phase in phases/PHASE_XX.md
- Reference decision framework in phases/INDEX.md
- Use Scenario 7 from PROMPT_TEMPLATES_QUICK_COPY.md (fix orphaned nodes)

**If validation fails**:
- Run kg_heal.py for suggestions
- Check visualization.html for visual debugging
- Review Phase 4 requirements (full connectivity)

**If unsure about migration**:
- Review audit report carefully
- Consider fresh start with PROMPT_TEMPLATE_NEW_PROJECT.md
- Ask AI for recommendation based on complexity

---

**Version**: 2.0  
**Last Updated**: November 28, 2025  
**Status**: Production Ready
