# AgentLoom Figure Specs

Reproducible figure specifications. Generated PNGs live in `docs/assets/figures/`.

**Source of truth for generation:**  
`C:/projects/professional-figure-generator/examples/agentloom/`

**Regenerate:**

```bash
cd C:/projects/professional-figure-generator
python -m figgen.cli generate examples/agentloom/<id>/figure.yaml --quality medium
bash examples/agentloom/copy-to-agentloom.sh
```

## Catalog

| ID | Spec dir | PNG output |
|----|----------|------------|
| G01 | `g01-og-social-card/` | `docs/assets/figures/og-image.png` |
| G02 | `g02-dual-helix-simplified/` | `g02-dual-helix.png` |
| G03 | `g03-v3-architecture/` | `g03-v3-architecture.png` |
| G04 | `g04-builder-domain-roles/` | `g04-builder-domain.png` |
| G05 | `g05-workshop-quickstart/` | `g05-workshop-quickstart.png` |
| G06 | `g06-memory-hierarchy/` | `g06-memory-hierarchy.png` |
| G07 | `g07-ecosystem-publication/` | `g07-ecosystem.png` |
| G07b | `g07b-propose-review-publication/` | `g07b-propose-review.png` |
| G08 | `g08-authoring-vs-runtime/` | `g08-authoring-vs-runtime.png` |
| G09 | `g09-runtime-memory-layers/` | `g09-runtime-memory.png` |
| G10 | `g10-co-agenticOS-governance-helix/` | `g10-co-agenticOS-helix.png` |
| M01 | `m01-agent-memory-stack/` | `m01-memory-stack.png` |
| M02 | `m02-kg-topology/` | `m02-kg-topology.png` |
| M03 | `m03-retrieval-routing/` | `m03-retrieval-routing.png` |
| M04 | `m04-mutation-lifecycle/` | `m04-mutation-lifecycle.png` |

Legacy hand SVGs remain in `docs/assets/` for lightweight Pages embed.

See also `Agentic-AI-Research-Roadmap/research/figures/` for dual-helix and memory-hierarchy research specs.
