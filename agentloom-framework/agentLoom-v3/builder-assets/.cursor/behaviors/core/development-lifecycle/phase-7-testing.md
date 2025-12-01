# Phase 7: Integration & Testing

**Parent**: [AgentLoom Development Lifecycle](./INDEX.md)

---

## Goal

Verify that all components work together and the Knowledge Graph is healthy.

---

## 7.1 Test Individual Components

- **Behaviors**: Review rules for clarity and conflicts.
- **Knowledge**: Verify links and content accuracy.
- **Skills**: Run unit tests for scripts.

## 7.2 Test Integration

- **Cross-Track Links**: Verify `governed_by` and `references` links work.
- **KG Health**: Run `validate_kg_links.py` to check for broken links and orphans.
- **Workflows**: Step through the workflows defined in Phase 3.

## 7.3 Test with Real Usage

- Simulate user interactions.
- Test edge cases (e.g., missing files, invalid inputs).
- Verify the agent respects its constraints (Track 1).

---

**Output**: A validated, tested agent with a healthy Knowledge Graph.
