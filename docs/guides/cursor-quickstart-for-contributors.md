# Cursor Quick-Start for Framework Contributors

**Purpose:** Help contributors quickly set up their environment and understand the Agentic-AI Engineering Framework using Cursor AI  
**Audience:** Researchers applying the framework to their own projects  
**Use Case:** After onboarding Zoom session, use these prompts to get Cursor aligned  
**Last Updated:** November 11, 2025

---

## 🎯 Overview

This guide provides **copy-paste prompts for Cursor** that help you:
1. Understand the Agentic-AI Engineering Framework
2. Set up your OWN project following the framework
3. Prepare to contribute a case study (like DIVA did)

**Important:** You'll work in YOUR OWN repository, not this one. When complete, you'll contribute `inputRAW/` content similar to DIVA's extraction.

---

## 📋 Prerequisites

Before using these prompts:
- [x] Attended onboarding Zoom session with Dr. Guan
- [x] Installed Cursor IDE (cursor.sh)
- [x] Have access to Claude/GPT API or local LLMs (Ollama)
- [x] Have a project/domain to apply framework to

---

## 🚀 Phase 1: Framework Understanding Prompts

### Prompt 1: Load Framework Knowledge

**Copy this into Cursor chat:**

```
I'm a contributor to the Agentic-AI Engineering Framework. I need to understand the framework to apply it to my own project.

Please read and summarize the following key documents from the Agentic-AI-Research-Roadmap repository:

1. README.md — Project overview
2. docs/framework-foundations.md — Theoretical foundations (especially F6 Computer Architecture and F7 Tools & Automation)
3. docs/agentic-collaboration-guide.md — Complete methodology
4. docs/case-studies/dataverse-diva.md — Example case study

Focus on:
- The 5-stage adaptive framework (System Prompt → Docs → Indexing → RAG → Fine-Tuning)
- Memory hierarchy analogy (how stages map to computer memory)
- When to evolve from one stage to the next
- DIVA's patterns (plan-first, rules-as-memory, tiered configuration)
- Tools & automation as critical infrastructure

Provide a concise summary (500-1000 words) highlighting key concepts I need to apply.
```

**Expected outcome:** Cursor understands framework and can guide you

---

### Prompt 2: Assess My Project's Stage

**Copy this into Cursor chat:**

```
I want to apply the Agentic-AI Engineering Framework to my project in [YOUR DOMAIN].

My project context:
- Domain: [e.g., Healthcare, GIS, Education, IT Operations]
- Current documentation: [Estimate: 10 pages? 100 pages? 1000 pages?]
- Current code/data: [Estimate volume]
- Team size: [Number]
- Current pain points: [List issues with AI agent if you have one]

Based on the framework's 5 stages (System Prompt → Docs → Indexing/RAM → RAG/Disk → Fine-Tuning), which stage should I start at?

Provide:
1. Recommended starting stage
2. Why this stage (based on my information volume)
3. What I need to implement for this stage
4. Evolution triggers (when to move to next stage)

Reference the computer memory hierarchy analogy (Registers → L1 → RAM → Disk → CPU Upgrade).
```

**Expected outcome:** Clear stage recommendation for YOUR project

---

### Prompt 3: Understand Critical Patterns

**Copy this into Cursor chat:**

```
From the DIVA case study (docs/case-studies/dataverse-diva.md and archives/inputRAW/dataverse-diva/), extract the 6 key proven patterns:

1. Plan-First Discipline
2. Institutional Memory (Rules-as-Memory)
3. Tiered Configuration (87% token efficiency)
4. Multi-Model Orchestration
5. Bounded Autonomy
6. Documentation as Workflow

For each pattern:
- What is it? (brief description)
- Why does it work? (evidence from DIVA)
- How to implement? (practical steps)
- When to use? (applicability to my domain)

Focus on patterns applicable to [YOUR DOMAIN] projects.
```

**Expected outcome:** Understand which patterns to adopt

---

## 🛠️ Phase 2: Project Setup Prompts

### Prompt 4: Create Project Structure

