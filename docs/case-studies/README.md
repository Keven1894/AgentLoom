# Agentic AI Framework Case Studies

**Purpose:** Document real-world applications of the Agentic-AI Engineering Framework across domains  
**Status:** Active collection — submissions welcome!  
**Last Updated:** November 11, 2025

---

## Overview

This directory contains **production-validated case studies** demonstrating the Agentic-AI Engineering Framework in action across different domains. Each case study provides evidence that the framework's adaptive progression (Stages 0-4) produces reliable, maintainable, evolvable AI agents.

**Why Case Studies Matter:**

1. **Validation** — Prove framework effectiveness in real environments
2. **Generalizability** — Demonstrate cross-domain applicability
3. **Learning** — Share patterns, insights, and lessons learned
4. **Community** — Build collective knowledge about agentic AI engineering

---

## Existing Case Studies

### [Dataverse DIVA](dataverse-diva.md)

**Domain:** Digital Libraries & Institutional Repositories  
**Framework Stage:** Stage 2 (RAM: Indexing + Metadata + Docs)  
**Status:** Production (3+ months)  

**Key Contributions:**
- First documented AI agent for library/repository systems
- Rules-as-memory institutional memory (100% consistency, 87% token efficiency)
- Schema-based context engineering (+23% accuracy for Llama 3.2 3B)
- Multi-role single agent architecture (SysAdmin + Developer)
- Production metrics: 52.6% LLM accuracy, 100% deployment success, 9.2/10 satisfaction

**Novel Patterns:**
- Tiered `.cursor/rules/` configuration (memory hierarchy within Stage 2)
- Plan-first discipline enforcement
- Multi-model orchestration (Claude + GPT + local Llama)
- Automated documentation generation via Content Watcher agent

---

## Submitting a Case Study

### Who Should Submit

**We're looking for:**
- ✅ Researchers applying framework to their domain
- ✅ Engineers building production agentic systems
- ✅ Practitioners validating framework in real projects
- ✅ Innovators discovering new patterns and insights

**Target Domains:**
- GIS / Environmental Data
- Digital Libraries / Archives
- Education / Research Support
- IT Operations / DevOps
- Healthcare / Clinical Systems
- Industry Applications
- **Your innovative domain!**

---

### Prerequisites

Before submitting a case study, you must:

1. **Apply the Framework to a Real Project**
   - Not theoretical — must be actual implementation
   - Production deployment OR substantial pilot
   - Minimum 1-2 months of operation (3+ months preferred)

2. **Document Framework Application**
   - Identify current framework stage (0-4)
   - Explain how you implemented each applicable stage
   - Show evolution if you progressed through stages

3. **Provide Metrics and Evidence**
   - Quantitative outcomes (accuracy, efficiency, time savings, etc.)
   - Qualitative feedback (user satisfaction, lessons learned)
   - Production logs or pilot results

4. **Use AI-Agent-Enabled Workflow**
   - Cursor, Claude, GPT-powered IDE, or equivalent
   - Document how AI agents helped build the system
   - Demonstrate high-velocity development patterns

5. **Follow the Template**
   - Use case study template (see below)
   - Include all required sections
   - Provide proper attribution

---

## Case Study Template

### Required Frontmatter

```markdown
# [Your Domain] Agentic AI Case Study

**Domain:** [Domain name]  
**Authors:** [Full names]  
**Affiliations:** [Institutions/Organizations]  
**Framework Stage:** [Stage 0/1/2/3/4]  
**Status:** [Production / Pilot / Experimental]  
**Duration:** [Months in operation]  
**Contact:** [Email]  
**Date:** [Submission date]
```

---

### Required Sections

#### 1. Executive Summary

Brief overview (200-300 words):
- What problem you addressed
- How you applied the framework
- Key results and metrics
- Novel contributions or patterns

#### 2. Domain Context

**Background information:**
- Domain description and characteristics
- Specific problem being solved
- Why agentic AI is applicable
- Unique challenges of the domain

**Technology landscape:**
- Existing systems and tools
- Data types and volumes
- Technical constraints
- Integration requirements

#### 3. Framework Application

**Stage Identification:**
- Which framework stage you're currently at (0-4)
- Why you're at this stage (information volume, constraints)
- Evolution path if you progressed through multiple stages

