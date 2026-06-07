# Reference Examples

## Purpose

This folder contains **complete, working examples** from the Agentic AI Project Manager project. These serve as reference patterns for LLMs to understand what a finished file should look like.

**IMPORTANT**: These are NOT templates. Do not copy-paste and replace placeholders. Instead, **read to understand the pattern**, then **generate fresh content** following the corresponding spec.

---

## Files

### 1. `identity.md`

**From**: Agentic AI Project Manager  
**Shows**: How to define BOTH roles (Agent Builder + Domain Role)  
**Spec**: `../specs/identity-structure.spec.md`

**Key Patterns**:

- Dual-role structure
- Role definitions with ID, personality, responsibilities, boundaries
- Operating principles and core values

---

### 2. `master-graph.json`

**From**: Agentic AI Project Manager  
**Shows**: How to reference ALL graphs (builder + domain)  
**Spec**: `../specs/master-graph-structure.spec.md`

**Key Patterns**:

- 6 graph entries (3 builder + 3 domain)
- 2 role entries (builder + domain)
- Consistent ID naming

---

### 3. `NEW_AGENT_START_HERE.md`

**From**: Agentic AI Project Manager  
**Shows**: How to onboard new agents to BOTH roles  
**Spec**: `../specs/start-here-structure.spec.md`

**Key Patterns**:

- Quick start checklist
- Separate sections for each role
- Knowledge graph explanation
- Validation workflows

---

### 4. `USER_MANUAL.md`

**From**: Agentic AI Project Manager (Antigravity version)  
**Shows**: How to write user-facing documentation for BOTH roles  
**Spec**: `../specs/user-manual-structure.spec.md`

**Key Patterns**:

- Magic activation prompts
- Role-specific workflows
- Troubleshooting guides
- Written for HUMANS, not AI

---

## How to Use

### ❌ Wrong Way (V2 - Failed)

```
1. Copy identity.md
2. Find "Agentic AI Project Manager" → Replace with "My Project"
3. Find "Project Manager" → Replace with "My Role"
... (LLM misses some, breaks formatting)
```

### ✅ Right Way (V3 - Works)

```
1. Read examples/identity.md to see the pattern
2. Read specs/identity-structure.spec.md to understand requirements
3. Extract variables from Phase 1 output
4. Generate NEW identity.md following the spec
   - Role 1 (Builder): Use description from example as reference
   - Role 2 (Domain): Generate based on Phase 1 data
```

---

## Why This Works

**LLMs are good at**:

- Understanding patterns from examples
- Generating coherent content
- Following structural specifications

**LLMs are bad at**:

- Precise find-and-replace
- Character-level editing
- Preserving encoding through copy-paste

**Solution**: Show the pattern (example) + Define the structure (spec) + Generate fresh (LLM strength)

---

## Related Files

- **Specs**: `../specs/` - Structural requirements for each file
- **Generation Pattern**: `../specs/generation-pattern.md` - Overall approach
- **Builder Assets**: `../builder-assets/` - Reusable builder components

---

## Maintenance

When updating these examples:

1. Ensure they represent current best practices
2. Update corresponding specs if structure changes
3. Test generation with new LLM to verify pattern clarity
