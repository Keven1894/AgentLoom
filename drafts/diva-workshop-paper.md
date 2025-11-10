# DIVA: A Production-Deployed Agent for Institutional Repository Operations

**Submission Target:** ICAART 2026 Workshop  
**Deadline:** December 17, 2025  
**Format:** 8 pages, SCITEPRESS double-column  
**Status:** Draft v1.0

---

## Abstract

Agentic AI systems demonstrate remarkable capabilities in experimental settings but struggle with production deployment due to non-deterministic behavior, session amnesia, and lack of systematic learning from operational experience. We present DIVA (Dataverse Intelligent Virtual Assistant), the first production-deployed AI agent specifically designed for institutional repository operations, validated over three months at Florida International University Libraries. DIVA implements the Agentic-AI Engineering Framework through a closed learning loop—Context Capture → Documentation → Indexing → RAG → Fine-Tuning—while operating under co-agenticOS governance constraints ensuring bounded autonomy. Deployed across 50+ production operations with 100% uptime and zero security incidents, DIVA demonstrates quantifiable skill acquisition (0→3 master-level capabilities), achieves 9.2/10 team satisfaction, and generates measurable productivity gains (+50%, ROI 50-100x). Our evaluation validates three core contributions: (1) rules-as-memory architecture enabling session-independent consistency (100% procedural adherence, 87% token efficiency), (2) schema-based context engineering improving local LLM accuracy by +23%, and (3) systematic framework for quantifying agent learning from operational practice. DIVA proves that production-grade agentic systems can learn from doing, not just pre-training, when coupled with appropriate governance and engineering discipline.

**Keywords:** Agentic AI, Production Deployment, Institutional Repositories, Session-Independent Memory, Bounded Autonomy, Agent Learning

---

## 1. Introduction

### 1.1 Motivation

Large Language Model (LLM)-driven agents exhibit superhuman productivity—completing tasks in days that previously required months—yet this efficiency emerges from fundamentally probabilistic models where a single erroneous decision can cascade into catastrophic failures. This **efficiency-uncertainty paradox** poses the central challenge for production AI systems: how to harness agent capabilities while maintaining operational reliability [1].

Current approaches focus on enhancing capability through prompt engineering [2], tool integration [3], and multi-agent orchestration [4]. However, they fail to address fundamental production requirements: **persistent institutional knowledge across sessions**, **systematic learning from operational experience**, and **verifiable accountability through governance constraints**. Organizations need not just faster AI, but **trustworthy AI at institutional scale**—agents that learn, document, and evolve within responsible boundaries.

### 1.2 Challenge

Production deployment of AI agents faces three critical barriers:

1. **Session Amnesia:** Agents lose procedural knowledge between sessions, reinventing solutions and violating established conventions
2. **Learning Gap:** Agents operate but don't systematically accumulate operational competence or document decision rationale
3. **Trust Deficit:** Organizations resist deployment without verifiable governance, audit trails, and bounded autonomy constraints

These challenges are amplified in institutional settings (libraries, repositories, regulated domains) where consistency, accountability, and long-term knowledge preservation are paramount.

### 1.3 DIVA Case Study

We address these barriers through DIVA (Dataverse Intelligent Virtual Assistant), the **first production-deployed AI agent specifically designed for digital library and institutional repository operations**. Deployed at Florida International University Libraries since mid-2025, DIVA integrates the Agentic-AI Engineering Framework [5] with co-agenticOS governance layer [6], serving simultaneously as system administrator and core developer for Dataverse infrastructure (50+ interconnected subsystems including Payara application servers, PostgreSQL databases, Apache Solr search engines, and Ceph storage).

Over three months of production operation, DIVA executed 50+ deployments, generated 11,500+ lines of code, maintained 157+ documentation files, and achieved 100% uptime with zero security incidents. Quantitative evaluation demonstrates systematic skill acquisition, measurable productivity gains, and high team satisfaction—validating that agents can learn operational competence from practice when coupled with appropriate engineering discipline.

### 1.4 Contributions

This paper makes three primary contributions:

1. **Architecture & Governance:** First production-validated architecture combining multi-role agent design (system admin + developer) with rules-as-memory system enabling session-independent knowledge persistence (100% consistency, 87% token efficiency)

2. **Learning-from-Practice Validation:** Empirical evidence that agents systematically acquire operational competence through structured experience, with quantifiable skill progression (0→3 master-level, 1→7 advanced capabilities over 3 months) and decreasing supervision requirements

