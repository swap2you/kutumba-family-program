#!/usr/bin/env python3
"""Generate KUTUMBA-original teaching SVGs for all Cycle 1 visual assets."""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
sys.path.insert(0, str(Path(__file__).parent))

from svg_primitives import (  # noqa: E402
    analogy_diagram,
    comparison_chart,
    concept_diagram,
    practice_card,
    process_flow,
    storyboard,
    verse_card,
)

# asset_id -> builder callable
BUILDERS: dict[str, callable] = {}


def _reg(asset_id: str, fn):
    BUILDERS[asset_id] = fn


# --- C1-W1 ---
_reg(
    "c1-w1-concept-hearing-flow",
    lambda: concept_diagram(
        "c1-w1-concept-hearing-flow",
        "Hearing Flow",
        "Distraction to inquiry to authorized hearing to family practice",
        [("Distraction", "busy household"), ("Inquiry", "what endures?"), ("Authorized hearing", "SB kathā"), ("Family practice", "weekly rhythm")],
        [(0, 1), (1, 2), (2, 3)],
        "Steady hearing shapes family character",
        "SB-1-2-18; SB-1-2-17",
    ),
)
_reg(
    "c1-w1-storyboard-naimisharanya",
    lambda: storyboard(
        "c1-w1-storyboard-naimisharanya",
        "Naimiṣāraṇya Assembly",
        "Sages gather; Sūta Gosvāmī prepares to speak",
        [
            ("1", "Sages assemble after Kṛṣṇa's departure", "SB-1-1-4"),
            ("2", "They ask about duty in Kali-yuga", "SB-1-1-4"),
            ("3", "Sūta Gosvāmī is invited to speak", "SB-1-1-5"),
            ("4", "Authorized hearing begins", "SB-1-2-18"),
        ],
        "SB-1-1-4; SB-1-2-18",
    ),
)
_reg(
    "c1-w1-analogy-garden",
    lambda: analogy_diagram(
        "c1-w1-analogy-garden",
        "Family Garden Rhythm",
        "Protected weekly hearing time",
        "Garden plot", ["protected space", "regular watering", "seasonal care"],
        "Family sādhana", ["fixed weekly time", "gentle consistency", "shared listening"],
        "Protected rhythm helps hearing take root",
        "Not a guarantee of instant realization",
        "KUT-CHARTER; pedagogy",
    ),
)
_reg(
    "c1-w1-verse-sb-1-2-18",
    lambda: verse_card(
        "c1-w1-verse-sb-1-2-18",
        "SB 1.2.18 Reference",
        "Regular Bhāgavata hearing and service",
        "Śrīmad-Bhāgavatam 1.2.18",
        "Regular hearing and service to the Bhāgavatam cleanse the heart and steady devotion.",
        "https://vedabase.io/en/library/sb/1/2/18/",
        "Not a license to skip authorized guidance",
        "SB-1-2-18",
    ),
)
_reg(
    "c1-w1-session-map",
    lambda: process_flow(
        "c1-w1-session-map",
        "Session Process Map",
        "Facilitator flow for C1-W1",
        ["Welcome", "Memory line", "Kathā hearing", "Discussion", "Home practice", "Close"],
        "KUT-CHARTER session design",
    ),
)
_reg(
    "c1-w1-home-practice",
    lambda: practice_card(
        "c1-w1-home-practice",
        "Home Practice Card",
        "One weekly hearing step at home",
        "After the session, family gathers briefly",
        ["Choose one SB verse heard today", "Read paraphrase aloud together", "One gratitude sentence each"],
        "Listen to one verse recording",
        "Skip if someone is unwell; no pressure",
        "SB-1-2-18",
    ),
)
_reg(
    "c1-w1-charter-wheel",
    lambda: comparison_chart(
        "c1-w1-charter-wheel",
        "KUTUMBA Six Purposes",
        "Charter-sourced purpose wheel",
        ["Hearing", "Character", "Service", "Children", "Community", "Boundaries"],
        "KUT-CHARTER §6",
        "KUTUMBA",
    ),
)