**Copy this into Cursor composer:**

```
I'm setting up my [DOMAIN] project to follow the Agentic-AI Engineering Framework.

Based on DIVA's structure (from archives/inputRAW/dataverse-diva/02-AGENT-DESIGN-PATTERNS.md), help me create:

1. Initial directory structure:
   - docs/ (documentation)
   - .cursor/rules/ (tiered configuration)
   - [my existing project directories]

2. Core .cursor/rules.md file:
   - Agent identity (name, role, personality)
   - Domain context (what I'm working on)
   - Framework stage (Stage [X] based on earlier assessment)
   - Safety boundaries (what agent can/cannot do)

3. Initial docs/README.md:
   - Project overview
   - Framework stage explanation
   - Documentation index

Please create these files for my [DOMAIN] project following the DIVA pattern but adapted to my domain.
```

**Expected outcome:** Basic structure created, ready to customize

---

### Prompt 5: Set Up Tiered Rules (If Stage 2+)

**Copy this into Cursor composer:**

```
I'm at Framework Stage 2 (Indexing + Metadata like RAM), so I need tiered .cursor/rules/ configuration following DIVA's 87% token-efficient pattern.

Based on archives/inputRAW/dataverse-diva/02-AGENT-DESIGN-PATTERNS.md (Tiered Configuration section), create:

.cursor/rules/
├── core/ (Tier 0 - Always loaded)
│   ├── identity.md (My agent's identity for [DOMAIN])
│   ├── language.md (English-only policy)
│   └── safety.md (Critical safety rules for [DOMAIN])
│
├── standards/ (Tier 1 - Context-based)
│   ├── coding.md (Code quality for [LANGUAGE])
│   └── [domain-specific].md
│
├── workflows/ (Tier 1)
│   ├── daily.md (End-of-day procedures)
│   └── planning.md (Plan-first discipline)
│
└── actions/ (Tier 1)
    └── [common operations in my domain]

For each file:
- Provide basic content adapted to [MY DOMAIN]
- Include metadata (alwaysApply, tier, priority)
- Follow DIVA's template format

Domain context: [Describe your domain, typical tasks, tools used]
```

**Expected outcome:** Tiered rules structure ready to fill in

---

### Prompt 6: Create Master Functions Template

**Copy this into Cursor composer:**

```
Based on DIVA's master function pattern (from docs/agentic-collaboration-guide.md, Stage 5), help me identify and create master functions for my [DOMAIN] project.

Common operations in my domain:
- [Operation 1: e.g., "Send notifications"]
- [Operation 2: e.g., "Validate data"]
- [Operation 3: e.g., "Query database"]

For each operation, create a master function following DIVA's pattern:
- Retry logic (3 attempts, exponential backoff)
- Comprehensive logging
- Error handling
- Input validation
- Clear interface

Also create corresponding rule files in .cursor/rules/actions/ that enforce usage.

Language: [JavaScript/Python/etc.]
```

**Expected outcome:** Deterministic tools for your domain

---

## 📊 Phase 3: Documentation & Measurement Prompts

### Prompt 7: Set Up Plan-First Discipline

**Copy this into Cursor composer:**

```
Implement DIVA's plan-first discipline for my project (from archives/inputRAW/dataverse-diva/02-AGENT-DESIGN-PATTERNS.md).

Create:

1. docs/plan/todo/ directory (for upcoming work)
2. docs/plan/complete/ directory (for finished work)
3. Plan template (docs/plan/TEMPLATE.md) including:
   - Objective
   - Step-by-step approach
   - Risk assessment
   - Testing strategy
   - Documentation requirements

4. Rule in .cursor/rules/core/identity.md enforcing:
   "No implementation without documented plan"

5. Workflow in .cursor/rules/workflows/planning.md:
   - How to create plan
   - When plan required (significant work only)
   - How to follow plan
   - How to summarize completion

Adapt to [MY DOMAIN] needs.
```

**Expected outcome:** Plan-first workflow established

---

### Prompt 8: Create Learning Journey Tracker