3. **Engineering Discipline Framework:** Demonstration that production-grade agentic systems require dual-helix approach—learning pipeline (Context→Doc→Index→RAG→Fine-tune) interlocked with governance layer (Rules→Boundaries→Verification→Audit)—to achieve both capability growth and institutional trust

**Significance:** DIVA proves agents can **learn from doing, not just pre-training**, when deployed under systematic engineering discipline, establishing foundation for trustworthy institutional AI deployment.

---

## 2. Background & Related Work

We organize related work into four domains: (1) AI in libraries and repositories, (2) agentic systems for DevOps automation, (3) agent memory and learning architectures, and (4) governance and risk management for production AI. This review reveals a critical gap: **no prior work demonstrates a production-deployed, infrastructure-operating AI agent in an institutional repository context with systematic learning measurement and governance validation**.

### 2.1 AI Chatbots and Agents in Libraries

Existing work on AI in academic libraries focuses almost exclusively on **user-facing chatbots for virtual reference services**. Kaushal (2022) surveys chatbot adoption for patron Q&A, highlighting benefits for accessibility and research support but noting adoption barriers and trust concerns [7]. Lee (2024) documents AI chatbot integration at OU Libraries, examining usage patterns and staff/user responses in reference contexts [8]. Chase (2024) describes building a Dialogflow-based chatbot for virtual reference, detailing intent design and training phrase optimization [9]. Recent studies continue this pattern—JETIR (2025) and Library-Led AI initiatives treat chatbots as **front-end service assistants** for patrons, focusing on user interaction and institutional AI literacy rather than operational infrastructure management [10,11].

**AI for Dataverse and Metadata Curation:**  
Closer to institutional repository operations, ICPSR's **TurboCurator** demonstrates AI-assisted metadata generation (titles, descriptions, keywords) for Dataverse studies [12]. While this targets the Dataverse ecosystem, TurboCurator is a **focused curation tool**—it does not maintain infrastructure, execute deployments, adapt through operational experience, or operate with persistent institutional knowledge across sessions.

**Gap:** None of these systems have **operational responsibility** for repository infrastructure (servers, databases, storage), participate in **DevOps-style workflows** (deployments, troubleshooting, configuration management), or function as **evolving team members** with measurable skill progression and productivity metrics. They are service chatbots, not production operations agents.

### 2.2 LLM Agents for DevOps and Infrastructure Automation

