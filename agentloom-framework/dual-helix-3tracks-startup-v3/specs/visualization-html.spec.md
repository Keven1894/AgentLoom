# Visualization HTML Specification

## Purpose

Generate a standalone HTML file that visualizes all Knowledge Graphs interactively.

## Input Required

Before generating, the agent MUST know:

- `PROJECT_NAME`: The human-readable project name
- `DOMAIN_ROLE_NAME`: The domain role name (e.g., "Project Manager")
- `DOMAIN_ROLE_ID`: The kebab-case ID (e.g., "project-manager")
- `DOMAIN_ID`: The domain graph prefix (e.g., "project-management")

## Output File

`agents/knowledge-graphs/visualization.html`

## Functional Requirements

### 1. Graph Loading

- Load JSON files from the same directory
- Support these graph files:
  - `master-graph.json`
  - `agent-builder-knowledge-graph.json`
  - `agent-builder-skills-graph.json`
  - `agent-builder-behaviors-graph.json`
  - `{DOMAIN_ROLE_ID}-knowledge-graph.json`
  - `{DOMAIN_ROLE_ID}-skills-graph.json`
  - `{DOMAIN_ROLE_ID}-behaviors-graph.json`
  - `{DOMAIN_ID}-content-graph.json` (optional)

### 2. Sidebar Navigation

- Fixed sidebar on left
- Project name as header
- Button groups:
  - System Views: "Unified Brain (ALL)", "Master Graph"
  - Agent Builder: Knowledge, Skills, Behaviors
  - {DOMAIN_ROLE_NAME}: Knowledge, Skills, Behaviors
- Active button highlighted

### 3. Graph Rendering

- Use vis-network library (CDN: <https://unpkg.com/vis-network/standalone/umd/vis-network.min.js>)
- Parse nodes from JSON (handle: nodes, skills, behaviors, graphs arrays)
- Create edges from `parent` field (solid lines)
- Create edges from `links` object (dashed lines with labels)

### 4. Node Visualization

- Colors by type:
  - Root/master: violet (#8b5cf6)
  - Agent Builder nodes: blue (#3b82f6)
  - Domain role nodes: green (#10b981)
  - Behaviors: yellow (#eab308)
  - Skills: pink (#ec4899)
  - Concepts: orange (#f97316)
  - Documents: slate (#64748b)
- Shapes:
  - root/master: diamond
  - skill: triangle
  - behavior: hexagon
  - concept: star
  - document: ellipse
  - default: dot

### 5. Statistics Overlay

- Show current graph name
- Show node count
- Show link count

### 6. Legend

- Fixed at bottom-right
- Show node type colors and shapes
- Show link type meanings (solid = parent, dashed = cross-link)

### 7. Composite Views

When loading skills graph, also load behaviors graph (and vice versa) to show cross-links.

### 8. Unified Brain View

Load ALL graphs simultaneously to show complete system.

## Style Requirements

- Dark theme (background: #0f172a)
- Light text (#f1f5f9)
- Rounded corners on UI elements
- Subtle shadows
- Full viewport graph area

## Technical Constraints

- Single HTML file (no external CSS/JS files except CDN)
- Must work when opened directly in browser (file:// protocol)
- No build step required

## Validation Criteria

After generation, verify:

1. File opens in browser without errors
2. Master graph loads on start
3. All buttons are clickable and load correct graphs
4. Node colors match specification
5. Statistics update when switching views
