# Protocol JSON Templates

This directory contains reusable JSON templates for the AI Agent Setup Protocol V2.0.

## Directory Structure

```
json-templates/
├── README.md
└── agent-builder/
    ├── agent-builder-knowledge-graph.json.template
    ├── agent-builder-skills-graph.json.template
    └── agent-builder-behaviors-graph.json.template
```

## Templates

### Agent Builder Templates (100% Reusable)

The Agent Builder role is **standardized** across all projects. These three JSON files are **100% identical** for every agent system.

#### `agent-builder-knowledge-graph.json.template`

**Purpose**: Agent Builder's understanding of system architecture
**Used in**: Phase 4, Action 4.3a
**Reusability**: 100% - No customization needed

**Size**: ~70 lines

**Features**:
- System architecture nodes (sys:root, sys:agents, sys:config, sys:docs)
- Documentation structure (general + builder)
- Knowledge Graph meta-concepts
- Fully connected (all nodes have parent)

**Usage in Phase 4**:

```bash
# Copy to project (no changes needed)
cp [protocol-path]/json-templates/agent-builder/agent-builder-knowledge-graph.json.template \
   agents/knowledge-graphs/agent-builder-knowledge-graph.json
```

---

#### `agent-builder-skills-graph.json.template`

**Purpose**: Agent Builder's system maintenance capabilities
**Used in**: Phase 4, Action 4.4a
**Reusability**: 100% - No customization needed

**Size**: ~78 lines

**Features**:
- KG Maintenance skill tree (maintain-kg orchestrator + 3 sub-skills)
- Structure validation skill
- Full parent-child hierarchy
- Cross-links to behaviors
- Implementation types defined

**Skills included**:
1. `skill-maintain-kg` (orchestrator, hybrid)
   - `skill-kg-monitor` (rule-based)
   - `skill-kg-update` (hybrid)
   - `skill-kg-heal` (rule-based)
2. `skill-validate-structure` (rule-based)

**Usage in Phase 4**:

```bash
# Copy to project (no changes needed)
cp [protocol-path]/json-templates/agent-builder/agent-builder-skills-graph.json.template \
   agents/knowledge-graphs/agent-builder-skills-graph.json
```

---

#### `agent-builder-behaviors-graph.json.template`

**Purpose**: Agent Builder's system protocols
**Used in**: Phase 4, Action 4.5a
**Reusability**: 100% - No customization needed

**Size**: ~51 lines

**Features**:
- Core behaviors (system safety)
- Agent Builder-specific behaviors (KG consistency, system integrity)
- Cross-links to skills
- Cross-links to system components
- Priority levels defined

**Behaviors included**:
1. `behavior:core:safety` (all roles)
2. `behavior:agent-builder:kg-consistency` (enforces skill-maintain-kg)
3. `behavior:agent-builder:system-integrity` (enforces skill-validate-structure)

**Usage in Phase 4**:

```bash
# Copy to project (no changes needed)
cp [protocol-path]/json-templates/agent-builder/agent-builder-behaviors-graph.json.template \
   agents/knowledge-graphs/agent-builder-behaviors-graph.json
```

---

## Template Rigidity Level

### ⭐⭐⭐⭐⭐ **LEVEL 1: REQUIRED (Copy Exactly)**

**These templates MUST be copied with minimal/no changes**:
- ✅ `agent-builder-knowledge-graph.json.template`
- ✅ `agent-builder-skills-graph.json.template`
- ✅ `agent-builder-behaviors-graph.json.template`

**Why REQUIRED**:
- 🔒 **Structural integrity**: JSON syntax must be perfect
- 🔒 **Graph connectivity**: Parent links must be exact
- 🔒 **Standardized component**: Agent Builder is identical across all projects
- 🔒 **Tested and validated**: Known to work, reduces errors
- 🔒 **Cross-project consistency**: All agents have same foundation

**When to deviate**: NEVER for Agent Builder graphs. These are the structural foundation.

**Risk if generated instead of copied**:
- ❌ Orphaned nodes (missing parent fields)
- ❌ Broken cross-links
- ❌ JSON syntax errors
- ❌ Inconsistent node IDs
- ❌ Time wasted debugging

## Benefits

### Why Templates for Agent Builder?

- ✅ **100% Reusable**: Agent Builder is standardized across all projects
- ✅ **Zero Errors**: Copy tested JSON instead of regenerating
- ✅ **Faster**: Instant copy vs. AI generation (saves 5-10 min per graph)
- ✅ **Consistency**: All projects have identical Agent Builder foundation
- ✅ **Maintainability**: Improve templates once, all projects benefit
- ✅ **Validation**: Pre-validated, guaranteed to pass validators

### Why NOT Templates for Domain Role?

- ❌ **Highly Customized**: Each domain has unique skills, behaviors, knowledge
- ❌ **Variable Structure**: Different domains need different graph structures
- ❌ **Small Examples**: Domain role JSON examples are only ~30-40 lines each
- ✅ **Better as Examples**: Agent learns the pattern and generates custom version
- ✅ **Agent is capable**: LLMs excel at generating project-specific JSON

## Usage Pattern

### In Phase 4

**For Agent Builder graphs** (Actions 4.3a, 4.4a, 4.5a):
```bash
# Simply copy the templates
cp [protocol-path]/json-templates/agent-builder/*.template agents/knowledge-graphs/
rename .template ""  # Remove .template extension
```

**For Domain Role graphs** (Actions 4.3b, 4.4b, 4.5b):
```markdown
# Follow the examples in Phase 4
# Generate custom JSON based on Phase 1/2 design
```

---

## Version

**Protocol Version**: 2.0
**Last Updated**: November 28, 2025
**Templates**: 3 files (Agent Builder only)

