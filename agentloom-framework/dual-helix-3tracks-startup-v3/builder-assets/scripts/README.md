# Builder Scripts (Reusable Validation Tools)

## Purpose

These Python scripts validate the agent project structure and Knowledge Graphs. They are designed to be reusable across all agent projects.

---

## Scripts Overview

### 1. `kg_heal.py` ✅ 100% Reusable

**Purpose**: Validates Knowledge Graph connectivity  
**Checks**:

- Orphaned nodes (nodes without parents)
- Broken parent references (invalid parent IDs)

**Usage**:

```bash
python scripts/kg_heal.py
```

**Customization**: None needed - works with any KG structure

---

### 2. `kg_monitor.py` ⚙️ 95% Reusable

**Purpose**: Detects file system changes vs Knowledge Graph  
**Checks**:

- New files not yet in KG
- Deleted files still in KG

**Usage**:

```bash
python scripts/kg_monitor.py
```

**Customization Required**:

- **Line 19-23**: Update `MONITORED_DIRS` list for your project
- Default monitors: `.cursor/behaviors`, `agents/skills`, `docs`
- Add/remove directories based on your domain role

**Example**:

```python
MONITORED_DIRS = [
    '.cursor/behaviors',
    'agents/skills',
    'docs',
    'custom-domain-folder'  # Add your domain-specific folders
]
```

---

### 3. `validate_graphs.py` ✅ 100% Reusable

**Purpose**: Validates JSON structure and file references  
**Checks**:

- Valid JSON syntax
- Required fields present
- Referenced files exist

**Usage**:

```bash
python scripts/validate_graphs.py
```

**Customization**: None needed - validates any graph type

---

### 4. `validate_structure.py` ⚙️ 90% Reusable

**Purpose**: Validates project folder structure  
**Checks**:

- Required directories exist
- Core files present

**Usage**:

```bash
python scripts/validate_structure.py
```

**Customization Required**:

- **Line 14**: Update `'agents/behaviors/manager'` to your domain role
- **Line 30**: Update `'agents/USER_MANUAL.md'` path if different

**Example**:

```python
required_dirs = [
    # ... other dirs ...
    'agents/behaviors/builder',
    'agents/behaviors/researcher',  # Change 'manager' to your role
]
```

---

## Reusability Summary

| Script | Reusability | Customization Needed |
|--------|-------------|---------------------|
| `kg_heal.py` | 100% | None |
| `kg_monitor.py` | 95% | Update MONITORED_DIRS |
| `validate_graphs.py` | 100% | None |
| `validate_structure.py` | 90% | Update domain role name |

---

## Integration with Protocol V3

### Phase 3: Project Structure

Copy all 4 scripts to `scripts/` folder

### Phase 6: Validation

Customize `kg_monitor.py` and `validate_structure.py` with domain-specific values

### Phase 9: Final Validation

Run all scripts to verify project integrity

---

## Dependencies

All scripts use Python standard library only:

- `json`
- `sys`
- `pathlib`
- `os`
- `datetime`

**No external packages required** ✅
