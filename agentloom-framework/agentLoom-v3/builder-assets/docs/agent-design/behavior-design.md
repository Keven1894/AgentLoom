# Behavior Design - Creating Agent Rules & Workflows

**Category**: Agent Design  
**Audience**: AI Agent Developers  
**Version**: 1.0

---

## What Are Behaviors?

**Behaviors** (Track 1) define **HOW** an agent operates:
- **Identity**: Who the agent is
- **Rules**: Principles and constraints
- **Workflows**: Step-by-step procedures

Think of behaviors as the agent's "personality" and "operating manual."

---

## Components of Track 1

```
.cursor/
├── identity.md          # Who the agent is
├── INDEX.md             # Master index
└── rules/
    ├── core/            # Core principles and rules
    └── workflows/       # Step-by-step procedures
```

---

## Designing Identity

### Purpose
Define the agent's fundamental nature.

### Key Elements
```markdown
# identity.md structure

## Name & Role
- What is the agent called?
- What is its primary function?

## Personality
- How does it communicate?
- What is its tone?
- What are its traits?

## Boundaries
- What will it NOT do?
- What are its limitations?
- What requires human intervention?

## Knowledge Scope
- What domain does it cover?
- What is it expert in?
- What is outside its scope?
```

### Example: TA Agent
```markdown
**Name**: Professor AI - Teaching Assistant
**Role**: Support students learning CEN5064 Software Design

**Personality**:
- Encouraging and patient
- Clear and pedagogical
- Professional yet approachable

**Boundaries**:
- Will NOT give direct answers to assignments
- Will NOT grade student work
- Will NOT make policy decisions

**Scope**:
- Expert: Software design patterns, UML, SOLID principles
- Out of scope: Other courses, personal issues
```

---

## Designing Core Rules

### Purpose
Establish non-negotiable principles.

### Rule Categories

**1. Critical Rules** ⚡
- Must NEVER be violated
- System breaks if not followed
- Requires highest priority

Example: `academic-integrity.md` for TA

**2. Important Rules** ⚠️
- Should be followed
- Violations degrade quality
- Exceptions rare but possible

Example: `documentation-first.md` for Developer

**3. Guidelines** ℹ️
- Best practices
- Flexible interpretation
- Context-dependent

Example: `communication-style.md`

### Rule Structure
```markdown
# Rule Title

## Principle
One sentence core principle

## Rationale
Why this rule exists

## Guidelines
- Specific do's and don'ts
- Examples
- Edge cases

## Exceptions
When (if ever) rule can be bent

## Related Rules
Links to related rules
```

### Example Rule
```markdown
# Academic Integrity

## Principle
Never provide direct answers to graded assignments.

## Rationale
Students must learn by doing their own work. Giving answers 
prevents learning and violates academic integrity.

## Guidelines
✅ DO:
- Explain concepts clearly
- Provide general examples
- Guide thinking process
- Point to course materials

❌ DON'T:
- Give assignment answers
- Write code for projects
- Solve homework problems
- Complete exam questions

## Edge Cases
- Q: "Is this code correct?" 
  A: Ask guiding questions, don't debug for them
- Q: "Show me an example"
  A: Generic example OK, assignment-specific NOT OK

## Exceptions
NONE - This is a critical rule

## Related
- pedagogical-approach.md
- student-interaction.md (workflow)
```

---

## Designing Workflows

### Purpose
Define repeatable procedures for common tasks.

### Workflow Structure
```markdown
# Workflow Title

## Purpose
What this workflow accomplishes

## When to Use
Triggering conditions

## Prerequisites
What must be true before starting

## Steps
1. Step 1: Description
   - Details
   - Expected outcome
   
2. Step 2: Description
   - Details
   - Expected outcome

## Validation
How to verify workflow completed successfully

## Error Handling
What to do if something goes wrong

## Related
Links to other workflows, rules, skills
```

### Workflow Types

**1. Interaction Workflows**
How to interact with users.

Example: `student-interaction.md`
```
1. Understand query
2. Check academic integrity
3. Provide appropriate response
4. Verify understanding
5. Offer additional resources
```

**2. Development Workflows**
How to build and maintain the agent.

Example: `skill-creation.md`
```
1. Define skill purpose
2. Create structure
3. Document skill
4. Implement logic
5. Test thoroughly
6. Integrate with KG
```

**3. Operational Workflows**
Day-to-day operations.

Example: `knowledge-extraction.md`
```
1. Analyze source
2. Extract content
3. Structure markdown
4. Quality check
5. Integrate into KB
```

---

## Design Principles

### 1. Clarity Over Brevity
```
Rules should be crystal clear
Better to be verbose than ambiguous
```

**Bad**:
```markdown
Don't help too much with assignments.
```

**Good**:
```markdown
Never provide direct answers to graded assignments. 
Instead, guide students' thinking by:
- Asking clarifying questions
- Explaining relevant concepts
- Providing generic examples (not assignment-specific)
```

### 2. Explicit Priorities
```
Mark criticality clearly
Agent needs to know what's non-negotiable
```

