#!/usr/bin/env python3
"""Update Cycle 1 Gamma asset maps to V8 asset-complete status."""
from __future__ import annotations

import re
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

ASSET_RE = re.compile(r"\[ASSET:\s*([^\]]+)\]")
PLACEHOLDER_PATTERNS = [
    "photo timeline placeholder",
    "Table from VISUAL-PLAN.md",
    "generic icon",
    "[IMAGE:",
]


def card_records(module_dir: Path, assets: list) -> list[dict]:
    cards = []
    for i, asset in enumerate(assets, 1):
        aid = asset["asset_id"]
        cards.append(
            {
                "card_number": i,
                "audience": "all-decks",
                "asset_id": aid,
                "svg": f"visuals/rendered/{aid}.svg",
                "png": f"visuals/png/{aid}.png",
                "rights": asset.get("rights_status", "kutumba-original"),
                "source_keys": asset.get("source_keys", ["module-research-pack"]),
                "speaker_note": f"Use {aid} per SPEAKER-NOTES.md; doctrinal review open.",
                "accessibility": asset.get("alt_text", ""),
            }
        )
    return cards


def fix_deck_prompt(path: Path, module_dir: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    for pat in PLACEHOLDER_PATTERNS:
        if pat.lower() in text.lower() and pat != "[IMAGE:":
            # replace visual lines containing placeholder with first available asset
            manifest = module_dir / "visuals" / "VISUAL-ASSET-MANIFEST.yaml"
            if manifest.exists():
                data = yaml.safe_load(manifest.read_text(encoding="utf-8"))
                assets = data.get("assets", [])
                if assets:
                    default = assets[0]["asset_id"]
                    text = re.sub(
                        r"\*\*Visual:\*\*[^\n]*placeholder[^\n]*",
                        f"**Visual:** `[ASSET: visuals/rendered/{default}.svg]`",
                        text,
                        flags=re.I,
                    )
                    text = text.replace(
                        "**Visual:** Table from VISUAL-PLAN.md",
                        f"**Visual:** `[ASSET: visuals/rendered/{default}.svg]`",
                    )
    text = ASSET_RE.sub(
        lambda m: f"`[ASSET: {m.group(1).strip()}]`" if not m.group(0).startswith("`") else m.group(0),
        text,
    )
    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir() or not d.name.startswith("c1-w"):
            continue
        manifest_path = d / "visuals" / "VISUAL-ASSET-MANIFEST.yaml"
        if not manifest_path.exists():
            continue
        data = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
        assets = data.get("assets", [])
        code = data.get("module_id", d.name[:5].upper())
        asset_map = {
            "module_id": code,
            "render_status": "assets-complete-upload-required",
            "deck_format": "16:9",
            "default_assets": [a["asset_id"] for a in assets],
            "cards": card_records(d, assets),
        }
        (d / "gamma" / "GAMMA-ASSET-MAP.yaml").write_text(
            yaml.safe_dump(asset_map, sort_keys=False, allow_unicode=True),
            encoding="utf-8",
        )
        gamma = d / "gamma"
        for deck in gamma.glob("GAMMA-*-DECK-PROMPT.md"):
            fix_deck_prompt(deck, d)
        print(f"Updated {code} gamma pack ({len(assets)} cards)")


if __name__ == "__main__":
    main()
