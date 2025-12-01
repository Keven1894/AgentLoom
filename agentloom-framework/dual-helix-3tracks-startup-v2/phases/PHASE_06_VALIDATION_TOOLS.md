# Phase 6: Create Validation Tools

**AI Agent Setup Protocol V2.0**

---

## 📌 Phase Context

**Prerequisites**: Phases 1-5 complete  
**Input needed from previous phases**:
- Domain role ID (Phase 1) for structure validator
- Graph filenames (Phase 4) for validation

**Output**: 2 Python validation scripts  
**Estimated time**: 20-30 minutes

**Creates for next phases**:
- validate_graphs.py → Used in Phase 9, ongoing
- validate_structure.py → Used in Phase 9, ongoing

---

## Objective

Create scripts to validate structure and graph integrity with V2 connectivity checks and Agent Builder + Domain Role architecture.

---

## Before You Begin

The protocol package includes **reusable validation scripts** that you can copy directly to your project.

**Location**: `[protocol-package]/scripts/`

- `reusable/` - Copy directly (no changes needed)
- `templates/` - Copy and customize

See `[protocol-package]/scripts/README.md` for details.

---

## Action 6.1: Copy Graph Validator

The graph validator is **100% reusable** across all projects.

**Copy the script**:

```bash
# Copy from protocol package to your project
cp [protocol-path]/scripts/reusable/validate_graphs.py scripts/
```

**What it validates**:

- ✅ All non-root nodes have `parent` field
- ✅ No broken parent references
- ✅ No orphaned nodes
- ✅ Graph structure integrity
- ✅ File references (if `path` field exists)

**Test it**:

```bash
python scripts/validate_graphs.py
```

**Expected output**:

```
Validating 8 knowledge graphs...
============================================================

Checking master-graph.json...
  ✅ Valid

Checking agent-builder-knowledge-graph.json...
  ✅ Valid

... (all graphs)

============================================================

✅ All 8 graphs are fully connected and valid!
```

**If you see issues**:

- `orphaned`: Node missing `parent` field → Add parent link
- `broken_parent`: Parent ID doesn't exist → Fix parent reference
- `no_root`: Graph has no root node → Add root node
- `empty_graph`: No nodes in graph → Check graph creation

**Report**:

```
✅ Copied scripts/validate_graphs.py (100% reusable, no changes needed)
```

---

## Action 6.2: Copy and Customize Structure Validator

The structure validator is a **template** that needs customization for each project.

**Step 1: Copy the template**:

```bash
# Copy template from protocol package
cp [protocol-path]/scripts/templates/validate_structure.py.template scripts/validate_structure.py
```

**Step 2: Customize for your project**:

Open `scripts/validate_structure.py` and update:

### Update REQUIRED_DIRS (lines 20-35)

Replace `[DOMAIN-ROLE]` with your actual domain role ID:

```python
REQUIRED_DIRS = [
    '.cursor',
    '.cursor/behaviors',
    '.cursor/behaviors/core',
    '.cursor/templates',
    'agents',
    'agents/knowledge-graphs',
    'agents/skills',
    'agents/skills/agent-builder',
    'agents/skills/project-manager',  # ← Your domain role
    'docs',
    'docs/general',
    'docs/agent-builder',
    'docs/project-manager',  # ← Your domain role
    'scripts',
    'temp'
]
```

### Update REQUIRED_FILES (lines 37-47)

Add your domain role graph files:

```python
REQUIRED_FILES = [
    '.cursor/identity.md',
    '.cursor/rules.md',
    'agents/knowledge-graphs/master-graph.json',
    'agents/knowledge-graphs/agent-builder-knowledge-graph.json',
    'agents/knowledge-graphs/agent-builder-skills-graph.json',
    'agents/knowledge-graphs/agent-builder-behaviors-graph.json',
    # Add your domain role graphs
    'agents/knowledge-graphs/project-manager-knowledge-graph.json',
    'agents/knowledge-graphs/project-manager-skills-graph.json',
    'agents/knowledge-graphs/project-manager-behaviors-graph.json',
]
```

### Implement get_domain_role_id() (lines 55-65)

Read the domain role from your `identity.md`:

```python
def get_domain_role_id():
    """Extract domain role ID from identity.md"""
    with open('.cursor/identity.md', 'r', encoding='utf-8') as f:
        content = f.read()
        # Parse based on your identity.md format
        # Example: Look for "Domain Role: project-manager"
        for line in content.split('\n'):
            if 'Domain Role:' in line:
                return line.split(':')[1].strip().lower().replace(' ', '-')
    return 'unknown'
```

**Step 3: Test it**:

```bash
python scripts/validate_structure.py
```

**Expected output**:

```
Validating project structure...
============================================================

✅ Project structure is complete and valid!
```

**If you see issues**:

- Missing directories → Create them with `mkdir -p`
- Missing files → Check which phase creates them

**Report**:

```
✅ Created and customized scripts/validate_structure.py
```

---

## Action 6.3: Test Both Validators

Run both validators to confirm everything works:

```bash
# Test structure
python scripts/validate_structure.py

# Test graphs
python scripts/validate_graphs.py
```

Both should pass at this point (after Phase 5 completion).

---

## Validation Checkpoint

```
✅ Validation tools created:
- scripts/validate_graphs.py (copied from protocol, 100% reusable)
- scripts/validate_structure.py (customized for this project)

Both validators tested and passing.

Ready to proceed to Phase 7?
```

---

## Notes

**Why copy instead of write?**

- ✅ **Efficiency**: No need to regenerate identical code
- ✅ **Consistency**: All projects use the same tested scripts
- ✅ **Maintainability**: Bug fixes in protocol benefit all projects
- ✅ **Clarity**: Clear what's reusable vs. customizable

**Script locations in protocol package**:

- `scripts/reusable/validate_graphs.py` - 100% reusable
- `scripts/templates/validate_structure.py.template` - Requires customization

**For more details**: See `[protocol-package]/scripts/README.md`

---

**Previous Phase**: [Phase 5: Content Templates](PHASE_05_CONTENT_TEMPLATES.md)  
**Next Phase**: [Phase 7: KG Maintenance](PHASE_07_KG_MAINTENANCE.md)
