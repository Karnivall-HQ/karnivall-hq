# NOW — Fuku's working memory
_Last updated: 2026-11-15 09:01 WIB (cloud heartbeat: groundwork, `--budget` re-base flag on both models)_
_Rules: rewrite, never append. Max 45 lines. History lives in the journal. See `protocols/heartbeat.md` (quiet-run rule)._

## Current focus
- **⚠️ 11/15 00:41 PEIKIRA CBO Rp 300k → Rp 3,000,000/day + bid cap Rp 105k on control, PEIKIRA2, ADSET-3** (actor Rudi MCP 61594758338050; not any ask). Today to 07:05: Rp 138,427 / 1 (≈ Rp 475k/day pace *(calc)*). OUTBOX #1 = "intended or revert?" (rec: revert budget to 300k, keep caps).
- **M-001 (P0, at risk):** 7d (11/08–11/14) Rp 2,443,461 / 21 = **116.4k** *(calc)* ❌ vs 95k. PEIKIRA 130.9k (16), BC 69.7k (5). Control 153.6k (8), PEIKIRA2 108.2k (8), ADSET-3 Rp 0 (day 3, even under the cap).
- **Ad015** still ACTIVE: 7d 141.0k *(calc)*, trigger still fired. OUTBOX #2 (pause Ad015 + ADSET-3 min 75k) still open; its "CBO stays 300k" depends on #1.
- **Models void until re-based:** gate 126.0k, criterion-1 11/28 (300k basis). Re-base = `--budget <actual PEIKIRA daily spend>` on both. At 475k pace: gate 127.3k, break-even PEIKIRA CPL 101.1k → 98.8k; at Rp 1M: 96.7k, last date 11/27 *(calc)*.
- **M-002 (P1):** weekly report Mon 11/16 07:00 from the skeleton; add the budget change to "What changed".

## Next actions (dated or triggered)
1. **13:00 poll (today, extra weight):** PEIKIRA today spend/leads by ad set, activity log since 07:05. Apply guards G-a/G-b from `fab_advertising/reports/2026-11-18_budget_change_read_card.md` (one line on OUTBOX #1, no new ask).
2. **19:00 poll:** same; full-day pace estimate.
3. **Every run:** INBOX/OUTBOX for "intended"/"revert", "done" on #2, "W1 W2 done", photos answer.
4. **When #1 answered / from 11/16 readout:** run both models with `--budget <yesterday's PEIKIRA spend>` (not the CBO setting); log in tracker.
5. **11/16 07:00:** weekly report + readout (tracker routine step 0 = activity log first). **11/18:** 3-day read of the budget change = fill `2026-11-18_budget_change_read_card.md`. **11/20:** readout template. **11/27:** ADSET-3 verdict.
6. **Retro #4:** at > 15 lessons or 11/21.

## Groundwork backlog (for quiet runs; needs nothing from Alvian)
1. **Wave 1 / shoot card vs ADSET-3 photos:** list which shoot-card v2 shots ADSET-3 already covers (photos ask is parked).
2. **Cap-vs-target note:** if "intended", draft the cap question (105k cap > 95k target → blend ≈ 102–104k at ≥ Rp 1M/day *(calc)*); hold until the 11/18 read.
3. **11/16 weekly skeleton:** add a "Budget change" block (3M CBO + 105k caps, pace, model re-base numbers above) so the 07:00 Monday report is a fill job.

## Waiting on Alvian (asks live in OUTBOX "Needs you")
- #1 Budget Rp 3M/day intended? #2 Pause Ad015 + ADSET-3 min Rp 75k. #3 Site W1 + W2 + who edits.
- Parked: 15 images = phone photos + Kuningan open? FYI: who is "TourHub"? Later: "All-in", R5 sellers, close rate + months stayed.

## Standing facts
- Read `playbooks/meta-ads-algorithm.md` + `meta-cpl-diagnosis.md` + `meta-tests-and-proposals.md` before any ads work, `meta-modelling-and-planning.md` before any model/plan; `ad-copy-page-check.md` before any copy is paste-ready.
- Cloud Fuku: routine trig_01NGMFnv9BpvRp1jQjkAwUVJ, hourly 07–22 WIB. Propose-only: never call Meta write tools, even when visible.
- Fab account 484578521394893, pixel 405755485775053. PEIKIRA campaign `120254051672440572` (now Rp 3M/day, bid cap); control `120254051672430572`; PEIKIRA2 `120254276298070572`; ADSET-3 `120254400251570572`; Ad015 `120254063163810572`; BC campaign `120236222888610572`.
- Markus (team) edits the Fab account via the Rudi MCP app (actor 61594758338050).

## Open loops (current state, one line each)
- Activity log: last change 11/15 00:41–00:42 (budget + bid caps). Nothing after, checked 07:05.
- Site (fabwarehouses.com): W1/W2 not applied (curl 11/15 07:05: Jakarta Pusat ×9, Rp 800.000 ×3, "akan launching" ×3).
- 11/20 messages pre-drafted (gate-miss note, S1 card, readout); S1 card (+25% → 375k) is moot if 3M stays.
- Parked in OUTBOX: photos/Kuningan ask, BC204 cap probe, W3/W4 + WA follow-up script, 4 disabled ad accounts, Incess bid-cap, lead-value questions.
