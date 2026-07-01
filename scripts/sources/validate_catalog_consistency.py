#!/usr/bin/env python3
"""Validate MASTER vs split catalogs and report tier consistency."""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "scripts" / "sources"))
from url_cleanup import clean_url  # noqa: E402

CATALOG_DIR = REPO / "14-research-source-register/public-source-catalog"
MASTER = CATALOG_DIR / "MASTER-SOURCE-CATALOG.yaml"
SPLITS = {
    "primary": CATALOG_DIR / "PRABHUPADA-PRIMARY-AND-ARCHIVAL.yaml",
    "secondary": CATALOG_DIR / "PRABHUPADA-STRUCTURED-SECONDARY.yaml",
    "education": CATALOG_DIR / "ISKCON-EDUCATION-AND-CONGREGATION.yaml",
    "supplementary": CATALOG_DIR / "SUPPLEMENTARY-GAUDIYA-SANATANA.yaml",
    "media": CATALOG_DIR / "MEDIA-AND-YOUTUBE-DISCOVERY.yaml",
}
EXPECTED_TOTAL = None  # resolved from master after load


def load_entries(path: Path) -> list[dict]:
    return yaml.safe_load(path.read_text(encoding="utf-8")).get("entries", [])


def entry_key(e: dict) -> str:
    return e["source_id"]


def compare(a: dict, b: dict, fields: list[str]) -> list[str]:
    issues = []
    for f in fields:
        if a.get(f) != b.get(f):
            issues.append(f"{a['source_id']}: {f} master={a.get(f)!r} split={b.get(f)!r}")
    return issues


def main() -> int:
    failures = []
    master_data = yaml.safe_load(MASTER.read_text(encoding="utf-8"))
    master_entries = master_data.get("entries", [])
    expected = len(master_entries)
    if EXPECTED_TOTAL and expected != EXPECTED_TOTAL:
        failures.append(f"master entry_count {expected} != expected {EXPECTED_TOTAL}")

    ids = [e["source_id"] for e in master_entries]
    if len(ids) != len(set(ids)):
        failures.append("duplicate source_id in master")

    urls = [e["exact_entry_url"] for e in master_entries]
    if len(urls) != len(set(urls)):
        failures.append("duplicate exact_entry_url in master")

    norm_urls = [clean_url(u) for u in urls]
    if len(norm_urls) != len(set(norm_urls)):
        seen: dict[str, str] = {}
        for e in master_entries:
            nu = clean_url(e["exact_entry_url"])
            if nu in seen:
                failures.append(f"duplicate normalized URL: {nu} ({seen[nu]} vs {e['source_id']})")
            seen[nu] = e["source_id"]

    tiers = Counter(e["authority_tier"] for e in master_entries)
    fields = [
        "exact_entry_url", "authority_tier", "status", "last_verified",
        "verification_method", "rights_posture",
    ]
    split_ids: set[str] = set()
    for name, path in SPLITS.items():
        split_entries = load_entries(path)
        smap = {entry_key(e): e for e in split_entries}
        for e in master_entries:
            bucket = e.get("_catalog_bucket") or {
                "A": "primary", "B": "secondary", "C": "media", "supplementary": "supplementary",
            }.get(e["authority_tier"], "media")
            if e["authority_tier"] == "A" and (
                "iskconeducation" in e.get("exact_entry_url", "")
                or "iskconcongregation" in e.get("exact_entry_url", "")
                or "iskconmumbai" in e.get("exact_entry_url", "")
            ):
                bucket = "education"
            if name != bucket:
                continue
            if e["source_id"] not in smap:
                failures.append(f"{e['source_id']} missing from split {name}")
                continue
            failures.extend(compare(e, smap[e["source_id"]], fields))
            split_ids.add(e["source_id"])

    queue = yaml.safe_load((CATALOG_DIR / "SOURCE-VERIFICATION-QUEUE.yaml").read_text(encoding="utf-8"))
    for item in queue.get("queue", []):
        if item.get("item_id") not in ids:
            failures.append(f"queue item {item.get('item_id')} not in master")

    print(f"Tier counts: {dict(tiers)}")
    if failures:
        for f in failures[:40]:
            print(f"FAIL: {f}")
        print(f"Total failures: {len(failures)}")
        return 1
    print(f"PASS: catalog consistency ({len(master_entries)} entries, tiers={dict(tiers)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
