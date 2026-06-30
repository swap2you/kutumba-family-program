#!/usr/bin/env python3
"""Create .md Mermaid viewer wrappers for every .mmd file under weekly library."""

from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library"


def main() -> None:
    count = 0
    for mmd in sorted(WEEKLY.rglob("*.mmd")):
        md = mmd.with_suffix(".md")
        if md.name in ("concept-map.md", "process-flow.md") and md.exists():
            text = md.read_text(encoding="utf-8")
            if "```mermaid" in text:
                continue
        source = mmd.read_text(encoding="utf-8").strip()
        title = mmd.stem.replace("-", " ").title()
        content = f"""# {title}

Rendered viewer for [`{mmd.name}`]({mmd.name}). Open this file in Markdown preview to see the diagram.

```mermaid
{source}
```

_Source file: `{mmd.name}` — edit the `.mmd` file for diagram changes._
"""
        md.write_text(content, encoding="utf-8", newline="\n")
        count += 1
    print(f"Created/updated {count} Mermaid viewer pages")


if __name__ == "__main__":
    main()