Use markers:
- ⚡ CRITICAL - Never violate
- ⚠️ IMPORTANT - Rarely violate
- ℹ️ GUIDELINE - Flexible

### 3. Actionable Content
```
Rules should be implementable
Workflows should be followable
```

**Bad**:
```markdown
Be helpful to students.
```

**Good**:
```markdown
When student asks a question:
1. Clarify intent: "Are you asking about X or Y?"
2. Check scope: Is this about the course?
3. Apply integrity: Is this about graded work?
4. Provide response: Concept explanation or guidance
```

### 4. Examples Matter
```
Abstract rules are hard to apply
Examples make intent clear
```

Include:
- ✅ Good examples
- ❌ Bad examples
- Edge cases
- Real scenarios

### 5. Interconnected
```
Rules reference each other
Workflows invoke skills
Everything links to KG
```

Example:
```markdown
## Related Rules
- [Academic Integrity](./core/academic-integrity.md) ⚡ CRITICAL
- [Pedagogical Approach](./core/pedagogical-approach.md)

## Related Skills
- [Guide Problem Solving](../../agents/skills/ta/teaching/guide-problem-solving/skill.md)

## Related Workflows
- [Student Interaction](./workflows/student-interaction.md)
```

---

## Common Patterns

### The Boundary Pattern
Define what agent will/won't do:

```markdown
## Will Do
- Answer conceptual questions
- Explain with examples
- Guide problem-solving thinking

## Will NOT Do
- Solve assignments
- Grade work
- Make policy decisions
```

### The Decision Tree Pattern
Guide complex decisions:

```markdown
## Handling Student Questions

Is it a course topic?
├─ NO → Politely redirect to course scope
└─ YES → Is it about graded work?
          ├─ YES → Guide thinking, don't give answer
          └─ NO → Explain concept directly
```

### The Checklist Pattern
Ensure completeness:

```markdown
Before responding to student:
- [ ] Understood the question?
- [ ] Checked academic integrity?
- [ ] Referenced course materials?
- [ ] Maintained encouraging tone?
- [ ] Verified understanding?
```

### The Priority Pattern
Handle conflicts:

```markdown
## Priority Order
1. Academic integrity (NEVER compromise)
2. Student learning (primary goal)
3. Efficiency (desirable but secondary)

If efficient response violates integrity: Choose integrity
If learning requires more time: Take the time
```

---

## Role-Specific Behaviors

### TA Role Behaviors
Focus: Teaching, learning, academic integrity

```
Core Rules:
- academic-integrity.md
- pedagogical-approach.md
- language-and-tone.md

Workflows:
- student-interaction.md
- plan-work-complete-flow.md
```

### Developer Role Behaviors
Focus: Quality, documentation, system integrity

```
Core Rules:
- code-quality.md
- documentation-first.md
- test-before-deploy.md
- knowledge-graph-integrity.md

Workflows:
- agent-development.md
- skill-creation.md
- knowledge-extraction.md
- testing-validation.md
```

### Multi-Role Considerations
When agent has multiple roles:

1. **Separate by directory**
   ```
   rules/core/ta/
   rules/core/developer/
   ```

2. **Document role switching**
   ```
   rules/core/role-switching.md
   ```

3. **Share when appropriate**
   ```
   rules/core/communication-standards.md  # Both roles
   ```

---

## Testing Behaviors

### How to Test a Rule

```yaml
Rule: academic-integrity

Test Scenarios:
  1. Direct request for answer
     Input: "Give me the solution to Assignment 1"
     Expected: Refuses, offers guidance
     
  2. Legitimate concept question
     Input: "What is the Adapter pattern?"
     Expected: Explains concept
     
  3. Borderline case
     Input: "Can you check if my code is correct?"
     Expected: Asks guiding questions, doesn't debug

Validation:
  - Rule applied correctly in all cases
  - No false positives (blocking legitimate help)
  - No false negatives (allowing cheating)
```

### How to Test a Workflow

```yaml
Workflow: skill-creation

Test:
  1. Execute each step
  2. Verify outputs at each stage
  3. Check error handling
  4. Validate final result

Success Criteria:
  - All steps complete without errors
  - Skill is functional
  - Documentation is complete
  - KG is updated correctly
```

---

## Maintenance

### When to Update Behaviors

**Update Rules When**:
- New edge cases discovered
- Policy changes
- User feedback reveals gaps
- Agent makes mistakes

**Update Workflows When**:
- Process improvements found
- New tools available
- Steps become outdated
- Efficiency gains possible

### Version Control
```markdown
---
Version: 2.0
Last Updated: 2025-11-18
Changes:
  - Added edge case handling for X
  - Clarified step 3 in workflow
  - Updated related skills links
---
```

---

## Related Documentation
- [3-Track Architecture](./3-track-architecture.md)
- [Skill Design](./skill-design.md)
- [Knowledge Graphs](./knowledge-graphs.md)

## Related Rules
- See `.cursor/rules/core/` for examples
- See `.cursor/rules/workflows/` for workflow examples

---

**Last Updated**: November 18, 2025  
**Status**: Core documentation  
**Priority**: HIGH - Foundation of agent behavior

