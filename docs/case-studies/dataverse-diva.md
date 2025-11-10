# Dataverse DIVA Case Study

**Domain:** Digital Libraries & Institutional Repositories  
**Source Project:** FIU Dataverse — Dataverse Intelligent Virtual Assistant (DIVA)  
**Extraction Date:** 2025-11-10 (see archived `inputRAW/digital-library-domain/dataverse-diva/`)  
**Status:** Production system, 3+ months continuous operation  
**Primary Contact:** Dr. Boyuan (Keven) Guan (bguan@fiu.edu)

---

## Executive Summary

DIVA is the first production-validated AI agent engineered specifically for managing institutional repository platforms. Operating as both a **virtual system administrator** and **core developer** for FIU’s Dataverse installation, DIVA documents and executes end-to-end workflows, demonstrating the Agentic-AI Engineering Framework in a high-stakes, compliance-heavy environment.

**Key takeaways:**
- **Domain specialization:** No documented competitors in digital library operations; addresses a 70+ installation Dataverse community.
- **Framework validation:** Confirms Context → Documentation → Indexing → RAG stages with 157+ docs, 11,500+ LoC, and fully indexed knowledge stores.
- **Institutional memory:** Rules-as-memory paradigm yields 100% procedural consistency across 50+ sessions with 87% token savings.
- **Schema-based context engineering:** Novel “schema-as-chunking” approach improves implicit relationship accuracy by **+23 pp** for Llama 3.2 3B.
- **Production metrics:** 52.6% accuracy for local 3B models on 95-question comprehension suite, 100% reliability across 190 tests, 0 security incidents.

---

## Alignment with Agentic-AI Engineering Framework

| Stage | Evidence from DIVA | Research Implication |
|-------|-------------------|----------------------|
| **Context Capture** | Automated logging across server ops, deployments, emails, documentation (157+ files, 10k+ lines) | Confirms feasibility of comprehensive multi-modal capture in legacy enterprise systems. |
| **Documentation** | Structured learning journey, skills matrix, lessons learned, ADR-style decisions | Demonstrates documentation not as overhead but as institutional knowledge base feeding later stages. |
| **Indexing** | Hierarchical, searchable repositories with tiered `.cursor` rule sets and schema catalogs | Provides blueprint for hybrid indexing without dedicated vector DB, ready for governance reuse. |
| **RAG** | `ask_doc.py` command-line retrieval using schema-enriched prompts for local LLMs | Validates retrieval grounding on small models when combined with schema metadata. |
| **Fine-Tuning** | Curated, validated transcript corpus prepared; data volume sufficient for LoRA run | Highlights near-term opportunity for small-model fine-tuning using production traces. |

---

## Research Streams and Findings

### 1. Local Small LLM Evaluation
- **Question scope:** 95-question benchmark over `.env` configuration; 190 trials.
- **Models:** Llama 3.2 1B vs 3B running locally via Ollama.
- **Results:** 3B model reaches **52.6%** overall accuracy (+47% vs 1B); handles explicit credentials at **100%** accuracy, uncovering censorship behaviour in 1B model.
- **Innovation:** Schema-as-chunking template (structure, relationships, critical facts, ambiguities) lifts implicit relationship accuracy from **42.3% → 65.4%** (+23 pp).
- **Actionable output:** Publication-ready dataset and methodology for ACL/EMNLP style venues; demonstrates privacy-preserving alternative to cloud RAG.

### 2. Institutional Memory System
- **Technique:** Tiered `.cursor/rules` configuration (core identity → standards → external docs → archives).
- **Outcome:** 100% consistency across 50+ sessions, **87% token reduction**, session-independent onboarding for new agent instances.
- **Research angle:** Supports AI governance claims—rules-as-memory becomes enforceable boundary within co-agenticOS.

