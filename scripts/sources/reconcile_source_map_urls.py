#!/usr/bin/env python3
"""Reconcile authoritative source-map URLs against MASTER-SOURCE-CATALOG."""
from __future__ import annotations

import csv
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

import yaml

REPO = Path(__file__).resolve().parents[2]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from scripts.sources.url_cleanup import clean_url, extract_urls  # noqa: E402

DOCX = REPO / (
    "00-source-materials/01-current-kutumba-originals/9. KUTUMBA Digital Repository and Source Library/"
    "Public Source Map for Prabhupada and Related Sanatana Content.docx"
)
CANONICAL = REPO / "09-digital-repository-publishing/PUBLIC-SOURCE-MAP-FOR-PRABHUPADA-AND-SANATANA-CONTENT.md"
MASTER = REPO / "14-research-source-register/public-source-catalog/MASTER-SOURCE-CATALOG.yaml"
REPORT = REPO / "build-evidence/SOURCE-MAP-URL-RECONCILIATION.md"
CSV_OUT = REPO / "build-evidence/SOURCE-MAP-URL-RECONCILIATION.csv"

# Approved aliases (normalized redirect targets)
APPROVED_ALIASES: dict[str, str] = {
    "https://www.prabhupada.com/": "https://prabhupada.com/",
    "https://www.bbti.org/": "https://bbt.org/",
}

INTENTIONALLY_EXCLUDED: dict[str, str] = {}


def normalize(url: str) -> str:
    u = clean_url(url.strip().rstrip(".,;)`"))
    return APPROVED_ALIASES.get(u, u)


def urls_from_docx() -> set[str]:
    try:
        from docx import Document
    except ImportError as exc:
        raise SystemExit("python-docx required") from exc
    doc = Document(str(DOCX))
    text = "\n".join(p.text for p in doc.paragraphs if p.text.strip())
    return {normalize(u) for u in extract_urls(text)}


def urls_from_canonical() -> set[str]:
    text = CANONICAL.read_text(encoding="utf-8")
    body = text.split("---", 2)[-1] if text.startswith("---") else text
    return {normalize(u) for u in extract_urls(body)}


def catalog_urls() -> dict[str, dict]:
    data = yaml.safe_load(MASTER.read_text(encoding="utf-8"))
    out: dict[str, dict] = {}
    for e in data.get("entries", []):
        out[normalize(e["exact_entry_url"])] = e
    return out


def main() -> int:
    if not all(p.exists() for p in (DOCX, CANONICAL, MASTER)):
        print("Missing required files", file=sys.stderr)
        return 1
    docx_urls = urls_from_docx()
    canon_urls = urls_from_canonical()
    authoritative = docx_urls | canon_urls
    catalog = catalog_urls()
    catalog_set = set(catalog.keys())

    rows = []
    missing = []
    for u in sorted(authoritative):
        if u in catalog_set:
            status = "catalogued"
            sid = catalog[u]["source_id"]
        elif u in INTENTIONALLY_EXCLUDED:
            status = "intentionally-excluded"
            sid = ""
        else:
            # check if any catalog URL is prefix/alias
            matched = next((c for c in catalog_set if c.rstrip("/") == u.rstrip("/")), None)
            if matched:
                status = "catalogued-normalized"
                sid = catalog[matched]["source_id"]
            else:
                status = "MISSING"
                sid = ""
                missing.append(u)
        rows.append({"url": u, "status": status, "source_id": sid})

    extra = sorted(catalog_set - authoritative - set(APPROVED_ALIASES.values()))
    # extra catalog entries from code block starter set only - flag if no provenance
    unprovenanced = [u for u in extra if catalog[u].get("notes", "").find("KUT-SRC-0013") < 0]

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    with CSV_OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["url", "status", "source_id"])
        w.writeheader()
        w.writerows(rows)

    lines = [
        "# Source Map URL Reconciliation",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Summary",
        "",
        f"| Metric | Count |",
        f"|--------|-------|",
        f"| Authoritative URLs (DOCX ∪ canonical) | {len(authoritative)} |",
        f"| Catalogued | {sum(1 for r in rows if r['status'].startswith('catalogued'))} |",
        f"| Missing from catalog | {len(missing)} |",
        f"| Catalog entries not in source map | {len(extra)} |",
        "",
    ]
    if missing:
        lines.append("## Missing URLs (must resolve)")
        for u in missing:
            lines.append(f"- {u}")
        lines.append("")
    else:
        lines.append("All authoritative source-map URLs are catalogued or aliased.")
        lines.append("")

    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Reconciled {len(authoritative)} URLs; missing={len(missing)}")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
