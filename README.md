# Agentic-AI Lab — Engineering the Next Generation of Intelligent Systems

![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)
![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)
![Made with: GPT-5 · Claude 4.5 · Cursor](https://img.shields.io/badge/Made%20with-GPT--5%20·%20Claude%204.5%20·%20Cursor-blue)

**Author:** Dr. Boyuan (Keven) Guan  
**Affiliation:** FIU Library & GIS Center  
**First Public Release:** November 8, 2025  
**Version:** 1.0

---

## Mission

**The Agentic-AI Lab explores how large-language-model agents can evolve through documented, reproducible, and production-grade workflows.** The goal is to make intelligent systems learn from real-world experience as human engineers do.

## Overview

This repository documents and open-sources the foundation of the **Agentic-AI Engineering Framework**, a systematic methodology that transforms AI from theoretical reasoning to practical, production-ready systems.

While Large Language Models (LLMs) are powerful theorists, **Agents are practitioners** — operating in real environments, performing concrete tasks, and learning through trial and feedback.

## The Core Framework

Our framework implements a closed learning loop:

> **Context → Documentation → Indexing → RAG → Fine-Tuning**

Where each stage strengthens the next:
- **Context** captures the working environment and raw artifacts
- **Documentation** turns experience into reusable knowledge
- **Indexing** organizes knowledge for retrieval and reasoning
- **RAG** (Retrieval-Augmented Generation) connects AI reasoning to verified data
- **Fine-Tuning** distills accumulated experience into domain-specialized models

This transforms one-off AI experiments into **continuous, evidence-based AI systems**.

## Key Insight

**"LLM is the theorist, Agent is the practitioner."**

To bring AI from conversation to production, we must systematize how agents:
- Accumulate knowledge from real tasks
- Document their decision-making processes
- Evolve through structured feedback loops
- Persist context across interactions

## Research Vision

Establish a **repeatable, scalable, and evaluable Agentic-AI engineering framework** that integrates LLM reasoning with traditional software engineering discipline, enabling sustainable AI engineering where AI systems:
- Not only respond but **operate**
- Not only answer but **record**
- Not only reason but **evolve**

## Repository Structure

```
agentic-ai-lab/
├── README.md                          # This file
├── docs/
│   ├── Agentic-AI-Research-Roadmap.md # Complete research roadmap
│   └── Research-Timeline-2025-2027.md # Detailed timeline and milestones
├── figures/                           # Diagrams and visualizations
├── drafts/
│   └── workshop-paper-outline.md      # First workshop paper preparation
├── experiments/                       # Experimental code (to be released)
├── LICENSE                           # CC BY-NC 4.0
└── .gitignore
```

## Experimental Domains

We are validating this framework across multiple domains:

| Domain | Use Case | Expected Outcome |
|--------|----------|------------------|
| **GIS / Environmental Data** | Automatic buoy data annotation, anomaly detection (EnviStor) | Validate RAG for spatiotemporal reasoning |
| **Digital Libraries** | Metadata repair, catalog enrichment (Dataverse) | Improve retrieval precision |
| **Education** | AI teaching assistants, research support | Demonstrate adaptive learning |
| **IT Operations** | Log analysis, system self-healing | Evaluate feedback loops |
| **Industry Applications** | Multi-agent coordination (Virtual Guard) | Measure operational reliability |

## Engineering Framework

Based on the **Agentic-Dev Workflow**:

```
Plan → Implement → Verify → Document → Summarize → Iterate
```

**Core Elements:**
- `.cursor/rules.md` — Context-aware AI editing policy
- `decision_log/` — Persistent design rationale
- `daily/` — Auto-summaries of activity and changes
- **CI/CD + Changesets** — Continuous integration with changelog tracking
- **Documentation Site** — Public transparency and collaboration

## Collaboration

We welcome collaborations with:
- **Academic Institutions** — Research validation and datasets
- **Industry Partners** — Real-world deployment and feedback
- **Open Source Community** — Tools, benchmarks, and standards

**Current Partners:**
- FIU Library & GIS Center (lead)
- FIU Computer Science Department
- FIU Division of IT
- Pelican, OSG, and other research infrastructure partners

## Publications & Roadmap

**Stage 1 (2025 Q4):** Framework workshop paper  
**Stage 2 (2026 Q1-Q3):** Domain-specific case studies  
**Stage 3 (2026 Q4):** Integrative system paper  
**Stage 4 (2027):** Monograph and curriculum development

See [Research Timeline](docs/Research-Timeline-2025-2027.md) for detailed milestones.

## Expected Outcomes

| Type | Description |
|------|-------------|
| **Software** | Open-source Agentic-Dev Workflow template and toolkit |
| **Publications** | Peer-reviewed papers at PEARC, JCDL, ICSE, AI-Engineering venues |
| **Education** | Agentic-AI course modules and tutorials |
| **Datasets** | Curated agent-interaction logs for research use |
| **Industry Pilots** | Operational agents in production systems |

## Citation

If you reference this framework or methodology, please cite:

```bibtex
@misc{guan2025agenticai,
  author = {Guan, Boyuan (Keven)},
  title = {Agentic-AI Lab: Engineering the Next Generation of Intelligent Systems},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/Keven1894/Agentic-AI-Research-Roadmap}},
  note = {First released: November 8, 2025}
}
```

## Contact

**Dr. Boyuan (Keven) Guan**  
Lead Developer & Research Engineer  
FIU Library & GIS Center  
📧 bguan@fiu.edu  
🌐 https://dataversedev.fiu.edu/ai/

---

## License

© 2025 Dr. Boyuan (Keven) Guan, FIU Library & GIS Center

This work is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](http://creativecommons.org/licenses/by-nc/4.0/).

You are free to:
- **Share** — copy and redistribute the material
- **Adapt** — remix, transform, and build upon the material

Under the following terms:
- **Attribution** — You must give appropriate credit
- **NonCommercial** — You may not use the material for commercial purposes

---

*This repository is a living research project. Contributions, collaborations, and feedback are welcome.*

**Last Updated:** November 8, 2025