**Implementation Details:**

For each applicable stage, document:

**Stage 0: System Prompt (if applicable)**
- Initial prompt design
- Domain knowledge encoded
- Capabilities defined

**Stage 1: Documentation (if applicable)**
- Documentation structure
- What knowledge was captured
- How organized

**Stage 2: Indexing + Metadata (if applicable)**
- Indexing strategy
- Metadata schema
- Organizational hierarchy
- Token efficiency achieved

**Stage 3: RAG System (if applicable)**
- Database choice (PostgreSQL + pgvector, etc.)
- Vector embedding strategy
- Retrieval approach
- Query optimization

**Stage 4: Fine-Tuning (if applicable)**
- Training data curation approach
- Fine-tuning method (LoRA, PEFT, etc.)
- Baseline vs. fine-tuned comparison
- Deployment strategy

**Toolset & Automation (CRITICAL - Required for all stages):**
- **Master Functions:** What deterministic tools did you build?
- **Automation Platforms:** n8n, make.io, Zapier, or custom workflows?
- **Background Agents:** Any autonomous agents running continuously?
- **API Integrations:** External services connected (Gmail, databases, etc.)?
- **MCP/A2A/A2P:** Standardized protocols used?
- **Tool ROI:** Time savings, reliability improvements from automation?
- **How tools complement LLM:** Division of probabilistic vs. deterministic tasks

