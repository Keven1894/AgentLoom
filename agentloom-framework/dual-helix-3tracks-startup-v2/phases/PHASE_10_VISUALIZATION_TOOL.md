# Phase 10: Visualization Tool

**AI Agent Setup Protocol V2.0**

---

## 📌 Phase Context

**Prerequisites**: Phases 1-9 complete  
**Input needed from previous phases**:
- Domain role ID and name (Phase 1)
- All graph filenames (Phase 4)
- Project name (Phase 1)

**Output**: visualization.html + VIEW_VISUALIZATION.md  
**Estimated time**: 30-45 minutes

**Creates for next phases**:
- visualization.html → Phase 11 (referenced in user manual)
- Visual validation tool → Ongoing KG maintenance

**Critical**: Copy template and customize ~8-10 placeholders

---

## Objective

Create an interactive HTML tool to visualize and validate Knowledge Graph connectivity.

---

## Why This Matters

Without visualization, you cannot verify:

- Are all nodes connected?
- Do cross-graph links work?
- Are there orphaned nodes?
- Is the graph truly a "Unified Brain"?

**This tool enables visual validation** that complements the automated validators from Phase 9.

---

## When This Is Used

**Created in**: Phase 10 (this phase)
**Used in**:

- Phase 9 validation (visual confirmation)
- Ongoing maintenance (verify KG updates)
- Documentation (show graph structure)

**Note**: This is created BEFORE the user manual (Phase 11), so users can visually validate the system before testing cold-start.

---

## Action 10.1: Copy and Customize Visualization Template

The protocol package includes a **reusable visualization template** that you can copy and customize.

**Step 1: Copy the template**:

```bash
# Copy from protocol package to your project
cp [protocol-path]/htmls/templates/visualization.html.template agents/knowledge-graphs/visualization.html
```

**Step 2: Customize placeholders**:

Open `agents/knowledge-graphs/visualization.html` and replace:

1. **Line 5, 68**: `[Project Name]` → Your project name
2. **Line 86**: `[Domain Role Name]` → Your domain role name (e.g., "Project Manager")
3. **Lines 127, 151**: `[domain-id]` → Your domain graph ID (e.g., "project-management")
4. **Lines 87-89, 132-134, 152-154, 177**: `[domain-role-id]` → Your domain role ID (e.g., "project-manager")

**Example customization**:

```html
<!-- Before -->
<h2>🧠 [Project Name]</h2>
<div class="btn-group-label">[Domain Role Name]</div>
<button onclick="loadGraph('[domain-role-id]-knowledge')" ...>

<!-- After -->
<h2>🧠 Project Management Assistant</h2>
<div class="btn-group-label">Project Manager</div>
<button onclick="loadGraph('project-manager-knowledge')" ...>
```

**Step 3: Test it**:

Open `agents/knowledge-graphs/visualization.html` in a web browser.

**Expected result**:

- Master Graph loads by default
- Sidebar shows all role views
- Statistics show node/link counts
- No console errors

**Report**:

```
✅ Created visualization.html (~550 lines) with:
- Unified Brain view (all graphs merged)
- Agent Builder views (knowledge/skills/behaviors)
- Domain Role views (knowledge/skills/behaviors)
- Composite loading (skills + behaviors together)
- Cross-graph link visualization (dashed amber lines)
- Color-coded node types
- Interactive tooltips
```

---

## Action 10.2: Create Visualization Instructions

Create `agents/knowledge-graphs/VIEW_VISUALIZATION.md`:

