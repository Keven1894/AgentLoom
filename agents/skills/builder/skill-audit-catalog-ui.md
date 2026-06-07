# Skill: Audit Catalog UI

**ID**: `skill:builder:audit-catalog-ui`
**Category**: catalog-tools
**Priority**: medium
**Created**: 2026-05-18

---

## Purpose

Developer-friendly audit tool for catalog HTML files. Runs both the visible-section check and the Schema.org Dataset JSON-LD check in one pass, prints grouped, color-coded violations with hints on how to fix each. Complements (does NOT replace) the two CI-facing Tier-A validators by giving humans actionable feedback in one command.

Workshop attendees iterating on their viewer use this skill to debug "why is my catalog failing CI?" without having to read two separate validator outputs.

---

## When to use

**Required**:
- Anytime you edit a catalog `index.html` and want to know if it still complies before pushing
- When a CI run fails on `catalog_ui_must_tell_the_story.py` or `catalog_must_embed_dataset_jsonld.py` and you want a unified diagnostic

**Not required**:
- For CI itself — CI runs the two underlying validators directly. This skill is for humans.

---

## How to run

```bash
# Audit one file
python scripts/builder/audit_catalog_ui.py --file starter/quake-catalog/index.html

# Audit all catalog apps
python scripts/builder/audit_catalog_ui.py
# (defaults to starter/*/index.html)

# Show recommended-but-not-required JSON-LD fields too
python scripts/builder/audit_catalog_ui.py --strict
```

Exit code:
- `0` — all checks passed (file is workshop-grade)
- `1` — at least one required check failed
- `2` — internal error (file unreadable, etc.)

---

## Output shape

```
=== starter/quake-catalog/index.html ===

Visible sections (8 required):
  ✓ title
  ✗ provenance     — section missing. Add: <section data-catalog-role="provenance">…</section>
  ✗ acquisition    — section missing.
  ✗ data-shape     — section missing.
  ✗ processing     — section missing.
  ✗ kg-link        — section missing.
  ✗ reuse          — section missing.
  ✓ data-view

Schema.org Dataset JSON-LD:
  ✗ no <script type="application/ld+json"> block found.
    Required fields: @context, @type, name, description, url, license, creator,
                     distribution, dateModified.

Summary: 7 violations. See:
  - knowledge:builder:data-catalog-ui-storytelling
  - knowledge:builder:dataset-jsonld-discovery
```

---

## What it does NOT do

- Generate the missing sections for you (use `skill:builder:scaffold-catalog-ui` once it exists, currently a stub)
- Validate that section CONTENT is correct (only structural marker presence)
- Run a headless browser — purely static HTML parsing
- Modify files (read-only audit)

---

## Implements behaviors

- `behavior:builder:every-skill-must-have-script` — `path` resolves to `scripts/builder/audit_catalog_ui.py`

## Uses knowledge

- `knowledge:builder:data-catalog-ui-storytelling` — defines the 8 sections to check
- `knowledge:builder:dataset-jsonld-discovery` — defines the JSON-LD requirements

## Composes with

- `behavior:builder:catalog-ui-must-tell-the-story` (Tier-A validator runs the same logic in CI)
- `behavior:builder:catalog-must-embed-dataset-jsonld` (Tier-A validator runs the same logic in CI)
