"""server/dashboard/app.py — FastAPI dashboard MVP.

Read-only views over the canonical KG, the pending proposals folder, and the
mutation timeline (UPDATE_LOG_*.md). No write endpoints — accept/reject
happens via CLI + git PR review.

Endpoints:
  GET /                  static index.html with tabs
  GET /api/health        liveness probe
  GET /api/kg-data       all 6 KGs merged into Cytoscape elements (nodes + edges)
  GET /api/kg-stats      counts per role/track
  GET /api/proposals     list of pending proposals (parsed JSON + matched UPDATE_LOG)
  GET /api/timeline      reverse-chrono list of UPDATE_LOG_*.md headers

Run:
    pip install fastapi uvicorn
    python -m uvicorn server.dashboard.app:app --reload --port 8000
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from agentloom import REPO_ROOT as WORKSPACE
KG_DIR = WORKSPACE / "agents" / "knowledge-graphs"
PROPOSALS_DIR = KG_DIR / "proposals"
STATIC_DIR = Path(__file__).resolve().parent / "static"

KG_FILES = {
    "builder-knowledge": (KG_DIR / "builder-knowledge-graph.json", "nodes"),
    "builder-skills":    (KG_DIR / "builder-skills-graph.json",    "skills"),
    "builder-behaviors": (KG_DIR / "builder-behaviors-graph.json", "behaviors"),
    "domain-knowledge":  (KG_DIR / "domain-knowledge-graph.json",  "nodes"),
    "domain-skills":     (KG_DIR / "domain-skills-graph.json",     "skills"),
    "domain-behaviors":  (KG_DIR / "domain-behaviors-graph.json",  "behaviors"),
}

MASTER_FILE = KG_DIR / "master-graph.json"

app = FastAPI(title="AgentLoom KG Dashboard", version="0.1.0")


@app.get("/api/health")
def health() -> dict:
    return {"ok": True, "workspace": str(WORKSPACE)}


def _normalize_node(node: dict, source: str) -> dict:
    """Flatten nested data/relationships if present, then add display fields."""
    nid = node.get("id", "?")
    role = "builder" if source.startswith("builder") else "domain"
    track = source.split("-", 1)[1]  # knowledge|skills|behaviors

    if "data" in node and isinstance(node["data"], dict):
        d = node["data"]
        title = d.get("title") or d.get("name") or nid
        desc = d.get("description", "")
        category = d.get("category", "")
        path = d.get("path", "")
    else:
        title = node.get("name") or node.get("title") or nid
        desc = node.get("description", "")
        category = node.get("category", "")
        path = node.get("path", "")

    return {
        "id": nid,
        "label": title,
        "type": node.get("type", "?"),
        "role": role,
        "track": track,
        "source": source,
        "category": category,
        "path": path,
        "description": desc,
    }


def _collect_edges(node: dict, all_ids: set[str]) -> list[dict]:
    """Pull parent/child + links.* edges for one node, dropping refs to
    nodes that aren't in the corpus."""
    nid = node.get("id")
    edges = []

    # nested relationships shape
    rel = node.get("relationships") or {}
    parent = rel.get("parent")
    if parent and parent in all_ids:
        edges.append({"source": parent, "target": nid, "label": "child"})

    # flat shape — parent at top-level
    flat_parent = node.get("parent")
    if flat_parent and flat_parent in all_ids:
        edges.append({"source": flat_parent, "target": nid, "label": "child"})

    # links: {label: [target_ids]}
    links = node.get("links") or {}
    for label, val in links.items():
        if isinstance(val, list):
            for tgt in val:
                if isinstance(tgt, str) and tgt in all_ids:
                    edges.append({"source": nid, "target": tgt, "label": label})
        elif isinstance(val, str) and val in all_ids:
            edges.append({"source": nid, "target": val, "label": label})
    return edges


