"""Governance gate as a pytest suite.

These tests are thin wrappers over AgentLoom's own validators so that the full
KG + Tier-A governance gate runs under `pytest` (and therefore in CI) exactly as
it does via `make validate-all`.
"""
import subprocess
import sys

import pytest

GATES = [
    pytest.param("agentloom.kg.validate_all", id="kg-validate-all"),
    pytest.param("agentloom.validators.run_all", id="tier-a-validators"),
]


@pytest.mark.parametrize("module", GATES)
def test_governance_gate(module):
    result = subprocess.run(
        [sys.executable, "-m", module],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"{module} failed (exit {result.returncode}).\n"
        f"--- stdout ---\n{result.stdout}\n--- stderr ---\n{result.stderr}"
    )
