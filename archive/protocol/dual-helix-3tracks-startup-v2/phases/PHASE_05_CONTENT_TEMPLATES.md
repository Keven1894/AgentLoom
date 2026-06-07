# Phase 5: Create Content Templates & Behavior/Skill Files

**AI Agent Setup Protocol V2.0**

---

## 📌 Phase Context

**Prerequisites**: Phases 1-4 complete  
**Input needed from previous phases**:
- Behavior taxonomy (Phase 2)
- Skills list (Phase 2)
- KG node IDs (Phase 4) for indexing
- Domain role ID (Phase 1)

**Output**: 20-50+ behavior and skill markdown files  
**Estimated time**: 60-120 minutes (30-60 with express mode)

**Creates for next phases**:
- Behavior files → Phase 6 (referenced in KG)
- Skill files → Phase 8 (implementation references)
- CONTENT_TEMPLATE.md → Ongoing content creation

---

## Objective

Create standard templates and initial behavior/skill documentation for Agent Builder (system role) and Domain Role (custom).

---

## ⚡ Express Mode (For Experienced Builders)

**If you've built agents before and understand behavior/skill file structures**:

1. ✅ Copy `CONTENT_TEMPLATE.md.template` → `docs/general/CONTENT_TEMPLATE.md`
2. ✅ Use `behavior-file.md.template` as GUIDE (adapt as needed)
3. ✅ Create all core behaviors from Phase 2 design
4. ✅ Create all Agent Builder behaviors (use template or SKILL_TEMPLATE_GUIDE)
5. ✅ Create all Domain Role behaviors (adapt to domain needs)
6. ✅ Create all Agent Builder skills (follow Phase 7 definitions)
7. ✅ Create all Domain Role skills (reference SKILL_TEMPLATE_GUIDE)
8. ✅ Skip to validation checkpoint

**Time saved**: ~30-45 minutes

**If this is your first time**: Follow all steps below for detailed guidance.

---

## Action 5.1: Create Content Template

The protocol package includes a **reusable content template** for general documentation.

**Copy the template**:

```bash
# Copy from protocol package to your project (no customization needed)
cp [protocol-path]/docs-templates/CONTENT_TEMPLATE.md.template docs/general/CONTENT_TEMPLATE.md
```

**What it includes**:
- YAML frontmatter with metadata fields
- Standard sections (Overview, Key Concepts, Detailed Content, Examples)
- Troubleshooting section
- Related resources
- KG indexing reference

**Template location**: `[protocol-package]/docs-templates/CONTENT_TEMPLATE.md.template`

**Confirm to human**:
```
✅ Copied docs/general/CONTENT_TEMPLATE.md (100% reusable)
```

---

## Action 5.2: Create Core Behavior Files

For each core behavior from Phase 2, create behavior files.

### **Option A: Use Template (Recommended for Beginners)**

**For each core behavior**:

```bash
# Copy template
cp [protocol-path]/docs-templates/behavior-file.md.template \
   .cursor/behaviors/core/[behavior-id].md
```

**Then customize**:
1. Set `category: core`
2. Set `applies-to: all-roles`
3. Replace `[behavior-id]`, `[Behavior Name]`
4. Fill in description from Phase 2
5. Add specific rules and examples
6. Define related components

**Template location**: `[protocol-package]/docs-templates/behavior-file.md.template`

### **Option B: Generate Custom (For Experienced Builders)**

**Generate** behavior files that match your needs. Ensure each file includes:

**Required**:
- YAML frontmatter: `type`, `category`, `id`, `priority`, `applies-to`, `indexed-in-kg`
- Description section
- Rules section (at least 1-2 rules)
- Related components (skills that enforce this, what it governs)

**Recommended**:
- Context (when/why this behavior applies)
- Examples (good/bad practices)
- Validation checklist

**Why this flexibility**:
- ✅ Behaviors vary widely (safety protocols vs workflow orchestration)
- ✅ Agent understands markdown structure well
- ✅ Template shows pattern, but agent can adapt to complexity
- ✅ Some behaviors need custom sections

**Template as guide**: Use `behavior-file.md.template` to see the pattern, adapt as needed.

**Create each core behavior file** (copy template OR generate custom) from Phase 2 design.

**Confirm to human**:
```
✅ Created [N] core behavior files in .cursor/behaviors/core/
```

---

## Action 5.3: Create Role-Specific Behavior Files

### Action 5.3a: Agent Builder Behavior Files

For Agent Builder's standard behaviors from Phase 2, create files in `.cursor/behaviors/agent-builder/`:

**Standard Agent Builder Behaviors**:

- `kg-consistency.md` - Knowledge Graph must reflect file system reality
- `system-integrity.md` - Never modify `.cursor/` without explicit instruction
- `validation-protocol.md` - Always validate structure/graphs after changes
- `self-evolution.md` - Maintain KG when files change

