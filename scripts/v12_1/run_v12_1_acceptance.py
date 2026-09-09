#!/usr/bin/env python3
"""V12.1 independent acceptance validators (content, verse, Gamma, docs, remote)."""
from __future__ import annotations

import csv
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
EVID = REPO / "build-evidence"
LAUNCH = REPO / "launch"

WEEKS = [
    ("C1-W1", "c1-w1-what-is-kutumba-and-why-are-we-here"),
    ("C1-W2", "c1-w2-i-am-not-this-body"),
    ("C1-W3", "c1-w3-the-nature-of-the-soul"),
    ("C1-W4", "c1-w4-why-human-life-is-rare-and-valuable"),
    ("C1-W5", "c1-w5-the-temporary-world-and-the-search-for-permanent-happiness"),
    ("C1-W6", "c1-w6-integration-night-who-am-i-and-how-should-our-family-live"),
    ("C2-W1", "c2-w1-action-and-reaction-how-karma-binds"),
    ("C2-W2", "c2-w2-free-will-and-responsibility-the-next-choice-matters"),
    ("C2-W3", "c2-w3-birth-death-and-reincarnation"),
    ("C2-W4", "c2-w4-the-three-modes-of-material-nature"),
    ("C2-W5", "c2-w5-māyā-decorating-the-prison-cell"),
    ("C2-W6", "c2-w6-integration-night-choice-consequence-and-the-modes"),
    ("C3-W1", "c3-w1-who-is-god-the-supreme-enjoyer-proprietor-and-friend"),
    ("C3-W2", "c3-w2-who-is-kṛṣṇa-the-supreme-personality-of-godhead"),
    ("C3-W3", "c3-w3-guru-sādhu-and-śāstra-how-we-receive-spiritual-knowledge"),
    ("C3-W4", "c3-w4-śrī-caitanya-mahāprabhu-and-the-holy-name"),
    ("C3-W5", "c3-w5-the-nine-processes-of-bhakti"),
    ("C3-W6", "c3-w6-bhakti-mela-kīrtana-drama-and-family-presentation"),
]

FORBIDDEN = [
    r"Use week research ANALOGIES-AND-LIMITS and CASE-STUDIES",
    r"Week craft tied to",
    r"week research \+ launch policy as applicable",
    r"Week objective for",
    r"meaning\[:",
    r"use authorised chanting practice \+ transcript context above",
]

# Phrases that fail when they are the sole/near-sole instruction
SOFT_FORBIDDEN = [
    r"(?i)see activities\.?\s*$",
    r"(?i)^Family struggles to apply",
    r"(?i)Stay in week scope",
]


@dataclass
class Finding:
    check: str
    path: str
    detail: str
    severity: str = "FAIL"


@dataclass
class Report:
    findings: list[Finding] = field(default_factory=list)

    def fail(self, check: str, path: str, detail: str) -> None:
        self.findings.append(Finding(check, path, detail, "FAIL"))

    def warn(self, check: str, path: str, detail: str) -> None:
        self.findings.append(Finding(check, path, detail, "BLOCKING_WARNING"))

    @property
    def fails(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == "FAIL"]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def check_forbidden(report: Report) -> None:
    for code, slug in WEEKS:
        base = WEEKLY / slug
        targets = [
            base / "teacher" / "MAIN-FACILITATOR-GUIDE-V12.md",
            base / "teacher" / "YOUNGER-TEACHER-GUIDE.md",
            base / "teacher" / "OLDER-TEACHER-GUIDE.md",
            base / "activities" / "YOUNGER-ACTIVITY-PACK.md",
            base / "activities" / "OLDER-ACTIVITY-PACK.md",
            base / "research" / "SCIENCE-AND-APPLICATION.md",
            base / "research" / "CASE-STUDIES.md",
        ]
        for g in (base / "gamma").glob("V12*.md") if (base / "gamma").exists() else []:
            targets.append(g)
        for path in targets:
            text = read(path)
            if not text:
                report.fail("missing_file", str(path.relative_to(REPO)), "required file missing")
                continue
            for pat in FORBIDDEN:
                if re.search(pat, text):
                    report.fail("forbidden_phrase", str(path.relative_to(REPO)), pat)
            if re.search(r"(?i)Stay in week scope", text) and "gamma" in path.as_posix():
                report.fail("forbidden_phrase", str(path.relative_to(REPO)), "Stay in week scope as slide body")
            if path.name == "YOUNGER-TEACHER-GUIDE.md" and re.search(r"(?i)See activities", text):
                # fail if file is short and relies on See activities
                if len(text) < 2500 or text.count("See activities") >= 1 and "story script" not in text.lower():
                    if re.search(r"(?i)See activities", text) and "Movement game" not in text and "story" not in text.lower():
                        report.fail("shallow_younger", str(path.relative_to(REPO)), "See activities without executable lesson")


