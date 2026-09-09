# V12.2.1 Week-1 Visual QA (agent-authored after opening images)

**Method:** Opened every contact sheet under `build-evidence/v12_2_1-week1-rasters/**/contact-sheet-*.png` with the image viewer, then opened critical individual `page-*.png` files. Observations below were written after viewing — not synthesized by a text-extraction script.

**Date:** 2026-09-09  
**Total PDF pages:** 156 (4+4+12+15+20+20+81)  
**Contact sheets:** 23  

## Contact sheets (all opened)

| Artifact | Sheets | Visible content (after open) | Layout/glyph | Status |
|---|---|---|---|---|
| START-HERE | 001 | Cover, locked schedule table, print-one-packet paths, Friday prep, EXTERNAL_OPEN | Readable; schedule verified via PDF text as 2:30/3:10 | PASS |
| OWNER-RUNBOOK | 001 | Cover, schedule, Friday ≤60 prep, role table | Clean cream/plum | PASS |
| ORIENTATION | 001–002 | Is/Is Not tables, covenant, acknowledgement initials, house rules | Tables readable; no markup | PASS |
| PARENT | 001–002 | Run sheet 0–5…35–40; P01 writing space; P02 purpose/example cards; TEACHER-ONLY key; P03–P05 forms | Real card grids; keys separated | PASS |
| YOUNGER | 001–003 | Run sheet; Y01 signs with icons; Y02 card grids; TEACHER-ONLY key; Y03 flower with center phrase; Y04 badge/bookmark; Y05 mats/cards/key | Real graphics; no placeholders | PASS |
| OLDER | 001–003 | Run sheet; O01 worksheet; O02 mats/cards/key; O03 purposes/examples/key; O04 scenarios/key; O05 compass; O06 exit | Real layouts; TEACHER-ONLY clear | PASS |
| SATURDAY | 001–011 | Full ordered packet: schedule→mantras→orientation→covenant→parent→younger→older→home practice→TEACHER-ONLY→run sheets→checklist | No HTML/fences/ASCII final art; keys labeled | PASS |

## Critical individual pages opened

| Page | Observation | Status |
|---|---|---|
| Younger p9 Y01 HEAR | Large HEAR + ear/book icon + sentence; no bracket placeholders | PASS |
| Younger p13 Y02 | 2-col Word-table cards 1–6; cut borders | PASS |
| Younger p16 Y03 | Four-petal flower; center memory phrase baked in; write line + checkbox | PASS (fixed iteration 2 after empty-center FAIL) |
| Younger p17 Y04 | Badge + bookmark with text inside outlines; 4 mini-icons | PASS (fixed iteration 2) |
| Older p7 O02 mats | IS / IS NOT two-column mat | PASS |
| Older p10 O03 | Six purpose cards in table | PASS |
| Older p19 O05 | Compass graphic HEAR/PRACTICE/SERVE/ASSOCIATE + write lines | PASS |
| Parent p8 P02 | Six purpose cards table | PASS |
| Saturday p2 schedule | Locked 1:50–4:00 with 2:30/3:10; TIME CUE correct | PASS |
| Saturday p13 acknowledgement | Initials table + privacy warning | PASS |
| Saturday p24 TEACHER-ONLY P02 key | Large TEACHER-ONLY + match table | PASS |

## Visual FAILs found / fixed

| FAIL | Fix iteration |
|---|---|
| Y03 flower center empty (phrase only below) | Regenerated flower PNG with center text; re-rendered |
| Y04 memory text outside cut shapes | Regenerated badge/bookmark PNGs with interior text; re-rendered |

## Remaining visual defects

- Simple programmatic line-art icons (intentional; not photo clip art).
- Some guide pages still list `.md` filenames in materials tables (teacher provenance; not participant craft ASCII).
- Acknowledgement pages may show canonical source/SHA line from safe markdown renderer (adult form; not HTML/fence leak).
- Gamma remains prompt-only (owner render EXTERNAL_OPEN).
