"""AgentLoom — executable governance framework for builder agents.

Python code lives under ``src/agentloom/``. Data and content (knowledge graphs,
docs, ``.clinerules``) live at the repository root. ``REPO_ROOT`` is discovered
by walking up from this file until a directory containing
``agents/knowledge-graphs`` is found, so scripts work regardless of how deeply
the package is installed or invoked.
"""

from __future__ import annotations

from pathlib import Path

__version__ = "3.0.0"


def _find_repo_root() -> Path:
    here = Path(__file__).resolve()
    for candidate in (here, *here.parents):
        if (candidate / "agents" / "knowledge-graphs").is_dir():
            return candidate
    # Fallback: src/agentloom/__init__.py -> repo root is parents[2]
    return here.parents[2]


REPO_ROOT = _find_repo_root()
KG_DIR = REPO_ROOT / "agents" / "knowledge-graphs"
DOCS_DIR = REPO_ROOT / "docs"
CLINERULES_DIR = REPO_ROOT / ".clinerules"

__all__ = ["REPO_ROOT", "KG_DIR", "DOCS_DIR", "CLINERULES_DIR", "__version__"]