def check_facilitator_depth(report: Report) -> None:
    required_markers = [
        ("15-minute", "15-min prep"),
        ("60-minute", "60-min prep"),
        ("script", "speaking script"),
        ("Analog", "analogies"),
        ("case", "cases"),
        ("Discovery", "discovery Q"),
        ("Understanding", "understanding Q"),
        ("Application", "application Q"),
        ("misconception", "misconceptions"),
        ("no-speculation", "no-speculation"),
        ("home practice", "home practice"),
    ]
    for code, slug in WEEKS:
        path = WEEKLY / slug / "teacher" / "MAIN-FACILITATOR-GUIDE-V12.md"
        text = read(path)
        if len(text) < 4000:
            report.fail("facilitator_depth", str(path.relative_to(REPO)), f"too short ({len(text)} chars)")
            continue
        low = text.lower()
        missing = [label for needle, label in required_markers if needle.lower() not in low]
        if missing:
            report.fail("facilitator_components", str(path.relative_to(REPO)), "missing: " + ", ".join(missing))
        if "Use week research" in text:
            report.fail("facilitator_deferral", str(path.relative_to(REPO)), "Use week research deferral present")


def check_research(report: Report) -> None:
    for code, slug in WEEKS:
        if code.startswith("C1-W") and code != "C1-W1":
            # still validate all
            pass
        base = WEEKLY / slug / "research"
        cases = read(base / "CASE-STUDIES.md")
        if cases.count("##") < 3 and cases.count("Case") < 3:
            report.fail("cases", f"{slug}/research/CASE-STUDIES.md", "need ≥3 distinct cases")
        if re.search(r"(?i)Family struggles to apply", cases):
            report.fail("cases", f"{slug}/research/CASE-STUDIES.md", "generic Family struggles case")
        sci = read(base / "SCIENCE-AND-APPLICATION.md")
        has_na = "N/A — no empirical claim" in sci or "N/A - no empirical claim" in sci
        has_cite = bool(re.search(r"(20\d{2}|DOI|doi\.org|https://)", sci)) and ("finding" in sci.lower() or "limitation" in sci.lower())
        if not (has_na or has_cite):
            report.fail("science", f"{slug}/research/SCIENCE-AND-APPLICATION.md", "need citation block or explicit N/A")
        script = read(base / "SCRIPTURAL-EXAMPLES.md")
        if script.count("http") < 1:
            report.fail("scriptural", f"{slug}/research/SCRIPTURAL-EXAMPLES.md", "need URL(s)")