**Use template OR generate** (your choice):

```bash
# Option A: Copy template (recommended for consistency)
cp [protocol-path]/docs-templates/behavior-file.md.template \
   .cursor/behaviors/agent-builder/[behavior-id].md
# Then customize: category=agent-builder, applies-to=agent-builder

# Option B: Generate custom (if you prefer custom structure)
# Agent generates based on behavior-file.md.template pattern
```

**Required elements** (whether template or custom):
- YAML frontmatter with metadata
- Description and context
- At least 2 rules with examples
- Related components (skills, system parts)

**Create each Agent Builder behavior** (template or custom).

**Confirm to human**:
```
✅ Created [N] Agent Builder behavior files in .cursor/behaviors/agent-builder/
```

### Action 5.3b: Domain Role Behavior Files

For [Domain Role Name]'s behaviors from Phase 2, create files in `.cursor/behaviors/[domain-role-id]/`:

**Use template OR generate** (your choice):

```bash
# Option A: Copy template (for consistency)
cp [protocol-path]/docs-templates/behavior-file.md.template \
   .cursor/behaviors/[domain-role-id]/[behavior-id].md
# Then customize for domain context

# Option B: Generate custom (recommended for complex domain workflows)
# Agent generates based on domain requirements from Phase 2
```

**Required elements** (whether template or custom):
- YAML frontmatter with metadata
- Description and context
- Domain-specific rules
- Examples relevant to domain
- Related components

**Recommendation**: For **complex domain workflows**, generate custom structure. For **simple behaviors**, use template.

**Create each domain behavior** (template or custom).

**Confirm to human**:
```
✅ Created [N] [Domain Role Name] behavior files in .cursor/behaviors/[domain-role-id]/
✅ Total: [M] role-specific behavior files created
```

---

## Action 5.4: Create Skill Definition Files

**Reference**: For detailed skill template and examples, see [SKILL_TEMPLATE_GUIDE.md](../guides/SKILL_TEMPLATE_GUIDE.md)

**Reference**: For implementation type reasoning, see [SKILLS_CLASSIFICATION_GUIDE.md](../guides/SKILLS_CLASSIFICATION_GUIDE.md)

### Action 5.4a: Agent Builder Skill Files

For Agent Builder's standard skills from Phase 4.4a, create files in `agents/skills/system/`:

**Key Agent Builder Skills**:

1. **skill-maintain-kg.md** (Orchestrator)
   - Implementation: Hybrid
   - Sub-skills: skill-kg-monitor, skill-kg-update, skill-kg-heal
   - See template guide for complete example

2. **skill-kg-monitor.md**
   - Implementation: Rule-based
   - Parent: skill-maintain-kg

3. **skill-kg-update.md**
   - Implementation: Hybrid
   - Parent: skill-maintain-kg

4. **skill-kg-heal.md**
   - Implementation: Rule-based
   - Parent: skill-maintain-kg

5. **skill-validate-structure.md**
   - Implementation: Rule-based

Use the skill template from the guide, ensuring:

- `category: system`
- `roles: [agent-builder]`
- Implementation type matches Phase 2.3 classification
- Orchestrator skills include sub-skills section

**Create each Agent Builder skill file** using the skill template guide.

**Confirm to human**:
```
✅ Created [N] Agent Builder skill files in agents/skills/system/
```

### Action 5.4b: Domain Role Skill Files

For [Domain Role Name]'s skills from Phase 2, create files in `agents/skills/[category]/`:

Use the skill template from the guide, ensuring:

- `category: [appropriate category]`
- `roles: [domain-role-id]`
- Implementation type from Phase 2.3 classification
- Reference to classification reasoning

**Create each domain skill file** using the skill template guide.

**Confirm to human**:
```
✅ Created [N] [Domain Role Name] skill files across [M] categories
✅ Total: [P] skill definition files created
```

---

## Validation Checkpoint

```
✅ Documentation created:
- Content template (1 file)
- Core behavior files ([N] files)
- Agent Builder behavior files ([M] files)
- [Domain Role Name] behavior files ([P] files)
- Agent Builder skill files ([Q] files, including KG maintenance tree)
- [Domain Role Name] skill files ([R] files)

Total: [count] markdown files

All files reference:
- Phase 2 for behavior/skill definitions
- Phase 2.3 for implementation classifications
- Phase 4 for KG node IDs
- Skill template guide for structure

Proceed to Phase 6?
```

---

**Previous Phase**: [Phase 4: Create Knowledge Graphs](PHASE_04_KNOWLEDGE_GRAPHS.md)  
**Next Phase**: [Phase 6: Create Validation Tools](PHASE_06_VALIDATION_TOOLS.md)
