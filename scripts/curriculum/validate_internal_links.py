#!/usr/bin/env python3
"""Validate internal Markdown links with UTF-8 and NFC normalization."""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote

REPO = Path(__file__).resolve().parents[2]
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
MOJIBAKE_RE = re.compile(r"\u00c3")
SKIP_PREFIX = ("http://", "https://", "mailto:", "#")
REPO_ROOT_PREFIXES = (
    "00-",
    "01-",
    "02-",
    "09-",
    "11-",
    "12-",
    "14-",
    "17-",
    "build-evidence/",
    "docs/",
)


def nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s)


def resolve_target(md: Path, target: str) -> Path:
    if target.startswith("/"):
        return (REPO / target.lstrip("/")).resolve()
    if target.startswith(REPO_ROOT_PREFIXES):
        return (REPO / target.replace("/", "\\")).resolve()
    return (md.parent / target).resolve()


def main() -> int:
    broken: list[str] = []
    mojibake: list[str] = []

    for md in sorted(REPO.rglob("*.md")):
        if ".git" in md.parts:
            continue
        try:
            text = md.read_text(encoding="utf-8")
        except OSError as e:
            print(f"WARN: cannot read {md}: {e}")
            continue
        for m in LINK_RE.finditer(text):
            target = m.group(1).split("#")[0].strip()
            if not target or target.startswith(SKIP_PREFIX):
                continue
            try:
                target = unquote(target)
            except Exception:
                pass
            target = nfc(target)
            if MOJIBAKE_RE.search(target):
                mojibake.append(f"{md.relative_to(REPO)}: {target}")
                continue
            if " " in target and not target.startswith(REPO_ROOT_PREFIXES):
                continue
            resolved = resolve_target(md, target)
            if not resolved.exists():
                broken.append(f"{md.relative_to(REPO)}: {target}")

    failures = []
    if mojibake:
        failures.extend(mojibake[:10])
        if len(mojibake) > 10:
            failures.append(f"... and {len(mojibake) - 10} more mojibake links")
    if broken:
        failures.extend(broken[:20])
        if len(broken) > 20:
            failures.append(f"... and {len(broken) - 20} more broken links")

    if failures:
        for f in failures:
            sys.stdout.buffer.write((f"FAIL: {f}\n").encode("utf-8", errors="replace"))
        print(f"Internal links: {len(broken)} broken, {len(mojibake)} mojibake")
        return 1

    print("PASS: internal link checks OK (UTF-8, NFC, 0 broken, 0 mojibake)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