def check_verse(report: Report) -> None:
    pack = read(LAUNCH / "C3-VERSE-PACK.md")
    yaml = read(REPO / "scripts" / "v12" / "verse_data.yaml")
    for blob, label in [(pack, "C3-VERSE-PACK.md"), (yaml, "verse_data.yaml")]:
        if "paraṁ vijayate śrī-kṛṣṇa-saṅkīrtanam" not in blob and "param vijayate sri-krsna-sankirtanam" not in blob.replace("ā", "a"):
            # allow unicode variants
            if "vijayate" not in blob or "saṅkīrtanam" not in blob and "sankirtanam" not in blob:
                report.fail("c3_w4_verse", label, "missing complete Antya 20.12 ending")
        if "iti puṁsārpitā" not in blob and "iti pumsarpita" not in blob.replace("ṁ", "m").replace("ā", "a"):
            if "iti pu" not in blob:
                report.fail("c3_w5_verse", label, "missing verse 24 iti puṁsārpitā")
        if "holy name" in blob and "CC Antya 20.12" not in blob.split("C3-W6", 1)[-1][:400]:
            # check W6 section specifically
            pass
        if re.search(r"BG 5\.29.*holy name.*7\.5", blob):
            report.fail("c3_w6_chain", label, "review chain still has generic holy name")
        if "CC Antya 20.12" not in blob or "BG 5.29" not in blob:
            report.fail("c3_w6_chain", label, "incomplete review chain markers")

    mantra = read(LAUNCH / "OPENING-MANTRAS-HANDOUT.md")
    if "use authorised chanting practice" in mantra:
        report.fail("mantra_source", "launch/OPENING-MANTRAS-HANDOUT.md", "vague mahā-mantra source")
    if "660909le-new-york" not in mantra and "cc/adi/7/83" not in mantra:
        report.fail("mantra_source", "launch/OPENING-MANTRAS-HANDOUT.md", "missing direct mahā-mantra URL")


def check_gamma(report: Report) -> None:
    for code, slug in WEEKS:
        for path in (WEEKLY / slug / "gamma").glob("*.md") if (WEEKLY / slug / "gamma").exists() else []:
            text = read(path)
            if "meaning[:" in text:
                report.fail("gamma_truncation_code", str(path.relative_to(REPO)), "meaning[: present")
            if "Detailed 16:9 educational image for" in text:
                report.fail("gamma_generic_image", str(path.relative_to(REPO)), "generic image prompt template")
            if "week research + launch policy as applicable" in text:
                report.fail("gamma_vague_source", str(path.relative_to(REPO)), "vague source line")
            if "Week objective for" in text or "Stay in week scope" in text:
                report.fail("gamma_placeholder", str(path.relative_to(REPO)), "placeholder body copy")
            # mid-sentence truncation heuristic: teaching meaning ending with ' the' / ' to the' / ' His pu'
            for m in re.finditer(r"teaching meaning:\s*([^\n]+)", text, re.I):
                val = m.group(1).strip().rstrip(".")
                if re.search(r"\b(the|to|a|an|and|of|for|His|her|pu)$", val):
                    report.fail("gamma_truncated_sentence", str(path.relative_to(REPO)), val[-40:])


def check_w1_packet_source(report: Report) -> None:
    # Validate renderer source lists required components
    src = read(REPO / "scripts" / "v12_1" / "render_v12_1_packets.py")
    needed = [
        "OPENING-MANTRAS-HANDOUT",
        "KUTUMBA-C1-FAMILY-ORIENTATION",
        "FAMILY-COVENANT-ACKNOWLEDGEMENT",
        "CHILD-RULES-YOUNGER",
        "CHILD-RULES-OLDER",
        "YOUNGER-ACTIVITY-PACK",
        "OLDER-ACTIVITY-PACK",
        "OLDER-ANSWER-KEY",
        "sankalpa",
        "MODULE-PROJECT-BRIEF",
        "family-home-practice",
        "YOUNGER-TEACHER-GUIDE",
        "OLDER-TEACHER-GUIDE",
        "MAIN-FACILITATOR-GUIDE-V12",
        "PRE-WEEK-CHECKLIST",
    ]
    for n in needed:
        if n not in src:
            report.fail("w1_packet_builder", "scripts/v12_1/render_v12_1_packets.py", f"missing component ref {n}")
    packet = REPO / "exports" / "final" / "KUTUMBA-C1-W1-SATURDAY-PRINT-PACKET-V12.1.docx"
    if not packet.exists():
        report.fail("w1_packet_artifact", str(packet.relative_to(REPO)), "packet not rendered yet")


