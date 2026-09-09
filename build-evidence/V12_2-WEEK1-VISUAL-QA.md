# V12.2 Week-1 Visual QA

**Method:** Opened contact sheets under `build-evidence/v12_2-week1-rasters/**/contact-sheet-*.png` with the image viewer, then cross-checked PDF page body text. Brightness/blank heuristics alone were **not** used as PASS criteria.

**Date:** 2026-09-09  
**Scope:** All Week-1 final PDFs in `exports/final/week1/`

## Contact sheets opened (examples)

| Artifact | Sheets opened | Concrete observations |
|---|---|---|
| START-HERE | contact-sheet-001 | Cover + locked schedule table with **2:30 / 3:10**; print-one-packet path; Friday ≤60 prep; EXTERNAL_OPEN verdict language |
| OWNER-RUNBOOK | contact-sheet-001 | 4 pages; Friday prep blocks; role table; handoff at 2:30 / reunite 3:10 callout |
| ORIENTATION+COVENANT | contact-sheet-001–002 | Is/Is Not tables; acknowledgement initials table; child house rules; trailing blank page stripped → **10 pages** |
| PARENT-TRACK | contact-sheet-001–002 | Six timed blocks 0–5…35–40; P01–P05 forms; facilitator match key table; saṅkalpa builder |
| YOUNGER-TEACHER-PACK | contact-sheet-001–003 | Memory phrase *Our family helps one another remember Kṛṣṇa*; Y01–Y05 layouts; Four Corners answer key table; SAFE/NEEDS RESET key |
| OLDER-TEACHER-PACK | contact-sheet-001–003 | O01 verse observation; O02–O04 cut cards + keys; O05 compass; O06 exit ticket; 2:30–3:10 window |
| SATURDAY-PRINT-PACKET | contact-sheet-001–012 | Ordered sections: schedule → mantras → orientation → covenant → parent → younger → older → home practice → TEACHER-ONLY → run sheets → checklist |

## Issues found and fixed

| Issue | Fix |
|---|---|
| Orientation PDF trailing empty page (header/footer only) | Stripped trailing empty PDF page; renderer now strips after Word convert |
| Baseline shallow parent / wrong clock / missing printables | Rebuilt guides + `v12_2-*` printables + V12.2 renderer (not V12.1 2:35/3:25 builder) |

## Remaining visual defects

- ASCII/line-art craft layouts are printer-usable but not illustrated SVG art (acceptable for gold printables; no dark full-page backgrounds).
- Gamma remains **prompt-only** until owner renders in Gamma Studio (not a packet visual defect).

## Page ledger

See `build-evidence/V12_2-WEEK1-PAGE-QA.csv` — one row per final PDF page with non-generic `visual_observation`.
