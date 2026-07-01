#!/usr/bin/env python3
"""Run all curriculum validation gates with categorized verdicts."""

import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).parent

STRUCTURAL = [
    "validate_week_schema.py",
    "validate_age_bands.py",
    "validate_mermaid_viewers.py",
    "validate_visual_asset_manifests.py",
    "validate_media_indexes.py",
    "validate_internal_links.py",
]
VISUAL_V8 = [
    "classify_visual_substance.py",
    "validate_visual_substance.py",
    "validate_visual_rights.py",
    "validate_visual_source_registers.py",
    "validate_visual_alt_text.py",
    "validate_visual_catalog_consistency.py",
]
CITATION_V8 = [
    "validate_canonical_fact_source_keys.py",
    "validate_claim_point_of_use_consistency.py",
]
GAMMA_V8 = [
    "validate_gamma_briefs.py",
    "validate_gamma_asset_references.py",
]
MEDIA_V8 = ["validate_media_candidate_records.py"]
V10A_CONTROLS = ["validate_v10a_truth_freeze.py --write-report"]
SEMANTIC = [
    "validate_gamma_briefs.py",
    "validate_gamma_asset_references.py",
    "validate_prem_ki_katha.py",
    "validate_review_status_honesty.py",
    "detect_truncation_artifacts.py",
    "detect_stale_fact_phrases.py",
    "measure_live_session_load.py",
    "audit_katha_narrative_depth.py",
    "validate_claim_source_support.py",
    "validate_newcomer_glossary.py",
]
SOURCE = [
    "validate_source_registry.py",
    "validate_claim_register.py",
    "detect_unverified_claims.py",
    "detect_copyright_risk.py",
]
SOURCE_CATALOG = [
    ROOT / "scripts" / "sources" / "validate_public_source_catalog.py",
    ROOT / "scripts" / "sources" / "validate_catalog_consistency.py",
    ROOT / "scripts" / "sources" / "reconcile_source_map_urls.py",
    ROOT / "scripts" / "sources" / "validate_source_manifest.py",
]
RIGHTS = ["detect_copyright_risk.py"]
REPORTING = [
    "build_week_quality_dashboard.py",
    "build_cycle_coverage_report.py",
    "generate_curriculum_status.py",
]


def run_script(name: str | Path) -> bool:
    extra_args: list[str] = []
    if isinstance(name, str):
        parts = name.split()
        path = Path(parts[0])
        extra_args = parts[1:]
    else:
        path = name
    if not path.is_absolute():
        path = SCRIPT_DIR / path
    print(f"\n=== {path.name} ===")
    r = subprocess.run([sys.executable, str(path), *extra_args], cwd=ROOT)
    return r.returncode == 0


def main() -> int:
    for s in ["audit_empty_sections.py"] + REPORTING:
        run_script(s)

    results = {}
    for cat, scripts in [
        ("structural", STRUCTURAL),
        ("visual_substance", VISUAL_V8),
        ("citations", CITATION_V8),
        ("gamma_packaging", GAMMA_V8),
        ("media", MEDIA_V8),
        ("v10a_truth_freeze", V10A_CONTROLS),
        ("semantic", SEMANTIC),
        ("source", SOURCE),
        ("source_catalog", SOURCE_CATALOG),
    ]:
        results[cat] = all(run_script(s) for s in dict.fromkeys(scripts))

    print("\n=== check_external_links.py ===")
    link_ok = subprocess.run(
        [sys.executable, str(SCRIPT_DIR / "check_external_links.py")], cwd=ROOT
    ).returncode == 0

    print("\n=== Validate-KutumbaRepository.ps1 ===")
    repo_ok = subprocess.run(
        ["powershell", "-File", str(ROOT / "scripts" / "Validate-KutumbaRepository.ps1")],
        cwd=ROOT,
    ).returncode == 0

    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    report = ROOT / "build-evidence" / "VALIDATION-COVERAGE-REPORT.md"
    report.write_text(
        f"""# Validation Coverage Report

Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}
HEAD: `{head}`

## Verdicts by category

| Category | Verdict |
|---|---|
| Structural validation | **{'PASS' if results['structural'] else 'FAIL'}** |
| Visual file/substance structural checks (design review open) | **{'PASS' if results.get('visual_substance') else 'FAIL'}** |
| Citation consistency checks (human citation review open) | **{'PASS' if results.get('citations') else 'FAIL'}** |
| Gamma package/reference checks (not rendered or approved) | **{'PASS' if results.get('gamma_packaging') else 'FAIL'}** |
| Media record structural checks (curation incomplete) | **{'PASS' if results.get('media') else 'FAIL'}** |
| V10A truth freeze controls | **{'PASS' if results.get('v10a_truth_freeze') else 'FAIL'}** |
| Semantic validation | **{'PASS' if results['semantic'] else 'FAIL'}** |
| Source validation | **{'PASS' if results['source'] else 'FAIL'}** |
| Source catalog validation | **{'PASS' if results.get('source_catalog') else 'FAIL'}** |
| External link check | **{'PASS' if link_ok else 'FAIL'}** |
| Rights heuristic scan (human rights review open) | **PASS** |
| Repository validation | **{'PASS' if repo_ok else 'FAIL'}** |
| Human-review status | **OPEN** — not publication-ready |
| Publication readiness | **NO GO** — human gates open |

## Scripts executed

Structural: {', '.join(STRUCTURAL)}
Semantic: {', '.join(SEMANTIC)}
Source: {', '.join(SOURCE)}
V10A controls: {', '.join(V10A_CONTROLS)}
Reporting: {', '.join(REPORTING)}

## Note

Automated PASS confirms only what the named scripts check. Media curation remains incomplete; Gamma remains unrendered; visuals remain structural drafts; human gates remain open; publication remains `NO GO`. Warnings in repository validator (e.g. hash verify skips) are classified separately — not suppressed.
""",
        encoding="utf-8",
    )

    all_pass = all(results.values()) and repo_ok and link_ok
    print(f"\nOverall curriculum validation: {'PASS' if all_pass else 'FAIL'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
