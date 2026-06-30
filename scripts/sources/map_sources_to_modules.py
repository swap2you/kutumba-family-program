#!/usr/bin/env python3
"""Map public source catalog entries to first-six-month modules."""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
MODULES_ROOT = REPO / "11-weekly-program-library/first-six-months"
MAP_OUT = REPO / "14-research-source-register/public-source-catalog/SOURCE-TO-MODULE-MAP.yaml"
REPORT = REPO / "build-evidence/MODULE-SOURCE-COVERAGE-REPORT.md"

TODAY = date.today().isoformat()

MODULE_SPECS: list[dict] = [
    {
        "module_id": "C1-W1",
        "slug": "c1-w1-what-is-kutumba-and-why-are-we-here",
        "title": "What Is KUTUMBA and Why Are We Here",
        "controlling_books": ["SB 1.1", "BG introduction themes"],
        "vedabase": ["https://vedabase.io/en/library/sb/", "https://vedabase.io/en/library/transcripts/"],
        "lectures": ["SB 1.1 lecture candidates — Vedabase transcript library"],
        "education": ["https://iskconeducation.org/philosophy-of-education/"],
        "excluded": ["Desire Tree bulk PDF directories"],
    },
    {
        "module_id": "C1-W2",
        "slug": "c1-w2-i-am-not-this-body",
        "title": "I Am Not This Body",
        "controlling_books": ["BG 2.13", "BG 2.22", "BG 13.1-3"],
        "vedabase": ["https://vedabase.io/en/library/bg/", "https://vedabase.io/en/library/transcripts/"],
        "lectures": ["BG 2.13 London 1973", "BG 2.22 London 1973"],
        "education": ["https://iskconeducation.org/materials/"],
        "excluded": ["Anonymous quote pages without Vanisource context"],
    },
    {
        "module_id": "C1-W3",
        "slug": "c1-w3-the-nature-of-the-soul",
        "title": "The Nature of the Soul",
        "controlling_books": ["BG 2.20", "BG 2.23-25", "SB soul teachings"],
        "vedabase": ["https://vedabase.io/en/library/bg/"],
        "lectures": ["BG 2.20 lecture candidates"],
        "education": ["https://iskconeducation.org/books-for-kids/"],
        "excluded": [],
    },
    {
        "module_id": "C1-W4",
        "slug": "c1-w4-why-human-life-is-rare-and-valuable",
        "title": "Why Human Life Is Rare and Valuable",
        "controlling_books": ["BG 8.6", "SB human form teachings"],
        "vedabase": ["https://vedabase.io/en/library/bg/", "https://vedabase.io/en/library/sb/"],
        "lectures": [],
        "education": ["https://iskconeducation.org/article/starting-a-sunday-school/"],
        "excluded": [],
    },
    {
        "module_id": "C1-W5",
        "slug": "c1-w5-the-temporary-world-and-the-search-for-permanent-happiness",
        "title": "The Temporary World and Permanent Happiness",
        "controlling_books": ["BG 8.15", "BG 13.27-28"],
        "vedabase": ["https://vedabase.io/en/library/bg/"],
        "lectures": [],
        "education": [],
        "excluded": [],
    },
    {
        "module_id": "C1-W6",
        "slug": "c1-w6-integration-night-who-am-i-and-how-should-our-family-live",
        "title": "Integration Night — Who Am I",
        "controlling_books": ["Cycle 1 integration — BG 2.x synthesis"],
        "vedabase": ["https://vedabase.io/en/library/"],
        "lectures": [],
        "education": ["https://iskconcongregation.com/programs/bhakti-vriksha/"],
        "excluded": ["Bhakti-vṛkṣa as operating model replacement"],
    },
    {
        "module_id": "C2-W1",
        "slug": "c2-w1-action-and-reaction-how-karma-binds",
        "title": "Action and Reaction — Karma",
        "controlling_books": ["BG 3.9", "BG 4.17", "BG 9.2"],
        "vedabase": ["https://vedabase.io/en/library/bg/"],
        "lectures": [],
        "education": [],
        "excluded": [],
    },
    {
        "module_id": "C2-W2",
        "slug": "c2-w2-free-will-and-responsibility-the-next-choice-matters",
        "title": "Free Will and Responsibility",
        "controlling_books": ["BG 3.27", "BG 5.14"],
        "vedabase": ["https://vedabase.io/en/library/bg/"],
        "lectures": [],
        "education": [],
        "excluded": [],
    },
    {
        "module_id": "C2-W3",
        "slug": "c2-w3-birth-death-and-reincarnation",
        "title": "Birth, Death and Reincarnation",
        "controlling_books": ["SB 5.8-5.9 Bhārata Mahārāja", "BG 2.13"],
        "vedabase": ["https://vedabase.io/en/library/sb/"],
        "lectures": [],
        "education": [],
        "supplementary": [],
        "excluded": ["Partial SB 5.8.1-only mapping for full Bharata narrative"],
    },
    {
        "module_id": "C2-W4",
        "slug": "c2-w4-the-three-modes-of-material-nature",
        "title": "Three Modes of Material Nature",
        "controlling_books": ["BG 14.5-18", "BG 18.19-40"],
        "vedabase": ["https://vedabase.io/en/library/bg/"],
        "lectures": [],
        "education": [],
        "excluded": [],
    },
    {
        "module_id": "C2-W5",
        "slug": "c2-w5-māyā-decorating-the-prison-cell",
        "title": "Māyā Decorating the Prison Cell",
        "controlling_books": ["BG 7.14", "BG 15.1-4"],
        "vedabase": ["https://vedabase.io/en/library/bg/"],
        "lectures": [],
        "education": [],
        "excluded": [],
    },
    {
        "module_id": "C2-W6",
        "slug": "c2-w6-integration-night-choice-consequence-and-the-modes",
        "title": "Integration Night — Choice and Modes",
        "controlling_books": ["Cycle 2 synthesis"],
        "vedabase": ["https://vedabase.io/en/library/bg/"],
        "lectures": [],
        "education": [],
        "excluded": [],
    },
    {
        "module_id": "C3-W1",
        "slug": "c3-w1-who-is-god-the-supreme-enjoyer-proprietor-and-friend",
        "title": "Who Is God — Enjoyer, Proprietor, Friend",
        "controlling_books": ["BG 5.29", "SB 10.24 Govardhana stewardship"],
        "vedabase": ["https://vedabase.io/en/library/bg/", "https://vedabase.io/en/library/sb/"],
        "lectures": [],
        "education": [],
        "excluded": ["SB 10.14 mislabeled as gopī prayers"],
    },
    {
        "module_id": "C3-W2",
        "slug": "c3-w2-who-is-kṛṣṇa-the-supreme-personality-of-godhead",
        "title": "Who Is Kṛṣṇa — SPG",
        "controlling_books": ["SB 10.3 appearance", "SB 10.5 transfer to Gokula"],
        "vedabase": ["https://vedabase.io/en/library/sb/"],
        "lectures": [],
        "education": [],
        "excluded": ["Imprecise Vṛndāvana birth geography"],
    },
    {
        "module_id": "C3-W3",
        "slug": "c3-w3-guru-sādhu-and-śāstra-how-we-receive-spiritual-knowledge",
        "title": "Guru, Sādhu and Śāstra",
        "controlling_books": ["SB 1.5 Nārada instructs Vyāsa", "SB 1.6 Nārada childhood"],
        "vedabase": ["https://vedabase.io/en/library/sb/"],
        "lectures": [],
        "education": [],
        "excluded": ["SB 1.4.25 as Nārada receiving Bhāgavatam"],
    },
    {
        "module_id": "C3-W4",
        "slug": "c3-w4-śrī-caitanya-mahāprabhu-and-the-holy-name",
        "title": "Śrī Caitanya and the Holy Name",
        "controlling_books": ["CC Ādi", "SB holy name themes"],
        "vedabase": ["https://vedabase.io/en/library/cc/"],
        "lectures": [],
        "education": [],
        "excluded": [],
    },
    {
        "module_id": "C3-W5",
        "slug": "c3-w5-the-nine-processes-of-bhakti",
        "title": "Nine Processes of Bhakti",
        "controlling_books": ["SB 7.5.23-24", "BG 9.26-27"],
        "vedabase": ["https://vedabase.io/en/library/sb/", "https://vedabase.io/en/library/bg/"],
        "lectures": [],
        "education": [],
        "excluded": [],
    },
    {
        "module_id": "C3-W6",
        "slug": "c3-w6-bhakti-mela-kīrtana-drama-and-family-presentation",
        "title": "Bhakti Mela — Kīrtana and Family Presentation",
        "controlling_books": ["Congregation presentation — not lecture-heavy"],
        "vedabase": ["https://prabhupadavani.org/audio/"],
        "lectures": [],
        "education": ["https://iskconeducation.org/video/"],
        "media": ["https://www.youtube.com/channel/UCBN88f0nRlRMg1CnffvinXw"],
        "excluded": ["Bulk bhajan downloads"],
    },
]


