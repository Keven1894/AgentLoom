# Phase 2: Architecture Design

**AI Agent Setup Protocol V2.0**

---

## 📌 Phase Context

**Prerequisites**: Phase 1 complete  
**Input needed from Phase 1**:
- Domain definition (domain, purpose, users)
- Domain role specification (ID, name, tasks, personality)
- Knowledge requirements (content folders if shared)
- Skills inventory
- Workflow requirements

**Output**: Complete architecture design for Phase 3  
**Estimated time**: 30-45 minutes

**Creates for next phases**:
- Behavior taxonomy → Phase 3, 5
- KG structure design → Phase 4
- Skills classification → Phase 5, 8

---

## Objective

Design the complete system architecture including behavior taxonomy, knowledge structure, skills classification, and **KG connectivity patterns**.

**Note**: This phase uses information gathered in Phase 1, including the mandatory Agent Builder role and custom domain role.

---

## Action 2.0: Analyze Shared Content (If Provided in Phase 1)

**If user shared content folders in Phase 1**, analyze them first:

### Scan Provided Folders

1. **Identify content structure**:
   - File types and extensions
   - Directory hierarchy depth
   - Naming conventions
   - Content categories

2. **Map to KG categories**:
   - Which folders map to knowledge nodes?
   - What's the natural hierarchy?
   - Are there cross-references between folders?

3. **Document findings**:

   ```
   Content Analysis:
   
   **Folder**: [path]
   - File types: [.md, .pdf, .txt, etc.]
   - Structure: [flat / 2-level / deep hierarchy]
   - Categories identified: [list]
   - Suggested KG mapping:
     - [folder/subfolder] → [knowledge-node-id]
     - [folder/subfolder] → [knowledge-node-id]
   
   **Cross-references detected**:
   - [folder A] references [folder B] → suggests link relationship
   ```

**If no folders shared**: Skip to Action 2.1.

---

## Action 2.1: Design Behavior Taxonomy

Based on gathered information from Phase 1, create a structured list:

### Core Behaviors (apply to all roles)

- Safety protocols (data protection, destructive action confirmation)
- Communication standards (how agent responds, error handling)
- System integrity (validation before changes)
- [Add 2-5 more based on Phase 1 answers]

### Agent Builder Behaviors (System Role - Standard)

**These are standard for every agent**:

- **KG Consistency**: Knowledge Graph must reflect file system reality
- **System Integrity**: Never modify `.cursor/` without explicit instruction
- **Validation Protocol**: Always validate structure/graphs after changes
- **Self-Evolution**: Maintain KG when files change
- [Add 1-2 more based on Phase 1 safety requirements]

### Domain Role Behaviors (Custom - Based on Phase 1)

**For [Domain Role Name]** (defined in Phase 1):

- [Behavior 1] - [Description based on role responsibilities]
- [Behavior 2] - [Description based on role tasks]
- [Behavior 3] - [Description based on role boundaries]
- [Continue with 3-5 total based on Phase 1 input]

### Workflow Behaviors

- Multi-step processes that must be followed in order
- Orchestration patterns (when to chain behaviors/skills)

### Present to Human

```
I've designed the behavior system:

**Core Behaviors** (all roles):
1. System Safety Protocol - Never delete data without confirmation
2. Communication Protocol - Clear, structured responses
3. [Continue with 3-8 more]

**Agent Builder Behaviors** (System Role - Standard):
1. KG Consistency - Knowledge Graph must reflect file system state
2. System Integrity - Never modify .cursor/ without explicit instruction
3. Validation Protocol - Always validate after structural changes
4. Self-Evolution - Maintain KG when files/folders change
[Add 1-2 more based on your requirements]

**[Domain Role Name] Behaviors** (Custom):
1. [Behavior 1] - [Description]
2. [Behavior 2] - [Description]
[Continue with 3-5 total based on Phase 1]

**Critical Workflows**:
1. [Workflow name]: [Step 1] → [Step 2] → [Step 3]

Should I proceed with this structure?
```

---

## Action 2.2: Design Knowledge Graph Structure (V2: FULLY CONNECTED)

**Critical V2 Addition**: Design for full connectivity from the start.

### Root Node Strategy

- Each graph MUST have a root node
- All top-level nodes MUST have `parent` field pointing to root
- All child nodes MUST have `parent` field pointing to their parent

### Cross-Graph Links Strategy

- Identify semantic relationships between tracks (Behaviors ↔ Skills ↔ Knowledge)
- Use `links` field with relationship types: `governs`, `enforces`, `implements`, `tracks`, etc.

### Example Structure