```markdown
# Knowledge Graph Visualization Guide

## Quick Start

1. Open `visualization.html` in a web browser
2. The Master Graph loads by default
3. Use sidebar buttons to explore different views

## Views

### 🌌 Unified Brain (ALL)
Shows ALL graphs merged together. Use this to:
- Verify full system connectivity
- See cross-graph relationships
- Validate that no nodes are orphaned
- Understand the complete "mind" of the agent

**Note**: This view can be cluttered for large systems. Use role-specific views for detailed exploration.

### 🌐 Master Graph
High-level entry point showing:
- System architecture
- Role definitions
- Graph structure
- Project/domain overview

### Agent Builder Views (System Role)

The Agent Builder is always active and handles system maintenance:

- **🏗️ Knowledge**: System architecture, KG structure, protocol knowledge
- **🛠️ Skills**: KG maintenance, validation, healing (shows related behaviors)
- **🛡️ Behaviors**: Core protocols, safety rules (shows related skills)

### [Domain Role] Views

Your domain-specific role for actual work:

- **📚 Knowledge**: Domain concepts, documentation, content
- **⚡ Skills**: Domain-specific capabilities (shows related behaviors)
- **🤝 Behaviors**: Domain protocols, workflows (shows related skills)

## Node Colors & Shapes

**Colors**:
- 🟣 **Violet**: Root nodes, system entry points
- 🔵 **Blue**: Agent Builder nodes
- 🟢 **Green**: Domain role nodes
- 🟡 **Yellow**: Behavior nodes
- 🟣 **Pink**: Skill nodes
- 🟠 **Orange**: Concept nodes
- ⚫ **Slate**: Document/file nodes

**Shapes**:
- ◆ **Diamond**: Root/master nodes
- ▲ **Triangle**: Skills
- ⬡ **Hexagon**: Behaviors
- ★ **Star**: Concepts
- ● **Dot**: General nodes
- ○ **Ellipse**: Documents
- ▢ **Box**: Projects/databases

## Edge Types

- **Solid lines**: Parent-child hierarchical relationships (structural)
- **Dashed amber lines**: Cross-graph semantic links (labeled with relationship type)

**Example**: A skill node might have:
- Solid line to parent skill (hierarchy)
- Dashed line to related behavior (cross-graph semantic link)

## Validation Checklist

Use this tool to verify:

- [ ] **Unified Brain view**: All nodes are connected (no floating nodes)
- [ ] **Each graph**: Has exactly one root node
- [ ] **Cross-graph links**: Visible as dashed amber lines
- [ ] **Behaviors ↔ Skills**: Related nodes are linked
- [ ] **Document nodes**: Properly nested under folders/concepts
- [ ] **Statistics**: Show reasonable counts (not 0 or unexpectedly low)
- [ ] **Agent Builder**: Has all 4 KG maintenance skills
- [ ] **Domain Role**: Has expected skills and behaviors

## Composite Views

Some views automatically load related graphs:

- **Skills view**: Also loads behaviors (to show relationships)
- **Behaviors view**: Also loads skills (to show relationships)
- **Master view**: Also loads domain graph

This helps you see cross-graph connections without switching views.

## Troubleshooting

### Problem: Graph shows disconnected (floating) nodes
- **Cause**: Missing `parent` field in JSON
- **Fix**: Add `"parent": "[parent-id]"` to disconnected nodes
- **Verify**: Run `python scripts/kg_heal.py`

### Problem: No cross-graph links visible
- **Cause**: Missing `links` field or target node not in current view
- **Fix**: Use "Unified Brain" view to see all links
- **Check**: Verify `links` field in JSON has correct target IDs

### Problem: Graph is too cluttered
- **Cause**: Too many nodes in one view
- **Fix**: Use role-specific views instead of Unified Brain
- **Tip**: Master view filters out deep document nodes for clarity

### Problem: Graph file not found (console error)
- **Cause**: Graph file doesn't exist or wrong filename
- **Fix**: Check `agents/knowledge-graphs/` directory
- **Verify**: Filenames match those in `allGraphFiles` object (line 127)

### Problem: Nodes all the same color
- **Cause**: Node IDs don't match expected patterns
- **Fix**: Update `getNodeColor()` function (line 162) with your role IDs

## Advanced: Customizing the Visualization

### Update Role IDs
If you need to change role IDs after initial setup:
- Edit `allGraphFiles` object (line 127)
- Edit `viewDependencies` object (line 139)
- Update button onclick handlers (lines 87-89)

### Add More Graphs
Edit `allGraphFiles` object:
```javascript
'my-graph': 'my-graph.json'
```

Add button in sidebar:

```html
<button onclick="loadGraph('my-graph')" id="btn-my-graph">📊 My Graph</button>
```

### Customize Colors

Edit `getNodeColor()` function (line 162) to match your node ID patterns.

## Next Steps

After validating connectivity:

1. Note any disconnected nodes
2. Fix JSON files (add `parent` fields)
3. Refresh visualization (F5)
4. Re-validate until all nodes connected
5. Proceed to Phase 11 (User Manual & Testing)

```

**Create** `agents/knowledge-graphs/VIEW_VISUALIZATION.md` with the content above.

**Confirm to human**:
```
✅ Created VIEW_VISUALIZATION.md (comprehensive usage guide)
```

---

## Validation Checkpoint

```

✅ Visualization tool complete:

- visualization.html (copied and customized from template)
- VIEW_VISUALIZATION.md (usage guide)

Ready for visual validation:

1. Open visualization.html in browser
2. Check Unified Brain view for connectivity
3. Verify no floating nodes
4. Confirm cross-graph links visible

After visual validation, proceed to Phase 11 (User Manual & Testing).

## Notes

**Why use a template?**

- ✅ **Efficiency**: Copy instead of recreate
- ✅ **Consistency**: All projects use same tested code
- ✅ **Maintainability**: Bug fixes in protocol benefit all projects
- ✅ **Clarity**: Phase focuses on instructions, not code

**Template location**: `[protocol-package]/htmls/templates/visualization.html.template`

**For more details**: See `[protocol-package]/htmls/README.md`

---

**Previous Phase**: [Phase 9: Final Validation](PHASE_09_FINAL_VALIDATION.md)  
**Next Phase**: [Phase 11: User Manual & Testing](PHASE_11_USER_MANUAL_TESTING.md)
