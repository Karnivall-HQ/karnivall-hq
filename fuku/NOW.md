# NOW — Fuku's working memory
_Last updated: 2026-11-15 18:01 WIB (cloud heartbeat: groundwork, AKIRA-016 history = none)_
_Rules: rewrite, never append. Max 45 lines. History lives in the journal. See `protocols/heartbeat.md` (quiet-run rule)._

## Current focus
- **⚠️ 11/15 00:41 PEIKIRA CBO Rp 300k → Rp 3,000,000/day + bid cap Rp 105k on control, PEIKIRA2, ADSET-3** (actor Rudi MCP 61594758338050; not any ask). 13:02: today Rp 143,793 / 1, only Rp 5,366 spent since 07:05 → cap throttles (pace ≈ 265k/day *(calc)*); all 3 ad sets back in LEARNING since 00:42. Guards none tripped. OUTBOX #1 = "intended or revert?" (rec held to 11/18 read).
- **M-001 (P0, at risk):** 7d (11/08–11/14) Rp 2,443,461 / 21 = **116.4k** *(calc)* ❌ vs 95k. PEIKIRA 130.9k (16), BC 69.7k (5). Control 153.6k (8), PEIKIRA2 108.2k (8), ADSET-3 Rp 0 (day 3, even under the cap).
- **Ad015** still ACTIVE: 7d 141.0k *(calc)*, trigger still fired. OUTBOX #2 (pause Ad015 + ADSET-3 min 75k) still open; its "CBO stays 300k" depends on #1. 14:01: ADSET-3 = same audience as PEIKIRA2 → overlap + cap starve it; only #2(b) fixes it (INFERRED). 17:02: ADSET-3 holds AKIRA-016 = home clutter + stickers (best-history look), so starvation blocks that test too. 18:01: 016's images never spent before (PEIKIRA2 copy paused 2 min after creation 11/05) → fresh test, no prior CPL.
- **Models void until re-based:** gate 126.0k, criterion-1 11/28 (300k basis). Re-base = `--budget <actual PEIKIRA daily spend>` on both. At 475k pace: gate 127.3k, break-even PEIKIRA CPL 101.1k → 98.8k; at Rp 1M: 96.7k, last date 11/27 *(calc)*.
- **M-002 (P1):** weekly report Mon 11/16 07:00 from the skeleton (budget-change line, 11/15 log rows, `--budget` on row 12, Top-3 item 0 all pre-staged 10:02).

## Next actions (dated or triggered)
1. **19:00 poll:** activity log since 06:00Z + today by ad set; `python3 fuku/bin/peikira_guard.py --day 2026-11-14:309404:3 --day 2026-11-15:<S>:<L>:partial@19`. Only touch OUTBOX #1 if a guard trips or spend moves (13:02 base Rp 143,793 / 1).
2. **11/16 07:00:** full 11/15 day goes into G-b (≥ 285k with ≤ 1 lead); at today's pace it likely won't reach 285k → STARVED watch, not G-b.
3. **Every run:** INBOX/OUTBOX for "intended"/"revert", "done" on #2, "W1 W2 done", photos answer.
4. **When #1 answered / from 11/16 readout:** run both models with `--budget <yesterday's PEIKIRA spend>` (not the CBO setting); log in tracker.
5. **11/16 07:00:** weekly report + readout (tracker routine step 0 = activity log first). **11/18:** 3-day read of the budget change = fill `2026-11-18_budget_change_read_card.md`. **11/20:** readout template. **11/27:** ADSET-3 verdict.
6. **Retro #4:** at > 15 lessons or 11/21.

## Groundwork backlog (for quiet runs; needs nothing from Alvian)
1. **Cap-vs-target note:** if "intended", draft the cap question (105k cap > 95k target → blend ≈ 102–104k at ≥ Rp 1M/day *(calc)*); hold until the 11/18 read.
2. **11/18 read card dry-run:** walk every ⟨⟩ cell to a named pull (as done for the 11/27 template 11/14).
3. **Benchmark sanity for L1a:** pull BC Image087's lifetime + last-28d CPL (read-only) into the read card L1a row, so a first ADSET-3 read has a number to beat.

## Waiting on Alvian (asks live in OUTBOX "Needs you")
- #1 Budget Rp 3M/day intended? #2 Pause Ad015 + ADSET-3 min Rp 75k. #3 Site W1 + W2 + who edits.
- Parked: Kuningan open? (photos half answered 15:01: not the shoot) FYI: who is "TourHub"? Later: "All-in", R5 sellers, close rate + months stayed.

## Standing facts
- Read `playbooks/meta-ads-algorithm.md` + `meta-cpl-diagnosis.md` + `meta-tests-and-proposals.md` before any ads work, `meta-modelling-and-planning.md` before any model/plan; `ad-copy-page-check.md` before any copy is paste-ready.
- Cloud Fuku: routine trig_01NGMFnv9BpvRp1jQjkAwUVJ, hourly 07–22 WIB. Propose-only: never call Meta write tools, even when visible.
- Fab account 484578521394893, pixel 405755485775053. PEIKIRA campaign `120254051672440572` (now Rp 3M/day, bid cap); control `120254051672430572`; PEIKIRA2 `120254276298070572`; ADSET-3 `120254400251570572`; Ad015 `120254063163810572`; BC campaign `120236222888610572`.
- Markus (team) edits the Fab account via the Rudi MCP app (actor 61594758338050).

## Open loops (current state, one line each)
- Activity log: last change 11/15 00:41–00:42 (budget + bid caps). Nothing after, checked 13:02.
- Site (fabwarehouses.com): W1/W2 not applied (curl 11/15 07:05: Jakarta Pusat ×9, Rp 800.000 ×3, "akan launching" ×3).
- 11/20 messages pre-drafted (gate-miss note, S1 card, readout); S1 card (+25% → 375k) is moot if 3M stays.
- Parked in OUTBOX: photos/Kuningan ask, BC204 cap probe, W3/W4 + WA follow-up script, 4 disabled ad accounts, Incess bid-cap, lead-value questions.