**Why this is required:**
- Tools are ESSENTIAL for production reliability (not optional)
- Tools solve research problems (#1 Reliability, #4 Interoperability, #7 Scalability)
- Without tools: Framework is theoretical; With tools: Framework is production-ready
- DIVA evidence: 100% reliability, 60-100 hours/month saved through tools/automation

#### 4. Tools & Automation Infrastructure

**CRITICAL SECTION — Required for all case studies**

Document your tools and automation setup:

**A. Master Functions (Deterministic Tools)**

What standardized functions did you create?

```markdown
| Function Name | Purpose | Reliability Improvement | Usage Frequency |
|---------------|---------|----------------------|-----------------|
| [e.g., sendEmail()] | [Email with retry] | [100% vs 80% manual] | [100 times/month] |
| [Function 2] | [Purpose] | [Metric] | [Frequency] |
```

**B. Automation Platforms**

Did you use workflow automation? Document:
- **Platform:** n8n / make.io / Zapier / Custom scripts
- **Workflows created:** [Names and purposes]
- **Systems integrated:** [What platforms connected]
- **Autonomous capacity:** [e.g., 100 emails/day]
- **Setup time:** [Hours to implement]
- **Maintenance:** [Hours/month]

**C. Background Agents**

Any agents running autonomously in background?
- **Agent name/purpose:** [e.g., Content Watcher for docs→HTML]
- **Technology:** [Node.js + chokidar, Python scheduler, etc.]
- **Operations:** [What it does automatically]
- **Time savings:** [Manual time → Automated time]
- **Frequency:** [How often runs]

**D. API Integrations**

What external services/platforms did you integrate?
- **APIs used:** [Gmail, Slack, Database, Cloud services, etc.]
- **Integration patterns:** [REST, GraphQL, Webhooks, etc.]
- **Authentication:** [OAuth, API keys, etc.]
- **Reliability measures:** [Retry logic, error handling, logging]

**E. Standards & Protocols**

- **MCP compliance:** [Yes/No - Model Context Protocol]
- **A2A/A2P:** [Agent-to-Agent or Agent-to-Platform patterns used]
- **Tool discovery:** [How tools are registered and discovered]

**F. Tools-LLM Division**

How did you divide tasks between LLM and tools?

| Task Type | Handled By | Rationale |
|-----------|------------|-----------|
| [e.g., Email composition] | LLM | Requires natural language, reasoning |
| [e.g., Email sending] | Tool (sendEmail) | Must be 100% reliable |
| [e.g., Data analysis] | LLM | Requires interpretation |
| [e.g., Data validation] | Tool (validator) | Must be deterministic |

**G. Tool ROI Metrics**

**Required:** Show measurable impact of tools/automation

| Tool/Automation | Time Saved | Reliability Gain | Monthly Impact |
|----------------|------------|------------------|----------------|
| [Tool 1] | [Before→After] | [%] | [Hours saved] |
| [Total] | [Aggregate] | [Overall %] | [Total hours] |

**Example (DIVA):**
- Master functions + automation: 60-100 hours/month saved
- Reliability: 100% (vs ~80-95% manual)
- Consistency: 100% (vs ~70-80% manual)

---

#### 5. Metrics & Evidence

**Quantitative Metrics** (provide at least 3):
- Accuracy / Performance metrics
- Efficiency gains (time, cost, tokens)
- Reliability metrics (uptime, success rate)
- Consistency measurements
- User satisfaction scores

**Qualitative Evidence:**
- User feedback and testimonials
- Team adoption patterns
- Observed behavior changes
- Unexpected benefits

**Validation Methodology:**
- How metrics were collected
- Baseline comparisons (before/after)
- Testing approach
- Sample sizes and duration

#### 5. Novel Patterns & Innovations

**What's new or unique in your implementation:**
- Design patterns not seen elsewhere
- Domain-specific adaptations
- Technical innovations
- Process innovations

**Examples:**
- DIVA: Rules-as-memory, schema-based context, tiered configuration

#### 6. Lessons Learned

**What worked well:**
- Successful patterns and practices
- Positive surprises
- Validated hypotheses

**What didn't work:**
- Challenges encountered
- Failed approaches
- What you'd do differently

**Recommendations:**
- For others applying framework to your domain
- For framework improvements
- For future research

#### 7. Future Directions

**Next steps for your project:**
- Planned enhancements
- Evolution to next framework stage
- Research questions emerged

**Broader implications:**
- What your case study suggests for the field
- Open questions for community

#### 8. References

**Framework citation:**
```bibtex
@software{guan2025agenticai,
  author = {Guan, Boyuan (Keven)},
  title = {Agentic-AI Lab: Engineering the Next Generation of Intelligent Systems},
  year = {2025},
  publisher = {Zenodo},
  version = {1.1.0},
  doi = {10.5281/zenodo.17561541},
  url = {https://doi.org/10.5281/zenodo.17561541}
}
```

**Your project citation:**
```bibtex
[Your project citation]
```

**Additional references:**
- Domain-specific literature
- Technical documentation
- Related work

---

## Attribution & Co-Authorship Policy

### How You'll Be Credited

**In This Repository:**
- ✅ Byline on your case study document
- ✅ Listed in [CONTRIBUTORS.md](../../CONTRIBUTORS.md)
- ✅ Git commit history (permanent attribution)
- ✅ Acknowledgment in framework documentation

**In Academic Publications:**

#### Case Study-Specific Papers

If we write a paper featuring your case study:
- **Primary author:** You (case study contributor)
- **Co-author:** Dr. Guan (framework creator)
- **Additional authors:** Other contributors (by contribution level)

**Example:**  
*"Healthcare AI Agent: Applying the Agentic-AI Framework to Clinical Documentation"*  
Authors: Smith, J., **Guan, B.**, & Doe, J.

#### Integrative Papers

If your case study is included in multi-domain analysis:
- **Primary author:** Dr. Guan (framework creator)
- **Co-authors:** Case study contributors (alphabetical or by significance)

**Example:**  
*"Agentic AI Across Domains: Validation of the Engineering Framework"*  
Authors: Guan, B., Smith, J., Jones, A., & Lee, K.

#### Framework Methodology Papers

- **By invitation** for sustained framework development
- Core team and major contributors

### Co-Authorship Criteria

**Automatic co-authorship if:**
- ✅ Substantial case study contribution (validated implementation)
- ✅ Novel patterns or insights documented
- ✅ Significant metrics and evidence provided
- ✅ Active collaboration on paper writing

**Acknowledgment (not co-authorship) if:**
- Partial implementation or preliminary results
- Minor adaptations without novel insights
- Theoretical application without empirical validation

**We err on the side of inclusion** — contributions are valued and credited generously.

---

## Quality Standards

### Minimum Acceptable Case Study

**Must include:**
- [ ] Real implementation (not simulated or theoretical)
- [ ] Framework stage clearly identified
- [ ] At least 3 quantitative metrics with evidence
- [ ] Lessons learned section
- [ ] Follows template structure
- [ ] Proper attribution and citations

### High-Quality Case Study

**Additional characteristics:**
- [ ] Production deployment (not just pilot)
- [ ] 3+ months operational data
- [ ] Comparison to baseline
- [ ] Novel patterns documented
- [ ] Reproducible methodology
- [ ] Code/data artifacts available
- [ ] Multiple validation methods

### Excellent Case Study (Publication-Ready)

**Publication-worthy characteristics:**
- [ ] Significant novel contributions
- [ ] Rigorous empirical validation
- [ ] Statistical analysis where appropriate
- [ ] Comprehensive documentation
- [ ] Replicable by others
- [ ] Addresses open research questions
- [ ] Community impact potential

**Example:** DIVA case study exemplifies excellent standard

---

## Submission Process

### Step 1: Prepare Your Case Study

1. **Apply framework** to your project (2-4 weeks typical)
2. **Collect metrics** and evidence (ongoing)
3. **Write case study** using template above
4. **Self-review** against quality checklist

### Step 2: Fork and Create

```bash
# Fork repository on GitHub
git clone https://github.com/[your-username]/Agentic-AI-Research-Roadmap
cd Agentic-AI-Research-Roadmap

# Create your case study file
# Filename: docs/case-studies/[domain]-[short-name].md
# Example: docs/case-studies/healthcare-clinical-documentation.md
```

### Step 3: Submit Pull Request

```bash
# Create branch
git checkout -b case-study-[domain]

# Add your case study
git add docs/case-studies/[your-file].md

# Commit with descriptive message
git commit -m "docs(case-study): add [domain] case study by [your name]"

# Push to your fork
git push origin case-study-[domain]

# Open PR on GitHub
# Use the PR template that will auto-populate
```

### Step 4: Review Process

**What happens next:**

1. **Automated checks** (linting, links, formatting)
2. **AI-agent-assisted review** by core team
   - Verify framework application
   - Check metrics and evidence  
   - Assess quality and completeness
3. **Feedback provided** (usually within 1 week)
4. **Iterate** based on comments
5. **Approval and merge**

**Timeline:** 1-2 weeks typical from submission to merge

### Step 5: Publication Collaboration

After case study is merged:

1. **Discuss publication opportunities** with core team
2. **Co-develop paper** featuring your case study
3. **Joint submission** to conferences/journals
4. **Shared dissemination** and presentation

---

## Review Criteria

### Technical Validity

- [ ] Framework application is correct
- [ ] Stage identification is accurate
- [ ] Implementation details are sound
- [ ] Metrics are properly measured
- [ ] Evidence supports claims

### Research Quality

- [ ] Methodology is rigorous
- [ ] Sample sizes are adequate
- [ ] Baselines are appropriate
- [ ] Analysis is valid
- [ ] Conclusions are supported

### Documentation Quality

- [ ] Well-written and clear
- [ ] Properly structured
- [ ] Examples are helpful
- [ ] Cross-references work
- [ ] Citations are complete

### Community Value

- [ ] Fills a gap in existing case studies
- [ ] Provides actionable insights
- [ ] Advances framework understanding
- [ ] Benefits other implementers
- [ ] Opens new research directions

---

## FAQ

### Q: Do I need to complete all 5 framework stages?

**A:** No! Document whichever stage you're currently at. The framework is **adaptive** — you implement stages based on your information volume.

**Examples:**
- Stage 1: Small project, docs fit in context → perfectly valid case study
- Stage 2: Like DIVA, indexed corpus → excellent case study
- Stage 4: Achieved fine-tuning → exceptional case study

### Q: How long should my case study be?

**A:** 2,000-5,000 words typical. DIVA case study (~2,000 words) is a good reference.

**Focus on quality over length.**

### Q: Can I submit if my project is still in pilot/experimental phase?

**A:** Yes, but clearly mark status as "Pilot" or "Experimental" rather than "Production."

**Preference:** Production deployments with longitudinal data, but substantial pilots are valuable too.

### Q: What if I discover the framework doesn't work for my domain?

**A:** **Document that!** Negative results are valuable for research.

Include:
- What you tried
- Why it didn't work
- Domain-specific challenges
- Recommendations for adaptation

### Q: Do I need to open-source my project code?

**A:** No. The case study documents your **application of the framework**, not necessarily the code itself.

**However:** Sharing code/data (when possible) significantly increases research value.

### Q: How is co-authorship determined?

**A:**

**Automatic co-authorship:**
- Substantial case study (production validated, novel insights)
- Active collaboration on paper writing
- Significant contribution to framework understanding

**Paper-specific:**
- Case study-focused paper: You're primary author
- Multi-domain analysis: Co-author by contribution
- Framework methodology paper: By invitation

**Always discussed and agreed upon before submission.**

### Q: Can I update my case study after submission?

**A:** Yes! Case studies are living documents.

Submit updates via PR with:
- Description of changes
- Reason for update
- Updated metrics if applicable

### Q: What if I'm applying framework to a domain not listed?

**A:** **Excellent!** Novel domains are highly valuable.

Your case study helps demonstrate framework generalizability. Be thorough in explaining domain characteristics and challenges.

### Q: Do I need to use Cursor specifically?

**A:** No. Any AI-agent-enabled IDE works (Cursor, GitHub Copilot, Claude + IDE, etc.).

**Requirement:** AI-augmented workflow at high velocity, not traditional manual coding.

### Q: How do I get help while developing my case study?

**A:** 
- **GitHub Discussions:** Ask questions publicly
- **GitHub Issues:** Report specific problems
- **Email:** bguan@fiu.edu for direct collaboration

**We're here to help!**

---

## Case Study Template

### Copy-Paste Template

```markdown
# [Your Domain] Agentic AI Case Study

**Domain:** [Your domain]  
**Authors:** [Your name(s)]  
**Affiliations:** [Your institution(s)]  
**Framework Stage:** [Stage 0/1/2/3/4]  
**Status:** [Production / Pilot / Experimental]  
**Duration:** [Months in operation]  
**Contact:** [Your email]  
**Date:** [YYYY-MM-DD]

---

## Executive Summary

[200-300 words overview]
- Problem addressed
- Framework application approach
- Key results
- Novel contributions

---

## Domain Context

### Background

[Describe your domain]
- Domain characteristics
- Specific problem
- Why agentic AI
- Unique challenges

### Technology Landscape

[Your technology stack]
- Existing systems
- Data types and volumes
- Technical constraints
- Integration requirements

---

## Framework Application

### Current Framework Stage

**Stage [X]: [Stage Name]**

[Explain why you're at this stage]
- Information volume
- Context constraints
- Evolution from previous stage (if applicable)

### Implementation Details

#### [For Each Applicable Stage]

**Stage 0: System Prompt** (if used)
- Prompt design
- Domain knowledge
- Capabilities

**Stage 1: Documentation** (if used)
- Structure
- Knowledge captured
- Organization

**Stage 2: Indexing + Metadata** (if used)
- Indexing strategy
- Metadata schema
- Hierarchy design
- Efficiency metrics

**Stage 3: RAG System** (if used)
- Database architecture
- Embedding strategy
- Retrieval approach
- Query optimization

**Stage 4: Fine-Tuning** (if used)
- Data curation
- Fine-tuning method
- Baseline comparison
- Deployment

#### Toolset Integration

[Your APIs, MCP, A2P integrations]
- What tools built
- How they complement LLM
- Deterministic vs probabilistic task division

---

## Metrics & Evidence

### Quantitative Metrics

[Provide at least 3 metrics with numbers]

| Metric | Value | Baseline | Improvement |
|--------|-------|----------|-------------|
| [Metric 1] | [Value] | [Before] | [% or abs] |
| [Metric 2] | [Value] | [Before] | [% or abs] |
| [Metric 3] | [Value] | [Before] | [% or abs] |

**Examples:**
- Accuracy: 52.6%
- Token efficiency: 87% reduction
- Time savings: 60-100 hours/month
- Deployment success: 100% (50 deployments)
- User satisfaction: 9.2/10

### Qualitative Evidence

[User feedback, observations, testimonials]
- Team feedback
- User experiences
- Behavioral changes
- Unexpected benefits

### Validation Methodology

[How you measured]
- Data collection methods
- Sample sizes
- Duration
- Baseline establishment

---

## Novel Patterns & Innovations

### What's New or Unique

[Your innovations]
- Patterns not seen elsewhere
- Domain-specific adaptations
- Technical breakthroughs
- Process innovations

### Why It Matters

[Impact and implications]
- For your domain
- For framework understanding
- For broader community

---

## Lessons Learned

### What Worked Well

[Successful patterns]
- What succeeded
- Why it worked
- Recommendations

### What Didn't Work

[Challenges and failures]
- What failed
- Why it failed
- How you adapted
- What to avoid

### Recommendations

**For your domain:**
- Specific guidance for others in your field

**For the framework:**
- Suggested improvements
- Missing pieces
- Enhancement ideas

---

## Future Directions

### Project Roadmap

[Your next steps]
- Planned enhancements
- Evolution to next stage
- Research questions

### Broader Implications

[For the field]
- What your work suggests
- Open questions
- Research opportunities

---

## References

### Framework Citation

```bibtex
@software{guan2025agenticai,
  author = {Guan, Boyuan (Keven)},
  title = {Agentic-AI Lab: Engineering the Next Generation of Intelligent Systems},
  year = {2025},
  publisher = {Zenodo},
  version = {1.1.0},
  doi = {10.5281/zenodo.17561541},
  url = {https://doi.org/10.5281/zenodo.17561541}
}
```

### Your Project

[Your citations]

### Related Work

[Domain-specific references]

---

**Prepared:** [Date]  
**Status:** [Draft/Complete]  
**Part of:** Agentic-AI Research Roadmap Case Studies

```

---

## Quality Checklist

Before submitting, verify:

### Content Completeness

- [ ] All required sections included
- [ ] Frontmatter complete
- [ ] Executive summary present
- [ ] Metrics with evidence
- [ ] Lessons learned documented

### Technical Accuracy

- [ ] Framework stage correctly identified
- [ ] Implementation details accurate
- [ ] Metrics properly measured
- [ ] Evidence supports claims

### Research Quality

- [ ] Methodology explained
- [ ] Baselines established
- [ ] Sample sizes adequate
- [ ] Analysis valid
- [ ] Conclusions supported

### Documentation Quality

- [ ] Well-written and clear
- [ ] Proper markdown formatting
- [ ] Working links and cross-references
- [ ] Citations complete
- [ ] Examples helpful

### Framework Alignment

- [ ] Demonstrates framework application
- [ ] Explains stage progression
- [ ] Shows adaptive nature
- [ ] Provides validation evidence
- [ ] Contributes to framework understanding

---

## After Submission

### Review Timeline

**Typical process:**
- Week 1: Initial review and feedback
- Week 2: Iteration based on comments
- Week 3: Final approval and merge

**Urgent reviews available** for time-sensitive submissions (conferences, grants, etc.)

### Publication Opportunities

After your case study is accepted:

1. **We'll discuss** publication opportunities
2. **Co-develop** paper featuring your work
3. **Joint submission** to appropriate venue
4. **Shared presentation** at conferences

**Target venues based on domain:**
- Technical: ACL, EMNLP, AAAI
- Applied: JCDL, Code4Lib, domain-specific conferences
- Interdisciplinary: HAI, CHI

---

## Examples of Strong Case Studies

### DIVA (Digital Libraries) — The Standard

**Strengths:**
- ✅ 3+ months production validation
- ✅ Comprehensive metrics (10+ quantitative)
- ✅ Novel patterns documented (3 major innovations)
- ✅ Systematic methodology
- ✅ Lessons learned with evidence
- ✅ Publication-ready quality

**Study this case study as a model!**

---

## Contact & Support

### Questions About Case Studies

- **General:** [GitHub Discussions](https://github.com/Keven1894/Agentic-AI-Research-Roadmap/discussions)
- **Specific:** Create issue with `case-study` label
- **Direct:** bguan@fiu.edu

### Collaboration Proposals

**Email bguan@fiu.edu with:**
- Domain and use case
- Current project status
- Timeline and goals
- Collaboration interests

**We respond within 1 week!**

---

## Summary

**Case studies are the PRIMARY way the framework gets validated and improved.**

Your contribution:
- ✅ Proves framework works in your domain
- ✅ Teaches the community new patterns
- ✅ Opens collaboration opportunities
- ✅ Advances the field

**We eagerly await your case study!** 🚀

---

**Last Updated:** November 11, 2025  
**Status:** Active — Submissions Welcome!  
**Contact:** bguan@fiu.edu


