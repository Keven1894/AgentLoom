# Protocol HTML Templates

This directory contains reusable HTML templates for the AI Agent Setup Protocol V2.0.

## Directory Structure

```
htmls/
└── templates/
    ├── visualization.html.template
    └── (user_manual.html.template - Phase 11)
```

## Templates

### `visualization.html.template`

**Purpose**: Interactive Knowledge Graph visualization tool
**Used in**: Phase 10
**Reusability**: Template - Requires customization

**Customization Required**:

1. Replace `[Project Name]` with your project name (line 5, 68)
2. Replace `[Domain Role Name]` with your domain role name (line 86)
3. Replace `[domain-id]` with your domain graph ID (lines 127, 151)
4. Replace `[domain-role-id]` with your domain role ID (lines 87-89, 132-134, 152-154, 177)

**Features**:

- Unified Brain view (all graphs merged)
- Role-specific views (Agent Builder + Domain Role)
- Composite loading (skills + behaviors together)
- Cross-graph link visualization
- Color-coded node types
- Interactive tooltips
- Statistics overlay

**Usage in Phase 10**:

```bash
# Copy template to project
cp [protocol-path]/htmls/templates/visualization.html.template agents/knowledge-graphs/visualization.html

# Customize placeholders
# Edit agents/knowledge-graphs/visualization.html
```

### `user_manual.html.template` (Coming in Phase 11)

**Purpose**: Interactive user manual with navigation
**Used in**: Phase 11
**Features**: TBD

## Template Rigidity Level

### ⭐⭐⭐⭐⭐ **LEVEL 1: REQUIRED (Copy and Customize)**

**This template MUST be copied** (minimal customization required):

- ✅ `templates/visualization.html.template`

**Why REQUIRED**:
- 🔒 **Complex interactive code**: ~550 lines of HTML/CSS/JavaScript
- 🔒 **Library integration**: Uses vis-network for graph rendering
- 🔒 **Tested and working**: Known to work across browsers
- 🔒 **Agent would struggle**: Frontend code with external dependencies

**Customization required** (minimal):
- Replace `[Project Name]` (2 places)
- Replace `[Domain Role Name]` (1 place)
- Replace `[domain-role-id]` (4-5 places)
- Replace `[domain-id]` (2 places)

**Total changes**: ~8-10 simple find-replace operations

**Risk if regenerated instead of copied**:
- ❌ JavaScript syntax errors
- ❌ Library integration issues
- ❌ Missing features (Unified Brain, composite views)
- ❌ Hours of debugging
- ❌ Inconsistent visualization across projects

**Agent capability for this**: Low-Medium (complex frontend code)

---

## Benefits

- ✅ **Separation of concerns**: HTML templates separate from markdown instructions
- ✅ **Reusability**: Copy and customize instead of writing from scratch
- ✅ **Maintainability**: Bug fixes and improvements in one place
- ✅ **Clarity**: Phases focus on instructions, not code
- ✅ **Consistency**: All projects use same tested templates
- ✅ **Reliability**: Known-working visualization with minimal effort

## Version

**Protocol Version**: 2.0
**Last Updated**: November 28, 2025
