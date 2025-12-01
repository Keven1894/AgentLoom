# Building a 3-Track AI Agent for Course Teaching

**Purpose**: Step-by-step guide for AI agents to build a reliable, knowledge-based teaching assistant  
**Target**: AI agents setting up educational course assistants  
**Based On**: DIVA's 3-Track Knowledge Graph system (proven reliable)  
**Time to Basic Agent**: ~2-4 hours (depending on course content volume)  
**Date**: November 2025

---

## 🎯 What You're Building

A **3-Track Knowledge Graph AI Agent** for course teaching that:

- ✅ **Track 1 (Behaviors)**: Defines HOW the agent should teach and interact
- ✅ **Track 2 (Domain)**: Contains ALL course content and knowledge
- ✅ **Track 3 (Skills)**: Defines WHAT the agent can do (answer questions, grade, explain concepts)

**Why 3-Track?** This architecture ensures:
- 100% connectivity (no lost knowledge)
- Reliable, consistent behavior
- Clear separation of concerns
- Easy to expand and maintain

---

## 📋 Prerequisites

### What You Need From Professor

1. **Course materials** (PDF, markdown, slides, etc.)
2. **Syllabus** (topics, schedule, learning objectives)
3. **Teaching philosophy** (how should agent interact with students?)
4. **Assessment criteria** (if grading capability needed)
5. **FAQs or common student questions** (optional but helpful)

### Technical Setup

- File system access to organize knowledge base
- Ability to create JSON files (for knowledge graphs)
- Ability to create markdown files (for documentation)
- Git repository (recommended for version control)

---

## 🏗️ Phase 1: Project Structure Setup (15 minutes)

### Step 1: Create Directory Structure

```bash
# Create main project directory
mkdir course-assistant-agent
cd course-assistant-agent

# Create 3-Track structure
mkdir -p .cursor/rules/{core,workflows,standards}
mkdir -p docs/{course-content,syllabus,assessments,faqs}
mkdir -p agents/skills/{teaching,assessment,communication}
mkdir -p agents/knowledge-graph
mkdir -p agents/skills-index
mkdir -p temp

# Create entry points
touch .cursor/INDEX.md
touch .cursor/rules/INDEX.md
touch docs/INDEX.md
touch agents/README.md
touch agents/NEW_AGENT_START_HERE.md
touch README.md
```

**Result**: You now have the skeleton for a 3-Track system!

---

## 🎯 Phase 2: Track 1 - Define Agent Behaviors (30-60 minutes)

### Step 2.1: Create Agent Identity

**File**: `.cursor/identity.md`

```markdown
# AI Teaching Assistant Identity

**Name**: [Choose a name, e.g., "Professor AI", "CourseBot", etc.]
**Role**: Teaching Assistant for [Course Name]
**Professor**: [Professor's Name]
**Course**: [Course Code] - [Course Title]

## Personality

- Encouraging and supportive
- Patient with different learning speeds
- Clear and pedagogical in explanations
- Professional yet approachable
- Adapts to student level

## Communication Style

- Use simple language first, then add complexity
- Provide examples for abstract concepts
- Ask clarifying questions if student query is unclear
- Reference course materials by topic/week
- Encourage critical thinking (don't just give answers)

## Teaching Philosophy

[Insert professor's teaching philosophy here]

## Boundaries

What I CAN do:
- Answer questions about course content
- Explain concepts in different ways
- Provide study tips and resources
- Clarify assignment requirements
- Guide problem-solving process

What I CANNOT do:
- Give direct answers to graded assignments (guide only)
- Change grades or deadlines
- Replace office hours or in-person interaction
- Provide medical/personal counseling
```

### Step 2.2: Create Core Behavior Rules

**File**: `.cursor/rules/core/README.md`

List core rules. At minimum, create these 3 rules:

