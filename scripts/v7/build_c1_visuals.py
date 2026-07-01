#!/usr/bin/env python3
"""Generate KUTUMBA-original Cycle 1 SVG visual packs and manifests."""
from __future__ import annotations

import textwrap
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

SVG_HEADER = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img">
  <title>{title}</title>
  <desc>{desc}</desc>
  <rect width="{w}" height="{h}" fill="#faf8f5"/>
'''

MODULE_ASSETS = {
    "c1-w1-what-is-kutumba-and-why-are-we-here": [
        ("concept-diagram", "c1-w1-concept-hearing-flow", "Hearing Flow", "Distraction to inquiry to authorized hearing to family practice"),
        ("storyboard", "c1-w1-storyboard-naimisharanya", "Naimiṣāraṇya Assembly", "Sages gather; Sūta Gosvāmī prepares to speak"),
        ("analogy-diagram", "c1-w1-analogy-garden", "Family Garden Rhythm", "Protected weekly hearing time"),
        ("scripture-reference-card", "c1-w1-verse-sb-1-2-18", "SB 1.2.18 Reference", "Regular Bhāgavata hearing and service"),
        ("process-flow", "c1-w1-session-map", "Session Process Map", "Facilitator flow for C1-W1"),
        ("family-practice-card", "c1-w1-home-practice", "Home Practice Card", "One weekly hearing step at home"),
        ("comparison-chart", "c1-w1-charter-wheel", "KUTUMBA Six Purposes", "Charter-sourced purpose wheel — not scripture quote"),
    ],
    "c1-w2-i-am-not-this-body": [
        ("concept-diagram", "c1-w2-concept-life-stages", "Life Stage Continuity", "Childhood youth old age — same self"),
        ("storyboard", "c1-w2-storyboard-chariot", "Chariot at Dawn", "Arjuna's sorrow; Kṛṣṇa as guide"),
        ("analogy-diagram", "c1-w2-analogy-driver-vehicle", "Driver and Vehicle", "Self and body — with limits"),
        ("analogy-diagram", "c1-w2-analogy-changing-clothes", "Changing Clothes", "Soul changes bodies — symbolic"),
        ("scripture-reference-card", "c1-w2-verse-bg-2-13", "BG 2.13 Reference", "Embodied self passes through stages"),
        ("process-flow", "c1-w2-session-map", "Session Process Map", "Facilitator flow for C1-W2"),
        ("family-practice-card", "c1-w2-home-practice", "Identity Pause Card", "Family identity pause practice"),
    ],
    "c1-w3-the-nature-of-the-soul": [
        ("concept-diagram", "c1-w3-concept-jiva-qualities", "Jīva Qualities Map", "Eternal conscious fragment of Kṛṣṇa"),
        ("storyboard", "c1-w3-storyboard-jada-bharata", "Jaḍa Bharata Sequence", "King Rahūgaṇa learns soul lesson"),
        ("analogy-diagram", "c1-w3-analogy-sunray", "Sunray Analogy", "Part and parcel — with limits"),
        ("scripture-reference-card", "c1-w3-verse-bg-2-20", "BG 2.20 Reference", "Soul not cut burned wetted dried"),
        ("process-flow", "c1-w3-session-map", "Session Process Map", "Facilitator flow for C1-W3"),
        ("family-practice-card", "c1-w3-home-practice", "Home Practice Card", "Remember the soul in daily care"),
        ("comparison-chart", "c1-w3-body-soul-care", "Body and Soul Care", "Care for body without contempt"),
    ],
    "c1-w4-why-human-life-is-rare-and-valuable": [
        ("concept-diagram", "c1-w4-concept-opportunity-path", "Human Opportunity Path", "Capacity inquiry practice compassion"),
        ("storyboard", "c1-w4-storyboard-mrgari", "Mṛgāri and Nārada", "Mercy transforms violent habit"),
        ("analogy-diagram", "c1-w4-analogy-crossroads", "Life Crossroads", "Human form as inquiry opportunity"),
        ("scripture-reference-card", "c1-w4-verse-bg-2-40", "BG 2.40 Reference", "No effort in Krishna consciousness is lost"),
        ("process-flow", "c1-w4-session-map", "Session Process Map", "Facilitator flow for C1-W4"),
        ("family-practice-card", "c1-w4-home-practice", "Home Practice Card", "One compassionate action this week"),
        ("comparison-chart", "c1-w4-compassion-map", "Compassion Map", "No degrading of animals"),
    ],
    "c1-w5-the-temporary-world-and-the-search-for-permanent-happiness": [
        ("concept-diagram", "c1-w5-concept-temporary-permanent", "Temporary vs Permanent", "Material pleasure cycle vs devotional fulfillment"),
        ("storyboard", "c1-w5-storyboard-dhruva", "Dhruva Sequence", "Aspiration transformed by devotion"),
        ("analogy-diagram", "c1-w5-analogy-pleasure-cycle", "Pleasure Cycle", "Temporary enjoyment with gratitude"),
        ("scripture-reference-card", "c1-w5-verse-bg-5-22", "BG 5.22 Reference", "Pleasures born of contact are temporary"),
        ("process-flow", "c1-w5-session-map", "Session Process Map", "Facilitator flow for C1-W5"),
        ("family-practice-card", "c1-w5-home-practice", "Home Practice Card", "Gratitude before enjoyment"),
        ("comparison-chart", "c1-w5-family-affection", "Family Affection Note", "Ordinary affection is not meaningless"),
    ],
    "c1-w6-integration-night-who-am-i-and-how-should-our-family-live": [
        ("concept-diagram", "c1-w6-cycle-synthesis-map", "Cycle 1 Synthesis Map", "Six-week learning integration"),
        ("comparison-chart", "c1-w6-memory-line-path", "Memory Line Path", "Six-week recall without ranking"),
        ("analogy-diagram", "c1-w6-family-presentation", "Family Presentation Flow", "Offering without performance pressure"),
        ("scripture-reference-card", "c1-w6-integration-verses", "Integration Verse Card", "Cycle 1 key verses review"),
        ("process-flow", "c1-w6-session-map", "Integration Session Map", "Stations and recall flow"),
        ("family-practice-card", "c1-w6-home-practice", "Family Commitment Card", "One family living decision"),
        ("process-flow", "c1-w6-gamma-asset-sheet", "Gamma Asset Sheet", "Asset selection for integration night"),
    ],
}


def simple_diagram_svg(asset_id: str, title: str, desc: str, bullets: list[str]) -> str:
    w, h = 800, 520
    lines = [f'<text x="400" y="48" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="22" font-weight="600">{title}</text>']
    y = 100
    for b in bullets:
        for chunk in textwrap.wrap(b, 70):
            lines.append(
                f'<text x="60" y="{y}" font-family="Segoe UI,sans-serif" font-size="16" fill="#333">{chunk}</text>'
            )
            y += 28
    lines.append(
        f'<text x="400" y="{h-30}" text-anchor="middle" font-size="12" fill="#666">KUTUMBA-original · {asset_id} · human doctrinal review required</text>'
    )
    return SVG_HEADER.format(w=w, h=h, title=title, desc=desc) + "\n".join(lines) + "\n</svg>\n"


def write_asset(vis: Path, asset_class: str, asset_id: str, title: str, desc: str) -> dict:
    rendered = vis / "rendered"
    source = vis / "source"
    rendered.mkdir(parents=True, exist_ok=True)
    source.mkdir(parents=True, exist_ok=True)
    bullets = [desc, f"Asset class: {asset_class}", "Source anchors: see module research pack", "Rights: kutumba-original"]
    svg = simple_diagram_svg(asset_id, title, desc, bullets)
    rel = f"visuals/rendered/{asset_id}.svg"
    out = vis / "rendered" / f"{asset_id}.svg"
    out.write_text(svg, encoding="utf-8")
    (source / f"{asset_id}.svg").write_text(svg, encoding="utf-8")
    return {
        "asset_id": asset_id,
        "asset_class": asset_class,
        "title": title,
        "path": rel,
        "format": "svg",
        "rights_status": "kutumba-original",
        "doctrinal_review": "human-review-required",
        "design_review": "human-review-required",
        "alt_text": desc,
    }


def main() -> None:
    catalog_entries = []
    for slug, assets in MODULE_ASSETS.items():
        vis = WEEKLY / slug / "visuals"
        vis.mkdir(exist_ok=True)
        manifest_assets = []
        for asset_class, asset_id, title, desc in assets:
            manifest_assets.append(write_asset(vis, asset_class, asset_id, title, desc))
            catalog_entries.append({"module": slug, **manifest_assets[-1]})
        manifest = vis / "VISUAL-ASSET-MANIFEST.yaml"
        lines = ["module_id: " + slug.split("-")[0].upper() + "-" + slug.split("-")[1].upper(), "assets:"]
        for a in manifest_assets:
            lines.append(f"  - asset_id: {a['asset_id']}")
            lines.append(f"    asset_class: {a['asset_class']}")
            lines.append(f"    path: {a['path']}")
            lines.append(f"    rights_status: {a['rights_status']}")
            lines.append(f"    alt_text: \"{a['alt_text']}\"")
            lines.append(f"    doctrinal_review: {a['doctrinal_review']}")
        manifest.write_text("\n".join(lines) + "\n", encoding="utf-8")
        alt = vis / "ALT-TEXT.md"
        alt.write_text(
            "# Alt Text — " + slug + "\n\n"
            + "\n".join(f"- **{a['asset_id']}**: {a['alt_text']}" for a in manifest_assets)
            + "\n",
            encoding="utf-8",
        )
        (vis / "README.md").write_text(
            f"# Visuals — {slug}\n\nKUTUMBA-original SVG pack (V7). See `VISUAL-ASSET-MANIFEST.yaml`.\n",
            encoding="utf-8",
        )
        print(slug, len(manifest_assets), "assets")
    print("Total assets:", len(catalog_entries))


if __name__ == "__main__":
    main()
