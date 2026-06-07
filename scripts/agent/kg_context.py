"""KG-as-context: dump every existing node as compact id+title pairs the LLM
can consume without exhausting context window. Also extracts the
'BEGIN-PROMPT'..'END-PROMPT' span from the canonical system-prompt KG node
and exposes it as a string for the LLM client.

The LLM does NOT receive full markdown bodies of every KG node — that would
cost ~50-100 KB. Instead it receives a compact summary, with an explicit
note that it can ask for full content of any specific node (a v2 feature;
v1 keeps it one-shot for clarity of attribution in run logs).
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
KG_ROOT = WORKSPACE / "agents" / "knowledge-graphs"

KG_FILES = {
    "knowledge": ["builder-knowledge-graph.json", "domain-knowledge-graph.json"],
    "skill":     ["builder-skills-graph.json",    "domain-skills-graph.json"],
    "behavior":  ["builder-behaviors-graph.json", "domain-behaviors-graph.json"],
}

NODE_KEY_BY_GRAPH = {
    "knowledge": "nodes",
    "skill": "skills",
    "behavior": "behaviors",
}


@dataclass(frozen=True)
class NodeStub:
    id: str
    title: str
    role: str
    layer: str  # 'knowledge' | 'skill' | 'behavior'


def load_node_stubs(kg_root: Path | None = None) -> list[NodeStub]:
    """Load every node from every KG file, return a flat list of stubs."""
    root = kg_root or KG_ROOT
    out: list[NodeStub] = []
    for layer, files in KG_FILES.items():
        for fname in files:
            fpath = root / fname
            if not fpath.exists():
                continue
            data = json.loads(fpath.read_text(encoding="utf-8"))
            key = NODE_KEY_BY_GRAPH[layer]
            raw_role = (data.get("role") or "").strip()
            if raw_role.startswith("role-"):
                raw_role = raw_role[len("role-"):]
            role = raw_role or ("builder" if "builder" in fname else "domain")
            for n in data.get(key, []):
                title = (
                    n.get("title")
                    or (n.get("data") or {}).get("title")
                    or ""
                )
                out.append(NodeStub(
                    id=n.get("id", "<missing-id>"),
                    title=title,
                    role=role,
                    layer=layer,
                ))
    return out


def existing_ids(stubs: list[NodeStub]) -> set[str]:
    return {s.id for s in stubs}


def render_kg_summary(stubs: list[NodeStub]) -> str:
    """Pretty-print the KG summary block the LLM will receive."""
    lines: list[str] = []
    lines.append("CURRENT KNOWLEDGE GRAPH (do not re-propose these):")
    lines.append("")
    for layer in ("knowledge", "skill", "behavior"):
        for role in ("builder", "domain"):
            subset = [s for s in stubs if s.layer == layer and s.role == role]
            if not subset:
                continue
            lines.append(f"  {layer}/{role} ({len(subset)} nodes):")
            for s in sorted(subset, key=lambda x: x.id):
                title = s.title or "(no title)"
                lines.append(f"    - {s.id} :: {title}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


_PROMPT_BEGIN = "<!-- BEGIN-PROMPT -->"
_PROMPT_END = "<!-- END-PROMPT -->"


def load_system_prompt(prompt_path: Path | None = None) -> tuple[str, str]:
    """Load the canonical system prompt content and a short version-id.

    Returns (prompt_text, prompt_version_id). The version id is the SHA-1
    of the extracted prompt bytes, so any change to the prompt changes the
    version id pinned in run logs. Paper-grade reproducibility: a row in
    the comparison table can be re-derived against the exact prompt text
    that produced it.
    """
    import hashlib

    p = prompt_path or (
        WORKSPACE / "docs" / "builder" / "concepts" / "builder-agent-system-prompt.md"
    )
    text = p.read_text(encoding="utf-8")

    if _PROMPT_BEGIN not in text or _PROMPT_END not in text:
        raise ValueError(
            f"system prompt file {p} is missing BEGIN-PROMPT/END-PROMPT markers"
        )
    body = text.split(_PROMPT_BEGIN, 1)[1].split(_PROMPT_END, 1)[0].strip()

    sha = hashlib.sha1(body.encode("utf-8")).hexdigest()[:10]
    return body, sha


def truncate_snapshot(snapshot_path: Path, max_bytes: int = 2048) -> str:
    """Read at most max_bytes of the snapshot, return as a string with a
    truncation marker. JSON snapshots are best-effort pretty-printed for
    LLM legibility.
    """
    raw = snapshot_path.read_text(encoding="utf-8", errors="replace")
    head = raw[:max_bytes]
    truncated = len(raw) > max_bytes
    if snapshot_path.suffix in (".json", ".geojson"):
        try:
            obj = json.loads(raw)
            pretty = json.dumps(obj, indent=2, ensure_ascii=False)
            head = pretty[:max_bytes]
            truncated = len(pretty) > max_bytes
        except Exception:  # noqa: BLE001
            pass
    suffix = (
        f"\n... [truncated; full file is {len(raw):,} bytes] ..."
        if truncated
        else ""
    )
    return head + suffix
