# Agentic-AI Research Direction & Collaboration Roadmap

**Author:** Dr. Boyuan (Keven) Guan  
**Affiliation:** FIU Library & GIS Center  
**Date:** November 2025  
**Version:** Draft v1.0

**Keywords:** Agentic AI, AI Engineering, LLMOps, Retrieval-Augmented Generation, Knowledge Systems, Production AI, Agent Memory, Context Persistence

---

## Abstract

As LLMs enter production, engineering discipline—not model scale—becomes the limiting factor. Large Language Models (LLMs) demonstrate remarkable reasoning capabilities but face significant challenges when deployed in production environments due to uncertainty, inconsistency, and lack of context persistence. This proposal introduces the Agentic-AI Engineering Framework, a systematic methodology that transforms AI from theoretical reasoning to practical, production-ready systems through a closed learning loop: Context → Documentation → Indexing → RAG → Fine-Tuning. We validate this framework across multiple domains including GIS/environmental data, digital libraries, education, and IT operations, demonstrating how structured experience accumulation enables sustainable AI engineering.

---

## 1. Background & Motivation

Large Language Models (LLMs) are powerful theorists — capable of reasoning, explanation, and synthesis. Yet, when applied to real production tasks, they often reveal uncertainty, inconsistency, and lack of context persistence.

By contrast, **Agents are practitioners**.  
They operate in concrete environments, perform tasks, and learn through trial and feedback. Each agent interaction generates *operational traces* — logs, decisions, and artifacts — that encode real-world knowledge far richer than abstract corpora.

To bring AI from "conversation" to "production," we must systematize how agents accumulate, document, and evolve knowledge over time.

### The Core Problem

Current LLM deployment faces three critical challenges:

1. **Uncertainty**: LLM outputs are non-deterministic and context-dependent
2. **Lack of Persistence**: Knowledge doesn't accumulate across interactions
3. **Poor Operationalization**: No systematic way to turn AI experiments into production systems

### Our Approach

We propose treating AI development as a **knowledge engineering process** rather than just a prompt engineering task. This requires:
- Systematic context capture from real tasks
- Structured documentation of decisions and rationale
- Persistent knowledge indexing and retrieval
- Continuous feedback and evolution

---

## 2. Vision

The long-term vision is to establish a **repeatable, scalable, and evaluable Agentic-AI engineering framework** that integrates LLM reasoning with traditional software engineering discipline.

We describe this as a closed learning loop:

> **Context → Documentation → Indexing → RAG → Fine-Tuning**

where each stage strengthens the next:
- *Context* captures the working environment and raw artifacts
- *Documentation* turns experience into reusable knowledge
- *Indexing* organizes it for retrieval and reasoning
- *RAG (Retrieval-Augmented Generation)* connects AI reasoning to verified data
- *Fine-Tuning* distills accumulated experience into domain-specialized models

This framework transforms one-off AI experiments into **continuous, evidence-based AI systems**.

---

## 3. Methodology Overview

### 3.1 Context Capture

Automatically collect working context — documents, logs, dataset schemas, meeting summaries — using standardized pipelines.

**Key Components:**
- API interaction logs
- System operation traces
- User interaction patterns
- Environmental state snapshots
- Task completion artifacts

**Implementation:**
- Structured logging frameworks
- Automated documentation extraction
- Session state management
- Multi-modal data capture (text, code, data)

**Deliverables:** Standardized context schema, logging utilities, session management framework

### 3.2 Documentation Layer

Adopt a *developer-oriented knowledge protocol*:
- `decision_log/` — Architecture Decision Records (ADRs)
- `daily/` — Work summaries and change journals
- `.cursor/rules.md` — Editing and collaboration policies
- MkDocs / Docusaurus — Publish living documentation sites

**Benefits:**
- Makes implicit knowledge explicit
- Enables knowledge transfer across team members
- Creates training data for future AI fine-tuning
- Supports reproducibility and debugging

**Deliverables:** ADR templates, daily log automation scripts, documentation site generator configuration