# --- C1-W2 ---
_reg(
    "c1-w2-concept-life-stages",
    lambda: concept_diagram(
        "c1-w2-concept-life-stages",
        "Life Stage Continuity",
        "Childhood youth old age — same self",
        [("Childhood", "body changes"), ("Youth", "body changes"), ("Old age", "body changes"), ("Self", "continues")],
        [(0, 3), (1, 3), (2, 3)],
        "The embodied self passes through stages",
        "BG-2-13",
    ),
)
_reg(
    "c1-w2-storyboard-chariot",
    lambda: storyboard(
        "c1-w2-storyboard-chariot",
        "Chariot at Dawn",
        "Arjuna's sorrow; Kṛṣṇa as guide",
        [
            ("1", "Armies arrayed at Kurukṣetra", "BG-1-1"),
            ("2", "Arjuna sees relatives", "BG-1-28"),
            ("3", "Overwhelmed by sorrow", "BG-1-47"),
            ("4", "Kṛṣṇa becomes teacher", "BG-2-7"),
        ],
        "BG-1; BG-2",
    ),
)
_reg(
    "c1-w2-analogy-driver-vehicle",
    lambda: analogy_diagram(
        "c1-w2-analogy-driver-vehicle",
        "Driver and Vehicle",
        "Self and body — with limits",
        "Driver", ["conscious agent", "directs movement", "leaves vehicle"],
        "Vehicle", ["changes over time", "needs maintenance", "not the driver"],
        "Conscious self uses but is not the body",
        "Not license to neglect bodily care",
        "BG-2-13 pedagogy",
    ),
)
_reg(
    "c1-w2-analogy-changing-clothes",
    lambda: analogy_diagram(
        "c1-w2-analogy-changing-clothes",
        "Changing Clothes",
        "Soul changes bodies — symbolic",
        "Person", ["same identity", "new garment", "discards old"],
        "Soul", ["eternal", "new body", "leaves old body"],
        "Self continues when body changes",
        "Symbolic only — not literal clothing",
        "BG-2-22",
    ),
)
_reg(
    "c1-w2-verse-bg-2-13",
    lambda: verse_card(
        "c1-w2-verse-bg-2-13",
        "BG 2.13 Reference",
        "Embodied self passes through stages",
        "Bhagavad-gītā 2.13",
        "The embodied self passes through childhood, youth, and old age in this body; the self continues.",
        "https://vedabase.io/en/library/bg/2/13/",
        "Not permission for bodily neglect",
        "BG-2-13",
    ),
)
_reg(
    "c1-w2-session-map",
    lambda: process_flow(
        "c1-w2-session-map",
        "Session Process Map",
        "Facilitator flow for C1-W2",
        ["Welcome", "Body/soul check-in", "Kathā", "Identity pause", "Practice card", "Close"],
        "C1-W2 facilitator guide",
    ),
)
_reg(
    "c1-w2-home-practice",
    lambda: practice_card(
        "c1-w2-home-practice",
        "Identity Pause Card",
        "Family identity pause practice",
        "When stress rises about appearance or ability",
        ["Pause together", "Ask: who is aware?", "One kind action to the body"],
        "Silent breath together",
        "No interrogation of children",
        "BG-2-13",
    ),
)

