# Agent Builder Assets (Reusable Components)

## Purpose

This folder contains **100% reusable** Agent Builder components that are identical across all agent projects. These files contain NO project-specific content and can be copied as-is.

---

## Contents

### `.cursor/behaviors/`

**Core Behaviors** (apply to all roles):

- `core/system-safety.md` - Data loss prevention
- `core/project-structure.md` - Folder organization rules
- `core/git-workflow.md` - Version control standards
- `core/confidentiality.md` - Data separation rules

**Builder Behaviors** (Agent Builder role):

- `builder/enforce-schema.md` - Template and schema enforcement
- `builder/graph-consistency.md` - KG must reflect file system reality

### `agents/skills/system/`

**System Skills** (Agent Builder capabilities):

- `maintain-kg.md` - KG maintenance orchestrator
- `kg-monitor.md` - Detect file system changes
- `kg-update-node.md` - Add/modify/remove KG nodes
- `kg-heal.md` - Fix orphaned nodes and broken links
- `validate-structure.md` - Check folder structure
- `validate-graphs.md` - Validate JSON graphs

### `agents/knowledge-graphs/`

**Builder Knowledge Graphs** (3 files):

- `builder-knowledge-graph.json` - System architecture understanding
- `builder-skills-graph.json` - Builder capabilities tree
- `builder-behaviors-graph.json` - Builder protocols

### `docs/general/`

**Templates**:

- `CONTENT_TEMPLATE.md` - Standard template for new markdown files

### `scripts/`

**Validation Scripts** (4 Python files):

- `kg_heal.py` - Validates graph connectivity (100% reusable)
- `kg_monitor.py` - Detects file system changes (95% reusable - customize MONITORED_DIRS)
- `validate_graphs.py` - Validates JSON structure (100% reusable)
- `validate_structure.py` - Validates folder structure (90% reusable - update domain role)

See `scripts/README.md` for detailed usage and customization instructions.

---

## Usage in Protocol V3

### Phase 3: Project Structure

Copy these folders to the new project:

```bash
# Copy behaviors
cp -r builder-assets/.cursor/behaviors/* <project>/.cursor/behaviors/

# Copy skills
cp -r builder-assets/agents/skills/system <project>/agents/skills/

# Copy knowledge graphs
cp builder-assets/agents/knowledge-graphs/builder-*.json <project>/agents/knowledge-graphs/

# Copy templates
cp builder-assets/docs/general/CONTENT_TEMPLATE.md <project>/docs/general/

# Copy validation scripts
cp builder-assets/scripts/*.py <project>/scripts/
```

**After copying scripts**: Customize `kg_monitor.py` and `validate_structure.py` with your domain-specific values (see `scripts/README.md`).

### What NOT to Copy

These are project-specific and must be generated/designed:

- Domain role behaviors (`.cursor/behaviors/<domain-role>/`)
- Domain role skills (`agents/skills/<domain-role>/`)
- Domain role knowledge graphs (`<domain-role>-*.json`)
- Domain-specific documentation (`docs/<domain-role>/`)

---

## Verification

All files in this folder have been verified to contain:

- ✅ No project names
- ✅ No project-specific IDs
- ✅ No domain-specific content
- ✅ Generic, reusable logic only

**Total files**: 21  
**Total size**: ~34KB

---

## Maintenance

If updating these files:

1. Ensure changes are generic (apply to ALL agents)
2. Test with multiple projects
3. Update this README if structure changes