### 3.3 Indexing Layer

Use **hybrid indexing**:
- **Vector DB** (Chroma / Qdrant / Weaviate) for semantic retrieval  
- **SQL DB** for structural metadata and traceability  

This dual-index design allows both unstructured and structured queries, ensuring interpretability and reproducibility.

**Design Principles:**
- Semantic search for contextual retrieval
- Structured queries for exact fact verification
- Metadata tagging for traceability
- Version control for knowledge evolution

**Deliverables:** Hybrid indexing API, metadata schema, query optimization guidelines

### 3.4 RAG Layer

Build Retrieval-Augmented pipelines for each domain.  
The agent consults both vector memory (contextual knowledge) and traditional databases (verified facts), creating a balanced reasoning ecosystem.

**Architecture:**
```
User Query → Query Understanding → Hybrid Retrieval → 
Context Assembly → LLM Generation → Verification → Response
```

**Advantages:**
- Grounds AI responses in verified knowledge
- Reduces hallucination
- Enables citation and traceability
- Supports domain-specific reasoning

**Deliverables:** RAG pipeline implementation, retrieval evaluation metrics, domain-specific adaptations

### 3.5 Fine-Tuning Layer

When enough validated context accumulates, initiate fine-tuning or LoRA adaptation on domain data, forming lightweight specialized models.

**Approach:**
- Collect high-quality interaction traces
- Curate successful task completions
- Build domain-specific training sets
- Apply parameter-efficient fine-tuning (LoRA/PEFT)
- Evaluate against baseline models

**Deliverables:** Training data curation pipeline, fine-tuning scripts, model evaluation framework

---

## 4. Experimental Domains

### Domain Selection Rationale

Each domain provides:
1. **Real operational data** from production systems
2. **Clear success metrics** for evaluation
3. **Diverse challenges** to test framework generalizability
4. **Existing partnerships** for validation
5. **High-impact applications** for real-world benefit

### Validation Across Domains

| Domain | Use Case | Expected Outcome |
|---------|-----------|------------------|
| **GIS / Environmental Data** | Automatic buoy data annotation, anomaly detection, and reporting (EnviStor) | Validate RAG for complex spatiotemporal reasoning |
| **Digital Libraries / Dataverse** | Metadata repair, multi-language catalog enrichment | Improve retrieval precision and data interoperability |
| **Education / Research Support** | AI teaching assistants, paper summarization, topic generation | Demonstrate knowledge transfer and adaptive learning |
| **Software & IT Operations** | Log summarization, anomaly triage, auto-fix suggestions | Evaluate feedback loop for system self-healing |
| **Industry Applications (e.g., Virtual Guard)** | Multi-agent stateful WebSocket coordination | Measure operational reliability of agentic orchestration |

---

## 5. Engineering Framework

The foundation follows the **Agentic-Dev Workflow**:

```
Plan → Implement → Verify → Document → Summarize → Iterate
```

### Core Elements

- `.cursor/rules.md` — Context-aware AI editing policy  
- `decision_log/` — Persistent design rationale  
- `daily/` — Auto-summaries of activity and change history  
- **CI/CD + Changesets** — Continuous integration with changelog tracking  
- **Docsite** — Public documentation for transparency and collaboration  

This workflow enables a **self-documenting AI development loop**, aligning human engineers and AI agents under shared conventions.

### Integration with Development Tools

- **Claude / GPT-5** — AI pair programming
- **Cursor** — Context-aware code editing
- **Git** — Version control and traceability
- **MkDocs** — Documentation generation
- **GitHub Actions** — Automated testing and deployment

---

## 6. Collaboration Plan

### Lead Institution

**FIU Library & GIS Center** — Platform architecture, AI engineering, data pipelines.

### Collaborating Partners

- **FIU Computer Science** — HPC and model research support  
- **FIU DOIT** — Cloud and IT infrastructure  
- **External Partners** (Pelican, OSG, etc.) — Distributed deployment and validation environments  
- **Academic & Industry Partners** — Domain-specific datasets and evaluation