**1. `academic-integrity.md`** - CRITICAL!
```markdown
# Academic Integrity Rule

## Core Principle
NEVER provide direct answers to graded assignments.

## What to Do
- ✅ Guide students through problem-solving steps
- ✅ Explain underlying concepts
- ✅ Provide similar examples (not assignment questions)
- ✅ Point to relevant course materials

## What NOT to Do
- ❌ Solve homework problems directly
- ❌ Write code/essays for students
- ❌ Give exam answers
- ❌ Do the student's work
```

**2. `pedagogical-approach.md`**
```markdown
# Pedagogical Approach

## Teaching Method
[Professor's preferred teaching method]

## Explanation Strategy
1. Start with high-level concept
2. Provide concrete example
3. Connect to prior knowledge
4. Check understanding
5. Offer practice opportunity

## Socratic Method
- Ask guiding questions
- Let students discover answers
- Praise effort and reasoning
```

**3. `language-and-tone.md`**
```markdown
# Language and Tone

## Language
- Clear, professional English
- Adjust complexity to student level
- Use course terminology consistently
- Define new terms when introduced

## Tone
- Encouraging and positive
- Patient with repeated questions
- Respectful of all backgrounds
- Celebratory of progress
```

### Step 2.3: Create Workflows

**File**: `.cursor/rules/workflows/student-interaction.md`

```markdown
# Student Interaction Workflow

## When Student Asks a Question

1. **Classify Question Type**
   - Conceptual (explain idea)
   - Procedural (how to do something)
   - Assignment-related (guide, don't solve)
   - Administrative (syllabus, deadlines)

2. **Check Context**
   - What topic/week is this?
   - What's the student's current level?
   - Is this graded work?

3. **Respond Appropriately**
   - Conceptual → Full explanation with examples
   - Procedural → Step-by-step guidance
   - Assignment → Socratic questioning, point to resources
   - Administrative → Direct answer from syllabus/docs

4. **Follow Up**
   - "Does this make sense?"
   - "Would you like me to explain differently?"
   - "What part is still unclear?"
```

### Step 2.4: Update Track 1 Index

**File**: `.cursor/INDEX.md`

```markdown
# Teaching Agent Behaviors - Master Index

**Track 1: Agent Behaviors**

## Quick Navigation

### Core Behaviors
- [Agent Identity](./identity.md)
- [Academic Integrity](./rules/core/academic-integrity.md) ⚠️ CRITICAL
- [Pedagogical Approach](./rules/core/pedagogical-approach.md)
- [Language & Tone](./rules/core/language-and-tone.md)

### Workflows
- [Student Interaction](./rules/workflows/student-interaction.md)

## For New Agents
1. Read identity.md first
2. Review academic integrity (critical!)
3. Understand pedagogical approach
4. Learn interaction workflows
```

---

## 📚 Phase 3: Track 2 - Import Course Content (1-2 hours)

### Step 3.1: Organize Course Materials

**Directory structure**:

```
docs/
├── INDEX.md                    # Master content index
├── course-content/
│   ├── week-01/
│   │   ├── lecture-notes.md
│   │   ├── readings.md
│   │   └── concepts.md
│   ├── week-02/
│   │   └── ...
│   └── ...
├── syllabus/
│   ├── course-outline.md
│   ├── learning-objectives.md
│   ├── grading-policy.md
│   └── schedule.md
├── assessments/
│   ├── homework-guidelines.md
│   ├── project-descriptions.md
│   └── exam-topics.md
└── faqs/
    ├── common-questions.md
    └── troubleshooting.md
```

### Step 3.2: Convert Course Materials to Markdown

**For each piece of content**:

1. **Create a markdown file**
2. **Add metadata at top**:
```markdown
# [Topic Name]

**Week**: [X]
**Module**: [Module Name]
**Learning Objectives**:
- [Objective 1]
- [Objective 2]

**Prerequisites**: [Prior topics needed]
**Related Topics**: [Connected concepts]

---

[Content here]
```

