# Protocol Scripts

This directory contains reusable scripts and templates for the AI Agent Setup Protocol V2.0.

## Directory Structure

```
scripts/
├── reusable/           # Copy directly to projects (no changes needed)
│   ├── validate_graphs.py
│   ├── kg_heal.py
│   └── kg_monitor.py
└── templates/          # Customize per project
    └── validate_structure.py.template
```

## Reusable Scripts

These scripts work for **any** agent project following the V2.0 protocol:

### `validate_graphs.py`

- **Purpose**: Validates Knowledge Graph connectivity and structure
- **Reusability**: 100% - No customization needed
- **Usage**: Copy to `scripts/validate_graphs.py` in your project
- **Validates**:
  - All non-root nodes have parent links
  - No broken parent references
  - No orphaned nodes
  - Graph structure integrity

### `kg_heal.py`

- **Purpose**: Validates graph connectivity (subset of validate_graphs.py)
- **Reusability**: 100% - No customization needed
- **Usage**: Copy to `scripts/kg_heal.py` in your project
- **Used by**: KG maintenance skill system

### `kg_monitor.py`

- **Purpose**: Detects file system changes and compares with KG
- **Reusability**: 95% - Minor config needed
- **Usage**:
  1. Copy to `scripts/kg_monitor.py`
  2. Update `MONITORED_DIRS` list (line 25) with your directories
- **Used by**: KG maintenance skill system

## Templates

These require customization for each project:

### `validate_structure.py.template`

- **Purpose**: Validates project directory structure
- **Reusability**: Template only - Requires customization
- **Usage**:
  1. Copy to `scripts/validate_structure.py`
  2. Update `REQUIRED_DIRS` with your project structure
  3. Update `REQUIRED_FILES` with your core files
  4. Implement `get_domain_role_id()` function

## How to Use in Protocol

### Phase 6 (Validation Tools)

```bash
# Copy reusable graph validator
cp [protocol-path]/scripts/reusable/validate_graphs.py scripts/

# Copy and customize structure validator
cp [protocol-path]/scripts/templates/validate_structure.py.template scripts/validate_structure.py
# Then edit scripts/validate_structure.py
```

### Phase 7/8 (KG Maintenance)

```bash
# Copy KG maintenance scripts
cp [protocol-path]/scripts/reusable/kg_heal.py scripts/
cp [protocol-path]/scripts/reusable/kg_monitor.py scripts/

# Customize kg_monitor.py if needed (line 25)
```

## Template Rigidity Levels

### ⭐⭐⭐⭐⭐ **LEVEL 1: REQUIRED (Copy Exactly)**

**These scripts MUST be copied with NO changes**:
- ✅ `reusable/validate_graphs.py`
- ✅ `reusable/kg_heal.py`
- ✅ `reusable/kg_monitor.py`

**Why REQUIRED**:
- 🔒 **Deterministic logic**: Validation rules should be identical across projects
- 🔒 **Tested and proven**: Known to work correctly
- 🔒 **Bug fixes propagate**: Improvements benefit all projects automatically
- 🔒 **Zero customization needed**: Works for any Agent Builder system

**Risk if regenerated**:
- ❌ Logic errors or subtle bugs
- ❌ Inconsistent validation between projects
- ❌ Time wasted debugging identical functionality
- ❌ Potential security issues in validation logic

---

### ⭐⭐⭐⭐ **LEVEL 2: RECOMMENDED (Copy and Customize)**

**This template needs project-specific customization**:
- ✅ `templates/validate_structure.py.template`

**Why template recommended**:
- 📋 **Structure is standard**: Same validation approach
- 📋 **Customization points clear**: Only lists change
- 📋 **Saves time**: Don't recreate validation logic

**Required customization**:
- Update directory lists with your domain role
- Update file lists with your graph names
- Minimal changes (< 10 lines)

---

## Benefits

- ✅ **Efficiency**: No need to write identical code
- ✅ **Consistency**: All projects use tested scripts
- ✅ **Maintainability**: Bug fixes in one place
- ✅ **Clarity**: Clear reusable vs. customizable distinction
- ✅ **Reliability**: Pre-tested code reduces errors

## Version

**Protocol Version**: 2.0
**Last Updated**: November 28, 2025
