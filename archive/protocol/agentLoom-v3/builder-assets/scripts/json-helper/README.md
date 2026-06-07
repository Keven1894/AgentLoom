# JSON Helper Toolkit for Knowledge Graph Maintenance

**Purpose**: Robust, modular toolkit for safe JSON Knowledge Graph operations

---

## Architecture

### Modules

1. **`validator.py`** - JSON Schema validation
   - Uses `jsonschema` (RFC compliant)
   - KG-specific schema definitions
   - Detailed error reporting

2. **`updater.py`** - Safe JSON updates
   - Uses `jsonpatch` (RFC 6902)
   - Atomic operations
   - Automatic backup & rollback

3. **`generator.py`** - JSON generation
   - Template-based node generation
   - Type-safe creation
   - Auto-completion of required fields

4. **`kg_editor.py`** - High-level KG operations
   - Wraps validator, updater, generator
   - KG-aware operations (add/update/remove nodes/links)
   - CLI interface

---

## Libraries Used

### Core Dependencies

```
jsonschema>=4.20.0    # Standard JSON Schema validation
jsonpatch>=1.33       # RFC 6902 JSON Patch operations
```

### Optional (Future)

```
pydantic>=2.5.0       # Type-safe models & schema generation
jsonschema-rs         # Rust-based high-performance validation
```

---

## Design Principles

1. **Atomic Operations**: All updates are atomic (all-or-nothing)
2. **Validation First**: Always validate before and after changes
3. **Non-Destructive**: Default to copying, not in-place modification
4. **Automatic Backup**: Create timestamped backups before changes
5. **Clear Error Messages**: Detailed, actionable error reporting
6. **Type-Aware**: Understand KG structure (skills/behaviors/knowledge)

---

## Usage Examples

### Validator

```python
from json_helper.validator import KGValidator

validator = KGValidator()
result = validator.validate_file('agents/knowledge-graphs/manager-skills-graph.json')
if not result.is_valid:
    print(result.errors)
```

### Updater (JSON Patch)

```python
from json_helper.updater import KGUpdater

updater = KGUpdater('agents/knowledge-graphs/manager-skills-graph.json')
patch = [
    {"op": "add", "path": "/skills/-", "value": {...}}
]
updater.apply_patch(patch)  # Atomic, with backup
```

### Generator

```python
from json_helper.generator import NodeGenerator

gen = NodeGenerator()
skill_node = gen.create_skill(
    id="skill-new",
    name="New Skill",
    category="learning-monitoring",
    ...
)
```

### High-Level Editor

```python
from json_helper.kg_editor import KGEditor

editor = KGEditor('agents/knowledge-graphs/manager-skills-graph.json')
editor.add_skill(skill_data)  # Validates, backs up, applies, validates again
editor.add_link('skill-a', 'skill-b', 'uses')
editor.save()
```

---

## CLI Interface

```bash
# Validate
python -m json_helper validate agents/knowledge-graphs/manager-skills-graph.json

# Add node
python -m json_helper add --file <kg.json> --node-file <node.json>

# Update field
python -m json_helper update --file <kg.json> --path "/skills/0/description" --value "New desc"

# Add link
python -m json_helper link --file <kg.json> --from skill-a --to skill-b --type uses

# Generate node template
python -m json_helper generate skill --output temp/new-skill.json
```

---

## Safety Features

### 1. Atomic Operations (jsonpatch)

- If any operation fails, entire patch is rolled back
- No partial updates
- Consistent state guaranteed

### 2. Pre/Post Validation (jsonschema)

- Validate before applying changes
- Validate after applying changes
- Ensure schema compliance

### 3. Automatic Backups

- Timestamped backups before modifications
- Easy rollback if needed
- Configurable retention

### 4. Conflict Detection

- Detect concurrent modifications
- Prevent overwriting changes
- Clear conflict messages

### 5. Test Operations

- JSON Patch `test` operation for pre-conditions
- Verify state before modifying
- Fail fast on unexpected state

---

## Next Steps

1. ✅ Research best libraries (DONE)
2. ⏳ Create JSON schemas for KG types
3. ⏳ Implement validator.py
4. ⏳ Implement updater.py (jsonpatch-based)
5. ⏳ Implement generator.py
6. ⏳ Implement kg_editor.py (high-level wrapper)
7. ⏳ Create CLI interface
8. ⏳ Write comprehensive tests
9. ⏳ Document usage patterns

---

## File Structure

```
scripts/json-helper/
├── __init__.py
├── README.md (this file)
├── requirements.txt
├── schemas/
│   ├── skills-graph.schema.json
│   ├── behaviors-graph.schema.json
│   ├── knowledge-graph.schema.json
│   └── project-graph.schema.json
├── validator.py
├── updater.py
├── generator.py
├── kg_editor.py
├── __main__.py (CLI entry point)
└── tests/
    ├── test_validator.py
    ├── test_updater.py
    ├── test_generator.py
    └── test_kg_editor.py
```
