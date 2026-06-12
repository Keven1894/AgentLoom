# Contributing to AgentLoom

**Welcome!** Thank you for your interest in advancing the field of production-grade agentic AI engineering.

This project is unique: we're not just building software—we're establishing a **new way of engineering intelligent systems** that learn, evolve, and operate reliably in production environments.

---

## 🎯 Understanding the Dual-Helix Framework

Before contributing, understand that this project consists of two complementary repositories:

- **[AgentLoom](https://github.com/Keven1894/AgentLoom)** (this repo) — Engineering strand: how agents learn and evolve
- **[co-agenticOS](https://github.com/Keven1894/co-agenticOS)** — Governance strand: rules, boundaries, human-AI interaction

**Both are necessary for reliable agentic intelligence.** See [Dual-Helix Clarification](docs/dual-helix-clarification.md) for details.

---

## Public release hygiene (maintainers)

Before any push to the public GitHub repos (`AgentLoom`, `agentloom-runtime`,
`co-agenticOS`), run an internal-info scan on changed paths and require **0 BLOCK**
(e.g. `Scripts/oss_release/scan_internal_info.py` in the envistor-data workspace).
Do not commit institution-specific deployment code, credentials, or production data.
Copyright stays under the maintainer's personal name; affiliation belongs in
`CITATION.cff` / README only.

---

## 🚀 Contribution Pathways

We offer two distinct contribution paths based on your goals and collaboration level:

### Path A: Case Study Contribution (External Collaborators)

**Who:** Researchers, engineers, practitioners applying the framework to their domain

**What:** Validate the Agentic-AI Engineering Framework in your own projects and contribute your findings as a case study

**Workflow:**

```bash
# 1. Fork this repository
git clone https://github.com/[your-username]/AgentLoom
cd AgentLoom

# 2. Create your case study
# Add to: docs/case-studies/[your-domain]-case-study.md
# Use template from: docs/case-studies/README.md

# 3. Submit Pull Request
git checkout -b case-study-[your-domain]
git add docs/case-studies/[your-domain]-case-study.md
git commit -m "docs: add [domain] case study"
git push origin case-study-[your-domain]
# Open PR on GitHub
```

**Requirements:**

- ✅ Must apply the framework to a real project (not theoretical)
- ✅ Must document all 5 stages or explain current stage
- ✅ Must provide metrics and evidence
- ✅ Must use AI-agent-enabled workflow (Cursor or similar)
- ✅ Must follow case study template

**Benefits:**

- 🎓 Co-authorship opportunity on research papers
- 📢 Visibility in framework documentation
- 🤝 Collaboration with framework creators
- 🏆 Attribution in CONTRIBUTORS.md and git history

**See:** [Case Studies Guide](docs/case-studies/README.md) for detailed template and requirements

---

### Path B: Framework Enhancement (Core Team, By Invitation)

**Who:** Trusted collaborators working closely with framework development

**What:** Direct contributions to framework methodology, core documentation, tooling

**Workflow:**

```bash
# 1. Request collaborator access (email bguan@fiu.edu)
# 2. Clone with write access
git clone https://github.com/Keven1894/AgentLoom
cd AgentLoom

# 3. Create feature branch
git checkout -b feature/[feature-name]

# 4. Make changes following project standards

# 5. Submit Pull Request for review
git push origin feature/[feature-name]
```

**Requirements:**

- ✅ Sustained collaboration commitment
- ✅ Deep engagement with framework principles
- ✅ Regular communication with core team
- ✅ Adherence to `.cursor/rules.md` standards

**Access:** By invitation only (contact <bguan@fiu.edu>)

---

## 🤖 The Agentic Collaboration Method

**Critical Understanding:** This project operates at **AI-augmented velocity**—10,000+ lines of code and 30+ documents per day using AI agents.

**This means:**

- ❌ **Traditional contribution methods won't keep pace** (manual coding, conventional workflows)
- ✅ **You must use AI-agent-enabled workflows** (Cursor, Claude, or similar tools)

### Prerequisites for Meaningful Contribution

**Required:**

1. **AI-Enabled IDE** — Cursor, GitHub Copilot, or equivalent AI-augmented development environment
2. **LLM Access** — Claude, GPT-4/5, or capable local models (Llama 3.1 8B+)
3. **Agentic Mindset** — Direct agents, don't code manually at traditional pace

**Recommended Reading:**

- [Agentic Collaboration Guide](docs/agentic-collaboration-guide.md) — **Essential reading!**
- [Framework Foundations](docs/framework-foundations.md) — Understand the theoretical basis
- [Dual-Helix Clarification](docs/dual-helix-clarification.md) — Engineering vs. Governance

### The Workflow Pattern (From DIVA Case Study)

**1. Institutional Memory Setup**

- Structure: Tiered `.cursor/rules/` configuration
- Result: 100% consistency, 87% token efficiency

**2. Plan-First Discipline**

- Create plan document before implementation
- No coding without approved plan
- Capture lessons in summaries

**3. Multi-Model Orchestration**

- Use right model for each task
- Balance: complexity, privacy, speed, cost

**4. Documentation as Workflow**

- Before: Plan
- During: Comment
- After: Summary
- Always: Update indexes

**5. Bounded Autonomy**

- Clear boundaries on what agent can/cannot do
- Approval gates for significant changes
- Build trust gradually

**Full details:** [Agentic Collaboration Guide](docs/agentic-collaboration-guide.md)

---

## 📝 Documentation Contributions

### For Quick Fixes (Traditional Method OK)

Small contributions like typos, link fixes, minor clarifications:

1. Fork repository
2. Make changes
3. Submit PR

**No special requirements** for minor documentation fixes.

### For Substantial Documentation (Agentic Method Required)

Significant documentation (new guides, major sections, comprehensive updates):

1. **Use AI agent** to draft content
2. **Follow framework principles** (see [Framework Foundations](docs/framework-foundations.md))
3. **Cite sources** when referencing existing docs
4. **Update metadata** (meta/directory-index.yaml, meta/search-manifest.json)
5. **Cross-reference** appropriately

---

## 🔬 Research Collaboration

### Case Study Submissions

**Most Valuable Contribution:** Apply the framework to your domain and share results!

**Process:**

1. **Apply framework** to your project (GIS, education, healthcare, IT ops, etc.)
2. **Document systematically** following our methodology
3. **Measure outcomes** (metrics, evidence, validation)
4. **Write case study** using template (see [Case Studies README](docs/case-studies/README.md))
5. **Submit PR** (see [PR Template](.github/PULL_REQUEST_TEMPLATE.md))

**What We're Looking For:**

| Domain | Example Applications | Framework Stage |
|--------|---------------------|-----------------|
| **GIS / Environmental** | Data annotation, anomaly detection | Any stage |
| **Digital Libraries** | Metadata repair, catalog enrichment | Any stage |
| **Education** | Teaching assistants, research support | Any stage |
| **IT Operations** | Log analysis, system automation | Any stage |
| **Healthcare** | Clinical decision support, documentation | Any stage |
| **Other** | Your innovative application! | Any stage |

**Requirements:**

- ✅ Real production or pilot deployment (not just theoretical)
- ✅ Quantitative metrics and evidence
- ✅ Framework stages clearly documented
- ✅ Used AI-agent-enabled workflow

**Co-Authorship:** Substantial case study contributions are eligible for co-authorship on research papers. See [Case Studies README](docs/case-studies/README.md) for policy.

---

## 🛠️ Code & Tool Contributions

### Framework Implementation Tools

We welcome contributions of:

- Context capture utilities
- Documentation generation tools
- Indexing and metadata frameworks
- RAG pipeline implementations
- Fine-tuning scripts and datasets
- Evaluation benchmarks

**Standards:**

- Follow language conventions (PEP 8 for Python, etc.)
- Include tests and documentation
- Provide usage examples
- Update relevant docs

### Quality Requirements

**All code contributions must:**

- ✅ Include docstrings/comments
- ✅ Pass existing tests
- ✅ Add new tests for new features
- ✅ Update documentation
- ✅ Follow project structure
- ✅ Be generated/reviewed with AI agent assistance

**Why AI agent requirement?**  
At 10k+ LoC/day velocity, manually-written code will create bottlenecks and slow the project. We need contributors who work at agentic pace.

---

## 📐 Commit Message Convention

Use conventional commit format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**

- `feat:` — New feature
- `docs:` — Documentation changes
- `fix:` — Bug fix
- `refactor:` — Code refactoring
- `test:` — Adding or updating tests
- `chore:` — Maintenance tasks
- `research:` — Research findings, case studies

**Examples:**

```bash
feat(rag): add PostgreSQL + pgvector integration
docs(case-study): add healthcare AI agent case study
research(validation): DIVA case study extraction and analysis
```

---

## 🏆 Attribution & Recognition

### How You'll Be Credited

**All Contributors:**

- ✅ Listed in [CONTRIBUTORS.md](CONTRIBUTORS.md)
- ✅ Git commit history (permanent attribution)
- ✅ Mentioned in release notes

**Case Study Contributors:**

- ✅ Byline on case study document
- ✅ Author credit in academic papers featuring your work
- ✅ Co-authorship on integrative papers (substantial contributions)
- ✅ Recognition on project website

**Core Team Members:**

- ✅ Listed as core contributor
- ✅ Co-authorship on framework papers
- ✅ Speaking opportunities at conferences

### Co-Authorship Policy

**Case Study Papers:**

- Primary author: Case study contributor
- Co-author: Framework creator (Dr. Guan)
- Additional authors: Other collaborators (by contribution level)

**Integrative Papers:**

- Primary author: Framework creator
- Co-authors: Case study contributors (by significance)

**Framework Papers:**

- By invitation for sustained framework development

**Full policy:** See [Case Studies README](docs/case-studies/README.md)

---

## ✅ Quality Standards

### For Case Studies

**Minimum Requirements:**

- [ ] Applied framework to real project
- [ ] Documented current framework stage (0-4)
- [ ] Provided quantitative metrics
- [ ] Evidence of production/pilot deployment
- [ ] Used AI-agent-enabled workflow
- [ ] Followed case study template

**Quality Indicators:**

- Clear domain context and motivation
- Systematic framework application
- Measurable outcomes with evidence
- Lessons learned and recommendations
- Reproducible methodology

### For Documentation

**Standards:**

- Professional tone matching existing docs
- Proper markdown formatting
- Working cross-references and links
- Citations where appropriate
- Examples and practical guidance

### For Code

**Standards:**

- Language-specific conventions
- Comprehensive documentation
- Test coverage
- Error handling
- Clean, maintainable code

---

## 🔍 Review Process

### Case Study Review (Agent-Assisted)

**Process:**

1. Submit PR using [template](.github/PULL_REQUEST_TEMPLATE.md)
2. Automated checks run (linting, link validation)
3. **AI-agent-assisted review** by core team
   - Verify framework application
   - Check metrics and evidence
   - Validate methodology
   - Assess quality and completeness
4. Feedback provided (usually within 1 week)
5. Iterate based on feedback
6. Approval and merge

**Why agent-assisted review?**  
At high contribution velocity, human-only review would create bottlenecks. Agents check technical aspects; humans verify research quality and alignment.

### Documentation Review

Similar process with focus on:

- Accuracy and clarity
- Consistency with existing docs
- Proper integration (metadata, cross-refs)

### Code Review

Standard practices with AI assistance for:

- Style and convention checks
- Common bug patterns
- Security considerations
- Documentation completeness

---

## 💬 Communication Channels

### GitHub Discussions

- Questions about the framework
- Ideas and proposals
- Community discussions

### GitHub Issues

- Bug reports
- Feature requests
- Documentation improvements
- Specific tasks

### Direct Contact

- **Email:** <bguan@fiu.edu>
- **Use for:** Collaboration proposals, sensitive topics, partnership inquiries

---

## 🎓 For Academic Researchers

### Collaboration Opportunities

We're actively seeking academic partnerships for:

1. **Multi-Domain Validation**
   - Apply framework to your research domain
   - Co-author papers on domain-specific findings
   - Share datasets and methodologies

2. **Theoretical Extensions**
   - Formalize framework components
   - Connect to formal verification approaches
   - Establish evaluation metrics

3. **Tool Development**
   - Build open-source implementations
   - Create benchmarks and datasets
   - Develop evaluation frameworks

4. **Educational Materials**
   - Course modules and curricula
   - Tutorials and workshops
   - Teaching case studies

**Contact:** <bguan@fiu.edu> with "Research Collaboration" in subject

---

## 🏢 For Industry Partners

### Pilot Programs

**We welcome industry validation:**

- Apply framework to your agentic AI projects
- Share results and feedback
- Contribute domain-specific patterns
- Co-develop production tools

**Benefits:**

- Early access to validated patterns
- Co-authorship on joint publications
- Framework optimization for your needs
- Open-source tooling development

**Contact:** <bguan@fiu.edu> with "Industry Partnership" in subject

---

## 📋 Before You Start

### Essential Reading (Priority Order)

1. **[README.md](README.md)** — Project overview and mission (5 min)
2. **[Framework Foundations](docs/framework-foundations.md)** — Theoretical basis (30 min)
3. **[Agentic Collaboration Guide](docs/agentic-collaboration-guide.md)** — **How to work at AI-augmented velocity** (45 min)
4. **[Research Problems & Positioning](docs/research-problems-and-positioning.md)** — Academic context (20 min)
5. **[DIVA Case Study](docs/case-studies/dataverse-diva.md)** — Example application (15 min)

**Total reading time:** ~2 hours (essential for meaningful contribution)

### Quick Start for Case Study Contributors

1. **Read:** [Agentic Collaboration Guide](docs/agentic-collaboration-guide.md)
2. **Set up:** Cursor IDE or AI-enabled environment — use **[Cursor Quick-Start Guide](docs/cursor-quickstart-for-contributors.md)** for ready prompts! ⚡
3. **Apply:** Framework to your project
4. **Document:** Using case study template
5. **Submit:** PR with completed case study

**Timeline:** 2-4 weeks for typical case study development

---

## ⚠️ Important Notes

### AI-Augmented Collaboration Requirement

**For case study contributions and framework development:**

This project operates at **AI-augmented velocity** (10,000+ lines of code and 30+ documents per day using AI agents like DIVA).

**This means:**

- Traditional contribution methods (manual coding, conventional workflows) **cannot keep pace**
- Contributors must use AI-agent-enabled workflows (Cursor, Claude, GPT-powered IDEs)
- Reviews are agent-assisted for efficiency
- Documentation is generated at high velocity

**If you're new to agentic workflows:**  
Start with [Agentic Collaboration Guide](docs/agentic-collaboration-guide.md) to learn the methodology.

### For Quick Contributions

**Minor documentation fixes, typos, link corrections:**  
Traditional contribution methods are perfectly fine! Fork, fix, PR.

---

## 🎯 What Makes a Great Contribution

### Excellent Case Study

- ✅ Real production or pilot deployment
- ✅ Clear framework stage identification (0-4)
- ✅ Quantitative metrics with evidence
- ✅ Novel domain insights
- ✅ Reproducible methodology
- ✅ Lessons learned documented
- ✅ Comparison to baseline (before/after)

**Example:** [DIVA Case Study](docs/case-studies/dataverse-diva.md) — Sets the standard

### Excellent Documentation

- ✅ Fills an identified gap
- ✅ Clear, well-structured
- ✅ Practical examples included
- ✅ Consistent with existing style
- ✅ Properly cross-referenced
- ✅ Adds genuine value

### Excellent Code

- ✅ Solves real framework need
- ✅ Well-documented and tested
- ✅ Follows project conventions
- ✅ Includes usage examples
- ✅ Integrates cleanly

---

## 🤝 Code of Conduct

### Our Pledge

We are committed to providing a welcoming, inclusive environment for all contributors, regardless of:

- Experience level
- Background
- Identity
- Perspective
- Contribution size

### Expected Behavior

- ✅ Be respectful and considerate
- ✅ Welcome diverse viewpoints
- ✅ Accept constructive criticism gracefully
- ✅ Focus on what's best for the community
- ✅ Show empathy towards others
- ✅ Cite and credit others' work appropriately

### Unacceptable Behavior

- ❌ Harassment or discriminatory language
- ❌ Personal attacks or trolling
- ❌ Publishing others' private information
- ❌ Unethical or unprofessional conduct
- ❌ Plagiarism or false attribution

### Enforcement

Instances of unacceptable behavior may be reported to <bguan@fiu.edu>. All complaints will be reviewed and investigated promptly and fairly.

---

## 📄 License

By contributing, you agree that your contributions will be licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)**.

**What this means:**

- ✅ Your work will be credited
- ✅ Others can build on it (with attribution)
- ✅ Non-commercial use only (protects research integrity)
- ✅ You retain copyright to your contributions

**Full license:** See [LICENSE](LICENSE)

---

## 📞 Getting Help

### Questions About Contributing?

- **General questions:** [GitHub Discussions](https://github.com/Keven1894/AgentLoom/discussions)
- **Specific issues:** [GitHub Issues](https://github.com/Keven1894/AgentLoom/issues)
- **Case study guidance:** See [Case Studies README](docs/case-studies/README.md)
- **Collaboration proposals:** Email <bguan@fiu.edu>

### Technical Support

- **Framework questions:** Read [Framework Foundations](docs/framework-foundations.md)
- **Implementation help:** See [Agentic Collaboration Guide](docs/agentic-collaboration-guide.md)
- **DIVA methodology:** Review [DIVA Case Study](docs/case-studies/dataverse-diva.md)

---

## 🎯 Summary: How to Contribute

### For Case Studies (Most Valuable)

```
Apply Framework → Document Results → Submit Case Study → Get Co-Authorship
```

**Start here:** [Case Studies README](docs/case-studies/README.md)

### For Documentation

```
Fork → Improve/Add Docs → Submit PR → Get Credited
```

**Start here:** [Framework Foundations](docs/framework-foundations.md)

### For Research Collaboration

```
Contact Dr. Guan → Discuss Partnership → Co-Develop → Co-Author Papers
```

**Contact:** <bguan@fiu.edu>

### For Quick Fixes

```
Fork → Fix → PR → Merge
```

**No special requirements!**

---

## 🌟 Make an Impact

The field of agentic AI engineering is just beginning. Your contributions—whether case studies, research insights, or practical implementations—help establish the foundation for the next generation of intelligent systems.

**Together, we're building:**

- 🎓 The theoretical foundations for reliable agentic AI
- 🛠️ Practical tools and methodologies
- 📊 Evidence-based validation across domains
- 🤝 A collaborative research community
- 📚 Educational resources for the next generation

**Thank you for helping advance the field of Agentic AI Engineering!** 🚀

---

**Questions?** Open a [GitHub Discussion](https://github.com/Keven1894/AgentLoom/discussions) or email <bguan@fiu.edu>

**Ready to contribute?** Start with the [Agentic Collaboration Guide](docs/agentic-collaboration-guide.md)!

---

**Last Updated:** November 11, 2025  
**Version:** 2.0 (Agentic Collaboration Edition)
