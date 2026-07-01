#!/usr/bin/env python3
"""Create Cycle 1 Gamma render-readiness files and update deck asset references."""
from __future__ import annotations

import re
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

RENDER_CHECKLIST = """# Gamma Render Checklist — {code}

- [ ] Deck version recorded
- [ ] 16:9 format selected
- [ ] All cards use local SVG paths from GAMMA-ASSET-MAP.yaml
- [ ] No `[IMAGE: placeholder]` remains
- [ ] Card-specific speaker notes on every card
- [ ] Source citation on factual cards
- [ ] No invented scripture quotations
- [ ] Alt text from visuals/ALT-TEXT.md applied
- [ ] Human doctrinal review before live use

**Status:** render-ready specification — exported deck not in Git until human QA.
"""

POST_QA = """# Gamma Post-Render QA — {code}

| Check | Pass |
|---|---|
| Text matches repository prompt | |
| Card order correct | |
| No invented facts | |
| Citations visible | |
| Image rights kutumba-original or cleared | |
| Diacritics not cropped | |
| Child readability (Lāla–Lālī deck) | |
| Color contrast | |
| Export parity PDF/PPT | |

Do not mark pilot-approved without named reviewer.
"""


def main() -> None:
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir() or not d.name.startswith("c1-w"):
            continue
        code = d.name.split("-")[0].upper() + "-" + d.name.split("-")[1].upper()
        gamma = d / "gamma"
        manifest = d / "visuals" / "VISUAL-ASSET-MANIFEST.yaml"
        if not manifest.exists():
            continue
        data = yaml.safe_load(manifest.read_text(encoding="utf-8"))
        assets = data.get("assets", [])
        asset_map = {
            "module_id": code,
            "render_status": "render-ready",
            "deck_format": "16:9",
            "default_assets": [a["asset_id"] for a in assets[:3]],
            "cards": [],
        }
        for a in assets:
            asset_map["cards"].append(
                {
                    "asset_id": a["asset_id"],
                    "path": a["path"],
                    "rights_status": a.get("rights_status", "kutumba-original"),
                }
            )
        (gamma / "GAMMA-ASSET-MAP.yaml").write_text(
            yaml.safe_dump(asset_map, sort_keys=False, allow_unicode=True),
            encoding="utf-8",
        )
        (gamma / "GAMMA-RENDER-CHECKLIST.md").write_text(
            RENDER_CHECKLIST.format(code=code), encoding="utf-8"
        )
        (gamma / "GAMMA-POST-RENDER-QA.md").write_text(POST_QA.format(code=code), encoding="utf-8")
        # Update master brief
        master = gamma / "GAMMA-MASTER-DECK-BRIEF.md"
        if master.exists():
            t = master.read_text(encoding="utf-8")
            t = re.sub(
                r"Image placeholders:.*",
                "Visual assets: see `GAMMA-ASSET-MAP.yaml` and `../visuals/rendered/*.svg`",
                t,
            )
            if "render_status" not in t:
                t += "\n\n## V7 render status\n\n**render-ready** — local KUTUMBA SVG assets linked; human review required before export.\n"
            master.write_text(t, encoding="utf-8")
        # Replace placeholders in deck prompts
        for deck in gamma.glob("GAMMA-*-DECK-PROMPT.md"):
            text = deck.read_text(encoding="utf-8")
            primary = assets[0]["path"] if assets else ""
            text = re.sub(
                r"\[IMAGE:[^\]]+\]",
                f"[ASSET: {primary}]" if primary else "[ASSET: see GAMMA-ASSET-MAP.yaml]",
                text,
            )
            deck.write_text(text, encoding="utf-8")
        print(code, "gamma pack updated")


if __name__ == "__main__":
    main()
