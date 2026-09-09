# -*- coding: utf-8 -*-
from pathlib import Path

BASE = Path("11-weekly-program-library/first-six-months")
dirs = [
    "c2-w5-māyā-decorating-the-prison-cell",
    "c2-w6-integration-night-choice-consequence-and-the-modes",
    "c3-w1-who-is-god-the-supreme-enjoyer-proprietor-and-friend",
    "c3-w2-who-is-kṛṣṇa-the-supreme-personality-of-godhead",
    "c3-w3-guru-sādhu-and-śāstra-how-we-receive-spiritual-knowledge",
    "c3-w4-śrī-caitanya-mahāprabhu-and-the-holy-name",
    "c3-w5-the-nine-processes-of-bhakti",
    "c3-w6-bhakti-mela-kīrtana-drama-and-family-presentation",
]
codes = ["C2-W5", "C2-W6", "C3-W1", "C3-W2", "C3-W3", "C3-W4", "C3-W5", "C3-W6"]
forbidden = "Use week research ANALOGIES-AND-LIMITS and CASE-STUDIES"
companions = [
    "teacher/YOUNGER-TEACHER-GUIDE.md",
    "teacher/OLDER-TEACHER-GUIDE.md",
    "activities/YOUNGER-ACTIVITY-PACK.md",
    "activities/OLDER-ACTIVITY-PACK.md",
    "activities/OLDER-ANSWER-KEY.md",
    "research/SCRIPTURAL-EXAMPLES.md",
    "research/ANALOGIES-AND-LIMITS.md",
    "research/CASE-STUDIES.md",
    "research/DEVOTIONAL-AND-HISTORICAL-EXAMPLES.md",
    "research/SCIENCE-AND-APPLICATION.md",
]

print(f"{'Code':8} {'Chars':>8} {'Bytes':>8} {'OK':>4}")
short = []
for code, d in zip(codes, dirs):
    p = BASE / d / "teacher" / "MAIN-FACILITATOR-GUIDE-V12.md"
    t = p.read_text(encoding="utf-8")
    ok = len(t) >= 15000
    if not ok:
        short.append((code, len(t)))
    print(f"{code:8} {len(t):8} {p.stat().st_size:8} {'YES' if ok else 'NO':>4}  forbid={forbidden in t}")
    missing = [f for f in companions if not (BASE / d / f).exists()]
    if missing:
        print("  MISSING", missing)
    y = (BASE / d / "teacher" / "YOUNGER-TEACHER-GUIDE.md").read_text(encoding="utf-8")
    if "Week craft tied to" in y:
        print("  younger has 'Week craft tied to'")
    if "Minute-by-minute executable plan" not in y:
        print("  younger missing minute-by-minute plan")
    # flag thin 'See activities' as sole instruction
    if y.count("See activities") and len(y) < 1500:
        print("  younger looks thin with See activities")

print("short:", short)
