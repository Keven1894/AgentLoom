"""bootstrap_builder_kg.py — populate the 3 builder-KG files with the 15 meta-nodes.

Idempotent: if a node id already exists in the target graph, it is skipped (not
duplicated, not overwritten).

Adds:
  - 6 knowledge nodes -> builder-knowledge-graph.json (key: nodes)
  - 5 skill nodes     -> builder-skills-graph.json    (key: skills)
  - 4 behavior nodes  -> builder-behaviors-graph.json (key: behaviors)
  - 3 root nodes (one per graph) for parent links

Run from repo root: python scripts/kg/bootstrap_builder_kg.py
"""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
KG_DIR = WORKSPACE / "agents" / "knowledge-graphs"

TODAY = date.today().isoformat()

# ---------------------------------------------------------------------------
# Roots
# ---------------------------------------------------------------------------
KNOWLEDGE_ROOT = {
    "id": "knowledge:builder:root",
    "type": "root",
    "data": {
        "title": "Builder Knowledge Root",
        "description": "Root of the builder-role meta-knowledge tree.",
        "category": "builder-meta",
    },
    "relationships": {
        "parent": None,
        "children": [],
    },
}

SKILLS_ROOT = {
    "id": "skill:builder:root",
    "type": "root",
    "name": "Builder Skills Root",
    "category": "builder-meta",
    "description": "Root of the builder-role skills tree.",
}

BEHAVIORS_ROOT = {
    "id": "behavior:builder:root",
    "type": "root",
    "name": "Builder Behaviors Root",
    "category": "builder-meta",
    "description": "Root of the builder-role behaviors tree.",
}

# ---------------------------------------------------------------------------
# Knowledge nodes (6)
# ---------------------------------------------------------------------------
def _kn(slug: str, ntype: str, title: str, path: str, summary: str) -> dict:
    """Build a knowledge node in the nested data/relationships shape."""
    return {
        "id": f"knowledge:builder:{slug}",
        "type": ntype,
        "data": {
            "title": title,
            "description": summary,
            "category": "builder-meta",
            "path": path,
            "tags": ["builder", "meta"],
        },
        "relationships": {
            "parent": "knowledge:builder:root",
            "children": [],
        },
    }


KNOWLEDGE_NODES = [
    _kn("agentloom-architecture", "architecture",
        "AgentLoom Architecture",
        "docs/builder/architecture/agentloom-architecture.md",
        "3-track / 2-role / dual-helix overview of the framework."),
    _kn("kg-node-schema", "reference",
        "KG Node Schema Reference",
        "docs/builder/architecture/kg-node-schema.md",
        "Field-by-field shape of skill / knowledge / behavior nodes."),
    _kn("propose-review-protocol", "protocol",
        "Propose-Review Protocol",
        "docs/builder/protocols/propose-review-protocol.md",
        "How the agent proposes new KG nodes and how humans review them."),
    _kn("validator-authoring-guide", "guide",
        "Validator Authoring Guide",
        "docs/builder/concepts/validator-authoring-guide.md",
        "How to author a Tier-A validator in <50 LOC, with a copy-paste template."),
    _kn("kg-update-log-template", "template",
        "UPDATE_LOG Template",
        "docs/builder/protocols/kg-update-log-template.md",
        "File-naming + content templates for proposal/accept/reject/migration logs."),
    _kn("governance-tiers", "concept",
        "Governance Tiers",
        "docs/builder/governance/governance-tiers.md",
        "Tier A (hard/AST/regex) vs Tier B (test-time) vs Tier C (process); when to use each."),
]

# Wire root.children to all knowledge node ids
KNOWLEDGE_ROOT["relationships"]["children"] = [n["id"] for n in KNOWLEDGE_NODES]