def coverage_scores(spec: dict) -> dict:
    return {
        "primary_text_coverage": "planned" if spec.get("controlling_books") else "gap",
        "prabhupada_spoken_source_coverage": "candidate-listed" if spec.get("lectures") else "to-be-selected",
        "katha_coverage": "human-review-required",
        "parent_application_coverage": "draft",
        "lala_lali_coverage": "draft",
        "kisora_kisori_coverage": "draft",
        "visual_media_coverage": "metadata-only",
        "rights_readiness": "link-and-metadata-only",
        "human_review_readiness": "open",
    }


def brief_markdown(spec: dict) -> str:
    books = "\n".join(f"- {b}" for b in spec.get("controlling_books", []))
    vedabase = "\n".join(f"- {u}" for u in spec.get("vedabase", [])) or "- TBD"
    lectures = "\n".join(f"- {l}" for l in spec.get("lectures", [])) or "- No reviewed lecture entry yet"
    edu = "\n".join(f"- {u}" for u in spec.get("education", [])) or "- None mapped yet"
    supp = "\n".join(f"- {s}" for s in spec.get("supplementary", [])) or "- None at this time"
    media = "\n".join(f"- {m}" for m in spec.get("media", [])) or "- See module MEDIA-INDEX.yaml"
    excluded = "\n".join(f"- {e}" for e in spec.get("excluded", [])) or "- None stated"
    scores = coverage_scores(spec)
    score_lines = "\n".join(f"| {k.replace('_', ' ').title()} | {v} |" for k, v in scores.items())
    return f"""# Source Expansion Brief — {spec["module_id"]}

| Field | Value |
|-------|-------|
| Module | {spec["title"]} |
| Generated | {TODAY} |
| Source map | KUT-SRC-0013 |
| Human review | **OPEN** |

## 1. Controlling Prabhupāda book references

{books}

## 2. Prabhupāda lecture / conversation / letter candidates

{lectures}

## 3. Source-grounded kathā references

- Align `katha/KATHA-SOURCE-REGISTER.yaml` with narrative claims
- Prefer Tier A VedaBase exact references

## 4. Official education / pedagogy resources

{edu}

## 5. Child-resource candidates

- Ministry books-for-kids and Sunday School indexes — metadata only
- KUTUMBA-authored adaptation required

## 6. Media candidates

{media}

## 7. Supplementary Gauḍīya / Sanātana references

{supp}

## 8. Sources intentionally excluded

{excluded}

## 9. Rights posture

- Default: **link-and-metadata-only**
- BBT material: permission workflow before republication

## 10. Review required

- Doctrinal review: OPEN
- Rights review: OPEN
- Pedagogy review: OPEN

## Tier A entry points

{vedabase}

## Coverage scores (not publication approval)

| Dimension | Score |
|-----------|-------|
{score_lines}
"""


