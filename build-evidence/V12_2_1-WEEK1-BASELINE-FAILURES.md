# V12.2.1 Week-1 Publishing Baseline Failures — Closure

**Baseline HEAD:** `3cb8b0a71b85b2e545328e97eb2db45eed79f5bd`  
**Safety tag:** `v12.2.1-pre-week1-publishing-3cb8b0a`

| ID | Status | Implementation | Deterministic evidence | Visual evidence |
|---|---|---|---|---|
| F01 | CLOSED | Safe markdown + printable builders; no HTML page breaks | validate_week1_publishing `<div` scan | Contact sheets / printables show no HTML |
| F02 | CLOSED | Fences skipped; layouts programmatic | fence scan 0 | Y/O/P pages use tables/images |
| F03 | CLOSED | PNG icons embedded | media present; placeholder scan 0 | Y01 icons viewed |
| F04 | CLOSED | Word tables + graphics replace ASCII | box-drawing scan 0 | Y02/P02/O02/O03 viewed |
| F05 | CLOSED | Real four-petal flower PNG with center phrase | asset + render | Younger p16 viewed |
| F06 | CLOSED | Explicit numbered paragraphs (no List Number runaway) | runaway strings absent | PASS |
| F07 | CLOSED | Raster script claims only dimensions/paths | raster_week1_publishing.py | Visual QA authored after open |
| F08 | CLOSED | Publishing validator + honest visual QA gate | validate PASS + VISUAL-QA.md | Agent opened all sheets |
| F09 | CLOSED | Operator acceptance re-answered honestly | OPERATOR-ACCEPTANCE.md | 8/8 YES |
| F10 | CLOSED | CURRENT-STATUS updated for publishing closure | CURRENT-STATUS.md | — |
