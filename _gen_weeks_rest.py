# -*- coding: utf-8 -*-
"""Gold-standard week dicts for C2-W6 through C3-W6 (REST_WEEKS).

Imported by _gen_gold_packs.py. Schema matches the C2-W5 dict in that file.
Week bodies are stored in _gen_weeks_rest_data.json to keep Unicode and long scripts intact.
"""
from __future__ import annotations

import json
from pathlib import Path

_DATA = Path(__file__).with_name('_gen_weeks_rest_data.json')
REST_WEEKS: list[dict] = json.loads(_DATA.read_text(encoding='utf-8'))

__all__ = ['REST_WEEKS']
