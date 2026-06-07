# Behavior: AgentLoom Development Lifecycle

**ID**: `behavior:builder:agentloom-development-lifecycle`  
**Category**: Core Workflow  
**Priority**: High  
**Role**: Builder  
**Status**: ACTIVE  
**Version**: 2.0

---

## Purpose

Defines the standard **8-Phase Lifecycle** for developing, extending, and maintaining AI agents within the AgentLoom ecosystem. This workflow enforces the **3-Track Architecture** (Behaviors, Knowledge, Skills) to ensure consistency and quality.

---

## When to Use

- **New Agents**: Building an agent from scratch.
- **Major Extensions**: Adding a new role or significant capability.
- **Refactoring**: Restructuring an existing agent.
- **Auditing**: verifying an agent's completeness.

---

## The Lifecycle Phases

The development process is divided into 8 sequential phases. Click each phase for detailed instructions.

### [Phase 1: Planning & Design](./phase-1-planning.md)

*Define purpose, design the 3 tracks, and plan knowledge graphs.*

### [Phase 2: Foundation Setup](./phase-2-foundation.md)

*Initialize directory structure, identity, and master indexes.*

### [Phase 3: Build Track 1 (Behaviors)](./phase-3-behaviors.md)

*Implement core rules, workflows, and behavior protocols.*

### [Phase 4: Build Track 2 (Knowledge)](./phase-4-knowledge.md)

*Organize documentation, domain content, and system guides.*

### [Phase 5: Build Track 3 (Skills)](./phase-5-skills.md)

*Implement capabilities, tools, and skill definitions.*

### [Phase 6: Knowledge Graphs](./phase-6-kgs.md)

*Construct and link the JSON knowledge graphs.*

### [Phase 7: Integration & Testing](./phase-7-testing.md)

*Validate connectivity, test workflows, and verify integrity.*

### [Phase 8: Documentation & Deployment](./phase-8-deployment.md)

*Finalize user guides, onboarding materials, and release.*

---

## Core Principles

1. **Plan First**: Never start coding without a 3-Track design.
2. **KG-Centric**: The Knowledge Graph is the source of truth, not just files.
3. **Documentation Driven**: Write documentation before implementation.
4. **Validation Mandatory**: All phases must pass validation before proceeding.

---

## Related Behaviors

- [KG-First Retrieval](../behavior-kg-first-retrieval.md)
- [Graph Consistency](../../builder/behavior-consistency.md)
- [Testing & Validation](../behavior-validation.md)