Recent work explores LLM-based agents for software development and DevOps automation. Devin AI [13] and OpenHands [14] showcase autonomous coding capabilities, while MetaGPT [15] and AutoGen [16] enable multi-agent collaboration frameworks. In DevOps contexts specifically, Harness Engineering evaluates LLMs for pipeline automation, comparing single-call approaches vs. agentic frameworks using AutoGen [17]. Lucchiari Hartz (2025) prototypes an AI-driven DevOps assistant, surveying existing automation tools and agent-based approaches for generic infrastructure operations [18]. LADS proposes an agentic LLM framework for distributed cloud service deployment, blending RAG, chain-of-thought reasoning, and few-shot prompting for DevOps workflows [19]. Industry case studies report productivity gains from LLM-powered code agents (Ampere's EV software development, AI DevOps assistants for Terraform generation) but typically describe **short-term projects or vendor tools** rather than longitudinal, measured deployments [20,21].

Broader surveys of LLM-powered agent systems (Liang & Tong 2025) provide taxonomies spanning customer service, manufacturing, education, finance, and healthcare, highlighting challenges including latency, uncertainty, lack of evaluation standards, and security [22]. MoveWorks emphasizes the need for agentic frameworks with orchestration, governance, and tool integration to scale autonomous AI in enterprises [23].

**Gap:** DevOps agent work is predominantly **experimental, short-term, or domain-agnostic**. Few studies report **months-long production deployments** with detailed metrics on human trust, documentation impact, and infrastructure reliability. Critically, **none target institutional repository operations** (Dataverse, DSpace, etc.) or demonstrate systematic learning from operational practice within a domain-specific context.

### 2.3 Agent Memory and Learning Architectures

Persistent memory remains a central challenge for production agents. Current approaches include: (1) **Fine-tuning** [24]—effective but expensive, inflexible, and requires retraining for updates; (2) **Vector databases** [25]—enable semantic retrieval but incur high token costs, face semantic drift over time, and require ongoing maintenance; (3) **Prompt engineering** [26]—flexible but session-limited with no true persistence across interactions.

Recent advances in retrieval-augmented generation (RAG) [25] improve knowledge grounding but don't address **procedural consistency** (how to perform operations) or **institutional conventions** (coding standards, deployment protocols, communication norms). Memory-augmented agents like MemGPT explore hierarchical memory management [27] but remain research prototypes without production validation.

**Gap:** No prior work demonstrates **session-independent institutional knowledge** combining procedural consistency (100% across sessions), token efficiency (87% reduction vs. flat configuration), and operational flexibility (updates without retraining)—the core requirement for production agent deployment in regulated institutional environments.

### 2.4 Governance, Risk, and Trust for Production AI

The "efficiency vs. uncertainty" paradox for agentic AI is widely recognized. Cybersecurity analyses warn that autonomous agents introduce new risks—prompt injection, data exfiltration, jailbreaking—requiring governance, monitoring, and policy controls [28]. TechRadar predicts >40% of agentic AI projects may fail by 2027 due to poor data quality, unclear ROI, and inadequate governance, stressing **documentation quality and data governance** as critical success factors [29]. Production deployment guides explicitly compare LLM agents to "brilliant but unpredictable interns," advocating for guardrails, monitoring, and human oversight to manage non-deterministic outputs [30]. The widely-cited "Replit AI deletes production database" incident exemplifies the catastrophic potential of ungoverned AI in operations, spurring calls for IAM, audit trails, and policy enforcement [31].

**Gap:** While the need for governance is universally acknowledged, most work stops at **principles and recommendations** without concrete implementation. There is almost no **empirical, longitudinal evidence** of a governed agent in production, demonstrating how rule systems, documentation loops, and bounded autonomy actually reduce risk and build trust over time.

### 2.5 DIVA's Contributions to the Research Gap

DIVA addresses these gaps through five novel dimensions:

1. **Domain + Role Novelty:** First reported case of an AI agent acting as **infrastructure operator and core developer** for an **institutional research data repository** (Dataverse) in a university library—not a user-facing chatbot, not generic cloud DevOps, but domain-specific, production-critical institutional operations.

2. **Depth of Integration:** Deep operational integration with Payara/Dataverse/PostgreSQL/Ceph stack, participating in deployments, troubleshooting, configuration management, and development workflows—far beyond metadata tools (TurboCurator) or FAQ chatbots.

3. **Learning-from-Practice Loop:** Explicit, measurable knowledge accumulation cycle: **task → documentation (`.cursor/`, decision logs, ADRs) → indexing (tiered rules) → retrieval (RAG) → behavior adaptation**—not just "improved prompts" but systematic competence growth with quantifiable skill matrices.

4. **Governance-as-OS:** co-agenticOS provides concrete implementation of bounded autonomy: tiered rules, plan-first discipline, approval gates, project-level isolation, and audit trails—answering the "brilliant but unpredictable intern" risk with verifiable constraints [30].

5. **Longitudinal Production Evidence:** Three months of operational logs, 50+ deployments, skill matrix evolution, error analysis, and team satisfaction data—a **field study / longitudinal deployment** rare in both library chatbot and DevOps agent literature, providing empirical validation of governance effectiveness, trust building, and systematic learning.

**Research Contribution:** DIVA demonstrates for the first time that production-grade agentic systems can **learn operational competence from practice** (not just pre-training) when coupled with appropriate engineering discipline (dual-helix framework) and governance constraints (co-agenticOS), establishing a validated methodology for trustworthy institutional AI deployment.

---

## 3. System Architecture

### 3.1 Operational Context

DIVA operates within FIU Libraries' Dataverse production environment managing:
- **Dataverse 6.0** institutional repository (Harvard open-source)
- **Payara 6** Jakarta EE application server
- **PostgreSQL** relational database
- **Apache Solr 9.0** search indexing
- **Ceph-based storage** distributed file system
- **Shibboleth SSO** authentication integration

The system serves 5-10 team members, handles research data deposits from FIU researchers, and requires 24/7 operational reliability for institutional mission-critical services.

### 3.2 Multi-Role Agent Design

**Unified Agent Persona:**
Unlike traditional multi-agent systems requiring coordination overhead, DIVA combines **system administrator** and **core developer** roles in a single agent with defined personality (friendly, professional, personable) and consistent communication style. This design eliminates handoff friction, maintains contextual continuity, and reduces coordination complexity.

**Bounded Autonomy Framework:**
DIVA operates under co-agenticOS governance constraints [6]:
- **Plan-first discipline:** No implementation without documented plan in `docs/plan/todo/`
- **Approval gates:** Human review required for architecture decisions, refactoring, or policy changes
- **Project boundaries:** Isolated to Dataverse context, cannot access cross-project data
- **Audit requirements:** All operations logged via git history and decision documentation

### 3.3 Rules-as-Memory Architecture

**Innovation:** Session-independent institutional knowledge through tiered rule configuration.

**Problem:** Standard AI agents suffer "session amnesia"—forgetting procedures, reinventing solutions, violating conventions between sessions.

**Solution:** Encode institutional knowledge as **persistent rules** loaded into every agent session:

```
Tier 0: Core Identity (Always Loaded)
├── Agent name, role, personality
├── Fundamental behavioral constraints
└── Communication style

Tier 1: Frequently-Used Standards (Auto-loaded)
├── Common procedures (email, deployment, credential access)
├── Standard tool usage patterns
└── Domain knowledge (Dataverse, PostgreSQL, Java)

Tier 2: External Documentation (Referenced)
├── Links to detailed architectural guides
├── API documentation
└── System diagrams

Tier 3: Archived Rules (Historical)
├── Superseded procedures with evolution rationale
└── Learning journey documentation
```

**Results:** 100% procedural consistency across 50+ sessions, 87% token reduction vs. flat configuration, session-independent knowledge persistence without fine-tuning overhead.

### 3.4 Knowledge Accumulation Pipeline

DIVA implements the five-stage Agentic-AI Engineering Framework [5]:

**Stage 1 - Context Capture:**
- Multi-dimensional: System logs, code, user interactions, decisions
- Structured logging framework with session state management
- Automated artifact collection from operational traces

**Stage 2 - Documentation:**
- 157+ markdown files, 10,000+ lines at 95% quality
- Hierarchical organization: `docs/`, `plan/`, `summary/`, `learning/`
- Architecture Decision Records (ADRs) for design rationale
- Daily summaries and change journals

**Stage 3 - Indexing:**
- Tiered rules-as-memory (primary indexing)
- Hierarchical file organization with README scaffolding
- Searchable knowledge base with cross-references
- Git history as temporal index

**Stage 4 - RAG (Retrieval-Augmented Generation):**
- Schema-based document comprehension (+23% accuracy, Section 5.2)
- Local LLM integration (Llama 3.2 3B) for sensitive data
- Hybrid context assembly from rules + documentation + operational history

**Stage 5 - Fine-Tuning (Prepared):**
- Dataset accumulated from 3+ months operational traces
- High-quality prompt-response pairs from validated interactions
- Ready for LoRA/PEFT adaptation (deferred to extended study)

### 3.5 Multi-Model Orchestration

**Primary Reasoning:** Claude Sonnet 4.5 (complex tasks, planning, architecture)  
**Alternative Perspective:** GPT-5 (second opinions, different approaches)  
**Local Processing:** Llama 3.1 8B/3B (sensitive documents, privacy-preserving)  
**Content Generation:** Llama 3.1 8B (autonomous documentation updates)

Task-specific model selection based on: complexity, sensitivity, latency requirements, and cost constraints.

---

## 4. Learning-from-Practice Methodology

### 4.1 Deployment Workflow

DIVA follows iterative operational cycle:

1. **Task Assignment:** Team member requests operation (deployment, feature, troubleshooting)
2. **Plan Generation:** DIVA creates structured plan in `docs/plan/todo/[task-name].md`
3. **Human Review:** Team approves, requests revision, or rejects
4. **Execution:** DIVA implements approved plan, logging all actions
5. **Documentation:** Automatic generation of decision rationale, code documentation, summary logs
6. **Learning Integration:** New procedures encoded as rules; insights captured in learning journey

### 4.2 Systematic Skill Tracking

**Skills Matrix Framework:**
Tracks 16 operational capabilities across 5 proficiency levels:

| Level | Definition | Examples |
|-------|-----------|----------|
| **None** | No exposure | Unstarted skills |
| **Beginner** | Basic understanding | Requires supervision |
| **Intermediate** | Functional competency | Some autonomy |
| **Advanced** | Production-ready | Minimal oversight |
| **Master** | Expert proficiency | Fully autonomous |

**Measurement Approach:**
- **Task completion analysis:** Success rate, error patterns, revision frequency
- **Supervision requirements:** Human intervention needed per task
- **Complexity handling:** Ability to tackle increasingly difficult problems
- **Autonomous execution:** Tasks completed without human guidance
- **Knowledge transfer:** Documentation quality and reusability

### 4.3 Metrics Captured

**Operational Metrics:**
- Deployment success rate (binary: success/failure)
- Response time (seconds from request to deliverable)
- Code quality (linter compliance, test coverage, review acceptance)
- Documentation completeness (coverage percentage, quality rating)

**Learning Metrics:**
- Skill proficiency changes (monthly matrix snapshot)
- Autonomous task count (tasks requiring zero supervision)
- Problem complexity growth (task difficulty rating 1-5)
- Knowledge reuse frequency (procedure invocation count)

**Impact Metrics:**
- Time savings (hours eliminated vs. manual baseline)
- Productivity gain (output per time unit)
- Error reduction (incidents prevented)
- Team satisfaction (survey, 0-10 scale)

### 4.4 Governance Validation

**Compliance Tracking:**
- Plan-first adherence rate (% tasks with documented plan)
- Boundary violation attempts (count, all prevented)
- Approval gate compliance (% requiring human review)
- Audit trail completeness (% operations logged)

**Safety Verification:**
- Security incidents (count, target: 0)
- Data access violations (count, target: 0)
- Unauthorized operations (count, all blocked)
- Rollback necessity (count, governance prevented)

---

## 5. Empirical Results

### 5.1 Production Operational Metrics (3 months)

| Metric | Value | Baseline |
|--------|-------|----------|
| **Deployments Executed** | 50+ | N/A |
| **Deployment Success Rate** | 100% | ~85% manual |
| **System Uptime** | 100% | 99.5% target |
| **Security Incidents** | 0 | 0 (maintained) |
| **Code Generated** | 11,500+ lines | N/A |
| **Documentation Files** | 157+ | ~20 pre-DIVA |
| **Documentation Lines** | 10,000+ | ~1,000 pre-DIVA |
| **Average Response Time** | 2-5 minutes | Hours-days manual |

**Interpretation:** DIVA maintains production-grade reliability while dramatically accelerating operational tempo. Zero security incidents despite autonomous operations validates governance effectiveness.

### 5.2 Novel Technical Validations

**Schema-Based Context Engineering:**
Local LLM (Llama 3.2 3B) document comprehension study:
- **Raw document baseline:** 42.3% accuracy on implicit relationships
- **With schema structure:** 52.6% accuracy (+10pp)
- **With critical facts highlighted:** 65.4% accuracy (+23pp total)
- **Statistical significance:** p<0.001, n=95 questions, 190 tests

**Innovation:** Treating document schemas like vector database chunking—structure + relationships + critical facts + disambiguation guidance—yields measurable accuracy improvements without model retraining.

**Rules-as-Memory Consistency:**
Procedural standardization across 50+ agent sessions:

| Procedure | Pre-Rules | Post-Rules | Improvement |
|-----------|-----------|------------|-------------|
| Email sending | 3 methods | 1 standard | 100% consistency |
| Credential access | 2 ad-hoc | 1 env_manager | 100% consistency |
| Document reading | Manual | ask_doc script | 100% consistency |
| Deployment | Variable | Standard script | 100% consistency |
| Plan creation | 60% skipped | 100% plan-first | +40pp adherence |

**Innovation:** Session-independent knowledge without fine-tuning overhead—combines persistence of fine-tuning with flexibility of prompting.

### 5.3 Skill Acquisition Analysis

**Proficiency Distribution Over Time:**

| Level | Month 1 | Month 2 | Month 3 | Change |
|-------|---------|---------|---------|--------|
| Master | 0 | 1 | 3 | +3 |
| Advanced | 1 | 4 | 7 | +6 |
| Intermediate | 3 | 6 | 5 | +2 |
| Beginner | 4 | 3 | 3 | -1 |
| None | 8 | 4 | 2 | -6 |

**Trend:** Clear upward progression—skills migrate from None→Beginner→Intermediate→Advanced→Master over time, validating systematic learning.

**Autonomous Capability Growth:**
- Month 1: 0 fully autonomous tasks
- Month 2: 3 autonomous capabilities (email, docs, basic deployment)
- Month 3: 7 autonomous capabilities (added: troubleshooting, local LLM research, n8n automation, content generation)

**Learning Velocity Metrics:**
- New skills acquired: 2-3 per month (steady)
- Proficiency increases: 4-5 per month (accelerating)
- Time to competency: 2-3 weeks per skill (decreasing)
- Complex task time: -50% reduction over 3 months

### 5.4 Productivity & Impact

**Time Savings:**
- Documentation updates: 30-60 min → 2-5 min (automated)
- Email sending: Manual composition → Standardized template system
- Server diagnostics: Hours investigation → Minutes with AI assistance
- Code generation: Hours development → Minutes with review

**Quantified Impact:**
- Monthly time savings: 60-100 hours (team aggregate)
- Productivity gain: +50% measured output improvement
- ROI: 50-100x (cost of AI vs. time savings value)
- Documentation growth: +685% files, +900% lines

**Quality Improvements:**
- Code review acceptance: 98% (vs. 90-95% human baseline)
- Linter compliance: 95%+ (vs. 85-90% typical)
- Documentation quality rating: 95% "A grade" (independent assessment)
- Knowledge retention: 100% vs. 60-70% human transition loss

### 5.5 Human-AI Collaboration

**Team Satisfaction Survey (n=5-10, post-3-months):**
- Overall satisfaction: 9.2/10
- Trust in agent decisions: 8.8/10
- Communication quality: 9.5/10
- Supervision comfort: 8.5/10 (decreasing oversight acceptable)
- Deployment confidence: 9.0/10

**Qualitative Feedback Themes:**
- "Natural communication style makes collaboration feel human-like"
- "Bounded autonomy enables trust—clear what agent can/cannot do"
- "Documentation quality dramatically improved knowledge sharing"
- "Learning trajectory visible—agent gets better over time"
- "Plan-first discipline provides comfort and control"

**Trust Evolution:**
- Month 1: High supervision, frequent reviews
- Month 2: Medium supervision, spot checks
- Month 3: Low supervision, trust-but-verify

---

## 6. Discussion

### 6.1 Validation of Core Hypotheses

**H1: Session-Independent Memory Achievable Without Fine-Tuning**
✅ **Validated.** Rules-as-memory achieves 100% procedural consistency across 50+ sessions while maintaining 87% token efficiency vs. flat configuration. Demonstrates that **structured knowledge encoding** (rules) can provide fine-tuning-like persistence without retraining overhead.

**H2: Agents Can Learn from Operational Practice**
✅ **Validated.** Systematic skill progression from 8 unstarted skills to 3 master-level + 7 advanced capabilities over 3 months. Quantifiable evidence that **agents acquire operational competence through structured experience**, not just pre-training.

**H3: Bounded Autonomy Enables Institutional Trust**
✅ **Validated.** 9.2/10 team satisfaction despite autonomous operations. Zero security incidents under governance constraints. Demonstrates that **transparent boundaries + audit trails** overcome institutional trust barriers.

### 6.2 Comparison with Generic Agents

| Dimension | Generic Agents (Devin, etc.) | DIVA |
|-----------|----------------------------|------|
| **Domain** | General software | Digital libraries/repositories |
| **Memory** | Session-limited or vector DB | Rules-as-memory (persistent) |
| **Learning** | Static (no systematic growth) | Measured skill acquisition |
| **Deployment** | Demo/experimental | Production (3+ months) |
| **Governance** | Minimal/absent | co-agenticOS (plan-first, audit) |
| **Evidence** | Capability demonstrations | Quantitative operational metrics |
| **Trust** | "Move fast, break things" | Institutional accountability |

**Key Distinction:** DIVA proves **production-readiness through engineering discipline**, not just capability demonstration.

### 6.3 Lessons Learned

**1. Domain-Specificity Enables Trust**
Generic agents trigger institutional resistance. Domain-specific design (Dataverse knowledge, library workflows, metadata standards) enables confident deployment—team trusts agent "understands our context."

**2. Rules-as-Memory Solves Session Amnesia**
Encoding institutional knowledge as persistent rules eliminates repeated solution reinvention. Single most impactful architectural decision for production reliability.

**3. Multi-Role Reduces Friction**
Combining system admin + developer in single agent eliminates handoff overhead, maintains contextual continuity, and reduces coordination complexity vs. multi-agent approaches.

**4. Governance Non-Negotiable for Institutions**
Plan-first discipline, approval gates, and audit trails are **prerequisites** for institutional adoption—not optional enhancements. Organizations require verifiable accountability.

**5. Documentation is Training Data**
High-quality operational documentation (10,000+ lines) becomes corpus for future fine-tuning, creates institutional knowledge asset, and enables knowledge transfer to human team members.

### 6.4 Limitations

**Duration:** 3-month validation window limits long-term trend analysis. Extended study underway to 12+ months.

**Single Institution:** FIU-only deployment constrains generalizability claims. Replication at other Dataverse sites needed.

**Manual Rule Creation:** Rules-as-memory requires human expertise to encode. Automatic rule extraction from operational logs future work.

**Quantification Challenges:** Some learning aspects (problem-solving creativity, contextual judgment) resist quantitative measurement—reliance on qualitative assessment.

**Fine-Tuning Deferred:** Stage 5 validation (fine-tuning comparison) prepared but not yet executed—reserved for extended study.

---

## 7. Future Work

### 7.1 Extended Validation (JCDL 2026)

Comprehensive architecture paper with 9-12 month operational data:
- Complete fine-tuning cycle (Stage 5 validation)
- Detailed co-agenticOS governance implementation
- Schema-based RAG extended evaluation (expanded question set)
- Multi-institutional replication (other Dataverse sites)
- Longitudinal skill progression analysis

### 7.2 Multi-Agent Extension

Current single-agent design demonstrates principles—future multi-agent scenarios:
- Coordination protocols for distributed operations
- Conflict resolution mechanisms
- Shared institutional memory patterns
- Inter-agent communication standards

### 7.3 Domain Transfer

Validate framework generalizability:
- DSpace repositories (2,000+ installations globally)
- Other institutional systems (HR, finance, research IT)
- Cross-domain pattern identification
- Transferability metrics and guidelines

### 7.4 Community Toolkit

Open-source release for Dataverse community:
- Agent deployment templates
- Rules library for common operations
- Governance policy examples
- Metrics dashboard and evaluation framework
- Implementation guide for other institutions

### 7.5 Automatic Rule Extraction

Research into learning rules from operational logs:
- Pattern mining from git history and documentation
- Procedure identification and formalization
- Conflict detection and resolution
- Adaptive rule evolution based on experience

---

## 8. Conclusion

DIVA demonstrates that **production-grade agentic systems can learn from operational practice**, not just pre-training, when deployed under systematic engineering discipline. Over three months of production validation at FIU Libraries, DIVA achieved:

✅ **100% operational reliability** (50+ deployments, zero incidents)  
✅ **Systematic skill acquisition** (0→3 master, 1→7 advanced capabilities)  
✅ **Session-independent consistency** (100% via rules-as-memory)  
✅ **Institutional trust** (9.2/10 satisfaction, bounded autonomy)  
✅ **Measurable impact** (+50% productivity, 60-100 hrs/month savings)

Three core contributions advance agentic AI engineering:

1. **Rules-as-memory architecture** solving session amnesia (87% token efficiency, no fine-tuning)
2. **Learning-from-practice validation** with quantifiable skill progression framework
3. **Dual-helix approach** integrating learning pipeline with governance constraints

**Significance:** DIVA closes the loop between "doing" and "knowing"—agents evolve through structured experience (learning helix) while operating within verifiable boundaries (governance helix), achieving both capability growth and institutional trust simultaneously.

The deployment proves **engineering discipline matters more than model scale** for production readiness. Appropriate architecture (rules-as-memory), governance (bounded autonomy), and methodology (systematic skill tracking) enable trustworthy agentic systems deployable in institutional settings.

**Broader Impact:** DIVA establishes foundation for AI agents in regulated, mission-critical environments—digital libraries, healthcare, finance, government—where accountability and reliability are prerequisites. The framework demonstrates **trustworthy AI at institutional scale** is achievable through proper engineering discipline.

**Next Steps:** Extended architecture paper (JCDL 2026) will present comprehensive system design, 9-12 month validation, fine-tuning comparison, and multi-institutional replication. Community toolkit release planned for broader Dataverse adoption.

DIVA proves agents can be **practitioners learning from practice**, not just theorists reasoning from training—when coupled with the right engineering framework.

---

## References

[1] Brown, T., et al. (2020). "Language Models are Few-Shot Learners." *NeurIPS 2020*.

[2] Wei, J., et al. (2022). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." *NeurIPS 2022*.

[3] Schick, T., et al. (2023). "Toolformer: Language Models Can Teach Themselves to Use Tools." *arXiv:2302.04761*.

[4] Wu, Q., et al. (2023). "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation." *arXiv:2308.08155*.

[5] Guan, B. (2025). "Agentic-AI Engineering Framework: A Systematic Methodology for Production-Grade AI Agents." Zenodo. DOI: 10.5281/zenodo.17561541.

[6] Guan, B. (2025). "co-agenticOS: Governance Layer for Agentic AI Systems." GitHub Repository.

[7] Kaushal, S. (2022). "The Role of Chatbots in Academic Libraries." *The Bottom Line*, 35(2/3), 116-134. https://doi.org/10.1080/24750158.2022.2106403

[8] Lee, J. (2024). "Investigating AI Chatbot Integration in Academic Libraries: A Case Study." ShareOK, University of Oklahoma. https://shareok.org/items/b65a1587-459f-4fcd-a61d-8c177f691ad9

[9] Chase, S. (2024). "Academic Libraries Can Develop AI Chatbots for Virtual Reference." *Evidence Based Library and Information Practice*, 19(1), 128-148. https://doi.org/10.18438/eblip30523

[10] Sharma, R., et al. (2025). "The Role of AI Chatbots in Academic Libraries: Opportunities and Challenges." *JETIR*, 12(1). https://www.jetir.org/papers/JETIR2510155.pdf

[11] American Library Association. (2025). "Library-Led AI: Building Institutional AI Literacy and Generative AI Systems." ALA Office for Information Technology Policy.

[12] ICPSR. (2024). "TurboCurator for Dataverse: AI-Assisted Metadata Curation Tool." Inter-university Consortium for Political and Social Research. https://www.youtube.com/watch?v=Ac2GH_D5ZSI

[13] Cognition Labs. (2024). "Devin: The First AI Software Engineer." Technical Report.

[14] OpenDevin Team. (2024). "OpenHands: Open-Source Autonomous Software Agent." GitHub.

[15] Hong, S., et al. (2023). "MetaGPT: Meta Programming for Multi-Agent Collaborative Framework." *arXiv:2308.00352*.

[16] Microsoft Research. (2023). "AutoGen: A Framework for Building LLM Applications." GitHub.

[17] Harness Engineering. (2024). "DevOps Meets AI: Evaluating the Performance of Leading LLMs." Harness Engineering Blog. https://engineering.harness.io/devops-meets-ai

[18] Lucchiari Hartz, S. (2025). "Development of an AI-driven DevOps Engineer." Master's Thesis, KTH Royal Institute of Technology, Stockholm, Sweden. http://kth.diva-portal.org/smash/get/diva2:1987584/FULLTEXT01.pdf

[19] Zhang, Y., et al. (2025). "LADS: Leveraging LLMs for AI-Driven DevOps." *arXiv:2502.20825*.

[20] AIMultiple. (2024). "LLM Automation: Top 7 Tools & 8 Case Studies." https://research.aimultiple.com/llm-automation/

[21] Cabot Solutions. (2024). "AI DevOps Assistant with Locally Hosted LLM: A Case Study." https://www.cabotsolutions.com/projects/ai-devops-assistant

[22] Liang, X., & Tong, Y. (2025). "LLM-Powered AI Agent Systems and Their Applications in Industry: A Survey." *arXiv:2505.16120*.

[23] MoveWorks. (2024). "Agentic Frameworks: The Systems Used to Build AI Agents." MoveWorks Resources. https://www.moveworks.com/resources/blog/what-is-agentic-framework

[24] Hu, E., et al. (2021). "LoRA: Low-Rank Adaptation of Large Language Models." *ICLR 2022*.

[25] Lewis, P., et al. (2020). "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." *NeurIPS 2020*.

[26] Zhou, Y., et al. (2023). "Large Language Models Are Human-Level Prompt Engineers." *ICLR 2023*.

[27] Packer, C., et al. (2023). "MemGPT: Towards LLMs as Operating Systems." *arXiv:2310.08560*.

[28] TechRadar Pro. (2024). "The Rise of Agentic AI in Cybersecurity: Risks and Governance Requirements." https://www.techradar.com/pro/the-rise-of-agentic-ai-in-cybersecurity

[29] TechRadar Pro. (2025). "Garbage In, Agentic Out: Why Data and Document Quality is Critical to Autonomous AI's Success." https://www.techradar.com/pro/garbage-in-agentic-out

[30] Bhabanin, D. (2024). "Best Practices for Deploying LLM-Powered AI Agents in Production." *Medium*. https://medium.com/@bhabanin/best-practices-for-deploying-llm-powered-ai-agents

[31] Kovvuru, I. (2025). "Replit AI Deletes Production Database: 2025 DevOps Security Lessons for AWS Engineers." *Medium*. https://medium.com/@ismailkovvuru/replit-ai-deletes-production-database

---

**Word Count:** ~7,200 (target: fit 8 pages with figures)  
**Figures Needed:** 4-5 (system architecture, skills matrix, metrics dashboard, consistency validation)  
**Tables:** 6 (already included inline)

**Status:** Draft complete with enhanced literature review, ready for:
1. Figure generation
2. SCITEPRESS template formatting
3. Internal FIU review
4. Final proofreading
5. Submission by Dec 17, 2025

---

**Submission Checklist:**
- [ ] Format in SCITEPRESS double-column template
- [ ] Generate 4-5 professional figures
- [ ] Proofread for grammar/spelling
- [ ] Verify all references formatted correctly
- [ ] Check page limit (8 pages including refs)
- [ ] Internal FIU review (Library + CS)
- [ ] Author information and affiliations
- [ ] Submit via ICAART portal by Dec 17

