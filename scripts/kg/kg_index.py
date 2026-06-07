"""kg_index.py — in-process KG + proposals index for MCP and tooling.

Read-only. Rebuilds when any agents/knowledge-graphs/*.json mtime changes.
Search uses simple token overlap (no external vector DB).
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
KG_DIR = REPO_ROOT / "agents" / "knowledge-graphs"
PROPOSALS_DIR = KG_DIR / "proposals"
DOCS_ROOT = REPO_ROOT / "docs"

KG_FILES: dict[str, tuple[Path, str]] = {
    "builder-knowledge": (KG_DIR / "builder-knowledge-graph.json", "nodes"),
    "builder-skills": (KG_DIR / "builder-skills-graph.json", "skills"),
    "builder-behaviors": (KG_DIR / "builder-behaviors-graph.json", "behaviors"),
    "domain-knowledge": (KG_DIR / "domain-knowledge-graph.json", "nodes"),
    "domain-skills": (KG_DIR / "domain-skills-graph.json", "skills"),
    "domain-behaviors": (KG_DIR / "domain-behaviors-graph.json", "behaviors"),
}


def _tokenize(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def _query_tokens(query: str) -> set[str]:
    tokens = _tokenize(query)
    if "iso" in tokens and "3166" in tokens:
        tokens.add("iso3166")
    return tokens


def _node_fields(node: dict) -> tuple[str, str, str, str]:
    """Return (id, title, description, path)."""
    nid = node.get("id", "")
    if "data" in node and isinstance(node["data"], dict):
        d = node["data"]
        title = d.get("title") or d.get("name") or nid
        desc = d.get("description") or ""
        path = d.get("path") or ""
    else:
        title = node.get("title") or node.get("name") or nid
        desc = node.get("description") or ""
        path = node.get("path") or ""
    return nid, str(title), str(desc), str(path)


def _graph_meta(source: str) -> tuple[str, str]:
    role = "builder" if source.startswith("builder") else "domain"
    track = source.split("-", 1)[1]
    return role, track


@dataclass
class IndexedNode:
    id: str
    title: str
    description: str
    path: str
    role: str
    track: str
    source: str
    node: dict
    body_text: str = ""

    def search_blob(self) -> str:
        return " ".join([self.id, self.title, self.description, self.body_text])


@dataclass
class KGIndex:
    repo_root: Path = field(default_factory=lambda: REPO_ROOT)
    _nodes: list[IndexedNode] = field(default_factory=list, init=False)
    _indexed_at_mtime: float = field(default=0.0, init=False)

    def _kg_mtime(self) -> float:
        mtimes = []
        for path, _ in KG_FILES.values():
            if path.exists():
                mtimes.append(path.stat().st_mtime)
        return max(mtimes) if mtimes else 0.0

    def _read_body(self, rel_path: str) -> str:
        if not rel_path:
            return ""
        full = self.repo_root / rel_path.replace("\\", "/")
        if not full.is_file():
            return ""
        try:
            return full.read_text(encoding="utf-8")
        except OSError:
            return ""

    def rebuild(self, force: bool = False) -> None:
        mtime = self._kg_mtime()
        if not force and mtime <= self._indexed_at_mtime and self._nodes:
            return
        nodes: list[IndexedNode] = []
        for source, (path, key) in KG_FILES.items():
            if not path.exists():
                continue
            kg = json.loads(path.read_text(encoding="utf-8"))
            role, track = _graph_meta(source)
            for raw in kg.get(key, []):
                if "id" not in raw:
                    continue
                nid, title, desc, rel_path = _node_fields(raw)
                body = self._read_body(rel_path)
                nodes.append(
                    IndexedNode(
                        id=nid,
                        title=title,
                        description=desc,
                        path=rel_path,
                        role=role,
                        track=track,
                        source=source,
                        node=raw,
                        body_text=body,
                    )
                )
        self._nodes = nodes
        self._indexed_at_mtime = mtime

    def search(
        self,
        query: str,
        limit: int = 5,
        role: str | None = None,
        track: str | None = None,
    ) -> list[dict[str, Any]]:
        self.rebuild()
        q_tokens = _query_tokens(query)
        if not q_tokens:
            return []

        scored: list[tuple[float, IndexedNode]] = []
        for n in self._nodes:
            if role and n.role != role:
                continue
            if track and n.track != track:
                continue
            n_tokens = _tokenize(n.search_blob())
            shared = q_tokens & n_tokens
            if not shared:
                continue
            score = len(shared) / len(q_tokens)
            if n.id.lower() in query.lower():
                score += 0.5
            scored.append((score, n))

        scored.sort(key=lambda x: (-x[0], x[1].id))
        out = []
        for score, n in scored[: max(1, limit)]:
            out.append(
                {
                    "id": n.id,
                    "title": n.title,
                    "role": n.role,
                    "track": n.track,
                    "path": n.path,
                    "score": round(score, 3),
                    "description_preview": n.description[:240],
                    "status": "accepted",
                }
            )

        # Also match pending proposals (not yet in live KG graphs).
        prop_hits: list[tuple[float, dict[str, Any]]] = []
        if not role or role == "domain":
            for p in self.list_proposals():
                blob = " ".join(
                    [
                        p.get("node_id") or "",
                        p.get("title") or "",
                        p.get("description_preview") or "",
                        p.get("slug") or "",
                    ]
                )
                p_tokens = _tokenize(blob)
                shared = q_tokens & p_tokens
                if not shared:
                    continue
                score = len(shared) / len(q_tokens)
                if "iso3166" in q_tokens and "iso3166" in p_tokens:
                    score += 0.5
                prop_hits.append((score, p))

        prop_hits.sort(key=lambda x: (-x[0], x[1].get("node_id") or ""))
        for score, p in prop_hits:
            if len(out) >= limit:
                break
            if any(r.get("id") == p.get("node_id") for r in out):
                continue
            out.append(
                {
                    "id": p.get("node_id"),
                    "title": p.get("title"),
                    "role": "domain",
                    "track": "knowledge",
                    "path": f"agents/knowledge-graphs/proposals/{p.get('filename')}",
                    "score": round(score, 3),
                    "description_preview": (p.get("description_preview") or "")[:240],
                    "status": "pending_proposal",
                }
            )

        out.sort(key=lambda r: -r["score"])
        return out[: max(1, limit)]

    def get_node(self, node_id: str) -> dict[str, Any] | None:
        self.rebuild()
        for n in self._nodes:
            if n.id == node_id:
                return {
                    "id": n.id,
                    "title": n.title,
                    "role": n.role,
                    "track": n.track,
                    "path": n.path,
                    "node": n.node,
                    "markdown_body": n.body_text,
                }
        return None

    def list_proposals(self) -> list[dict[str, Any]]:
        if not PROPOSALS_DIR.exists():
            return []
        out: list[dict[str, Any]] = []
        for jf in sorted(PROPOSALS_DIR.glob("*.json")):
            try:
                payload = json.loads(jf.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                payload = {"_error": str(exc)}

            data = payload.get("data") or {}
            slug_match = re.match(r"^\d{8}-\d{6}-(.+)\.json$", jf.name)
            slug = slug_match.group(1) if slug_match else jf.stem
            log_name = f"UPDATE_LOG_{jf.stem.split('-', 2)[0] if slug_match else ''}_proposal_{slug}.md"
            # match UPDATE_LOG by slug suffix
            log_path = next(
                (
                    p
                    for p in PROPOSALS_DIR.glob("UPDATE_LOG_*_proposal_*.md")
                    if p.name.endswith(f"_proposal_{slug}.md")
                ),
                None,
            )
            out.append(
                {
                    "filename": jf.name,
                    "slug": slug,
                    "node_id": payload.get("id"),
                    "title": data.get("title") or slug,
                    "description_preview": (data.get("description") or "")[:320],
                    "update_log_filename": log_path.name if log_path else None,
                }
            )
        return out


# Module-level singleton for MCP server process lifetime.
_index = KGIndex()


def get_index() -> KGIndex:
    return _index
