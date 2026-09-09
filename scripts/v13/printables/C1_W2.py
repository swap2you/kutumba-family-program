#!/usr/bin/env python3
"""Alias module: user-facing name C1_W2.py re-exports builders from C1-W2.py.

render_week.py loads scripts/v13/printables/{week_id}.py → C1-W2.py.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

_path = Path(__file__).with_name("C1-W2.py")
_spec = importlib.util.spec_from_file_location("v13_printables_C1_W2_src", _path)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)

YOUNGER_BUILDERS = _mod.YOUNGER_BUILDERS
OLDER_BUILDERS = _mod.OLDER_BUILDERS
PARENT_BUILDERS = _mod.PARENT_BUILDERS
FAMILY_BUILDERS = getattr(_mod, "FAMILY_BUILDERS", [])

if __name__ == "__main__":
    print(
        "C1_W2 alias OK:",
        len(YOUNGER_BUILDERS),
        len(OLDER_BUILDERS),
        len(PARENT_BUILDERS),
    )
