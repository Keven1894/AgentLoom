# 03 — Workshop Discipline (non-negotiable invariants)

These rules are framework-level, not Cline-specific. They apply to every operator and every agent host. They exist because we have already debugged each of them once and do not want to re-pay the cost.

## D1 — Paired-commit hard-launch

Every commit on `main` and every workshop branch must be **operationally green**: validators pass, pipeline produces expected output, catalog UI (if present) is storytelling-compliant. There is no "broken intermediate state" that gets fixed in a follow-up commit.

If a behavior validator is being introduced for the first time AND existing code violates it: introduce the behavior + fix the violations in the **same commit** (or a tightly-paired pair of commits where the introduction commit also adds the bootstrapping marker).

## D2 — Validators are not advisory

A behavior with `enforcement` ≥ `test` MUST link to a working validator. A rule without an enforcer is a wishlist, not a rule. If you find yourself writing prose-only behavior nodes, stop and write the validator first.

## D3 — Storytelling is required, not optional

Every catalog UI in `starter/<source>-catalog/index.html` must contain all 8 storytelling sections (`title / provenance / acquisition / data-shape / processing / kg-link / reuse / data-view`) AND embed a valid Schema.org `Dataset` JSON-LD block with the 7 required fields. Two Tier-A validators enforce this. Do not propose a catalog without checking validators green.

## D4 — Single source of truth for the system prompt

The canonical system prompt is `docs/builder/concepts/builder-agent-system-prompt.md`. Every Layer-3 host (builder-agent Python package, Cursor, Cline, future hosts) consumes it via the same BEGIN-PROMPT/END-PROMPT extraction. `.clinerules/01-builder-agent-prompt.md` is **generated**; do not hand-edit. A Tier-A validator catches drift.

## D5 — No "ground truth" framing in evaluation

When comparing model outputs, frame as **descriptive overlap** or **operational sufficiency** (validators-green pipeline). Do not call hand-authored content "ground truth." See `docs/research/agent-eval/2026-05-20-d3-rerun-gpt-5.2-vs-opus-4.7.md` for the corrected framing.

## D6 — Honest gap accounting

When implementing skills or UIs from agent-proposed KG, log every gap encountered as G-DATA / G-OUTSIDE / G-FRAMEWORK. The gap log is paper evidence; padding it or omitting awkward gaps invalidates the experiment.

## D7 — One concept per node

Composite proposals ("data shape AND units") get rejected by the human reviewer. Split. See the anti-pattern list in `01-builder-agent-prompt.md`.

## D8 — Agent never accepts its own proposals

The propose-review protocol is a two-actor protocol. Cline files via `propose_node.py`; a human runs `accept_proposal.py`. If you find Cline calling `accept_proposal.py` for a proposal it just filed, that is a serious bug — stop the session and escalate.

## D9 — Run logs survive

For workshop attendees and paper-grade reproducibility: any run that produces accepted KG nodes should leave a `runs/agent/*.kept.jsonl` file behind. Cline-driven runs save the equivalent chat transcript next to the run log.

## D10 — When in doubt, propose and let the human decide

The framework is conservative on what it auto-accepts (currently nothing). It is liberal on what it lets agents propose. If you have evidence that a node would help and you are not sure if it already exists, file the proposal — the reviewer will reject duplicates fast and the cost is small.