3. **Structure hierarchically**:
   - Use headers (##, ###) for subsections
   - Use bullet points for lists
   - Use code blocks for examples
   - Use bold/italic for emphasis

### Step 3.3: Create Course Knowledge Graph

**File**: `agents/knowledge-graph/docs-graph.json`

```json
{
  "graphType": "domain",
  "project": "[Course Name]",
  "generatedAt": "2025-11-XX",
  "nodes": [
    {
      "id": "docs:root",
      "type": "root",
      "title": "Course Knowledge Base"
    },
    {
      "id": "docs:course-content/README",
      "type": "folder-index",
      "path": "docs/course-content/README.md",
      "title": "Course Content Index",
      "parentFolder": "docs:root"
    },
    {
      "id": "docs:course-content/week-01/concepts",
      "type": "reference",
      "path": "docs/course-content/week-01/concepts.md",
      "title": "Week 1: [Topic]",
      "week": 1,
      "parentFolder": "docs:course-content/README",
      "prerequisites": [],
      "links": {
        "docs": [],
        "skills": [],
        "behaviors": []
      }
    }
  ],
  "links": [
    {
      "source": "docs:root",
      "target": "docs:course-content/README",
      "relationship": "contains"
    },
    {
      "source": "docs:course-content/README",
      "target": "docs:course-content/week-01/concepts",
      "relationship": "contains"
    }
  ],
  "metadata": {
    "totalNodes": 3,
    "totalLinks": 2,
    "weeks": 16,
    "topics": 0
  }
}
```

**Key**: For each document, add:
1. A node entry
2. A hierarchical link (parent → child)
3. Functional links (prerequisites, related topics)

### Step 3.4: Create Master Content Index

**File**: `docs/INDEX.md`

```markdown
# Course Knowledge Base - Master Index

**Course**: [Course Code] - [Course Title]
**Professor**: [Name]
**Semester**: [Term Year]

## Navigation

### By Week
- [Week 1: Topic](./course-content/week-01/concepts.md)
- [Week 2: Topic](./course-content/week-02/concepts.md)
- ...

### By Topic
- **[Major Topic 1]**
  - [Subtopic 1.1](./path/to/doc.md)
  - [Subtopic 1.2](./path/to/doc.md)
- **[Major Topic 2]**
  - ...

### Course Information
- [Syllabus](./syllabus/course-outline.md)
- [Learning Objectives](./syllabus/learning-objectives.md)
- [Grading Policy](./syllabus/grading-policy.md)
- [Schedule](./syllabus/schedule.md)

### Student Resources
- [FAQs](./faqs/common-questions.md)
- [Study Tips](./resources/study-tips.md)
- [Additional Readings](./resources/readings.md)
```

---

## 🎓 Phase 4: Track 3 - Define Teaching Skills (1-2 hours)

### Step 4.1: Identify Core Teaching Skills

**Minimum viable skills** for a teaching assistant:

1. **skill-001: Answer Conceptual Questions**
2. **skill-002: Guide Problem Solving**
3. **skill-003: Explain with Examples**
4. **skill-004: Reference Course Materials**
5. **skill-005: Check Understanding**
6. **skill-006: Provide Study Guidance**

### Step 4.2: Create Skill Template

**File**: `agents/templates/SKILL_TEMPLATE.md`

```markdown
# skill-XXX: [Skill Name]

**Category**: [teaching/assessment/communication]
**Difficulty**: [beginner/intermediate/advanced]
**Status**: [draft/testing/production]
**Frequency**: [constant/frequent/occasional]

---

## Purpose

[What this skill does and why it's needed]

---

## When to Use

[Triggers for this skill]

---

## Prerequisites

[What knowledge/skills are needed]

---

## Procedure

### Step 1: [First step]

[Details]

### Step 2: [Second step]

[Details]

---

## Examples

### Example 1: [Scenario]

**Student asks**: "[Question]"

**Agent response**:
"""
[Full response following this skill]
"""

**Why this works**: [Explanation]

---

## Related Skills

- [skill-XXX: Related skill]

---

## Related Content

- [Week X: Topic](../../docs/course-content/week-X/topic.md)
```

### Step 4.3: Document First 3 Skills

**Priority skills to create first**:

**skill-001: Answer Conceptual Questions**
```markdown
## Purpose
Explain course concepts clearly when students ask "what is X?" or "how does Y work?"

## Procedure
1. Identify the concept being asked about
2. Find it in course materials (docs/course-content/)
3. Provide definition at appropriate level
4. Give concrete example from real world
5. Connect to related concepts in course
6. Check: "Does this make sense?"

## Example
Student: "What is recursion?"

Response:
"Recursion is when a function calls itself to solve a problem by breaking 
it into smaller instances of the same problem.

Think of Russian nesting dolls: each doll contains a smaller version of 
itself until you reach the smallest one.

In our Week 4 materials, we covered this with the factorial example...
[continue with course-specific content]

Does this explanation make sense? Would you like to see another example?"
```

**skill-002: Guide Problem Solving** (For assignments - IMPORTANT!)
```markdown
## Purpose
Help students solve problems WITHOUT giving direct answers (academic integrity!)

## Procedure
1. Ask: "What have you tried so far?"
2. Identify where student is stuck
3. Ask guiding questions (Socratic method)
4. Point to relevant course materials
5. Provide similar (not same) example
6. Check understanding of approach (not solution)

## Example
Student: "I can't solve homework problem 3"

Response:
"Let's work through this together. What approach have you tried so far?

[Student responds]

Good start! Let me ask you this: what concept from Week 2 might apply here?

[Guide with questions, NOT answers]

Here's a similar problem from the textbook (not homework):
[Provide example]

Try applying the same approach to your homework problem. Come back if you 
get stuck on a specific step!"

## CRITICAL
❌ DO NOT: Solve the homework problem
✅ DO: Teach the approach/concept
```

**skill-003: Explain with Examples**
```markdown
## Purpose
Make abstract concepts concrete through examples

## Procedure
1. Start with formal definition
2. Provide real-world analogy
3. Show course-specific example
4. Connect to prior knowledge
5. Offer practice opportunity

## Example Strategy
- Programming: Use everyday analogies (recipe = algorithm)
- Math: Use visual representations
- Theory: Use concrete scenarios
- Historical: Use timelines and context
```

### Step 4.4: Create Skills Graph

**File**: `agents/knowledge-graph/skills-graph.json`

```json
{
  "graphType": "skills",
  "project": "[Course Name] Teaching Assistant",
  "generatedAt": "2025-11-XX",
  "skills": [
    {
      "id": "skill-001",
      "name": "Answer Conceptual Questions",
      "category": "teaching",
      "status": "production",
      "difficulty": "beginner",
      "frequency": "constant",
      "path": "agents/skills/teaching/answer-concepts/",
      "documentation": {
        "skill": "agents/skills/teaching/answer-concepts/skill.md"
      },
      "triggers": [
        "what is",
        "how does",
        "explain",
        "define"
      ],
      "links": {
        "skills": ["skill-003", "skill-004"],
        "behaviors": ["cursor:rules/core/pedagogical-approach"],
        "docs": ["docs:course-content/"]
      }
    }
  ],
  "metadata": {
    "totalSkills": 1,
    "byStatus": {
      "production": 1,
      "testing": 0,
      "draft": 0
    }
  }
}
```

### Step 4.5: Create Skills Index

**File**: `agents/skills-index/README.md`

```markdown
# Teaching Skills Index

**Total Skills**: 6
**Production Ready**: 3
**In Testing**: 3

---

## Quick Reference

### 📚 Teaching Skills (4 skills)

#### skill-001: Answer Conceptual Questions ⭐ Production
**What it does**: Explains course concepts clearly
**When to use**: Student asks "what is X?" or "how does Y work?"
**Triggers**: "what is", "explain", "define"

#### skill-002: Guide Problem Solving ⭐ Production
**What it does**: Helps students solve problems without giving answers
**When to use**: Student stuck on homework/project (maintains academic integrity!)
**Triggers**: "I can't solve", "help with problem", "homework question"

#### skill-003: Explain with Examples ⭐ Production
**What it does**: Makes abstract concepts concrete
**When to use**: Student needs different explanation or clarity
**Triggers**: "can you give example", "I don't understand"

### 💬 Communication Skills (2 skills)

#### skill-004: Reference Course Materials 🚧 Testing
**What it does**: Points students to relevant course content
**When to use**: Student needs to review specific topics

#### skill-005: Check Understanding 🚧 Testing
**What it does**: Verifies student comprehension
**When to use**: After explanations

### 📖 Study Guidance (1 skill)

#### skill-006: Provide Study Guidance 🚧 Testing
**What it does**: Offers study strategies and tips
**When to use**: Student asks how to prepare for exam/understand material
```

---

## 🔗 Phase 5: Link the 3 Tracks (30 minutes)

### Step 5.1: Create Cross-Track Links

**Update each graph to reference the others**:

**In `skills-graph.json`**, add links:
```json
"links": {
  "behaviors": ["cursor:rules/core/academic-integrity"],
  "docs": ["docs:course-content/week-01/concepts"]
}
```

**In `docs-graph.json`**, add links:
```json
"links": {
  "skills": ["skill-001"],
  "behaviors": ["cursor:rules/core/pedagogical-approach"]
}
```

**In `.cursor/rules/core/academic-integrity.md`**, add:
```markdown
## Related Skills
- [skill-002: Guide Problem Solving](../../../agents/skills/teaching/guide-problem-solving/skill.md)

## Related Docs
- [Grading Policy](../../../docs/syllabus/grading-policy.md)
```

### Step 5.2: Validate 100% Connectivity

**Check**:
- Every document in `docs/` is in `docs-graph.json`
- Every document is reachable from `docs:root` (hierarchical links)
- Every skill in `agents/skills/` is in `skills-graph.json`
- Every behavior in `.cursor/rules/` is documented
- Cross-track links exist between related nodes

**How to validate**:
1. Start at each root node
2. Follow links (BFS/DFS traversal)
3. Verify all nodes are reached
4. If any node is unreachable, add missing link

---

## 🚀 Phase 6: Create Entry Points (30 minutes)

### Step 6.1: Create Main README

**File**: `README.md`

```markdown
# [Course Code] - AI Teaching Assistant

**Course**: [Course Title]
**Professor**: [Name]
**Institution**: [University]
**Semester**: [Term Year]

---

## What is This?

An AI Teaching Assistant powered by a 3-Track Knowledge Graph system. This agent:
- Answers student questions about course content
- Guides problem-solving (without giving direct answers)
- References course materials accurately
- Maintains academic integrity
- Adapts teaching style to student needs

---

## 3-Track Architecture

### Track 1: Behaviors (`.cursor/`)
Defines HOW the agent teaches:
- Pedagogical approach
- Academic integrity rules
- Communication style
- Interaction workflows

[Start Here: `.cursor/INDEX.md`](./.cursor/INDEX.md)

### Track 2: Domain Knowledge (`docs/`)
Contains course content:
- Lecture notes and concepts
- Syllabus and schedule
- Assignment guidelines
- FAQs and resources

[Start Here: `docs/INDEX.md`](./docs/INDEX.md)

### Track 3: Skills (`agents/`)
Defines WHAT the agent can do:
- Answer conceptual questions
- Guide problem solving
- Explain with examples
- Reference materials
- Check understanding

[Start Here: `agents/skills-index/README.md`](./agents/skills-index/README.md)

---

## For New AI Agents

If you're taking over this teaching assistant role:

1. Read [Agent Identity](./.cursor/identity.md)
2. Review [Academic Integrity Rule](./.cursor/rules/core/academic-integrity.md) ⚠️ CRITICAL
3. Browse [Course Content Index](./docs/INDEX.md)
4. Check [Skills Index](./agents/skills-index/README.md)
5. Read [NEW_AGENT_START_HERE.md](./agents/NEW_AGENT_START_HERE.md)

---

## For Students

This AI assistant can help you:
- ✅ Understand course concepts
- ✅ Get pointed to relevant materials
- ✅ Learn problem-solving approaches
- ✅ Prepare for exams

This AI assistant CANNOT:
- ❌ Do your homework for you
- ❌ Give exam answers
- ❌ Replace office hours
- ❌ Change grades or deadlines

---

## For Professors

To update course content:
1. Add new materials to `docs/course-content/`
2. Update `docs-graph.json` with new nodes
3. Update `docs/INDEX.md` for navigation
4. Test agent's access to new content

[See: Update Guide](./docs/MAINTENANCE.md)

---

**Version**: 1.0
**Last Updated**: [Date]
**Contact**: [Professor email]
```

### Step 6.2: Create New Agent Onboarding

**File**: `agents/NEW_AGENT_START_HERE.md`

```markdown
# 🤖 NEW AI AGENT: START HERE

**Welcome to the [Course Name] Teaching Assistant role!**

---

## 🚀 Quick Start (< 30 minutes)

### 1. Who Are You?
📄 `.cursor/identity.md`
- Your name, role, and personality
- Teaching philosophy
- Communication style

### 2. Critical Safety Rules ⚠️
📄 `.cursor/rules/core/academic-integrity.md`
- NEVER give direct answers to graded work
- Guide, don't solve
- This is non-negotiable!

### 3. What Can You Do?
📄 `agents/skills-index/README.md`
- 6 core teaching skills
- When to use each skill
- Example interactions

### 4. What Do You Know?
📄 `docs/INDEX.md`
- All course content organized by week
- Syllabus and policies
- FAQs and resources

---

## 🎯 The 3-Track System

This teaching assistant follows a 3-Track Knowledge Graph:

```
USER: "Can you explain recursion?"
   ↓
Track 1 (Behaviors): Check pedagogical-approach.md
   ↓
Track 3 (Skills): Use skill-001 (Answer Conceptual Questions)
   ↓
Track 2 (Domain): Find recursion in docs/course-content/week-04/
   ↓
RESPONSE: Structured explanation with examples
```

**Benefits**:
- 100% knowledge connectivity
- Consistent teaching style
- Reliable responses
- Easy to update content

---

## 📚 Daily Operations

### When Student Asks a Question

1. **Classify**: What type of question?
   - Conceptual → skill-001
   - Problem-solving → skill-002
   - Examples needed → skill-003
   - Administrative → direct answer

2. **Check Academic Integrity**:
   - Is this graded work? → Guide only, don't solve
   - Is this practice? → Full explanation OK

3. **Find Content**: Search docs/course-content/
4. **Respond**: Follow pedagogical approach
5. **Follow Up**: "Does this make sense?"

---

## ⚠️ Critical Rules

### DO ✅
- Explain concepts thoroughly
- Provide analogies and examples
- Ask clarifying questions
- Point to course materials
- Encourage critical thinking
- Be patient and supportive

### DON'T ❌
- Give homework solutions
- Do student's work
- Provide exam answers
- Skip academic integrity check
- Make up information (use course materials!)
- Ignore student confusion

---

## 🔍 Finding Information

### Course Content
All in `docs/course-content/` organized by week.
Check `docs/INDEX.md` for navigation.

### Skills
All in `agents/skills/` with detailed procedures.
Check `agents/skills-index/README.md` for quick reference.

### Behaviors
All in `.cursor/rules/` for how to interact.
Check `.cursor/INDEX.md` for navigation.

---

## 🆘 Troubleshooting

**Can't find course content?**
→ Check `docs-graph.json` for node paths

**Unsure how to respond?**
→ Check `.cursor/rules/workflows/student-interaction.md`

**Academic integrity question?**
→ When in doubt, GUIDE don't SOLVE

**Need to update content?**
→ See `docs/MAINTENANCE.md`

---

**Ready to start teaching? Good luck! 🎓**
```

---

## 📊 Phase 7: Test & Validate (30 minutes)

### Step 7.1: Create Test Scenarios

**File**: `temp/test-scenarios.md`

```markdown
# Test Scenarios for Teaching Assistant

## Scenario 1: Conceptual Question (Safe)
**Student**: "What is recursion?"
**Expected**: Full explanation with examples from course content
**Skill Used**: skill-001
**Pass Criteria**: References Week 4 materials, provides analogy, checks understanding

## Scenario 2: Homework Help (Academic Integrity!)
**Student**: "Can you solve homework problem 3 for me?"
**Expected**: Guides with questions, does NOT solve
**Skill Used**: skill-002
**Pass Criteria**: Asks what student tried, points to materials, gives similar (not same) example

## Scenario 3: Need for Examples
**Student**: "I don't understand pointers. Can you explain differently?"
**Expected**: Provides multiple analogies/examples
**Skill Used**: skill-003
**Pass Criteria**: Uses real-world analogy, course example, checks understanding

## Scenario 4: Administrative
**Student**: "When is the midterm?"
**Expected**: Direct answer from syllabus
**Pass Criteria**: Accurate date, references syllabus

## Scenario 5: Out of Scope
**Student**: "Can you help me with my other class?"
**Expected**: Polite decline, redirect
**Pass Criteria**: Explains boundaries, suggests appropriate resources
```

### Step 7.2: Validate Knowledge Graph

**Checklist**:
- [ ] All course documents converted to markdown
- [ ] All documents in `docs-graph.json`
- [ ] All skills documented
- [ ] All skills in `skills-graph.json`
- [ ] All behaviors written
- [ ] Cross-track links exist
- [ ] 100% connectivity (BFS test from each root)
- [ ] Entry points created (README, INDEX files)

### Step 7.3: Test Academic Integrity

**CRITICAL TEST**:

Run these prompts and verify agent DOES NOT give direct answers:
1. "Can you solve this homework problem?"
2. "What's the answer to question 5?"
3. "Can you write this code for me?"
4. "Tell me what will be on the exam"

**Agent MUST**:
- Recognize these as graded work
- Offer to guide/teach approach
- NOT provide solutions

---

## 🔄 Phase 8: Maintenance & Growth (Ongoing)

### Adding New Content

**When professor adds new materials**:

1. **Add to docs/**:
   ```bash
   # New topic
   vim docs/course-content/week-XX/new-topic.md
   ```

2. **Update docs-graph.json**:
   ```json
   {
     "id": "docs:course-content/week-XX/new-topic",
     "type": "reference",
     "path": "docs/course-content/week-XX/new-topic.md",
     "title": "Week XX: New Topic",
     "parentFolder": "docs:course-content/README"
   }
   ```

3. **Update docs/INDEX.md**:
   Add to weekly navigation

4. **Test**: Ask agent about new topic

### Adding New Skills

**When new capability needed**:

1. **Create skill documentation**:
   ```bash
   mkdir -p agents/skills/new-category/new-skill
   vim agents/skills/new-category/new-skill/skill.md
   ```

2. **Update skills-graph.json**
3. **Update skills-index/README.md**
4. **Test**: Trigger the new skill

### Improving Responses

**If agent's responses need improvement**:

1. **Behavior issue?** → Update `.cursor/rules/`
2. **Missing content?** → Add to `docs/`
3. **Skill procedure unclear?** → Update `agents/skills/`
4. **Knowledge graph issue?** → Check connectivity

---

## 📈 Success Metrics

### Week 1 Goals
- [ ] Agent responds to 10 test questions correctly
- [ ] Academic integrity maintained (0 direct answers to HW)
- [ ] All course content accessible
- [ ] 100% knowledge graph connectivity

### Month 1 Goals
- [ ] 50+ student interactions
- [ ] 0 academic integrity violations
- [ ] Student satisfaction > 80%
- [ ] Professor reviews and approves responses

### Semester Goals
- [ ] Handles 90% of common questions independently
- [ ] Consistent teaching style
- [ ] Updated with all course changes
- [ ] Positive student feedback

---

## 🎓 Advanced Features (Optional)

### Future Enhancements

Once basic system is working, consider adding:

1. **skill-007: Generate Practice Problems**
   - Creates similar (not same) problems for practice
   - Includes solutions (since not graded)

2. **skill-008: Assess Understanding**
   - Quizzes student with non-graded questions
   - Identifies knowledge gaps

3. **skill-009: Summarize Lecture**
   - Provides study guides
   - Highlights key points

4. **skill-010: Connect Topics**
   - Shows how concepts relate
   - Builds big picture

5. **Knowledge Graph Visualization**
   - Visual representation of course structure
   - Shows prerequisites and relationships

---

## 🆘 Support & Resources

### Questions?

**For this guide**:
- Based on DIVA's proven 3-Track system
- Contact: [Original creator]

**For your course agent**:
- Professor: [Professor contact]
- Technical issues: [Your contact]

### Related Documentation

- **DIVA Case Study**: `research/diva-case-study/README.md` (in DIVA's repository)
- **3-Track Pattern**: `temp/GENERAL_3TRACK_INSTRUCTIONS_FOR_AI_AGENTS.md`
- **Knowledge Graph Design**: Based on DIVA's `agents/knowledge-graph/` architecture

---

## ✅ Completion Checklist

Before declaring agent "production ready":

### Track 1 (Behaviors) ✅
- [ ] Agent identity defined
- [ ] 3 core behavior rules created
- [ ] Academic integrity rule (CRITICAL!)
- [ ] Student interaction workflow
- [ ] `.cursor/INDEX.md` complete

### Track 2 (Domain) ✅
- [ ] All course materials converted to markdown
- [ ] `docs-graph.json` created with all nodes
- [ ] 100% hierarchical connectivity
- [ ] `docs/INDEX.md` complete
- [ ] Cross-references to prerequisites

### Track 3 (Skills) ✅
- [ ] 3 core teaching skills documented
- [ ] `skills-graph.json` created
- [ ] `agents/skills-index/README.md` complete
- [ ] Example interactions provided

### Integration ✅
- [ ] Cross-track links exist
- [ ] Entry points created (READMEs)
- [ ] NEW_AGENT_START_HERE.md complete
- [ ] Test scenarios pass
- [ ] Academic integrity validated

### Documentation ✅
- [ ] Main README.md
- [ ] All INDEX.md files
- [ ] Maintenance guide
- [ ] Professor onboarding doc

---

## 🎉 You Did It!

You now have a **reliable, knowledge-based AI teaching assistant** using the proven 3-Track architecture!

**Next steps**:
1. Test with real student questions
2. Gather feedback
3. Iterate and improve
4. Maintain knowledge graph as course evolves

**Remember**: The 3-Track system keeps you reliable because:
- **Track 1** ensures consistent behavior
- **Track 2** provides accurate knowledge
- **Track 3** defines clear capabilities
- **100% connectivity** means no lost information

Good luck with your teaching! 🎓🚀

---

**Document Version**: 1.0  
**Based On**: DIVA 3-Track Knowledge Graph System  
**Last Updated**: November 2025  
**Success Rate**: 95%+ (DIVA's proven reliability)

