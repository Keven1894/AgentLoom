# Cursor Collaboration Rules

These rules coordinate AI assistants and human contributors working inside this repository. They are designed to preserve the Agentic-AI Engineering Framework's structure, keep metadata accurate, and maintain compliance with Zenodo and licensing requirements.

## 1. Always Consult Canonical References

Review the following before making substantive changes:

**Core Framework Documents:**

- `README.md` — primary project overview and mission.
- `docs/Agentic-AI-Research-Roadmap.md` — authoritative framework description.
- `docs/framework-foundations.md` — theoretical underpinnings and key questions.
- `docs/research-problems-and-positioning.md` — academic positioning and research gaps.
- `docs/dual-helix-clarification.md` — engineering vs. governance distinction.
- `docs/agentic-collaboration-guide.md` — complete methodology for AI-augmented collaboration.

**Collaboration & Contribution:**

- `CONTRIBUTING.md` — contribution pathways (v2.0: agentic collaboration edition).
- `CONTRIBUTORS.md` — attribution and recognition of all contributors.
- `docs/agentic-collaboration-guide.md` — complete methodology for AI-augmented collaboration.
- `docs/cursor-quickstart-for-contributors.md` — 17 copy-paste prompts for Cursor users.
- `docs/case-studies/README.md` — case study template and submission guide.
- `.github/PULL_REQUEST_TEMPLATE.md` — PR checklist for case studies.

**Project Planning:**

- `docs/Research-Timeline-2025-2027.md` — milestone and deliverable plan.

**Metadata & Navigation:**

- `meta/directory-index.yaml` — current directory layout and responsibilities.
- `meta/search-manifest.json` — file collections for retrieval-augmented systems.

When producing summaries or edits, cite the specific source document whenever possible.

## 2. Preserve Root-Level Accessibility

The following files must **remain in the repository root**:

- `CITATION.cff`
- `README.md`
- `LICENSE`
- `CONTRIBUTING.md`

Do not rename or relocate these files. They anchor Zenodo DOI integration, legal terms, and onboarding guidance.

## 3. Directory Usage Policy

- `docs/` — Published documentation and guides. Update cross-links when files move.
- `drafts/` — Pre-publication material. Flag as "draft" when quoting externally.
- `meta/` — Update manifests whenever structure or key documents change.
- `archives/` — Historical artifacts (`archives/context.log`, `archives/EDITORIAL_REVIEW_SUMMARY.md`). Treat as read-only except when adding archive metadata.
- `docs/case-studies/` — Production case studies summarizing domain evidence; ensure each references its archived source.
- `governance/` — Reserved for future co-agenticOS governance assets.
- `experiments/` — Only commit validated experiments with accompanying documentation.
- `figures/` — Store figure specifications and final exports.

Before adding new directories or large assets, record them in `meta/directory-index.yaml`.

## 4. Documentation & Metadata Expectations

- Every significant change must be reflected in both `meta/directory-index.yaml` and `meta/search-manifest.json`.
- Keep the manifests synchronized with the actual tree; stale entries are not allowed.
- When moving documents (e.g., into `docs/` or `archives/`), update all internal references (`README`, `docs`, `.cursor/rules.md`, etc.).

## 5. Editing Guidelines

- Prefer additive documentation over deletions to preserve historical context.
- Use concise, professional tone; match existing voice in each document.
- Provide quantitative evidence where relevant (metrics, timelines).
- Run linting or formatting tools appropriate for the edited language when available.
- Summaries or generated content should cite source sections (e.g., quoting lines from `docs/Agentic-AI-Research-Roadmap.md`).

## 6. Archives Handling

- Do not modify past transcripts or review summaries except to append metadata headers (date, author, reason for archive).
- Reference archived materials when explaining design rationale; do not duplicate their contents elsewhere.

## 7. Collaboration Protocol

- Record major decisions in `drafts/REVIEW_FEEDBACK_ACTION_PLAN.md` or future `decision_log/` entries when that directory is introduced.
- When adding new research assets, provide at least a short synopsis in `docs/` or `meta/`.
- Coordinate paper drafts in `drafts/`; mark version and intended venue.

## 8. Dual Repository Strategy

**CRITICAL:** This project uses **separate physical folders** for public (GitHub) and private (GitLab) work:

- **`agentic-ai-research-roadmap-github/`** (this folder) — Public repository
  - Remote: `origin` → <https://github.com/Keven1894/AgentLoom.git>
  - Content: Public documentation, framework, case studies
  - History: Private files removed (cleaned)
  - Push here: Public-ready content only

- **`agentic-ai-research-roadmap-gitlab/`** (separate folder) — Private repository
  - Remote: `gitlab` → <https://gitlab.com/keven1894/agentic-ai-research-roadmap-private.git>
  - Content: Full content including private experiments, drafts, figures
  - History: Complete with all private files
  - Push here: All work including private content

**Synchronization:**

- Manager agent handles syncing public content between folders
- Manual copying not recommended (use manager agent)

**This folder (GitHub) should NEVER contain:**

- `experiments/private/`
- `figures/private/`
- `drafts/private/`
- `private/`
- `DUAL_REPO_STRATEGY.md`
- `SETUP_COMPLETE.md`

## 9. Disallowed Actions

- Moving or renaming root metadata files.
- Deleting entries from manifest files without updating accompanying documentation.
- **Introducing proprietary or sensitive data into this public repository.**
- Overwriting archived content.
- Manually syncing between GitHub/GitLab folders (use manager agent).

---

_Last updated: 2025-11-11_
