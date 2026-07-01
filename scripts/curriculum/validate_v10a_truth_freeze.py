#!/usr/bin/env python3
"""Validate V10A truth-freeze controls without implying human approval."""

from __future__ import annotations

import csv
import hashlib
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
GATE_REGISTER = REPO / "17-reviews-and-audits" / "PILOT-READINESS-GATE-REGISTER.yaml"
CURRENT_STATUS = REPO / "CURRENT-STATUS.md"
THEO_MAP = REPO / "14-research-source-register" / "theology-visual-library" / "krishna-and-expansions" / "DIAGRAM-SOURCE-MAP.yaml"
VISUAL_CATALOG = REPO / "14-research-source-register" / "visual-asset-library" / "VISUAL-ASSET-CATALOG.yaml"
DUP_REPORT = REPO / "build-evidence" / "V10A-VISUAL-DUPLICATE-REPORT.csv"
VALIDATION_REPORT = REPO / "build-evidence" / "V10A-VALIDATION-REPORT.md"

PRIORITY_MEDIA = [
    "c1-w1-what-is-kutumba-and-why-are-we-here",
    "c1-w2-i-am-not-this-body",
    "c1-w3-the-nature-of-the-soul",
    "c1-w4-why-human-life-is-rare-and-valuable",
    "c1-w5-the-temporary-world-and-the-search-for-permanent-happiness",
    "c1-w6-integration-night-who-am-i-and-how-should-our-family-live",
    "c3-w2-who-is-kṛṣṇa-the-supreme-personality-of-godhead",
]

REQUIRED_THEO_NODES = {
    "Kṛṣṇa",
    "Balarāma",
    "first catur-vyūha",
    "Nārāyaṇa",
    "second catur-vyūha",
    "Mahā-Viṣṇu",
    "Garbhodakaśāyī Viṣṇu",
    "Kṣīrodakaśāyī Viṣṇu",
}

APPROVAL_WORDS = {
    "verified-candidate",
    "approved-for-internal-pilot",
    "pilot-approved",
    "approved-for-pilot",
    "approved-for-publication",
    "publication-ready",
    "rendered-reviewed-approved",
}


def load_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return data if isinstance(data, dict) else {}


def sha(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def git_head() -> str:
    return subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=REPO, capture_output=True, text=True, check=False
    ).stdout.strip()


def check_status(failures: list[str]) -> None:
    text = CURRENT_STATUS.read_text(encoding="utf-8")
    required = [
        "Current phase: **internal-development**",
        "| Internal pilot | **NO GO**",
        "| Family-facing distribution | **NO GO**",
        "| Public publication | **NO GO**",
        "Automated validation must not be treated",
    ]
    for marker in required:
        if marker not in text:
            failures.append(f"CURRENT-STATUS missing required V10A marker: {marker}")

    gate_data = load_yaml(GATE_REGISTER)
    blocking_open = [
        g for g in gate_data.get("gates", []) if g.get("classification") == "blocking" and g.get("current_status") == "open"
    ]
    if not blocking_open:
        failures.append("No open blocking pilot gates found")
    if blocking_open and ("Internal pilot | **GO" in text or "Public publication | **GO" in text):
        failures.append("CURRENT-STATUS claims GO while blocking gates are open")


def check_gates(failures: list[str]) -> None:
    data = load_yaml(GATE_REGISTER)
    gates = data.get("gates", [])
    expected = {
        "GATE-SAFE-001",
        "GATE-CPO-002",
        "GATE-WOR-003",
        "GATE-DOC-004",
        "GATE-CIT-005",
        "GATE-PED-006",
        "GATE-VIS-007",
        "GATE-MED-008",
        "GATE-RGT-009",
        "GATE-GAM-010",
        "GATE-PD-011",
        "GATE-TMP-012",
        "GATE-OPS-013",
    }
    seen = {g.get("gate_id") for g in gates}
    if seen != expected:
        failures.append(f"Pilot gate IDs mismatch: expected {sorted(expected)}, got {sorted(seen)}")
    for g in gates:
        if g.get("decision") != "open" and not all([g.get("reviewer_name"), g.get("decision_date"), g.get("evidence_path")]):
            failures.append(f"{g.get('gate_id')}: non-open decision missing named evidence")
        if g.get("reviewer_name") not in (None, "") and g.get("decision") == "open":
            failures.append(f"{g.get('gate_id')}: reviewer name populated while decision still open")


def check_theology(failures: list[str]) -> None:
    data = load_yaml(THEO_MAP)
    if data.get("v10a_status") != "not-approved-not-for-pilot":
        failures.append("Theology map is not marked not-approved-not-for-pilot")
    if data.get("gamma_use") != "excluded" or data.get("facilitator_delivery_use") != "excluded":
        failures.append("Theology map is not excluded from Gamma and facilitator delivery")
    mismatch = data.get("required_node_mismatch", {})
    required = set(mismatch.get("required_nodes", []))
    if required != REQUIRED_THEO_NODES:
        failures.append("Theology required-node list is incomplete")
    if data.get("source_map_status") != "incomplete-no-edge-level-proof-table":
        failures.append("Theology source map is not marked incomplete")