**Copy this into Cursor composer:**

```
Set up learning journey tracking for my agent (following DIVA pattern from archives/inputRAW/dataverse-diva/02-AGENT-DESIGN-PATTERNS.md, Learning Journey section).

Create:

1. docs/[my-agent-name]/learning-journey/
   ├── timeline.md (chronological sessions)
   ├── skills-matrix.md (skills & proficiency levels)
   ├── lessons/ (directory for individual lessons)
   └── TEMPLATE.md (lesson template)

2. Initial skills matrix for [MY DOMAIN]:
   - Relevant skill categories
   - Proficiency levels (None, Beginner, Intermediate, Advanced, Master)
   - Initial assessment

3. Timeline entry format

4. Lesson template

Agent name: [Your agent name]
Domain: [Your domain]
Initial skills: [What your agent should learn]
```

**Expected outcome:** Systematic learning tracking ready

---

### Prompt 9: Set Up Metrics Collection

**Copy this into Cursor chat:**

```
Based on the case study template (docs/case-studies/README.md) and DIVA's metrics (docs/case-studies/dataverse-diva.md), help me set up metrics collection for my project.

For [MY DOMAIN], I need to track:

Quantitative:
- [Metric 1: e.g., accuracy, processing time]
- [Metric 2: e.g., user satisfaction]
- [Metric 3: e.g., error rate]

Qualitative:
- User feedback
- Team adoption
- Challenges encountered

Create:
1. docs/metrics/ directory structure
2. metrics/tracking-template.md (how to record metrics)
3. metrics/baseline.md (capture before-framework measurements)
4. Guide for measuring each metric systematically

Ensure metrics align with case study template requirements.
```

**Expected outcome:** Metrics framework ready

---

## 🔧 Phase 4: Tools & Automation Setup

### Prompt 10: Identify Tool Opportunities

**Copy this into Cursor chat:**

```
Based on F7 (Tools & Automation) in docs/framework-foundations.md, analyze my [DOMAIN] project to identify tool opportunities.

My typical tasks:
- [Task 1]
- [Task 2]
- [Task 3]

For each task, assess:
1. Is it deterministic? (same input → same output)
2. Is it frequent? (3+ times/week)
3. Is reliability critical? (errors unacceptable)
4. Is it time-consuming? (30+ minutes manual)

Recommend:
- Which tasks should become master functions
- Which tasks should use automation platforms (n8n, make.io)
- Which tasks could use background agents
- API integrations needed

Prioritize by ROI (time savings × frequency).
```

**Expected outcome:** Tool development roadmap

---

### Prompt 11: Create Automation Strategy

**Copy this into Cursor chat:**

```
Based on DIVA's automation architecture (archives/inputRAW/dataverse-diva/01-TECHNICAL-ARCHITECTURE.md), design automation strategy for my [DOMAIN] project.

Current repetitive tasks:
- [Task 1: e.g., "Generate weekly reports"]
- [Task 2: e.g., "Monitor logs for errors"]
- [Task 3: e.g., "Update documentation website"]

For each task, recommend:
- Automation approach (background agent, workflow automation, scheduled script)
- Technology (n8n, custom Node.js, Python scheduler)
- Effort estimate (hours to build)
- Expected ROI (time saved per month)

Reference DIVA's Content Watcher (30-60 min → 2-5 min) as example pattern.
```

**Expected outcome:** Automation implementation plan

---

## 📝 Phase 5: Case Study Preparation Prompts

### Prompt 12: Create Documentation Structure

**Copy this into Cursor composer:**

