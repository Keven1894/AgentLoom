# Data-Catalog UI Storytelling

**Node ID**: `knowledge:builder:data-catalog-ui-storytelling`
**Type**: concept
**Category**: builder-meta
**Created**: 2026-05-18

---

## Why this exists

Workshop attendees and the framework's own reference apps repeatedly ship catalog UIs that show data without telling the story behind it. A "pretty map" with no provenance is a museum exhibit with no plaque — visually pleasant, evidentially worthless. This knowledge node fixes that pattern at the framework level by canonizing the eight sections every catalog UI must contain.

The companion behavior `behavior:builder:catalog-ui-must-tell-the-story` enforces this taxonomy as a Tier-A check.

---

## The 8 required sections

Every `starter/<app>/index.html` must contain eight `<section>` elements (or any block-level element), each carrying a `data-catalog-role="<marker>"` attribute, in this order:

| # | `data-catalog-role` | Question answered | Required content (minimum) |
| --- | --- | --- | --- |
| 1 | `title` | What is this catalog? | App title (`<h1>` or equivalent), one-sentence summary |
| 2 | `provenance` | Where is the data from? | Source organization, original feed URL, license name + link, last upstream update date |
| 3 | `acquisition` | How was it obtained? | Skill chain that fetched it (e.g. `skill:domain:ingest-geojson-features`), parameters, our local fetch timestamp (UTC ISO) |
| 4 | `data-shape` | What's inside? | Feature count, bounding box (or "global"), temporal coverage, per-record schema sketch (key fields + types) |
| 5 | `processing` | What was applied? | Ordered list of transforms (skill ids) in the order they ran, each linking to its skill MD or visualizer node |
| 6 | `kg-link` | Which framework pieces back this? | Hyperlinks to the dashboard's Graph / Proposals / Timeline tabs; list of skill / knowledge / behavior IDs implementing this catalog |
| 7 | `reuse` | How can someone reuse this? | Citation snippet (BibTeX or APA), license badge, contact, "remix in your project" instructions |
| 8 | `data-view` | The actual data | The map, chart, table, or whatever payload visualization the catalog provides |

A `<section data-catalog-role="provenance">` may visually appear anywhere on the page; the enforcement is **structural** (the marker exists), not visual.

---

## Why these eight, and why not more / fewer?

Drawn from intersection of:

- **FAIR data principles** (Findable, Accessible, Interoperable, Reusable) → maps to provenance + reuse + acquisition
- **W3C PROV** (provenance) → maps to acquisition + processing
- **Schema.org `Dataset`** (machine readable) → covered separately by `knowledge:builder:dataset-jsonld-discovery`
- **AgentLoom dual-helix** → adds `kg-link` so the framework's own structure is visible to the user, not just to the agent

We did NOT include:
- License (subsumed into provenance)
- Update frequency (subsumed into provenance + acquisition)
- API endpoint (subsumed into reuse)
- Quality flags (per-feature concern, not catalog-level)

Eight is a pragmatic ceiling — fewer than this leaves real questions unanswered; more than this fragments the page and discourages compliance.

---

## Design principles

### 1. Structural before visual
The validator only checks markers exist. **You can style them however you want** — collapse panels, tabs, drawers, accordions, chat-style — as long as each section is present in the DOM at page load.

### 2. Populate from real data, not placeholders
Every required field should be sourced from:
- The KG itself (skill / knowledge / behavior IDs from `master-graph.json` and the 6 KG files)
- The ingest output's envelope (`source`, `fetched_at`, `feature_count`, `bbox`, `metadata`)
- A small per-app metadata file (e.g. `starter/<app>/catalog.json`) for citation + contact

Hardcoded `<p>TODO: provenance</p>` placeholders count as missing — the validator's HTML-pattern check rejects empty sections.

### 3. Narrative polish (Phase 5c — beyond structural compliance)

`behavior:builder:catalog-ui-must-tell-the-story` only checks that eight markers exist with minimum text length. A page can pass while a first-time viewer still cannot answer: *where is this from, what is it, how do I reuse it, and what am I looking at right now?*

Domain knowledge `knowledge:domain:story-map-must-answer-four-viewer-questions` (proposed during workshop polish) captures this **quality bar** for geospatial story-map catalogs. Populate an at-a-glance summary from loaded data where possible; keep JSON paths in acquisition/processing, not in the lead sentence.

### 4. KG-link is hyperlinkable
The `kg-link` section should produce clickable links to the dashboard at `http://127.0.0.1:8000/#proposals` etc. — so a curious user can navigate from "this map" to "the propose-review history that produced it" in one click.

### 5. Reuse must be honest
If your catalog isn't actually reusable (alpha quality, no stable URL, license unclear), the `reuse` section should say so plainly. Lying via prefilled citation strings is worse than admitting the gap.

---

## Anti-patterns

- ❌ Wrapping the map in `<section data-catalog-role="data-view">` and calling it a day with empty stub sections elsewhere
- ❌ Putting all 8 sections at the bottom in tiny gray text "for compliance"
- ❌ Rendering provenance from a hardcoded constant when the KG already has it via `master-graph.json`
- ❌ Treating `kg-link` as marketing ("powered by AgentLoom!") instead of as a clickable index into the actual KG

---

## See also

- `knowledge:builder:dataset-jsonld-discovery` — the complementary machine-readable layer
- `behavior:builder:catalog-ui-must-tell-the-story` — Tier-A enforcement
- `skill:builder:audit-catalog-ui` — developer-friendly audit tool
- Schema.org Dataset: https://schema.org/Dataset
- W3C PROV: https://www.w3.org/TR/prov-overview/
- FAIR principles: https://www.go-fair.org/fair-principles/
