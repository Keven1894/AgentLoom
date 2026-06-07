# Dataset JSON-LD for Catalog Discoverability

**Node ID**: `knowledge:builder:dataset-jsonld-discovery`
**Type**: reference
**Category**: builder-meta
**Created**: 2026-05-18

---

## Purpose

Schema.org `Dataset` JSON-LD is the canonical way to expose machine-readable metadata about a dataset embedded in HTML. Google Dataset Search, federated FAIR registries, and academic citation tools all consume it. Embedding it correctly turns every workshop catalog from "isolated demo" into "discoverable open-web resource" with a single `<script>` block.

This knowledge node specifies WHAT to embed and WHERE; the companion behavior `behavior:builder:catalog-must-embed-dataset-jsonld` enforces it.

---

## Where it goes

Inside `<head>` (preferred) or anywhere in `<body>`:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org/",
  "@type": "Dataset",
  "name": "...",
  "description": "...",
  ...
}
</script>
```

Multiple JSON-LD blocks per page are allowed; the validator finds the first whose `@type` is `"Dataset"`.

---

## Required minimum fields

The behavior validator requires all of these:

| Field | Type | Source for D1 quake-catalog | Notes |
| --- | --- | --- | --- |
| `@context` | URI string | `"https://schema.org/"` | Must be the schema.org context |
| `@type` | string | `"Dataset"` | Must be exactly this |
| `name` | string | "Past Week USGS Earthquakes" | Human-readable title |
| `description` | string | First paragraph of `provenance` section | Min ~50 chars |
| `url` | URI | The catalog page itself | Where this Dataset is published |
| `license` | URI or string | "https://www.usa.gov/government-works" (USGS public domain) | License URL preferred |
| `creator` | object | `{"@type": "Organization", "name": "U.S. Geological Survey", "url": "..."}` | Min 1 creator |
| `distribution` | array | `[{"@type": "DataDownload", "contentUrl": "...", "encodingFormat": "application/geo+json"}]` | Min 1 download |
| `dateModified` | ISO date | UTC ISO from `dist/d1-normalized.iso.json :: metadata.generated` | When the upstream produced this |

---

## Recommended (not required) fields

The validator does NOT require these but the audit skill will flag missing ones as "recommended":

- `temporalCoverage` — e.g. `"2026-05-11/2026-05-18"` for past-week feed
- `spatialCoverage` — `Place` object with `geo` containing `GeoShape.box` (the bbox)
- `keywords` — array of topic strings
- `version` — semver or date stamp
- `citation` — formal citation string
- `isAccessibleForFree` — boolean
- `identifier` — DOI or other persistent ID

---

## Worked example (D1 quake-catalog)

```json
{
  "@context": "https://schema.org/",
  "@type": "Dataset",
  "name": "Past Week USGS Earthquakes",
  "description": "All earthquakes globally detected by USGS within the past 7 days, with magnitude, depth, location, and review status. Refreshed nightly.",
  "url": "http://127.0.0.1:8003/starter/quake-catalog/",
  "license": "https://www.usa.gov/government-works",
  "creator": {
    "@type": "Organization",
    "name": "U.S. Geological Survey",
    "url": "https://www.usgs.gov/"
  },
  "distribution": [
    {
      "@type": "DataDownload",
      "contentUrl": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson",
      "encodingFormat": "application/geo+json"
    },
    {
      "@type": "DataDownload",
      "contentUrl": "../../dist/d1-normalized.iso.json",
      "encodingFormat": "application/json",
      "description": "Normalized output (UTC ISO timestamps) produced by skill:domain:ingest-geojson-features + skill:domain:epoch-ms-to-iso"
    }
  ],
  "dateModified": "2026-05-18T03:30:31.000Z",
  "temporalCoverage": "2026-05-11/2026-05-18",
  "spatialCoverage": {
    "@type": "Place",
    "geo": {
      "@type": "GeoShape",
      "box": "-58.35 -179.47 79.73 179.89"
    }
  },
  "keywords": ["earthquakes", "seismology", "geospatial", "real-time"]
}
```

---

## Why standalone from `data-catalog-ui-storytelling`

The visible storytelling sections answer human questions. JSON-LD answers machine questions. Their consumers, lifecycles, and validators are different. A catalog might:

- Embed JSON-LD without all 8 visible sections (e.g. an API explorer with minimal HTML)
- Have all 8 sections without JSON-LD (e.g. a private/internal catalog with no need for discoverability)

Splitting them into two behaviors lets each catalog adopt the right combination.

---

## See also

- Schema.org Dataset: https://schema.org/Dataset
- Google Dataset Search guidelines: https://developers.google.com/search/docs/data-types/dataset
- `knowledge:builder:data-catalog-ui-storytelling` — the visible companion
- `behavior:builder:catalog-must-embed-dataset-jsonld` — Tier-A enforcement