# ---------------------------------------------------------------------------
# Skill nodes (5)
# ---------------------------------------------------------------------------
SKILL_NODES = [
    {
        "id": "skill:builder:propose-node",
        "type": "skill",
        "name": "Propose KG Node",
        "category": "kg-tools",
        "description": "Agent-callable; writes candidate node JSON + UPDATE_LOG to proposals/.",
        "path": "agents/skills/builder/skill-propose-node.md",
        "parent": "skill:builder:root",
        "links": {
            "uses": [
                "knowledge:builder:propose-review-protocol",
                "knowledge:builder:kg-update-log-template",
                "knowledge:builder:kg-node-schema",
            ],
        },
    },
    {
        "id": "skill:builder:validate-kg",
        "type": "skill",
        "name": "Validate KG",
        "category": "kg-tools",
        "description": "Run schema + integrity validators over all 6 active KGs.",
        "path": "agents/skills/builder/skill-validate-kg.md",
        "parent": "skill:builder:root",
        "links": {
            "uses": [
                "knowledge:builder:kg-node-schema",
                "knowledge:builder:governance-tiers",
            ],
        },
    },
    {
        "id": "skill:builder:wire-validator",
        "type": "skill",
        "name": "Wire Validator",
        "category": "kg-tools",
        "description": "Scaffold a Tier-A validator script and link it into a behavior node.",
        "path": "agents/skills/builder/skill-wire-validator.md",
        "parent": "skill:builder:root",
        "links": {
            "uses": [
                "knowledge:builder:validator-authoring-guide",
                "knowledge:builder:governance-tiers",
            ],
        },
    },
    {
        "id": "skill:builder:emit-cline",
        "type": "skill",
        "name": "Emit Cline Format",
        "category": "transpiler",
        "description": "Compile canonical KG into Cline platform-native rules + settings.",
        "path": "agents/skills/builder/skill-emit-cline.md",
        "parent": "skill:builder:root",
        "links": {
            "uses": [
                "knowledge:builder:agentloom-architecture",
                "knowledge:builder:kg-node-schema",
            ],
        },
    },
    {
        "id": "skill:builder:emit-claude-code",
        "type": "skill",
        "name": "Emit Claude Code Format",
        "category": "transpiler",
        "description": "Compile canonical KG into Claude Code .claude/skills/ + AGENTS.md + CLAUDE.md.",
        "path": "agents/skills/builder/skill-emit-claude-code.md",
        "parent": "skill:builder:root",
        "links": {
            "uses": [
                "knowledge:builder:agentloom-architecture",
                "knowledge:builder:kg-node-schema",
            ],
        },
    },
]

