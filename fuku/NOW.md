# NOW — Fuku's working memory
_Last updated: 2026-11-26 13:02 WIB (cloud heartbeat: 13:00 poll)_
_Rules: rewrite, never append. Max 45 lines. History lives in the journal. See `protocols/heartbeat.md` (quiet-run rule)._

## Current focus
- **M-001 (P0):** 7d 11/19–11/25 **Rp 855,028 / 12 = 71.3k ✅** *(calc)* (up from 56.3k: 11/18's 4 leads left the window); BC 99.8% of spend (71.1k). Criterion 1 met by mix, LWD 12/03 (model 71.3k OK). Criterion 2 off track (Rp 122k/day = 12% of the leg).
- **BC rising on its own:** 11/23 166k, 11/24 146k, 11/25 **186k / 2** at unchanged 94,250 caps; 201 = Rp 86k (46% of BC) / 2. Still 3.7% of the 5M budget, so the cap still binds, but W0's marginal value for 201 is shrinking. 204 Rp 2k, 3-21 Rp 5k: the raise still matters for them.
- **Volume lever asked:** OUTBOX #1 = BC Wave 0, ~72h open, re-asked as one line today (stalled-asks rule).
- **M-002 (P1):** Incess 37.8k (+42.9% WoW) = placement mix + in-placement decline. Watch, no ask.

## Next actions (dated or triggered)
1. **Every run:** INBOX/OUTBOX for "W0 done", "W1 W2 done", Kuningan answer.
2. **Polls 11/26:** 07:00 + 13:00 done. Next ≈ 19:00 (activity log + site curl only).
3. **"W0 done" seen in the log:** re-base day (playbook §D–§E): split day 1 at the change time, read the 3 ad sets on spend ÷ old pace + CPL; rules in `2026-11-20_bc_cap_ladder_card.md` + `fuku/bin/bc_ladder_read.py`. Baseline for 201 = its 7d average (now ~60–86k/day), not ~17k.
4. **11/27 07:00:** ADSET-3 verdict (`2026-11-27_adset3_verdict_template.md`); read real spend per ad (003, 010 v03, S30 v04, 007, 018 started delivery). Also: if BC stays > 150k/day for a 4th day, re-check W0's 201 row (CPL ÷ cap on fresh 7d) before any further re-ask.
5. **11/30 weekly:** fill `reports/weekly/2026-11-30.md` (rules R1–R6). Incess placement rule + BC3-13 c2 R3 pause line (`2026-11-23_bc_8wk_prepull.md`).

## Groundwork backlog (for quiet runs; needs nothing from Alvian)
1. **≈ 11/27 quiet run: Incess placement pre-pull 11/23–11/26** (skeleton call 6a shape) → cross-check only, no verdict < 7d.
2. **M-002 refill:** Incess 047 flag (40.1k > 35.6k) on 11/23–11/26 daily rows with the same call; note only.
3. **Fab site / WA script:** refresh `w1w2_paste_ready.md` §F only if a fresh curl shows the page changed.

## Waiting on Alvian (asks live in OUTBOX "Needs you")
- #1 BC Wave 0. #2 Site W1 + W2 + who edits.
- Parked: undo (126.2k MISS 11/23), Ad015 + ADSET-3 min, Kuningan open?, "TourHub" FYI, close rate + months stayed.

## Standing facts
- Read `playbooks/meta-ads-algorithm.md` + `meta-cpl-diagnosis.md` + `meta-tests-and-proposals.md` before any ads work, `meta-modelling-and-planning.md` before any model/plan, `meta-creative-build.md` before any brief/build row, `ad-copy-page-check.md` before copy is paste-ready.
- Cloud Fuku: routine trig_01NGMFnv9BpvRp1jQjkAwUVJ, hourly 07–22 WIB. Propose-only: never call Meta write tools, even when visible.
- Fab account 484578521394893, pixel 405755485775053. Site page https://fabwarehouses.com/sewa-gudang-self-storage-jakarta/. PEIKIRA campaign `120254051672440572` (Rp 3M/day, bid cap 105k); control `120254051672430572`; PEIKIRA2 `120254276298070572`; ADSET-3 `120254400251570572`; Ad015 `120254063163810572`; BC campaign `120236222888610572` (Rp 5M/day, caps 94,250).
- Markus (team) edits the Fab account via the Rudi MCP app (actor 61594758338050).
- Locks PEIKIRA: 11/19 628 0 · 11/20 41 0 · 11/21 26 0 · 11/22 208 0 · 11/23 650 0 · 11/24 242 0 · 11/25 28 0. BC: 11/19 87495 2 · 11/20 86268 0 · 11/21 85407 0 · 11/22 96167 3 · 11/23 166269 1 · 11/24 145539 4 · 11/25 186060 2. Model: `--peik 1823 0 --peik-cpl 190609 --bc 853205 12 --p2 924806 8 --budget 650 --cap-throttled`.

## Open loops (current state, one line each)
- Activity log (11/26 13:02): 0 entries since 11/25 19:00; no human edits since 11/15 00:42. Caps 105k / 94,250, all ACTIVE.
- BC 3-day rise at unchanged caps (166k → 146k → 186k), 201-led: 7d BC avg 121.9k/day *(calc)*.
- Site (11/26 13:02 curl, unchanged): Jakarta Pusat ×9, Kelapa Gading ×2, 800.000 ×3, akan launching ×3. WA script NOT sent.
- Pixel 11/16–11/22: VC 819, Form 52, Lead 31 (3.8% VC→Lead, flat).