```
Master Graph (Entry Point)
├── Agent Builder (System Role - MANDATORY)
│   ├── Builder Knowledge Graph
│   │   ├── sys:root (ROOT NODE)
│   │   ├── sys:agents (parent: sys:root)
│   │   ├── sys:config (parent: sys:root)
│   │   ├── sys:docs (parent: sys:root)
│   │   │   ├── sys:docs:general (parent: sys:docs)
│   │   │   └── sys:docs:builder (parent: sys:docs)
│   │   │       ├── sys:docs:builder:arch (parent: sys:docs:builder)
│   │   │       │   └── [document nodes] (parent: sys:docs:builder:arch)
│   │   └── [concepts]
│   ├── Builder Skills Graph
│   │   ├── skill:builder:root (ROOT NODE)
│   │   ├── skill-validate-structure (parent: skill:builder:root)
│   │   └── skill-maintain-kg (parent: skill:builder:root)
│   │       ├── skill-kg-monitor (parent: skill-maintain-kg)
│   │       ├── skill-kg-update (parent: skill-maintain-kg)
│   │       └── skill-kg-heal (parent: skill-maintain-kg)
│   └── Builder Behaviors Graph
│       ├── behavior:builder:root (ROOT NODE)
│       ├── behavior:core:safety (parent: behavior:builder:root)
│       └── behavior:builder:consistency (parent: behavior:builder:root, links: {enforces: [skill-maintain-kg]})
└── [Domain Role Name] (Custom Role)
    ├── [Domain] Knowledge Graph
    │   ├── [domain]:root (ROOT NODE)
    │   ├── [content from shared folders mapped here]
    │   └── [domain-specific concepts]
    ├── [Domain] Skills Graph
    │   ├── skill:[domain]:root (ROOT NODE)
    │   └── [domain-specific skills]
    └── [Domain] Behaviors Graph
        ├── behavior:[domain]:root (ROOT NODE)
        └── [domain-specific behaviors from Phase 1]
```

### Present Structure

```
Knowledge Graph Architecture (V2 - Fully Connected):

**Connectivity Rules**:
1. Every graph has a root node
2. Every node (except root) has a parent
3. Cross-graph relationships use 'links' field

**Structure**:
Root
├── [Domain Knowledge]
│   ├── [Category 1] (parent: root)
│   │   ├── [Subcategory 1.1] (parent: Category 1)
│   │   │   └── [Document 1.1.1] (parent: Subcategory 1.1)
│   └── [Category 2] (parent: root)
├── [Role 1 Knowledge] (parent: root)
│   ├── [Component 1] (parent: Role 1 Knowledge)
│   └── [Concept 1] (parent: Role 1 Knowledge)

**Cross-Graph Links** (dashed amber lines in visualization):
- Behavior:consistency --enforces--> Skill:maintain-kg
- Skill:validate --implements--> Behavior:schema
- Knowledge:docs --tracked_by--> Knowledge:registry

Proceed with this architecture?
```

---

## Action 2.3: Classify Skills by Implementation Type (V2 NEW)

**V2 Addition**: Classify each skill by implementation type upfront for cost optimization.

### Understanding Skills Classification

For context on WHY we classify skills, see the "Cost Optimization Strategy" section in [V2_PROTOCOL_COMPLETE_PACKAGE_README.md](../V2_PROTOCOL_COMPLETE_PACKAGE_README.md).

**Key concept**: The system you BUILD can use cheaper models for many tasks. By classifying skills upfront, you design for optimal cost/performance from the start.

### Execute Classification

**Follow the detailed guide**: [SKILLS_CLASSIFICATION_GUIDE.md](../guides/SKILLS_CLASSIFICATION_GUIDE.md)

The guide provides:

- Decision tree (4 questions to classify each skill)
- 6 worked examples with reasoning
- Step-by-step execution process
- Presentation template for human review

**Process**:

1. Read the classification guide
2. For each skill from Phase 1, apply the decision tree
3. Document classification with reasoning
4. Present complete classification to human for approval

**Expected output**: Skills categorized as:

- Rule-Based (Python/Shell, $0 cost)
- LLM-Based Max Tier (Claude 4.5+, complex reasoning)
- LLM-Based SLM Tier (Llama 3.1 8B, simple tasks)
- Hybrid (Rules + LLM + Rules, optimized cost)

---

## Action 2.4: Define Core Agent Behaviors (V2 ENHANCED)

**V2 Addition**: Define foundational behaviors that ensure agent reliability and optimal performance.

These behaviors apply to **all agents** regardless of domain and are critical for stable, trustworthy operation.

### Core Behavior 1: Document Chunking Protocol

**Purpose**: Organize documentation and code for optimal LLM reasoning

