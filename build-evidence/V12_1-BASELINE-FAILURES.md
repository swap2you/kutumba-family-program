# V12.1 Baseline Failures

**Baseline HEAD:** `ac84e94d9813d2e6e0b2d4c702ca590698165c0f`  
**Safety tag:** `v12.1-pre-independent-closure-ac84e94`  
**Source:** Independent GitHub findings package `02_INDEPENDENT_FINDINGS.md` (F01–F19)  
**Date:** 2026-09-08

## Summary

| Status | Count |
|---|---|
| FAIL (implementation) | 19 (F01–F19) |
| BLOCKING_WARNING | 0 at baseline (all defects logged as FAIL) |
| EXTERNAL_OPEN | unchanged genuine human/temple/legal items (local tithi, pilot GO, etc.) |

## Controlling defect list (exact wording preserved)

### F01 — Remote final-head evidence gap
`build-evidence/V12-REMOTE-ACCEPTANCE.md` validates `6ecf005...`, while final HEAD is `ac84e94...`.  
**Baseline status:** FAIL

### F02 — "Every page visually inspected" was not performed/evidenced
`V12-FINAL-LOCAL-ACCEPTANCE.md` says only sample covers were inspected.  
`V12-DOCX-RENDER-QA.md` has no per-file/per-page audit.  
`V12-PDF-RENDER-QA.md` records page count/status from conversion, not human/vision inspection.  
**Baseline status:** FAIL

### F03 — DOCX renderer drops Markdown tables
`build_docx_from_md()` in `scripts/v12/render_v12_final_packets.py` skips lines beginning with `|`.  
**Baseline status:** FAIL

### F04 — Final docs do not embed promised instructional visuals
No meaningful `add_picture` integration is present in publication pipeline.  
**Baseline status:** FAIL

### F05 — W1 Saturday print packet is incomplete
Current builder only combines facilitator, younger, older, family-home-practice. Missing required 17-component order.  
**Baseline status:** FAIL

### F06 — C1 facilitator-depth regression
V12 controlling `MAIN-FACILITATOR-GUIDE-V12.md` regressed to generic shell with `Use week research ANALOGIES-AND-LIMITS and CASE-STUDIES...`.  
**Baseline status:** FAIL

### F07 — C2/C3 facilitator guides are shallow
Example C2-W1 has one-line core explanation and generic `Use week research...`.  
**Baseline status:** FAIL

### F08 — C2/C3 research is shallow
Scriptural examples, science, and cases are generic shells.  
**Baseline status:** FAIL

### F09 — Child teacher guides are shallow
Younger guides say `See activities...`; activity packs have generic `cause_effect_chain` / `Week craft tied to...`.  
**Baseline status:** FAIL

### F10 — Gamma teaching meanings are programmatically truncated
Generator uses `meaning[:110]` and `meaning[:140]`; meanings end mid-phrase.  
**Baseline status:** FAIL

### F11 — Gamma is still generic
Repeated generic image prompts, placeholder objectives, vague sources, boilerplate presenter notes.  
**Baseline status:** FAIL

### F12 — C3-W4 verse pack is incomplete
`CC Antya 20.12` stops at `vidyā-vadhū-jīvanam`; missing second half through `paraṁ vijayate śrī-kṛṣṇa-saṅkīrtanam`.  
**Baseline status:** FAIL

### F13 — C3-W5 verse pack is incomplete
Reference is `ŚB 7.5.23–24` but pack embeds only verse 23.  
**Baseline status:** FAIL

### F14 — C3-W6 review chain is imprecise
Uses generic `holy name` instead of exact `CC Antya 20.12`.  
**Baseline status:** FAIL

### F15 — Mahā-mantra source wording is vague
Opening mantra handout says `use authorised chanting practice + transcript context above`.  
**Baseline status:** FAIL

### F16 — Traceability was genericized
Rows such as `weekly completeness item 2` are not valid exact-requirement traceability.  
**Baseline status:** FAIL

### F17 — Final artifact manifest PASS overstates quality
Hash/presence is not visual/content acceptance; statuses must be separated.  
**Baseline status:** FAIL

### F18 — Owner navigation points to flawed artifacts
Must point only to V12.1 corrected artifacts after they pass.  
**Baseline status:** FAIL

### F19 — C2/C3 claimed "same gold standard" without gold-standard depth
Do not mark C2/C3 complete until every week passes gold-standard audit.  
**Baseline status:** FAIL

## Preserve (not defects)
Saturday 2–4; four-family public-safe model; privacy; Mṛgāri → CC Madhya 24; C1 verse chain; calendar; branding/rights; no false human approval.
