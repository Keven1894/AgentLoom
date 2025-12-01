# Phase 1: Planning & Design

**Parent**: [AgentLoom Development Lifecycle](./INDEX.md)

---

## Goal

Define the agent's purpose and design the 3-Track Architecture before writing any code.

---

## 1.1 Define Agent Purpose

Create a clear mission statement answering:

- **Role**: What is the agent's primary function?
- **Users**: Who will interact with it?
- **Problem**: What specific pain points does it solve?
- **Success**: What does "good" look like?

## 1.2 Design the 3 Tracks

### Track 1: Behaviors (The "Superego")

- **Rules**: What constraints must it obey? (e.g., "Never delete user data")
- **Workflows**: What are the standard operating procedures?
- **Personality**: How should it communicate?

### Track 2: Knowledge (The "Memory")

- **Domain**: What subject matter expertise is needed?
- **Procedures**: What "how-to" guides does it need?
- **Context**: What project-specific information is required?

### Track 3: Skills (The "Hands")

- **Capabilities**: What actions can it perform?
- **Tools**: What scripts or APIs does it need?
- **Infrastructure**: What system access is required?

## 1.3 Plan Knowledge Graphs

Sketch the graph structure:

- How will Behaviors link to Skills? (e.g., `governs` links)
- How will Skills link to Knowledge? (e.g., `references` links)
- What are the key nodes in the Master Graph?

---

**Output**: A design document or `implementation_plan.md` approved by the user.
