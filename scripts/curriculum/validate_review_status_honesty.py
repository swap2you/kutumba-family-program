#!/usr/bin/env python3
"""Fail when review-status claims enhancement-complete without gold-standard depth."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
PILOT = "c1-w2-i-am-not-this-body"
C1_GOLD_SLUGS = {
    "c1-w1-what-is-kutumba-and-why-are-we-here",
    "c1-w2-i-am-not-this-body",
    "c1-w3-the-nature-of-the-soul",
    "c1-w4-why-human-life-is-rare-and-valuable",
    "c1-w5-the-temporary-world-and-the-search-for-permanent-happiness",
    "c1-w6-integration-night-who-am-i-and-how-should-our-family-live",
}
C2_GOLD_SLUGS = {
    "c2-w1-action-and-reaction-how-karma-binds",
    "c2-w2-free-will-and-responsibility-the-next-choice-matters",
    "c2-w3-birth-death-and-reincarnation",
    "c2-w4-the-three-modes-of-material-nature",
    "c2-w5-māyā-decorating-the-prison-cell",
    "c2-w6-integration-night-choice-consequence-and-the-modes",
}
C3_GOLD_SLUGS = {
    "c3-w1-who-is-god-the-supreme-enjoyer-proprietor-and-friend",
    "c3-w2-who-is-kṛṣṇa-the-supreme-personality-of-godhead",
    "c3-w3-guru-sādhu-and-śāstra-how-we-receive-spiritual-knowledge",
    "c3-w4-śrī-caitanya-mahāprabhu-and-the-holy-name",
    "c3-w5-the-nine-processes-of-bhakti",
    "c3-w6-bhakti-mela-kīrtana-drama-and-family-presentation",
}
GOLD_SLUGS = C1_GOLD_SLUGS | C2_GOLD_SLUGS | C3_GOLD_SLUGS
MIN_GAMMA_LINES = 80
MIN_DOSSIER_LINES = 60
MIN_CLAIMS = 8
MIN_LALA_LINES = 80
MIN_KISORA_LINES = 80
MIN_TRANSITION_LINES = 40
MIN_REVIEW_LINES = 30


def week_code_from_dir(name: str) -> str:
    m = re.match(r"(c\d-w\d+)", name)
    return m.group(1).upper().replace("c", "C").replace("-w", "-W") if m else name


def count_claims(path: Path) -> int:
    if not path.exists():
        return 0
    return len(re.findall(r"-CLM-\d+", path.read_text(encoding="utf-8")))


def read_status(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if ":" in line and not line.strip().startswith("#"):
            k, _, v = line.partition(":")
            out[k.strip()] = v.strip()
    return out


def line_count(path: Path) -> int:
    if not path.exists():
        return 0
    return len(path.read_text(encoding="utf-8").splitlines())


def check_gold_depth(d: Path, label: str) -> list[str]:
    failures: list[str] = []
    gamma = d / "gamma" / "GAMMA-PARENT-DECK-PROMPT.md"
    if line_count(gamma) < MIN_GAMMA_LINES:
        failures.append(f"{label}: gamma parent deck too thin ({line_count(gamma)} lines)")
    dossier = d / "research" / "RESEARCH-DOSSIER.md"
    if line_count(dossier) < MIN_DOSSIER_LINES:
        failures.append(f"{label}: research dossier too thin ({line_count(dossier)} lines)")
    claims = count_claims(d / "research" / "CLAIM-REGISTER.yaml")
    if claims < MIN_CLAIMS:
        failures.append(f"{label}: claim register too thin ({claims} claims)")
    lala = d / "children" / "lala-lali-lesson.md"
    if line_count(lala) < MIN_LALA_LINES:
        failures.append(f"{label}: lala-lali lesson too thin ({line_count(lala)} lines)")
    kisora = d / "children" / "kisora-kisori-lesson.md"
    if line_count(kisora) < MIN_KISORA_LINES:
        failures.append(f"{label}: kisora-kisori lesson too thin ({line_count(kisora)} lines)")
    trans = d / "children" / "shared-family-transition.md"
    if line_count(trans) < MIN_TRANSITION_LINES:
        failures.append(f"{label}: shared-family-transition too thin ({line_count(trans)} lines)")
    for rn in ["DOCTRINAL-REVIEW.md", "PEDAGOGY-REVIEW.md"]:
        rv = d / "reviews" / rn
        if line_count(rv) < MIN_REVIEW_LINES:
            failures.append(f"{label}: {rn} too thin ({line_count(rv)} lines)")
    if not (d / "opening-hook.md").exists():
        failures.append(f"{label}: missing opening-hook.md")
    if not (d / "katha" / "KATHA-SOURCE-REGISTER.yaml").exists():
        failures.append(f"{label}: missing katha/KATHA-SOURCE-REGISTER.yaml")
    return failures


def main() -> int:
    failures: list[str] = []
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir():
            continue
        rs = d / "review-status.yaml"
        if not rs.exists():
            failures.append(f"Missing review-status.yaml in {d.name}")
            continue
        status = read_status(rs)
        pack = status.get("weekly_derivative_pack", "")
        if pack != "enhancement-complete":
            continue
        if d.name not in GOLD_SLUGS:
            failures.append(
                f"{week_code_from_dir(d.name)}: enhancement-complete reserved for gold-standard modules only"
            )
            continue
        failures.extend(check_gold_depth(d, week_code_from_dir(d.name)))

    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir() or d.name not in GOLD_SLUGS:
            continue
        rs = d / "review-status.yaml"
        if not rs.exists():
            continue
        status = read_status(rs)
        pack = status.get("weekly_derivative_pack", "")
        depth_ok = len(check_gold_depth(d, week_code_from_dir(d.name))) == 0
        if pack == "baseline-scaffold" and depth_ok:
            failures.append(
                f"{week_code_from_dir(d.name)}: has gold depth but review-status still baseline-scaffold"
            )

    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir() or d.name in GOLD_SLUGS:
            continue
        rs = d / "review-status.yaml"
        if not rs.exists():
            continue
        status = read_status(rs)
        pack = status.get("weekly_derivative_pack", "")
        if pack in {"", "baseline-scaffold"}:
            for key, val in status.items():
                if val == "complete" and key in {
                    "research_dossier",
                    "gamma_prompts",
                    "claim_traceability",
                    "source_registry",
                }:
                    failures.append(
                        f"{week_code_from_dir(d.name)}: {key}=complete inconsistent with baseline-scaffold"
                    )

    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        print(f"Total failures: {len(failures)}")
        return 1
    print("PASS: review-status labels honest relative to enhancement depth")
    return 0


if __name__ == "__main__":
    sys.exit(main())