# ---------------------------------------------------------------------------
# Behavior nodes (4) — all Tier A, all wired to validators
# ---------------------------------------------------------------------------
BEHAVIOR_NODES = [
    {
        "id": "behavior:builder:every-skill-must-have-script",
        "type": "rule",
        "name": "Every Skill Must Have a Script",
        "description": "Every type=skill node has a non-empty path that resolves on disk.",
        "path": "agents/behaviors/builder/behavior-every-skill-must-have-script.md",
        "category": "kg-integrity",
        "priority": "high",
        "enforcement": "hard",
        "parent": "behavior:builder:root",
        "links": {
            "validator": ["scripts/validators/every_skill_must_have_script.py"],
            "related": ["behavior:builder:every-non-soft-behavior-has-validator"],
            "uses": [
                "knowledge:builder:kg-node-schema",
                "knowledge:builder:governance-tiers",
            ],
        },
    },
    {
        "id": "behavior:builder:every-behavior-declares-tier",
        "type": "rule",
        "name": "Every Behavior Declares an Enforcement Tier",
        "description": "Every type=rule node has 'enforcement' in {hard,test,process,soft}.",
        "path": "agents/behaviors/builder/behavior-every-behavior-declares-tier.md",
        "category": "kg-integrity",
        "priority": "high",
        "enforcement": "hard",
        "parent": "behavior:builder:root",
        "links": {
            "validator": ["scripts/validators/every_behavior_declares_tier.py"],
            "related": ["behavior:builder:every-non-soft-behavior-has-validator"],
            "uses": [
                "knowledge:builder:governance-tiers",
            ],
        },
    },
    {
        "id": "behavior:builder:every-non-soft-behavior-has-validator",
        "type": "rule",
        "name": "Every Non-Soft Behavior Has a Validator",
        "description": "Every behavior with enforcement != 'soft' has links.validator pointing to a real Python file.",
        "path": "agents/behaviors/builder/behavior-every-non-soft-behavior-has-validator.md",
        "category": "kg-integrity",
        "priority": "critical",
        "enforcement": "hard",
        "parent": "behavior:builder:root",
        "links": {
            "validator": ["scripts/validators/every_non_soft_behavior_has_validator.py"],
            "related": [
                "behavior:builder:every-behavior-declares-tier",
                "behavior:builder:every-skill-must-have-script",
            ],
            "uses": [
                "knowledge:builder:validator-authoring-guide",
                "knowledge:builder:governance-tiers",
            ],
        },
    },
    {
        "id": "behavior:builder:kg-node-ids-are-unique",
        "type": "rule",
        "name": "KG Node IDs Are Unique",
        "description": "Globally across all 6 active KGs, no two nodes share an id.",
        "path": "agents/behaviors/builder/behavior-kg-node-ids-are-unique.md",
        "category": "kg-integrity",
        "priority": "critical",
        "enforcement": "hard",
        "parent": "behavior:builder:root",
        "links": {
            "validator": ["scripts/validators/kg_node_ids_are_unique.py"],
            "uses": [
                "knowledge:builder:kg-node-schema",
            ],
        },
    },
]


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _save(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8")


def _upsert(items: list[dict], new_items: list[dict]) -> tuple[int, int]:
    """Replace by id if present, otherwise append. Returns (added, replaced)."""
    by_id = {n.get("id"): i for i, n in enumerate(items)}
    added = 0
    replaced = 0
    for n in new_items:
        if n["id"] in by_id:
            items[by_id[n["id"]]] = n
            replaced += 1
        else:
            items.append(n)
            added += 1
    return added, replaced


def populate_graph(file_path: Path, array_key: str, root_node: dict,
                   payload: list[dict]) -> tuple[int, int]:
    kg = _load(file_path)
    if array_key not in kg:
        kg[array_key] = []
    items = kg[array_key]

    added_root, replaced_root = _upsert(items, [root_node])
    added, replaced = _upsert(items, payload)

    kg.setdefault("metadata", {})["last_updated"] = TODAY
    kg["metadata"]["total_nodes"] = len(items)

    _save(file_path, kg)
    return added + added_root, replaced + replaced_root


# ---------------------------------------------------------------------------
# Domain-side roots — seed only the root nodes; the rest of the domain KG
# grows bottom-up via propose-review during Phase 2.
# ---------------------------------------------------------------------------
DOMAIN_KNOWLEDGE_ROOT = {
    "id": "knowledge:domain:root",
    "type": "root",
    "data": {
        "title": "Domain Knowledge Root",
        "description": "Root of the domain (geospatial / catalog-app) knowledge tree.",
        "category": "domain-meta",
    },
    "relationships": {"parent": None, "children": []},
}

DOMAIN_SKILLS_ROOT = {
    "id": "skill:domain:root",
    "type": "root",
    "name": "Domain Skills Root",
    "category": "domain-meta",
    "description": "Root of the domain skills tree.",
}

DOMAIN_BEHAVIORS_ROOT = {
    "id": "behavior:domain:root",
    "type": "root",
    "name": "Domain Behaviors Root",
    "category": "domain-meta",
    "description": "Root of the domain behaviors tree.",
}


def main() -> int:
    plans = [
        (KG_DIR / "builder-knowledge-graph.json", "nodes",
         KNOWLEDGE_ROOT, KNOWLEDGE_NODES),
        (KG_DIR / "builder-skills-graph.json", "skills",
         SKILLS_ROOT, SKILL_NODES),
        (KG_DIR / "builder-behaviors-graph.json", "behaviors",
         BEHAVIORS_ROOT, BEHAVIOR_NODES),
        # Domain side — only roots; rest grows via propose-review
        (KG_DIR / "domain-knowledge-graph.json", "nodes",
         DOMAIN_KNOWLEDGE_ROOT, []),
        (KG_DIR / "domain-skills-graph.json", "skills",
         DOMAIN_SKILLS_ROOT, []),
        (KG_DIR / "domain-behaviors-graph.json", "behaviors",
         DOMAIN_BEHAVIORS_ROOT, []),
    ]

    total_added = 0
    total_skipped = 0
    for path, key, root, payload in plans:
        if not path.exists():
            print(f"[ERROR] target KG missing: {path.relative_to(WORKSPACE)}")
            return 2
        added, replaced = populate_graph(path, key, root, payload)
        print(f"  {path.name}: +{added} added, {replaced} replaced (upsert)")
        total_added += added
        total_skipped += replaced

    print(f"\nDone. Added {total_added} node(s); replaced {total_skipped} "
          f"existing (upsert mode).")
    print("Next: run `python scripts/kg/validate_all.py` and the per-behavior "
          "validators in scripts/validators/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