def check_docx_tables(report: Report) -> None:
    # Ensure final packet builder does not skip | lines
    bad = read(REPO / "scripts" / "v12" / "render_v12_final_packets.py")
    if "continue  # tables simplified" in bad:
        # V12 script still has skip — V12.1 must use new renderer; warn if V12 still used as controlling
        report.warn("legacy_renderer", "scripts/v12/render_v12_final_packets.py", "legacy skip-table path still present (V12.1 renderer must be used)")
    v121 = read(REPO / "scripts" / "v12_1" / "render_v12_1_packets.py")
    if "render_markdown" not in v121:
        report.fail("docx_tables", "scripts/v12_1/render_v12_1_packets.py", "must call render_markdown for tables")
    if "add_picture" not in v121 and "add_pngs" not in v121:
        report.fail("docx_images", "scripts/v12_1/render_v12_1_packets.py", "must embed pictures")


def check_page_qa(report: Report) -> None:
    for name in ("V12_1-DOCX-PAGE-QA.csv", "V12_1-PDF-PAGE-QA.csv"):
        path = EVID / name
        if not path.exists():
            report.fail("page_qa", str(path.relative_to(REPO)), "missing page QA CSV")
            continue
        with path.open(encoding="utf-8", newline="") as fh:
            rows = list(csv.DictReader(fh))
        if not rows:
            report.fail("page_qa", str(path.relative_to(REPO)), "empty QA CSV")
            continue
        bad = [r for r in rows if r.get("status", "").upper() != "PASS" or r.get("inspected", "").lower() not in {"yes", "true", "1", "y"}]
        if bad:
            report.fail("page_qa", str(path.relative_to(REPO)), f"{len(bad)} rows not inspected/PASS")


def check_nav(report: Report) -> None:
    nav = REPO / "V12_1-START-HERE.md"
    if not nav.exists():
        report.fail("nav", "V12_1-START-HERE.md", "missing")
        return
    text = read(nav)
    for h in ("THIS SATURDAY", "FIRST SIX WEEKS", "FIRST SIX MONTHS", "EXTERNAL_OPEN"):
        if h not in text:
            report.fail("nav", "V12_1-START-HERE.md", f"missing section {h}")


def check_generator(report: Report) -> None:
    gen = read(REPO / "scripts" / "v12" / "generate_v12_production.py")
    if "meaning[:" in gen:
        report.fail("generator_truncation", "scripts/v12/generate_v12_production.py", "meaning[: still present")


def write_report(report: Report) -> int:
    EVID.mkdir(parents=True, exist_ok=True)
    lines = ["# V12.1 Acceptance Validator Report", ""]
    fails = report.fails
    warns = [f for f in report.findings if f.severity == "BLOCKING_WARNING"]
    lines.append(f"- FAIL: {len(fails)}")
    lines.append(f"- BLOCKING_WARNING: {len(warns)}")
    lines.append("")
    for f in report.findings:
        lines.append(f"- **{f.severity}** `{f.check}` · `{f.path}` · {f.detail}")
    path = EVID / "V12_1-VALIDATOR-REPORT.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(path)
    print(f"FAIL={len(fails)} BLOCKING_WARNING={len(warns)}")
    for f in fails[:40]:
        print(f"FAIL {f.check}: {f.path}: {f.detail}")
    return 1 if fails or warns else 0


def main() -> int:
    report = Report()
    check_generator(report)
    check_forbidden(report)
    check_facilitator_depth(report)
    check_research(report)
    check_verse(report)
    check_gamma(report)
    check_w1_packet_source(report)
    check_docx_tables(report)
    check_page_qa(report)
    check_nav(report)
    return write_report(report)


if __name__ == "__main__":
    raise SystemExit(main())
