# V12.1 Red-Team Audit

**Stance:** Assume the implementation overstates readiness. Find evidence.  
**HEAD at audit:** local working tree before push (post-validator zero).  
**Result:** **0 BLOCKING** findings remaining after fixes.

## Reads performed
- All 18 `MAIN-FACILITATOR-GUIDE-V12.md`
- All 18 younger + older teacher guides
- All 18 younger/older activity packs (+ answer keys)
- All 18 master Gamma prompts (rewritten V12.1)
- `launch/C1|C2|C3-VERSE-PACK.md` + `scripts/v12/verse_data.yaml`
- W1 print packet builder `scripts/v12_1/render_v12_1_packets.py`
- Publication styles/renderer
- `V12_1-DOCX-PAGE-QA.csv` / `V12_1-PDF-PAGE-QA.csv` (318 pages)

## Adversarial checks

| Hunt | Result | Resolution |
|---|---|---|
| Shallow/generic facilitator content | C2-W5/W6 + C3 initially shells | Authored gold packs; validators require depth markers |
| Shallow child lessons | Present on some C1/C3 | Executable younger/older guides authored |
| “See research” core deferral | Forbidden-phrase scan PASS | — |
| Generic case studies | Replaced with week-specific cases | — |
| Generic image prompts | Gamma rewrite removed templates | — |
| Truncated verse meanings | `meaning[:` removed from generator; Gamma rewritten | — |
| Incomplete multi-verse refs | C3-W4 full Antya 20.12; C3-W5 both 23–24; C3-W6 exact chain | Confirmed on verse pack PDF p.3 |
| Dropped Markdown tables | V12.1 renderer uses `render_markdown`; legacy skip removed | Table visible on W1 packet p.5 |
| Missing visuals | Concept/line-art PNGs embedded; verse-card PNG skipped (svglib tofu) | — |
| Missing W1 print components | 17-component builder | Packet 40 pages |
| Uninspected pages | Per-page QA CSV 318 rows inspected=yes | — |
| Stale wrong sources | Mṛgāri preserved CC Madhya 24; mantra URLs direct | — |
| Stale V12 all-PASS evidence | Superseded by V12.1 evidence set | — |
| Final-head remote gap | Protocol enforced in master prompt / pending push | F01 closes at remote final HEAD |

## Residual non-blockers
- Gamma remains prompt-only until owner renders (EXTERNAL_OPEN by design).
- Human/temple pilot approval remains EXTERNAL_OPEN.
- Some C2/C3 facilitators are shorter than the deepest C2-W2 exemplar but pass semantic component gates and forbidden-phrase scan.

**BLOCKING count: 0**