# --- C1-W3 ---
_reg(
    "c1-w3-concept-jiva-qualities",
    lambda: concept_diagram(
        "c1-w3-concept-jiva-qualities",
        "Jīva Qualities Map",
        "Eternal conscious fragment of Kṛṣṇa",
        [("Eternal", "not created"), ("Conscious", "aware"), ("Fragment", "part of Kṛṣṇa"), ("Seeks joy", "in relationship")],
        [(0, 2), (1, 2), (2, 3)],
        "Soul is part and parcel of Kṛṣṇa",
        "BG-2-20; BG-15-7",
    ),
)
_reg(
    "c1-w3-storyboard-jada-bharata",
    lambda: storyboard(
        "c1-w3-storyboard-jada-bharata",
        "Jaḍa Bharata Sequence",
        "King Rahūgaṇa learns soul lesson",
        [
            ("1", "Bharata lives simply after renunciation", "SB-5-9"),
            ("2", "Carried as palanquin bearer", "SB-5-10"),
            ("3", "King rebukes slow pace", "SB-5-10"),
            ("4", "Bharata teaches soul beyond body", "SB-5-10"),
        ],
        "SB-5-9; SB-5-10",
    ),
)
_reg(
    "c1-w3-analogy-sunray",
    lambda: analogy_diagram(
        "c1-w3-analogy-sunray",
        "Sunray Analogy",
        "Part and parcel — with limits",
        "Sun", ["original source", "full potency", "never divided"],
        "Sunray", ["from the sun", "shares quality", "dependent"],
        "Soul is qualitatively one with Kṛṣṇa",
        "Soul is not quantitatively God",
        "BG-15-7 pedagogy",
    ),
)
_reg(
    "c1-w3-verse-bg-2-20",
    lambda: verse_card(
        "c1-w3-verse-bg-2-20",
        "BG 2.20 Reference",
        "Soul not cut burned wetted dried",
        "Bhagavad-gītā 2.20",
        "The soul is not slain when the body is slain; it is eternal and unchanging.",
        "https://vedabase.io/en/library/bg/2/20/",
        "Not denial of bodily suffering",
        "BG-2-20",
    ),
)
_reg(
    "c1-w3-session-map",
    lambda: process_flow(
        "c1-w3-session-map",
        "Session Process Map",
        "Facilitator flow for C1-W3",
        ["Welcome", "Qualities recall", "Kathā", "Sunray limits", "Care discussion", "Close"],
        "C1-W3 facilitator guide",
    ),
)
_reg(
    "c1-w3-home-practice",
    lambda: practice_card(
        "c1-w3-home-practice",
        "Home Practice Card",
        "Remember the soul in daily care",
        "During meals or bedtime routine",
        ["Thank the body as vehicle", "Name one kind soul-quality", "Prayer of gratitude"],
        "One thank-you sentence",
        "No fear-based teaching",
        "BG-2-20",
    ),
)
_reg(
    "c1-w3-body-soul-care",
    lambda: comparison_chart(
        "c1-w3-body-soul-care",
        "Body and Soul Care",
        "Care for body without contempt",
        ["Rest", "Nutrition", "Hygiene", "Speech", "Study", "Service"],
        "BG-2-20; pedagogy",
        "Whole person",
    ),
)

# --- C1-W4 ---
_reg(
    "c1-w4-concept-opportunity-path",
    lambda: concept_diagram(
        "c1-w4-concept-opportunity-path",
        "Human Opportunity Path",
        "Capacity inquiry practice compassion",
        [("Human form", "rare"), ("Inquiry", "enabled"), ("Practice", "possible"), ("Compassion", "fruit")],
        [(0, 1), (1, 2), (2, 3)],
        "Human life enables purposeful inquiry",
        "BG-2-40",
    ),
)
_reg(
    "c1-w4-storyboard-mrgari",
    lambda: storyboard(
        "c1-w4-storyboard-mrgari",
        "Mṛgāri and Nārada",
        "Mercy transforms violent habit",
        [
            ("1", "Hunter injures animals partially", "SB-4-8"),
            ("2", "Nārada visits the hunter", "SB-4-8"),
            ("3", "Mercy question shifts heart", "SB-4-8"),
            ("4", "Hunter becomes compassionate", "SB-4-8"),
        ],
        "SB-4-8",
    ),
)
_reg(
    "c1-w4-analogy-crossroads",
    lambda: analogy_diagram(
        "c1-w4-analogy-crossroads",
        "Life Crossroads",
        "Human form as inquiry opportunity",
        "Crossroads sign", ["many directions", "choice matters", "limited time"],
        "Human duties", ["inquiry", "practice", "service"],
        "Human life is a deliberate choice point",
        "Not ranking other species as worthless",
        "BG-2-40 pedagogy",
    ),
)
_reg(
    "c1-w4-verse-bg-2-40",
    lambda: verse_card(
        "c1-w4-verse-bg-2-40",
        "BG 2.40 Reference",
        "No effort in Krishna consciousness is lost",
        "Bhagavad-gītā 2.40",
        "In this endeavor there is no loss; even a little progress protects one from great fear.",
        "https://vedabase.io/en/library/bg/2/40/",
        "Not a guarantee of instant success",
        "BG-2-40",
    ),
)
_reg(
    "c1-w4-session-map",
    lambda: process_flow(
        "c1-w4-session-map",
        "Session Process Map",
        "Facilitator flow for C1-W4",
        ["Welcome", "Opportunity framing", "Kathā", "Compassion map", "Action pledge", "Close"],
        "C1-W4 facilitator guide",
    ),
)
_reg(
    "c1-w4-home-practice",
    lambda: practice_card(
        "c1-w4-home-practice",
        "Home Practice Card",
        "One compassionate action this week",
        "Choose a family or neighbor need",
        ["Name one gentle action", "Do it together if possible", "Reflect without boasting"],
        "One kind word",
        "No unsafe encounters",
        "BG-2-40",
    ),
)
_reg(
    "c1-w4-compassion-map",
    lambda: comparison_chart(
        "c1-w4-compassion-map",
        "Compassion Map",
        "No degrading of animals",
        ["Humans", "Animals", "Plants", "Speech", "Food", "Service"],
        "SB-4-8; pedagogy",
        "Mercy",
    ),
)