```
I'm preparing to contribute a case study to the Agentic-AI Research Roadmap. Based on the template (docs/case-studies/README.md), set up my documentation structure for eventual extraction.

Create directory structure for documentation that will become my inputRAW/ contribution (similar to archives/inputRAW/dataverse-diva/):

docs/[my-project-name]/
├── 00-PROJECT-OVERVIEW.md
├── 01-TECHNICAL-ARCHITECTURE.md
├── 02-AGENT-DESIGN-PATTERNS.md
├── 03-FRAMEWORK-VALIDATION.md
├── 04-RESEARCH-FINDINGS.md
├── 05-DOMAIN-RULES.md
├── 06-METRICS-EVIDENCE.md
├── 07-LESSONS-LEARNED.md
├── 08-FUTURE-DIRECTIONS.md
└── INDEX.md

For each file, provide:
- Template with sections
- What to document
- Examples from my [DOMAIN]

This will make case study extraction easy later.
```

**Expected outcome:** Documentation structure ready for gradual filling

---

### Prompt 13: Start Case Study Drafting

**After 1-2 months of applying framework, copy this:**

```
I'm ready to draft my case study contribution to the Agentic-AI Research Roadmap.

Based on:
- Case study template (docs/case-studies/README.md)
- DIVA example (docs/case-studies/dataverse-diva.md)
- My documentation in docs/[my-project]/

Create initial draft of my case study including:

1. Executive Summary (what I did, results, contributions)
2. Domain Context (my specific domain, challenges)
3. Framework Application (which stage I reached, how I implemented)
4. Tools & Automation (what I built, ROI metrics)
5. Metrics & Evidence (my quantitative and qualitative results)
6. Novel Patterns (anything unique to my domain)
7. Lessons Learned (what worked, what didn't)

Pull information from my documentation automatically. I'll review and refine.

Domain: [YOUR DOMAIN]
Framework Stage Reached: [Stage X]
Duration: [X months]
Key Metrics: [Your main achievements]
```

**Expected outcome:** First draft of case study ready for refinement

---

## 🎓 Special Prompts for Onboarding Session

### For Zoom Session (Dr. Guan and Contributors)

**Prompt A: Quick Framework Summary for Session**

```
Summarize the Agentic-AI Engineering Framework for a 30-minute onboarding Zoom session with new contributors.

Cover:
1. The core problem (LLM context limitations)
2. The adaptive 5-stage solution (with memory hierarchy analogy)
3. DIVA as proof (3 months, 100% reliability, 60-100 hrs/month saved)
4. What contributors will do (apply to their domain, document, contribute)
5. Expected timeline (1 month application → case study submission)

Make it engaging, use analogies, reference DIVA examples.

Output as presentation outline with talking points.
```

**Use:** During Zoom to explain framework

---

**Prompt B: Domain-Specific Adaptation**

```
For contributor in [DOMAIN], explain how Agentic-AI Engineering Framework applies specifically to their field.

Based on:
- Framework stages (docs/framework-foundations.md)
- DIVA patterns (archives/inputRAW/dataverse-diva/)
- Domain characteristics: [Describe contributor's domain]

Provide:
1. Likely starting stage for [DOMAIN]
2. Domain-specific challenges framework addresses
3. Relevant DIVA patterns to adopt
4. Expected benefits (time savings, reliability)
5. 3-month roadmap for framework application

Make it concrete and domain-specific.
```

**Use:** Personalized guidance during onboarding

---

## 🔄 Ongoing Prompts (During Framework Application)

### Prompt 14: Daily Check-In

**Use at end of each work session:**

```
End-of-day check for Agentic-AI Engineering Framework compliance.

Based on .cursor/rules/workflows/daily.md pattern from DIVA:

Review today's work and check:
1. Was plan-first discipline followed? (any implementation without plan?)
2. Is documentation up-to-date? (docs/INDEX.md current?)
3. Are new patterns documented? (anything that should become a rule?)
4. Should skills matrix be updated? (new skills acquired?)
5. Are metrics being collected? (tracking progress?)

Generate brief summary of:
- What was accomplished
- What was learned
- What should be improved
- Action items for tomorrow

This ensures knowledge persistence and framework compliance.
```

**Expected outcome:** Systematic knowledge capture

---

### Prompt 15: Weekly Framework Review

**Use weekly:**

