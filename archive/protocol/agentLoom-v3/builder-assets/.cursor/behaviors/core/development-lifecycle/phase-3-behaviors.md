# Phase 3: Build Track 1 (Behaviors)

**Parent**: [AgentLoom Development Lifecycle](./INDEX.md)

---

## Goal

Implement the rules, workflows, and protocols that govern the agent's behavior.

---

## 3.1 Define Core Rules

Create markdown files in `.cursor/rules/core/`:

- **Principles**: High-level values (e.g., `academic-integrity.md`, `code-quality.md`).
- **Constraints**: Hard limits (e.g., `no-internet-access.md`).
- **System Rules**: Operational mandates (e.g., `documentation-first.md`).

## 3.2 Define Workflows

Create markdown files in `.cursor/rules/workflows/`:

- **SOPs**: Standard Operating Procedures for common tasks.
- **Decision Trees**: How to handle complex choices.
- **Error Handling**: Protocols for failure recovery.

## 3.3 Link Behaviors

Ensure behaviors reference each other:

- Use relative links: `[Related Rule](../core/rule.md)`
- Establish hierarchy: Core rules override workflows.
- Define priorities in frontmatter (`priority: critical|high|medium|low`).

---

**Output**: A set of behavior markdown files defining *how* the agent acts.