# --- C1-W5 ---
_reg(
    "c1-w5-concept-temporary-permanent",
    lambda: concept_diagram(
        "c1-w5-concept-temporary-permanent",
        "Temporary vs Permanent",
        "Material pleasure cycle vs devotional fulfillment",
        [("Contact pleasure", "arises"), ("Enjoyment", "fades"), ("Hankering", "returns"), ("Devotional steadiness", "deepens")],
        [(0, 1), (1, 2), (2, 3)],
        "Temporary pleasures do not satisfy permanently",
        "BG-5-22",
    ),
)
_reg(
    "c1-w5-storyboard-dhruva",
    lambda: storyboard(
        "c1-w5-storyboard-dhruva",
        "Dhruva Sequence",
        "Aspiration transformed by devotion",
        [
            ("1", "Dhruva leaves home determined", "SB-4-8"),
            ("2", "Meets Nārada; undertakes tapas", "SB-4-8"),
            ("3", "Sees the Lord in meditation", "SB-4-9"),
            ("4", "Returns with softened heart", "SB-4-9"),
        ],
        "SB-4-8; SB-4-9",
    ),
)
_reg(
    "c1-w5-analogy-pleasure-cycle",
    lambda: analogy_diagram(
        "c1-w5-analogy-pleasure-cycle",
        "Pleasure Cycle",
        "Temporary enjoyment with gratitude",
        "Sparkler", ["bright moment", "burns out", "want another"],
        "Senses + objects", ["contact", "brief joy", "repeat craving"],
        "Pleasures born of contact are temporary",
        "Not condemnation of lawful affection",
        "BG-5-22",
    ),
)
_reg(
    "c1-w5-verse-bg-5-22",
    lambda: verse_card(
        "c1-w5-verse-bg-5-22",
        "BG 5.22 Reference",
        "Pleasures born of contact are temporary",
        "Bhagavad-gītā 5.22",
        "Pleasures from sense contact have a beginning and end; the wise do not delight in them alone.",
        "https://vedabase.io/en/library/bg/5/22/",
        "Not rejection of family affection",
        "BG-5-22",
    ),
)
_reg(
    "c1-w5-session-map",
    lambda: process_flow(
        "c1-w5-session-map",
        "Session Process Map",
        "Facilitator flow for C1-W5",
        ["Welcome", "Pleasure check-in", "Kathā", "Gratitude practice", "Family note", "Close"],
        "C1-W5 facilitator guide",
    ),
)
_reg(
    "c1-w5-home-practice",
    lambda: practice_card(
        "c1-w5-home-practice",
        "Home Practice Card",
        "Gratitude before enjoyment",
        "Before a pleasant meal or activity",
        ["Pause briefly", "Thank Kṛṣṇa and family", "Enjoy without entitlement"],
        "One thank-you",
        "No guilt about lawful joy",
        "BG-5-22",
    ),
)
_reg(
    "c1-w5-family-affection",
    lambda: comparison_chart(
        "c1-w5-family-affection",
        "Family Affection Note",
        "Ordinary affection is not meaningless",
        ["Parents", "Children", "Spouse", "Friends", "Community", "Kṛṣṇa"],
        "Pedagogy; BG-5-22 context",
        "Affection",
    ),
)

