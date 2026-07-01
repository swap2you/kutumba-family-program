"""Extract and measure Prem-kī-Kathā narrative section only."""
from __future__ import annotations

import re
from pathlib import Path

NARRATIVE_HEADING = re.compile(r"^##\s+6\.\s+Source-grounded narrative\s*$", re.I | re.M)
NEXT_HEADING = re.compile(r"^##\s+\d+\.", re.M)
WORD_RE = re.compile(r"\b[\w'-]+\b", re.UNICODE)
FACILITATOR_LINE = re.compile(r"^\s*_\s*\[Facilitator|^\s*\*\*Facilitator", re.I | re.M)
BOILERPLATE_PHRASES = [
    "before precise philosophy, the heart needs a real scene",
    "parents need not perform perfect devotion",
    "honor grief, fear, and confusion",
    "all narrative here is **paraphrase**",
    "the katha opens the heart; the philosophy block",
]

INTEGRATION_SLUGS = {
    "c1-w6-integration-night-who-am-i-and-how-should-our-family-live",
    "c2-w6-integration-night-choice-consequence-and-the-modes",
    "c3-w6-bhakti-mela-kirtana-drama-and-family-presentation",
}


def strip_frontmatter(text: str) -> str:
    return re.sub(r"^---.*?---\s*", "", text, count=1, flags=re.DOTALL)


def extract_narrative_section(text: str) -> str:
    body = strip_frontmatter(text)
    m = NARRATIVE_HEADING.search(body)
    if not m:
        return ""
    rest = body[m.end() :]
    n = NEXT_HEADING.search(rest)
    return rest[: n.start()] if n else rest


def word_count(text: str) -> int:
    return len(WORD_RE.findall(text))


def classify_narrative_words(narrative: str) -> dict[str, int]:
    lines = narrative.splitlines()
    narrative_words = 0
    facilitator_words = 0
    for line in lines:
        wc = word_count(line)
        if not wc:
            continue
        if FACILITATOR_LINE.match(line) or line.strip().startswith("_[Facilitator"):
            facilitator_words += wc
        else:
            narrative_words += wc
    return {
        "narrative_words": narrative_words,
        "facilitator_note_words": facilitator_words,
        "interaction_words": 0,
    }


def narrative_metrics(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    body = strip_frontmatter(raw)
    narrative = extract_narrative_section(raw)
    counts = classify_narrative_words(narrative)
    total = word_count(body)
    narr_w = counts["narrative_words"]
    minutes_low = narr_w / 135 if narr_w else 0
    minutes_high = narr_w / 115 if narr_w else 0
    paras = [p for p in narrative.split("\n\n") if word_count(p) >= 20]
    events = len(re.findall(r"\*\*Paraphrase", narrative))
    boiler = sum(1 for p in BOILERPLATE_PHRASES if p in narrative.lower())
    boiler_pct = int(100 * boiler / max(1, len(BOILERPLATE_PHRASES)))
    slug = path.parent.name
    integration = slug in INTEGRATION_SLUGS or "integration_exception:" in raw[:500]
    min_n, max_n = (350, 700) if integration else (700, 1200)
    return {
        "slug": slug,
        "narrative_words": narr_w,
        "facilitator_note_words": counts["facilitator_note_words"],
        "total_file_words": total,
        "minutes_low": round(minutes_low, 1),
        "minutes_high": round(minutes_high, 1),
        "source_paragraphs": events,
        "unique_events": len(paras),
        "boilerplate_pct": boiler_pct,
        "integration": integration,
        "meets_depth": min_n <= narr_w <= max_n,
        "min_narrative": min_n,
        "max_narrative": max_n,
    }