```
Weekly review of Agentic-AI Engineering Framework application to my [DOMAIN] project.

Analyze:
1. Current framework stage (am I still at the right stage?)
2. Evolution triggers (should I move to next stage?)
3. Information volume growth (how much new knowledge this week?)
4. Tool opportunities (new deterministic tasks to automate?)
5. Metrics progress (how are numbers improving?)

Based on:
- My current documentation volume
- Context window usage patterns
- Pain points encountered this week

Recommend:
- Stay at current stage OR evolve to next
- New tools to build
- Process improvements
- Metrics adjustments

Reference computer memory analogy for stage assessment.
```

**Expected outcome:** Framework evolution guidance

---

## 📦 Phase 6: Extraction & Contribution Prompts

### Prompt 16: Generate inputRAW Extraction

**After 2-3 months, when ready to contribute:**

```
I'm ready to contribute my case study to the Agentic-AI Research Roadmap.

Extract my project documentation into inputRAW/ format (like archives/inputRAW/dataverse-diva/).

From my docs/[my-project]/ directory, generate 9 extraction documents:

00-PROJECT-OVERVIEW.md
01-TECHNICAL-ARCHITECTURE.md
02-AGENT-DESIGN-PATTERNS.md
03-FRAMEWORK-VALIDATION.md
04-RESEARCH-FINDINGS.md
05-DOMAIN-RULES.md
06-METRICS-EVIDENCE.md
07-LESSONS-LEARNED.md
08-FUTURE-DIRECTIONS.md
INDEX.md

For each:
- Extract relevant content from my existing documentation
- Format following DIVA's structure
- Include all metrics, evidence, and patterns
- Ensure research-ready quality

Domain: [YOUR DOMAIN]
Project: [PROJECT NAME]
Duration: [X months]
Framework Stage: [Stage X]
```

**Expected outcome:** Complete inputRAW/ extraction ready to share

---

### Prompt 17: Final Case Study Polish

**Before submission:**

```
Polish my case study for submission to Agentic-AI Research Roadmap.

Review against:
- Case study template (docs/case-studies/README.md)
- Quality standards (minimum, high-quality, excellent)
- PR checklist (.github/PULL_REQUEST_TEMPLATE.md)

Check:
1. All required sections present?
2. Metrics provided (minimum 3 quantitative)?
3. Tools & Automation documented (CRITICAL section)?
4. Evidence supports claims?
5. Novel patterns identified?
6. Lessons learned included?
7. Framework citation correct?

Provide:
- Completeness score (% of requirements met)
- Missing elements
- Suggestions for improvement
- Quality assessment (minimum/high/excellent)

Help me reach "excellent" standard.
```

**Expected outcome:** Publication-ready case study

---

## 🎯 Quick Reference: Most Important Prompts

**For First Week:**
1. **Prompt 1** — Understand framework
2. **Prompt 2** — Assess my stage
3. **Prompt 4** — Create structure
4. **Prompt 14** — Daily check-in

**For Ongoing Work:**
- **Prompt 15** — Weekly review (every week)
- **Prompt 10-11** — Tools & automation (as needed)

**For Contribution:**
- **Prompt 16** — Generate extraction (after 2-3 months)
- **Prompt 17** — Polish case study (before submission)

---

## 💡 Pro Tips for Using These Prompts

### 1. Customize for Your Domain

**Replace placeholders:**
- `[YOUR DOMAIN]` → Your actual domain (Healthcare, GIS, etc.)
- `[LANGUAGE]` → Your programming language
- `[my-agent-name]` → Your agent's name
- `[PROJECT NAME]` → Your project name

### 2. Use Composer for File Creation

**For Prompts 4-8:** Use Cursor Composer (Cmd+I) to create multiple files

**For Prompts 1-3, 14-17:** Use Cursor Chat for analysis and guidance

### 3. Reference DIVA Archives

**When stuck, ask Cursor to:**
```
Show me how DIVA handled [SPECIFIC SITUATION] from archives/inputRAW/dataverse-diva/
```

Examples:
- "How DIVA structured rules" → 02-AGENT-DESIGN-PATTERNS.md
- "How DIVA measured metrics" → 06-METRICS-EVIDENCE.md
- "How DIVA learned" → 07-LESSONS-LEARNED.md