def find_module_dir(slug_prefix: str) -> Path | None:
    for d in MODULES_ROOT.iterdir():
        if d.is_dir() and d.name.startswith(slug_prefix.split("-")[0] + "-"):
            if slug_prefix in d.name or d.name.startswith(slug_prefix[:10]):
                pass
        if d.is_dir() and slug_prefix in d.name:
            return d
    # fallback: match by module_id prefix e.g. c1-w2
    mid = slug_prefix.split("-")[0] + "-" + slug_prefix.split("-")[1]
    for d in MODULES_ROOT.iterdir():
        if d.is_dir() and d.name.startswith(mid):
            return d
    return None


def main() -> int:
    modules = []
    for spec in MODULE_SPECS:
        mod_dir = None
        for d in MODULES_ROOT.iterdir():
            if not d.is_dir():
                continue
            if d.name == spec["slug"] or spec["module_id"].lower().replace("-", "") in d.name.replace("-", ""):
                mod_dir = d
                break
        if mod_dir is None:
            mid = spec["module_id"].lower()
            for d in MODULES_ROOT.iterdir():
                if d.is_dir() and d.name.startswith(mid.replace("-w", "-w")):
                    mod_dir = d
                    break
        if mod_dir is None:
            # prefix match c1-w1 etc
            prefix = spec["module_id"].lower().replace("-", "-")
            parts = spec["slug"].split("-")[:2]
            prefix2 = "-".join(parts)
            for d in MODULES_ROOT.iterdir():
                if d.is_dir() and d.name.startswith(prefix2):
                    mod_dir = d
                    break
        if mod_dir is None:
            print(f"WARN: module dir not found for {spec['module_id']}", file=sys.stderr)
            continue
        research = mod_dir / "research"
        research.mkdir(parents=True, exist_ok=True)
        (research / "SOURCE-EXPANSION-BRIEF.md").write_text(brief_markdown(spec), encoding="utf-8")
        modules.append(
            {
                "module_id": spec["module_id"],
                "module_path": str(mod_dir.relative_to(REPO)).replace("\\", "/"),
                "controlling_books": spec.get("controlling_books", []),
                "tier_a_urls": spec.get("vedabase", []),
                "lecture_candidates": spec.get("lectures", []),
                "education_urls": spec.get("education", []),
                "media_urls": spec.get("media", []),
                "supplementary": spec.get("supplementary", []),
                "excluded": spec.get("excluded", []),
                "rights_posture": "link-and-metadata-only",
                "review_status": "human-review-required",
                "coverage": coverage_scores(spec),
            }
        )

    MAP_OUT.parent.mkdir(parents=True, exist_ok=True)
    MAP_OUT.write_text(
        yaml.safe_dump(
            {
                "map_version": "1.0.0",
                "generated": TODAY,
                "source_map_id": "KUT-SRC-0013",
                "module_count": len(modules),
                "modules": modules,
            },
            sort_keys=False,
            allow_unicode=True,
        ),
        encoding="utf-8",
    )

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(
        f"""# Module Source Coverage Report

Generated: {TODAY}

## Summary

| Metric | Value |
|--------|-------|
| Modules mapped | {len(modules)} |
| Source map | KUT-SRC-0013 |
| Default rights posture | link-and-metadata-only |
| Human review | OPEN all modules |

## Per-module briefs

Each module has `research/SOURCE-EXPANSION-BRIEF.md`.

## Scoring note

Coverage scores indicate planning depth only — **not** publication approval.
""",
        encoding="utf-8",
    )
    print(f"Mapped {len(modules)} modules")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
