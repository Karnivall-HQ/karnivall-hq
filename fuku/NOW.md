# NOW — Fuku's working memory
_Last updated: 2026-11-13 07:02 WIB (cloud heartbeat: 11/13 readout + team's new ADSET-3 read card)_
_Rules: rewrite, never append. Max 45 lines. History lives in the journal. See `protocols/heartbeat.md` (quiet-run rule)._

## Current focus
- **M-001 (P0):** 7d Fab (11/06–11/12) **CPL Rp 103.3k** *(calc)* ❌ vs 95k (was 100.5k); Rp 339k/day vs 1M. PEIKIRA 116.4k (18), BC 56.0k (5). Control 124.9k (8), PEIKIRA2 109.6k (10). Benchmark: control 89% worse than peers, PEIKIRA2 69%.
- **Ad015:** 7d CTR 2.24%, CPL 114.5k, freq 1.38 → no trigger (CPL < 120k), 91.7% of control spend. CPL drifting up: watch.
- **🚀 Team launched ADSET-3** `120254400251570572` in the PEIKIRA CBO (Rp 300k/day now split 3 ways): 6 ads, new images (15 in library), copy "Rp750rb" + "Jakarta Selatan (Kuningan and Sudirman)", Advantage+ audience + creative enhancements on. ACTIVE 04:05 11/13. Built by new actor "TourHub Shared Office…" (61557670947597) + Markus. Read card (kill/compare/verdict): `fab_advertising/reports/2026-11-13_adset3_read_card.md`.
- **Site vs new ads:** page still "Jakarta Pusat" ×9, "Rp 800.000" ×1 → now contradicts the new ads. W1/W2 re-framed as OUTBOX #1 (with fix ≈ 91.5k *(calc)*). Paste-ready: `fab_advertising/reports/2026-11-11_w1w2_paste_ready.md`.
- **Our Wave 1–4 build sheets** may be partly overtaken by the team's own photo wave: hold them until Alvian answers ask #2 (are the 15 images the photos?).
- **M-002 (P1):** weekly report Mon 11/16 07:00; skeleton `fab_advertising/reports/weekly/2026-11-16.md`. Add ADSET-3 launch + read rules. Incess 019 Copy 5 rule: propose pause if 3-wk CPL > 105k.

## Next actions (dated or triggered)
1. **Polls today:** 07:00 done (ADSET-3 launch found). Next ~13:00 and ~19:00: activity log + ADSET-3 spend share/today (read card rule 1, flag only).
2. **11/14 07:00 readout:** tracker row; first full day of ADSET-3: spend, share of PEIKIRA, leads vs rules 1–2; Ad015 triggers (CTR < 1.30% / CPL > 120k / freq > 2.5).
3. **Every run:** INBOX/OUTBOX for "W1 W2 done", photos answer, TourHub actor answer. Log applied changes in the tracker.
4. **When W1/W2 are applied:** re-curl the page, run `fab_advertising/reports/w1w2_lift_template.md`.
5. **11/20 readout:** ADSET-3 day-7 comparative read (rule 3) + gate call: if 7d CPL > 95k, tell Alvian criterion 2 is out of reach by 12/05.
6. **Retro #3:** ~11/18 or at 15 new lessons.

## Groundwork backlog (for quiet runs; needs nothing from Alvian)
1. **Partial-week pre-pull for 11/16 (+ ADSET-3 rows):** on a quiet run 11/14–15, pull 11/09–11/13 Fab+Incess ad-set rows (by object_ids) into the skeleton as a draft so Monday is a delta.
2. **11/20 gate brief refresh** (due now: base 103.3k, add the ADSET-3 path): re-run the W1/W2 and Wave 1 paths on the new 7d (and "no site fix" path if W1/W2 still unanswered, per action 5).
3. **ADSET-3 copy check:** pull all 6 creatives' full asset text (only S30 returned a body) and run `playbooks/ad-copy-page-check.md`; write any fixes as a propose-only list for Markus.

## Waiting on Alvian (asks live in OUTBOX "Needs you")
- #1 Website W1 + W2, and who edits the site. #2 Are the 15 new images the phone photos? FYI: who is the "TourHub" actor?
- Later: G6 (is the site open for move-in), "All-in" meaning, R5 online sellers, close rate + months stayed.

## Standing facts
- Read `playbooks/meta-ads-algorithm.md` + `meta-cpl-diagnosis.md` + `meta-tests-and-proposals.md` before any ads work; `ad-copy-page-check.md` before any copy is paste-ready. Wave 1 is read with `fab_advertising/reports/wave1_read_template.md`.
- Cloud Fuku: routine trig_01NGMFnv9BpvRp1jQjkAwUVJ, hourly 07–22 WIB. Propose-only: never call Meta write tools, even when visible.
- Fab pixel/dataset id **405755485775053**. PEIKIRA campaign `120254051672440572`, control ad set `120254051672430572`, PEIKIRA2 `120254276298070572`, BC campaign `120236222888610572` (= "BC CBObass005").
- Markus (team) edits the Fab account via the Rudi MCP app (actor 61594758338050).

## Open loops (current state, one line each)
- Activity log: 11/13 00:04–04:08 ADSET-3 build (TourHub actor + Markus); nothing else since the 11/09 ad-006 pause. PEIKIRA2 ACTIVE.
- Site: W1/W2 not applied (curl 11/13 07:02). W3 on hold pending the W4 routing rule.
- Parked in OUTBOX: optional BC204 cap probe, W3/W4 + WA follow-up script, 4 disabled ad accounts, Incess bid-cap, lead-value questions.