### 4. Iterate Based on Cursor's Output

**Don't accept first output blindly:**
1. Review what Cursor generated
2. Ask for refinements
3. Adapt to your specific needs
4. Test in your environment

### 5. Document As You Go

**After using each prompt:**
- Note what worked
- Note what needed adjustment
- Update for next contributor
- Share insights in your case study

---

## 🤝 Support During Application

### If You Get Stuck

**Option 1: Ask Cursor**
```
I'm stuck with [ISSUE] while applying the Agentic-AI Engineering Framework to my [DOMAIN] project.

How did DIVA handle similar situation? Check archives/inputRAW/dataverse-diva/ for relevant patterns.

Suggest solution adapted to my context.
```

**Option 2: GitHub Discussions**
- Post question: https://github.com/Keven1894/Agentic-AI-Research-Roadmap/discussions
- Reference which prompt you used
- Describe your issue

**Option 3: Direct Contact**
- Email: bguan@fiu.edu
- Subject: "Framework Application Help - [YOUR DOMAIN]"
- Include which prompts you've used

---

## 📋 Checklist for Contributors

### Before Starting

- [ ] Attended onboarding Zoom session
- [ ] Cursor IDE installed and configured
- [ ] LLM access set up (Claude/GPT or Ollama)
- [ ] Have project/domain to apply framework to
- [ ] Read START_HERE.md

### Week 1

- [ ] Used Prompt 1 (understand framework)
- [ ] Used Prompt 2 (assess stage)
- [ ] Used Prompt 3 (understand patterns)
- [ ] Used Prompt 4 (create structure)
- [ ] Started daily check-ins (Prompt 14)

### Week 2-4

- [ ] Rules structure created (Prompt 5 if Stage 2+)
- [ ] Master functions identified (Prompt 10)
- [ ] Plan-first discipline adopted (Prompt 7)
- [ ] Learning journey tracking started (Prompt 8)
- [ ] Metrics collection begun (Prompt 9)
- [ ] Weekly reviews (Prompt 15)

### Month 2-3

- [ ] Framework applied consistently
- [ ] Metrics collected systematically
- [ ] Lessons documented
- [ ] Tools built and measured
- [ ] Patterns identified

### Contribution Phase

- [ ] Used Prompt 16 (generate extraction)
- [ ] Used Prompt 17 (polish case study)
- [ ] Submitted PR via GitHub
- [ ] Ready for co-authorship discussion

---

## 🎯 Success Indicators

**You're applying the framework successfully if:**

✅ Cursor knows your framework stage  
✅ Daily check-ins become routine  
✅ Rules prevent session amnesia  
✅ Plans created before implementation  
✅ Metrics collected systematically  
✅ Tools built for common operations  
✅ Documentation grows continuously  
✅ Learning journey tracked  

**After 1 month:** Should see measurable improvements  
**After 2-3 months:** Ready to contribute case study

---

## 📖 Additional Resources

### During Onboarding Zoom

**Dr. Guan can share screen showing:**
1. How to use these prompts in Cursor
2. Live demonstration with a sample domain
3. Q&A on framework application
4. Timeline expectations
5. Collaboration opportunities

### After Onboarding

**You'll have:**
- These prompts (copy-paste ready)
- DIVA archives (reference material)
- Framework docs (complete methodology)
- Direct support (email, Discussions)

---

## 🎊 You're Ready!

**With these prompts, you can:**
- ✅ Quickly understand framework (30 min)
- ✅ Set up your project (2-3 hours)
- ✅ Apply systematically (2-3 months)
- ✅ Contribute case study (1-2 weeks to write)

**Total timeline:** ~3 months from onboarding to case study submission

**Support available:** Throughout the journey!

---

**Last Updated:** November 11, 2025  
**Status:** Ready for use in onboarding sessions  
**Maintained by:** Agentic-AI Research Roadmap team  
**Questions:** bguan@fiu.edu or GitHub Discussions