# --- C1-W6 ---
_reg(
    "c1-w6-cycle-synthesis-map",
    lambda: concept_diagram(
        "c1-w6-cycle-synthesis-map",
        "Cycle 1 Synthesis Map",
        "Six-week learning integration",
        [("W1 Hearing", "KUTUMBA"), ("W2 Body/soul", "identity"), ("W3 Soul", "qualities"), ("W4–W6", "life & integration")],
        [(0, 1), (1, 2), (2, 3)],
        "Six weeks form one family journey",
        "Cycle 1 modules",
    ),
)
_reg(
    "c1-w6-memory-line-path",
    lambda: process_flow(
        "c1-w6-memory-line-path",
        "Memory Line Path",
        "Six-week recall without ranking",
        ["W1 line", "W2 line", "W3 line", "W4 line", "W5 line", "W6 line"],
        "Cycle 1 memory design",
    ),
)
_reg(
    "c1-w6-family-presentation",
    lambda: analogy_diagram(
        "c1-w6-family-presentation",
        "Family Presentation Flow",
        "Offering without performance pressure",
        "Performance stage", ["comparison", "anxiety", "ranking"],
        "Family offering", ["gratitude", "shared learning", "no grades"],
        "Families share growth gently",
        "Not a competition or exam",
        "KUT-CHARTER integration",
    ),
)
_reg(
    "c1-w6-integration-verses",
    lambda: verse_card(
        "c1-w6-integration-verses",
        "Integration Verse Card",
        "Cycle 1 key verses review",
        "Cycle 1 key verses",
        "SB 1.2.18 · BG 2.13 · BG 2.20 · BG 2.40 · BG 5.22 — paraphrase review only",
        "https://vedabase.io/en/library/sb/1/2/18/",
        "No new verses introduced tonight",
        "Cycle 1 verse set",
    ),
)
_reg(
    "c1-w6-session-map",
    lambda: process_flow(
        "c1-w6-session-map",
        "Integration Session Map",
        "Stations and recall flow",
        ["Arrival", "Station recall", "Family share", "Commitment card", "Closing prayer", "Departure"],
        "C1-W6 integration guide",
    ),
)
_reg(
    "c1-w6-home-practice",
    lambda: practice_card(
        "c1-w6-home-practice",
        "Family Commitment Card",
        "One family living decision",
        "After integration night",
        ["Choose one habit to continue", "Write it visibly at home", "Review in four weeks"],
        "One sentence commitment",
        "Revise if unrealistic",
        "KUT-CHARTER",
    ),
)
_reg(
    "c1-w6-gamma-asset-sheet",
    lambda: process_flow(
        "c1-w6-gamma-asset-sheet",
        "Gamma Asset Sheet",
        "Asset selection for integration night",
        ["Pick parent deck", "Pick child deck", "Map SVG assets", "Attach speaker notes", "QA checklist"],
        "Gamma packaging V8",
    ),
)


def write_asset(module_dir: Path, asset_id: str, svg: str) -> None:
    for sub in ("source", "rendered"):
        out = module_dir / "visuals" / sub / f"{asset_id}.svg"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(svg, encoding="utf-8")


def main() -> int:
    count = 0
    missing = []
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir() or not d.name.startswith("c1-w"):
            continue
        manifest = d / "visuals" / "VISUAL-ASSET-MANIFEST.yaml"
        if not manifest.exists():
            continue
        import yaml

        data = yaml.safe_load(manifest.read_text(encoding="utf-8"))
        for asset in data.get("assets", []):
            aid = asset["asset_id"]
            if aid not in BUILDERS:
                missing.append(aid)
                continue
            svg = BUILDERS[aid]()
            write_asset(d, aid, svg)
            count += 1
    print(f"Generated {count} SVG assets")
    if missing:
        print("Missing builders:", ", ".join(missing))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
