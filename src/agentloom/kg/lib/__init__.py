"""
JSON Helper Toolkit for Knowledge Graph Maintenance

A modular toolkit for safe JSON Knowledge Graph operations using
industry-standard libraries (jsonschema, jsonpatch).
"""

from .validator import KGValidator, ValidationResult
from .updater import KGUpdater, UpdateResult
from .generator import NodeGenerator
from .kg_editor import KGEditor

__version__ = "1.0.0"
__all__ = [
    "KGValidator", "ValidationResult",
    "KGUpdater", "UpdateResult",
    "NodeGenerator",
    "KGEditor"
]