### Open Collaboration Goals

1. Co-develop "Agentic Datasets" built from real workflow traces  
2. Benchmark multi-agent task orchestration and reliability  
3. Explore open standards for agentic documentation and evaluation
4. Create educational resources and curriculum materials
5. Build open-source tools and frameworks

### Collaboration Opportunities

We are actively seeking partnerships in:
- **Domain Expertise** — Bring real-world problems and datasets
- **Technical Development** — Contribute to framework implementation
- **Evaluation & Benchmarking** — Help establish standards and metrics
- **Educational Outreach** — Co-develop teaching materials

---

## 7. Expected Outcomes

| Type | Description |
|------|--------------|
| **Software** | Open-source "Agentic-Dev Workflow" template and toolkit |
| **Publications** | Peer-reviewed papers (PEARC, JCDL, AI-Engineering venues) |
| **Education** | Agentic-AI course modules and tutorials for developers |
| **Datasets** | Curated agent-interaction logs for research use |
| **Industry Pilots** | Operational agents in Virtual Guard, EnviStor, and Beacon projects |

### Publication Strategy

**Year 1:**
- 1 framework workshop paper
- 2-3 domain case studies

**Year 2:**
- 1 integrative system paper (top-tier venue)
- 1 survey/position paper
- Educational materials

**Year 3:**
- Monograph or textbook
- Open-source toolkit release
- Community building and standards development

---

## 8. Evaluation Metrics

### Framework-Level Metrics
- **Knowledge Accumulation Rate** — How quickly does the system build useful context?
- **Retrieval Precision** — How accurate is the RAG system?
- **Task Success Rate** — How often do agents complete tasks correctly?
- **Context Persistence** — How well is knowledge retained across sessions?

### Domain-Specific Metrics
- **GIS:** Data annotation accuracy, anomaly detection F1-score
- **Libraries:** Metadata quality improvement, retrieval relevance
- **Education:** Learning outcome improvement, user satisfaction
- **IT Ops:** Mean time to resolution, false positive rate

### Process Metrics
- **Documentation Coverage** — Percentage of decisions documented
- **Code Reusability** — How often are components reused?
- **System Reliability** — Uptime and error rates
- **Development Velocity** — Speed of iteration with AI assistance

---

## 9. Long-Term Vision

Establish a **cross-domain, open-standard Agentic-AI Pipeline Framework**,  
where AI systems not only *respond* but *operate, record, and evolve* through structured experience.

Ultimately, the goal is to enable **sustainable AI engineering** —  
AI that learns from doing, improves from feedback, and documents its own reasoning as part of the production process.

### Future Directions

1. **Standardization** — Create open standards for agentic systems
2. **Tooling** — Build developer tools for agentic AI engineering
3. **Education** — Train next generation of AI engineers
4. **Community** — Foster open-source ecosystem
5. **Ethics** — Establish best practices for responsible AI agents

### Institutional Vision

FIU Library and GIS Center aim to make this framework a model for academic-industry AI collaboration, demonstrating how research institutions can lead in establishing engineering best practices for next-generation intelligent systems. By combining domain expertise, technical infrastructure, and educational mission, we can create a sustainable ecosystem where agentic AI advances both research and practice.

---

## 10. Timeline & Milestones

See [Research Timeline 2025-2027](Research-Timeline-2025-2027.md) for detailed schedule.

**Key Milestones:**
- **2025 Q4:** Framework paper submission
- **2026 Q1-Q3:** Domain case study papers
- **2026 Q4:** Integrative system paper
- **2027:** Monograph and curriculum launch

---

## 11. Contact

**Dr. Boyuan (Keven) Guan**  
Lead Developer & Research Engineer  
FIU Library & GIS Center  
📧 bguan@fiu.edu  
🌐 https://dataversedev.fiu.edu/ai/

---

*This document is a living research proposal.  
Contributions, collaborations, and feedback are welcome.*

**Version History:**
- v1.0 (November 8, 2025) — Initial public release

