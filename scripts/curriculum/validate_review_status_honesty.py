#!/usr/bin/env python3
"""Fail when review-status claims enhancement-complete without gold-standard depth."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
PILOT = "c1-w2-i-am-not-this-body"
MIN_GAMMA_LINES = 80
MIN_DOSSIER_LINES = 60
MIN_CLAIMS = 6


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
        if d.name == PILOT:
            continue
        failures.append(
            f"{week_code_from_dir(d.name)}: weekly_derivative_pack=enhancement-complete "
            f"but module is not gold-standard pilot (only C1-W2 may use this label)"
        )

    pilot = WEEKLY / PILOT
    if pilot.exists():
        rs = read_status(pilot / "review-status.yaml")
        if rs.get("weekly_derivative_pack") != "enhancement-complete":
            failures.append("C1-W2 pilot must keep weekly_derivative_pack: enhancement-complete")
        gamma = pilot / "gamma" / "GAMMA-PARENT-DECK-PROMPT.md"
        if gamma.exists() and len(gamma.read_text(encoding="utf-8").splitlines()) < MIN_GAMMA_LINES:
            failures.append("C1-W2 gamma deck too thin for enhancement-complete")
        dossier = pilot / "research" / "RESEARCH-DOSSIER.md"
        if dossier.exists() and len(dossier.read_text(encoding="utf-8").splitlines()) < MIN_DOSSIER_LINES:
            failures.append("C1-W2 research dossier too thin for enhancement-complete")
        claims = count_claims(pilot / "research" / "CLAIM-REGISTER.yaml")
        if claims < MIN_CLAIMS:
            failures.append(f"C1-W2 claim register too thin ({claims} claims)")

    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir() or d.name == PILOT:
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
