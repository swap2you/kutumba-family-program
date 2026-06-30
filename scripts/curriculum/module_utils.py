"""Shared utilities for first-six-month module iteration."""
from __future__ import annotations

import re
from pathlib import Path

MODULE_DIR_RE = re.compile(r"^c[1-3]-w[1-6]-")


def iter_modules(weekly_root: Path):
    for d in sorted(weekly_root.iterdir()):
        if d.is_dir() and MODULE_DIR_RE.match(d.name):
            yield d


def module_count(weekly_root: Path) -> int:
    return sum(1 for _ in iter_modules(weekly_root))
