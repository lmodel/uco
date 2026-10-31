"""The schema modules and the valid examples are scripts' output; a hand edit,
or a stale regeneration, fails here."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent


@pytest.mark.parametrize("script", ["uco_to_linkml.py", "uco_examples.py"])
def test_output_matches_a_fresh_run(script):
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / script), "--check"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
