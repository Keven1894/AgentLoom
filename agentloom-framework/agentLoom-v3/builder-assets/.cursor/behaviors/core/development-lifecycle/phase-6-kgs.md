# Phase 6: Create Knowledge Graphs

**Parent**: [AgentLoom Development Lifecycle](./INDEX.md)

---

## Goal

Map the 3 Tracks (Behaviors, Knowledge, Skills) into structured JSON Knowledge Graphs.

---

## 6.1 Build Individual Graphs

Create the JSON files in `agents/knowledge-graphs/`:

- **`behaviors-graph.json`**: Nodes for every file in `.cursor/`.
- **`knowledge-graph.json`**: Nodes for every file in `docs/`.
- **`skills-graph.json`**: Nodes for every skill in `agents/skills/`.

*Use the `json-helper` toolkit (`generator.py`) to create these files from templates.*

## 6.2 Create Master Graph

Create `master-graph.json` to serve as the entry point:

- List all sub-graphs.
- Define Roles (Builder, Manager, etc.) and which graphs they access.

## 6.3 Validate Connectivity

- Ensure every node has a unique ID.
- Ensure all file paths are correct relative to project root.
- Use `validator.py` to check against schemas.

---

**Output**: A set of validated JSON files representing the agent's brain.
