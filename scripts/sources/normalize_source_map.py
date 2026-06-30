#!/usr/bin/env python3
"""Extract canonical Markdown from the ingested public source map DOCX."""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DOCX_PATH = REPO / (
    "00-source-materials/01-current-kutumba-originals/"
    "9. KUTUMBA Digital Repository and Source Library/"
    "Public Source Map for Prabhupada and Related Sanatana Content.docx"
)
CANONICAL = REPO / "09-digital-repository-publishing/PUBLIC-SOURCE-MAP-FOR-PRABHUPADA-AND-SANATANA-CONTENT.md"

SOURCE_ID = "KUT-SRC-0013"
SOURCE_GROUP_ID = "KUT-SRC-GRP-0013"
SOURCE_HASH = "bb05c18452b05649e5b8f57da3ce1beb13294b860aa9df07dd8fc19438ca775e"

REPO = Path(__file__).resolve().parents[2]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from scripts.sources.url_cleanup import strip_cite_markers  # noqa: E402


def extract_docx_paragraphs(path: Path) -> list[str]:
    try:
        from docx import Document
    except ImportError as exc:
        raise SystemExit("python-docx required for DOCX extraction") from exc
    doc = Document(str(path))
    lines: list[str] = []
    for para in doc.paragraphs:
        t = para.text.strip()
        if t:
            lines.append(t)
    return lines


def paragraphs_to_markdown(paragraphs: list[str]) -> str:
    out: list[str] = []
    i = 0
    while i < len(paragraphs):
        p = strip_cite_markers(paragraphs[i])
        if not p:
            i += 1
            continue
        if p.startswith("Public Source Map"):
            out.append(f"# {p}")
            i += 1
            continue
        if p in ("Scope and selection standard",) or (
            len(p) < 80 and p[0].isupper() and not p.startswith("http") and ":" not in p[:30]
        ):
            # heuristic: short title-case lines as h2 when followed by prose
            if i + 1 < len(paragraphs) and len(paragraphs[i + 1]) > 60:
                out.append(f"\n## {p}\n")
                i += 1
                continue
        if p.startswith("http://") or p.startswith("https://"):
            out.append(f"`{p}`  ")
            i += 1
            continue
        if p.startswith("Use these exact"):
            out.append(f"\n{p}\n")
            i += 1
            continue
        if p.startswith("```"):
            out.append(p)
            i += 1
            while i < len(paragraphs) and not paragraphs[i].startswith("```"):
                out.append(paragraphs[i])
                i += 1
            if i < len(paragraphs):
                out.append(paragraphs[i])
            i += 1
            continue
        out.append(p)
        out.append("")
        i += 1
    body = "\n".join(out)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body


def build_frontmatter() -> str:
    today = date.today().isoformat()
    return f"""---
source_id: {SOURCE_ID}
source_group_id: {SOURCE_GROUP_ID}
source_hash_sha256: {SOURCE_HASH}
extraction_date: {today}
version: "1.0.0"
status: normalized-extraction
rights_notice: >
  Public web access to third-party sources does not grant permission to bulk-download,
  re-host, redistribute, or republish copyrighted books, purports, media, or artwork.
  This repository uses links and metadata only unless separate permission is recorded.
verification_note: >
  Counts and availability claims in the source document require independent verification
  on access date. Do not treat research-pass observations as permanent statistics.
---

"""


def main() -> int:
    if not DOCX_PATH.exists():
        print(f"Missing DOCX: {DOCX_PATH}", file=sys.stderr)
        return 1
    paragraphs = extract_docx_paragraphs(DOCX_PATH)
    body = paragraphs_to_markdown(paragraphs)
    CANONICAL.parent.mkdir(parents=True, exist_ok=True)
    CANONICAL.write_text(build_frontmatter() + body + "\n", encoding="utf-8")
    print(f"Wrote {CANONICAL}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