def check_media(failures: list[str]) -> None:
    mandatory = {
        "speaker_or_creator",
        "date",
        "place",
        "stable_exact_url",
        "total_duration",
        "excerpt_start",
        "excerpt_end",
        "transcript_link",
        "supported_claim_ids",
        "audience",
        "age_suitability",
        "link_status",
        "doctrinal_review",
        "pedagogy_review",
    }
    for slug in PRIORITY_MEDIA:
        path = WEEKLY / slug / "audio-video" / "MEDIA-INDEX.yaml"
        data = load_yaml(path)
        if data.get("v10a_maturity") != "reference-record-incomplete":
            failures.append(f"{slug}: missing reference-record-incomplete maturity")
        if data.get("pilot_playback_status") != "prohibited-unless-item-reviewed":
            failures.append(f"{slug}: missing pilot playback prohibition")
        for item in data.get("media", []):
            status = str(item.get("status", ""))
            if status in APPROVAL_WORDS:
                missing = [k for k in mandatory if not item.get(k)]
                if missing:
                    failures.append(f"{slug}/{item.get('media_id')}: approval-like status lacks {missing}")


def check_gamma(failures: list[str]) -> None:
    for d in sorted(WEEKLY.glob("c1-w*")):
        path = d / "gamma" / "GAMMA-ASSET-MAP.yaml"
        data = load_yaml(path)
        if not data:
            failures.append(f"{d.name}: missing Gamma asset map")
            continue
        if data.get("render_status") != "assets-complete-upload-required":
            failures.append(f"{d.name}: render_status must remain packaging-only")
        expected = {
            "v10a_rendered_status": "not-rendered",
            "v10a_post_render_review_status": "not-post-render-reviewed",
            "v10a_pilot_approval_status": "not-approved-for-pilot",
        }
        for key, val in expected.items():
            if data.get(key) != val:
                failures.append(f"{d.name}: {key} must be {val}")


def check_visuals(failures: list[str], warnings: list[str]) -> None:
    catalog = load_yaml(VISUAL_CATALOG)
    if catalog.get("v10a_active_maturity") != "structural-instructional-draft-human-review-required":
        failures.append("Visual catalog missing V10A active maturity")

    hashes: dict[str, list[str]] = defaultdict(list)
    for root in [WEEKLY, REPO / "build-evidence" / "exports" / "Cycle-1-Gamma-Bundle"]:
        if not root.exists():
            continue
        for p in root.rglob("*"):
            if p.suffix.lower() in {".png", ".svg"} and ("c1-w" in str(p).lower() or "Cycle-1-Gamma-Bundle" in str(p)):
                hashes[sha(p)].append(p.relative_to(REPO).as_posix())

    duplicate_groups = {h: paths for h, paths in hashes.items() if len(paths) > 1}
    if not duplicate_groups:
        failures.append("Duplicate visual hash detection did not report any duplicate groups")
    if not DUP_REPORT.exists():
        failures.append("Missing V10A visual duplicate report")
    warnings.append(f"Duplicate visual hash groups detected: {len(duplicate_groups)}")


def check_head_model(failures: list[str]) -> None:
    trace = load_yaml(REPO / "build-evidence" / "V10A-FINDINGS-TRACEABILITY.yaml")
    if trace.get("v10a_traceability", {}).get("baseline_head") != "9c2eebe987f267cdb4181fc6298ff4b8f4d93eb6":
        failures.append("V10A traceability baseline head is missing or wrong")
    ledger = (REPO / "build-evidence" / "V10A-EXECUTION-LEDGER.md").read_text(encoding="utf-8")
    for marker in ["Starting HEAD", "Safety tag", "Internal pilot | NO GO"]:
        if marker not in ledger:
            failures.append(f"Execution ledger missing {marker}")


def write_report(failures: list[str], warnings: list[str]) -> None:
    head = git_head()
    verdict = "PASS" if not failures else "FAIL"
    lines = [
        "# V10A Validation Report",
        "",
        f"HEAD: `{head}`",
        f"Verdict: **{verdict}**",
        "",
        "## Scope",
        "",
        "This validator checks V10A truth-freeze controls. It does not approve doctrine, worship, safeguarding, rights, pedagogy, accessibility, media, Gamma, pilot launch, family distribution, or public publication.",
        "",
        "## Failures",
        "",
    ]
    lines.extend([f"- {f}" for f in failures] or ["- None"])
    lines.extend(["", "## Warnings", ""])
    lines.extend([f"- {w}" for w in warnings] or ["- None"])
    lines.append("")
    VALIDATION_REPORT.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    failures: list[str] = []
    warnings: list[str] = []
    for fn in [
        check_status,
        check_gates,
        check_theology,
        check_media,
        check_gamma,
        check_head_model,
    ]:
        fn(failures)
    check_visuals(failures, warnings)
    write_report(failures, warnings)
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print(f"Total failures: {len(failures)}")
        return 1
    for warning in warnings:
        print(f"WARN: {warning}")
    print("PASS: V10A truth-freeze controls hold; human gates remain open")
    return 0


if __name__ == "__main__":
    sys.exit(main())

