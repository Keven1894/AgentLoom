"""clinerules-must-match-system-prompt-kg-node — Tier A validator.

Behavior MD: agents/behaviors/builder/behavior-clinerules-must-match-canonical-prompt.md

Checks: .clinerules/01-builder-agent-prompt.md is a verbatim, byte-for-byte
re-rendering of the canonical system-prompt KG node body, as produced by
scripts/sync_clinerules.py.

Drift would silently let Cline (Layer-3 host #3) operate on a different
system prompt than the standalone agentloom.builder_agent (host #1) and
Cursor (host #2). The whole "host-agnostic" claim of the framework
collapses if hosts diverge.

This validator delegates to scripts/sync_clinerules.py --check, which:
  - exit 0 iff in sync (and prints the prompt_version).
  - exit 1 with a unified diff if drift is detected.
  - exit 1 if .clinerules/01-... is missing entirely.

Exit 0 iff in sync. Exit 1 on drift. Exit 2 on framework error (sync
script itself broken).
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
SYNC_SCRIPT = WORKSPACE / "scripts" / "sync_clinerules.py"


def main() -> int:
    if not SYNC_SCRIPT.exists():
        print(f"[ERROR] sync script not found at {SYNC_SCRIPT.relative_to(WORKSPACE)}.")
        return 2

    result = subprocess.run(
        [sys.executable, str(SYNC_SCRIPT), "--check"],
        cwd=str(WORKSPACE),
    )
    if result.returncode == 0:
        return 0
    if result.returncode == 1:
        return 1
    print(f"[ERROR] sync script exited with unexpected code {result.returncode}.")
    return 2


if __name__ == "__main__":
    sys.exit(main())