**Key Principles**:

1. **One concept per file** - Each file represents a single, cohesive concept
2. **Target 250-500 lines** per file (~1,500-3,000 tokens)
3. **Separate "what" from "how"** - Concept explanation vs execution instructions
4. **Cross-link instead of duplicate** - Use references, maintain single source of truth
5. **Chunk by behavior** - Split at natural boundaries, not arbitrary line counts

**Reasoning**:

- Prevents "lost in the middle" problem in LLM attention
- Keeps all information in high-attention zones (beginning/end of context)
- Enables reliable full-file regeneration
- Improves agent reasoning quality and edit accuracy

**Reference**: See detailed guide in [../guides/CHUNKING_BEST_PRACTICES.md](../guides/CHUNKING_BEST_PRACTICES.md)

**Implementation**:

- Behavior file: `.cursor/behaviors/core/document-chunking.md` (Phase 5)
- Applied to: All documentation and code organization
- Validated in: Phase 10

---

### Core Behavior 2: Regenerative Editing Protocol

**Purpose**: Ensure reliable file modifications by leveraging LLM generative strengths

**The Rule**: **Always regenerate entire files instead of inline edits**

**When to Apply**: ALL file modification requests unless user explicitly requests diff-only

**Process**:

1. Load entire file into context
2. Understand requested changes fully
3. **Regenerate complete file from scratch** with modifications applied
4. Ensure all unrelated parts preserved exactly
5. Output new complete file

**Reasoning**:

- **LLMs excel at**: Generating complete, coherent text from scratch
- **LLMs struggle with**: Precise positional edits, attention across long docs, applying patches
- **Regeneration prevents**: Positional drift, context loss, diff corruption, partial updates
- **Result**: Reliable, predictable, testable file modifications

**Exceptions**: Only when user explicitly says:

- "Apply a diff patch"
- "Do not regenerate the whole file"
- "Only show the changed lines"

**Reference**: See detailed guide in [../guides/REGENERATIVE_EDITING_PROTOCOL.md](../guides/REGENERATIVE_EDITING_PROTOCOL.md)

**Implementation**:

- Behavior file: `.cursor/behaviors/core/regenerative-editing.md` (Phase 5)
- Applied to: All file modification skills (Phase 8)
- Validated in: Phase 10

---

### Synergy Between Protocols

These two behaviors work together:

**Chunking** → Keeps files small (250-500 lines)
**Regeneration** → Small files regenerate quickly and reliably

**Combined Result**: Optimal reliability and performance

**Example**:

```
Instead of:
  giant-file.py (2000 lines) → Hard to regenerate reliably

Use (with chunking):
  component-a.py (300 lines) → Easy to regenerate ✅
  component-b.py (400 lines) → Easy to regenerate ✅
  component-c.py (350 lines) → Easy to regenerate ✅
```

---

### Present to Human

```
Core Agent Behaviors Defined:

**Foundational Protocols** (Apply to all agents):

1. ✅ Document Chunking Protocol
   - Ensures optimal file sizes for LLM reasoning
   - Prevents "lost in the middle" problem
   - Target: 250-500 lines per file
   - Detailed guide: guides/CHUNKING_BEST_PRACTICES.md

2. ✅ Regenerative Editing Protocol
   - Always regenerate full files for modifications
   - Prevents diff corruption and positional errors
   - Leverages LLM generative strengths
   - Detailed guide: guides/REGENERATIVE_EDITING_PROTOCOL.md

**Domain-Specific Behaviors** (From Phase 1):
[List behaviors from Action 2.1]

**Implementation Plan**:
- Phase 5: Create behavior files
- Phase 8: Implement in skills
- Phase 9: Validate compliance

These foundational protocols ensure:
- Reliable file modifications
- Optimal agent performance
- Consistent, trustworthy results

Proceed with this architecture?
```

Wait for human approval.

---

## Validation Checkpoint

```
Architecture designed with V2 enhancements:
✅ Behavior taxonomy complete (including foundational protocols)
✅ Fully-connected KG structure designed
✅ Skills classified by implementation type
✅ Core agent behaviors defined (chunking + regenerative editing)

Ready to create project structure. Proceed?
```

---

## Output

Document all architectural decisions:

- Complete behavior taxonomy (core + role-specific)
- Knowledge Graph structure with connectivity rules
- Skills inventory with implementation classifications
- Cross-graph relationship map

---

**Previous Phase**: [Phase 1: Information Discovery](PHASE_01_INFORMATION_DISCOVERY.md)  
**Next Phase**: [Phase 3: Create Project Structure](PHASE_03_PROJECT_STRUCTURE.md)