def _load_master() -> dict | None:
    if not MASTER_FILE.exists():
        return None
    try:
        return json.loads(MASTER_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def _master_root_node(master: dict) -> dict:
    return {
        "id": master.get("rootNodeId", "agentloom:root"),
        "label": master.get("rootNodeLabel", "AgentLoom"),
        "type": "root",
        "role": "master",
        "track": "master",
        "source": "master",
        "category": "master",
        "path": "agents/knowledge-graphs/master-graph.json",
        "description": master.get("description", ""),
    }


def _master_edges(master: dict, all_ids: set[str]) -> list[dict]:
    """Synthesize edges from master root → each role's KG roots.
    Skips any rootNodeId not actually present in the corpus (forward-compat
    for roles whose KG hasn't been seeded yet)."""
    out = []
    master_root = master.get("rootNodeId", "agentloom:root")
    for role in master.get("roles", []):
        for graph in role.get("graphs", []):
            target = graph.get("rootNodeId")
            if target and target in all_ids:
                out.append({
                    "source": master_root,
                    "target": target,
                    "label": "contains",
                })
    return out


@app.get("/api/kg-data")
def kg_data() -> dict:
    """Cytoscape-format elements: {nodes: [...], edges: [...]}.

    Includes a synthetic master-root node + edges to each role's KG roots,
    derived from agents/knowledge-graphs/master-graph.json. This makes the
    visualization a single weakly-connected component instead of 6 islands.
    """
    nodes: list[dict] = []
    edges: list[dict] = []
    all_ids: set[str] = set()
    raw_nodes: list[tuple[dict, str]] = []

    for source, (path, key) in KG_FILES.items():
        if not path.exists():
            continue
        kg = json.loads(path.read_text(encoding="utf-8"))
        for n in kg.get(key, []):
            if "id" in n:
                all_ids.add(n["id"])
                raw_nodes.append((n, source))

    for n, source in raw_nodes:
        nodes.append(_normalize_node(n, source))
        edges.extend(_collect_edges(n, all_ids))

    # Master-graph synthetic node + edges
    master = _load_master()
    if master:
        master_node = _master_root_node(master)
        all_ids.add(master_node["id"])
        nodes.append(master_node)
        edges.extend(_master_edges(master, all_ids))

    seen_edge = set()
    deduped = []
    for e in edges:
        key = (e["source"], e["target"], e["label"])
        if key not in seen_edge:
            seen_edge.add(key)
            deduped.append(e)
    return {"nodes": nodes, "edges": deduped}


@app.get("/api/kg-stats")
def kg_stats() -> dict:
    out: dict[str, Any] = {"per_graph": {}, "totals": {}}
    total = 0
    for source, (path, key) in KG_FILES.items():
        if not path.exists():
            out["per_graph"][source] = 0
            continue
        kg = json.loads(path.read_text(encoding="utf-8"))
        n = len(kg.get(key, []))
        out["per_graph"][source] = n
        total += n
    out["totals"]["nodes"] = total
    out["totals"]["pending_proposals"] = len(list(PROPOSALS_DIR.glob("*.json"))) \
        if PROPOSALS_DIR.exists() else 0
    return out


@app.get("/api/proposals")
def proposals() -> list[dict]:
    if not PROPOSALS_DIR.exists():
        return []
    out = []
    json_files = sorted(PROPOSALS_DIR.glob("*.json"))
    log_files = {p.name: p for p in PROPOSALS_DIR.glob("UPDATE_LOG_*.md")}

    for jf in json_files:
        try:
            payload = json.loads(jf.read_text(encoding="utf-8"))
        except Exception as exc:
            payload = {"_error": f"failed to parse: {exc}"}

        slug_match = re.match(r"^\d{8}-\d{6}-(.+)\.json$", jf.name)
        slug = slug_match.group(1) if slug_match else jf.stem
        log_name = next(
            (n for n in log_files
             if n.startswith("UPDATE_LOG_") and n.endswith(f"_proposal_{slug}.md")),
            None,
        )
        log_text = log_files[log_name].read_text(encoding="utf-8") if log_name else ""

        out.append({
            "filename": jf.name,
            "slug": slug,
            "node_id": payload.get("id"),
            "node_type": payload.get("type"),
            "node": payload,
            "update_log_filename": log_name,
            "update_log_text": log_text,
        })
    return out


@app.get("/api/timeline")
def timeline() -> list[dict]:
    """Reverse-chronological list of UPDATE_LOG_*.md across the repo."""
    if not PROPOSALS_DIR.exists():
        return []
    entries = []
    for md in PROPOSALS_DIR.glob("UPDATE_LOG_*.md"):
        text = md.read_text(encoding="utf-8")
        first_line = text.splitlines()[0] if text else md.name
        title = first_line.lstrip("# ").strip()
        m = re.match(r"^UPDATE_LOG_(\d{8})_(\w+)_(.+)\.md$", md.name)
        date_str = m.group(1) if m else ""
        kind = m.group(2) if m else ""
        slug = m.group(3) if m else md.stem
        entries.append({
            "filename": md.name,
            "date": f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}" if date_str else "",
            "kind": kind,
            "slug": slug,
            "title": title,
        })
    entries.sort(key=lambda e: (e["date"], e["filename"]), reverse=True)
    return entries


# Static files (must be mounted last so /api/* routes win).
if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/")
def index():
    idx = STATIC_DIR / "index.html"
    if not idx.exists():
        return JSONResponse({"error": "static/index.html not found"}, status_code=500)
    return FileResponse(str(idx))