### 3. Domain-Specific Agent Architecture
- **Roles:** Single agent responsibly handles system administration, application development, and operations (email, documentation).
- **Metrics:** Team satisfaction 9.2/10, 50+ deployments with 100% success, 60–100 hours/month saved.
- **Contribution:** First documented blueprint for library/repository AI agents; ideal primary case study for JCDL 2026 submission.

### 4. Agent Learning & Evolution
- **Artifacts:** Skills matrix, session timelines, lessons learned archive.
- **Measurements:** Quantified capability progression; meta-learning documentation ready for HAI/CHI venues.
- **Gap:** Need standard rubric for competency scoring to generalise beyond DIVA—candidate for new research stream.

---

## Implications for Roadmap & Publications

| Proposed Output | Venue / Audience | Status | Required Actions |
|-----------------|------------------|--------|------------------|
| **Paper:** “Schema-Based Context Injection for Local LLMs” | ACL / EMNLP (2026 cycle) | Publication-ready | Extract schema templates, anonymise `.env` variables, run statistical significance tests for additional documents. |
| **Paper:** “Institutional Memory for Session-Independent AI Agents” | AAAI / ICML (AI Systems) | Publication-ready | Formalise rules-as-memory architecture, add governance formalism, gather comparison against baseline without tiering. |
| **Paper:** “DIVA: A Domain-Specific Agent for Digital Libraries” | JCDL 2026 | Publication-ready | Build narrative around repository operations; include adoption roadmap for other libraries. |
| **Study / Poster:** “Measuring Agent Skill Acquisition in Production” | HAI / CHI | High potential | Develop standardised proficiency rubric, include longitudinal charts, gather human feedback surveys. |
| **Workshop:** “Building AI Agents for Digital Libraries” | Code4Lib / DLF | Ready | Transform design patterns and lessons into 3–4 hour curriculum with hands-on schema exercises. |

---

## Identified Gaps & Follow-up Tasks

1. **Multi-hop reasoning improvement:** Both 1B and 3B models perform at 20% accuracy on multi-step questions. → *Task:* Design decomposition prompts or evaluate 8B model to surpass 60% threshold.
2. **Ambiguity handling:** Need expanded schema fields for common ambiguity classes across Dataverse configuration files. → *Task:* Catalogue at least 10 recurring ambiguous terms with disambiguation guidance.
3. **Fine-tuning readiness:** Corpus assembled but not yet adapted for LoRA. → *Task:* Build anonymised prompt/response dataset and determine target objective (document QA vs. operations planning).
4. **Governance metrics:** Document quantitative compliance improvements (e.g., incidents avoided, rollback counts). → *Task:* Instrument logs to capture governance interventions.
5. **Competency rubric generalisation:** Current skills matrix is bespoke. → *Task:* Define cross-project agent competency taxonomy for future case comparisons.

These tasks have been added to the project TODO tracker for prioritisation.

---

## Recommendations for Repository Integration

- **Documentation:** Link this case study from `docs/Agentic-AI-Research-Roadmap.md` (Domain Application section) and from future co-agenticOS documentation to illustrate governance patterns.
- **Indexing:** Update `meta/directory-index.yaml` and `meta/search-manifest.json` to include this case study so RAG/assistants can surface it.
- **Archives:** Original extraction files archived under `archives/inputRAW/digital-library-domain/dataverse-diva/`.
- **Workshop Drafts:** Extend `drafts/workshop-paper-outline.md` with DIVA metrics (52.6% accuracy, 87% token efficiency) to strengthen evaluation section.

---

## Citation

```
Guan, B. (2025). DIVA: Dataverse Intelligent Virtual Assistant. 
Florida International University Libraries. https://dataversedev.fiu.edu/ai/
```

For reproducibility, cite this case study as:

```
Agentic-AI Research Roadmap – DIVA Case Study (2025).
```

---

_Prepared: 2025-11-09 (Agentic-AI Research Roadmap integration)_  
_Source archive: `archives/inputRAW/digital-library-domain/dataverse-diva/`_

