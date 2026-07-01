#!/usr/bin/env python3
"""Validate all three Gamma decks per module — content, not line count."""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
from module_utils import iter_modules  # noqa: E402

DECKS = [
    ("gamma/GAMMA-PARENT-DECK-PROMPT.md", "parent"),
    ("gamma/GAMMA-LALA-LALI-DECK-PROMPT.md", "lala-lali"),
    ("gamma/GAMMA-KISORA-KISORI-DECK-PROMPT.md", "kisora-kisori"),
]
CARD_RE = re.compile(r"### Card \d+", re.I)
# Incomplete generator truncation: word fragment immediately before "..."
CLIP_RE = re.compile(r"(?<![/\w])([a-z]{4,})\.\.\.(?!\.)")
GENERIC_NOTE = re.compile(r"deliver per facilitator-guide\.md|see speaker-notes\.md", re.I)
MIN_CARD_CONTENT = 25
CONTENT_RE = re.compile(
    r"\*\*Content:\*\*\s*(?:\n)?(.+?)(?=\n\*\*Visual|\n---|\Z)",
    re.S,
)


def extract_content(part: str) -> str | None:
    m = CONTENT_RE.search(part)
    if not m:
        return None
    return m.group(1).strip()


def main() -> int:
    failures = []
    for d in iter_modules(WEEKLY):
        for rel, label in DECKS:
            g = d / rel
            if not g.exists():
                failures.append(f"{d.name}: missing {label} gamma deck")
                continue
            text = g.read_text(encoding="utf-8")
            cards = CARD_RE.findall(text)
            if len(cards) < 10:
                failures.append(f"{d.name}/{label}: only {len(cards)} cards")
            if CLIP_RE.search(text):
                failures.append(f"{d.name}/{label}: clipped text (... truncation)")
            parts = re.split(r"### Card \d+", text)[1:]
            for i, part in enumerate(parts, 1):
                content = extract_content(part)
                if content is None:
                    failures.append(f"{d.name}/{label} card {i}: missing Content block")
                    continue
                title_card = "title" in part[:40].lower() or i == 1
                sanskrit_echo = "sanskrit" in part[:40].lower() or "echo" in part[:40].lower()
                if (
                    len(content) < MIN_CARD_CONTENT
                    and not title_card
                    and not sanskrit_echo
                ):
                    failures.append(f"{d.name}/{label} card {i}: content too short")
                note_m = re.search(r"\*\*Speaker note:\*\*\s*(.+)", part)
                if note_m and GENERIC_NOTE.search(note_m.group(1)):
                    if d.name.startswith("c1-w"):
                        failures.append(f"{d.name}/{label} card {i}: generic speaker note (Cycle 1)")
    if failures:
        for f in failures[:50]:
            print(f"FAIL: {f}")
        print(f"Total failures: {len(failures)}")
        return 1
    print("PASS: gamma brief checks OK (three decks per module)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
