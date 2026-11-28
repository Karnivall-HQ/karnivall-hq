# NOW — Fuku's working memory
_Last updated: 2026-11-28 08:02 WIB (cloud heartbeat: groundwork — incess_r2.py built, 11/20 files archived)_
_Rules: rewrite, never append. Max 45 lines. History lives in the journal. See `protocols/heartbeat.md` (quiet-run rule)._

## Current focus
- **M-001 (P0):** 7d 11/21–11/27 **Rp 986,743 / 15 = 65.8k ✅** *(calc)*; BC 99.9% of spend (140.8k/day). Criterion 1 on track for 12/05 (model 65.9k OK, LWD 12/03; window 11/28–12/04 needs ≥ 11 leads, expected 15, P(miss) 12% *(calc)*). Criterion 2 off track (14% of the leg); re-based 12:01: honest date mid 02/16 if W1 (016 + 018) is live 12/01, 01/15 MISS in every case *(calc)*.
- **ADSET-3 closed:** UNDER-TESTED (starved), Rp 277 / 14d. Photo-free Wave 1 = 016 + 018 (S30 if Kuningan not visitable); page-checked 11/27 11:01, ask line paste-ready in `criterion2_replan.md`. Ask only after W0 moves.
- **Volume lever asked:** OUTBOX #1 = BC W0 as 2 fields (204 + 3-21 + N2), re-asked 11/27 07:01 (not re-asked again: already one line). 11/27: 204 Rp 2,628, 3-21 Rp 3,073, 201 Rp 45,154 / 0; BC day 127.5k / 2 (4-08 22,890 / 1, 3-30 1,234 / 1).
- **M-002 (P1):** Incess 4d 11/23–11/26 **31.1k** *(calc)* (prior wk 37.8k) → R2 heading to close; 4 picks 30.7k → R7 heading to close; watch 047 (47.1k, post-click) + 030 (Rp 249k / 2). Cut-list skeleton ready. Weekly 11/30.

## Next actions (dated or triggered)
1. **Every run:** INBOX/OUTBOX for "W0 done", "W1 W2 done", Kuningan answer.
2. **Polls 11/28:** 07:00 done. Next ≈ 13:00 + 19:00 (activity log + `w1w2_snapshot.py --no-save`).
3. **"W1 W2 done" seen:** follow the 6-step runbook at the top of `w1w2_lift_template.md` (snapshot PASS → log → `w1w2_read.py dates` → d7/d14 reads).
4. **"W0 done" seen in the log:** follow the 6-step runbook at the top of `2026-11-20_bc_cap_ladder_card.md` (log → re-base §D–§E → N2 check → daily `bc_ladder_read.py --row 204 --row 3-21 --n2` → d7 ladder / d14 N2). 201 = control (in `--rest`).
5. **11/29–12/05 07:00 readouts** (11/28 run: 0 locked, status line 11 needed / 15 expected): after locking, run `fuku/bin/c1_closeout.py --locked <window spend> <leads> <days>` (12/05: add `--w1 <date|none>` → criterion-2 line, rules 5–6) (window 11/28–12/04; rules in `2026-12-05_criterion1_path.md` close-out). Needs ≥ 10 leads at ~945k; P(miss) now 17% *(calc)*.
6. **11/30 weekly:** fill `reports/weekly/2026-11-30.md` (rules R1–R7; R2 = `fuku/bin/incess_r2.py`, R7 = `fuku/bin/incess_r7.py`; run sheet dry-run 11/27 18:02, calls 0–10b, pixel prior row re-pulled in call 8).

## Groundwork backlog (for quiet runs; needs nothing from Alvian)
1. **`--rest` input helper:** one read-only entities call on BC campaign → print the `bc_ladder_read.py` inputs (BC total − 204 − 3-21 − N2, 204F ad) so the W0 daily read is one paste.
2. **11/30 weekly full dry-run with both scripts:** R2 (`incess_r2.py`) + R7 (`incess_r7.py`) outputs pasted into the skeleton on the 4d pre-pull, check no ⟨⟩ left without a named source.
3. **M-001 criterion-2 honesty note:** one-page "what 12/05 looks like" (criterion 1 likely ✅, criterion 2 MISS in every case) so the 12/05 close-out text is pre-agreed, not improvised.

## Waiting on Alvian (asks live in OUTBOX "Needs you")
- #1 BC Wave 0 (204 + 3-21 + N2). #2 Site W1 + W2 + who edits.
- Parked: undo (126.2k MISS 11/23), Ad015 + ADSET-3 min (now moot: ADSET-3 closed), Kuningan open?, "TourHub" FYI, close rate + months stayed.

## Standing facts
- Read `playbooks/meta-ads-algorithm.md` + `meta-cpl-diagnosis.md` + `meta-tests-and-proposals.md` before any ads work, `meta-modelling-and-planning.md` before any model/plan, `meta-creative-build.md` before any brief/build row, `ad-copy-page-check.md` before copy is paste-ready.
- Cloud Fuku: routine trig_01NGMFnv9BpvRp1jQjkAwUVJ, hourly 07–22 WIB. Propose-only: never call Meta write tools, even when visible.
- Fab account 484578521394893, pixel 405755485775053. Site page https://fabwarehouses.com/sewa-gudang-self-storage-jakarta/. PEIKIRA campaign `120254051672440572` (Rp 3M/day, bid cap 105k); control `120254051672430572`; PEIKIRA2 `120254276298070572`; ADSET-3 `120254400251570572`; Ad015 `120254063163810572`; BC campaign `120236222888610572` (Rp 5M/day, caps 94,250).
- Markus (team) edits the Fab account via the Rudi MCP app (actor 61594758338050).
- Locks PEIKIRA: 11/21 26 0 · 11/22 208 0 · 11/23 650 0 · 11/24 242 0 · 11/25 28 0 · 11/26 143 0 · 11/27 0 0. BC: 11/21 85407 0 · 11/22 96167 3 · 11/23 166269 1 · 11/24 145539 4 · 11/25 186123 2 · 11/26 178399 3 (relocked +193) · 11/27 127542 2. Model: `--peik 1297 0 --peik-cpl 190609 --bc 985446 15 --p2 924806 8 --budget 650 --cap-throttled`.

## Open loops (current state, one line each)
- Activity log (11/28 07:01): 0 entries since 11/27 19:00; no human edits since 11/15 00:42. Caps 105k / 94,250, all ACTIVE.
- BC 11/27 dipped to 127.5k (from 178k) at unchanged caps; 201 led again (45k / 0). 7d BC avg 140.8k/day *(calc)*.
- Site (11/28 07:01 snapshot `--no-save`, unchanged): Jakarta Pusat ×9, Kelapa Gading ×2, 800.000 ×3, akan launching ×3. WA script NOT sent; page re-check 11/27 14:01 = no claim changed (gates: 800, G6, All-in).
- Pixel (pulled 11/27): 11/16–11/25 PT VC 1,382 / Lead 49 = 3.55% *(calc)*; ~1,000 VC/week. Lift rule in `w1w2_lift_template.md` (11/27 section). W3 unreadable (MDE +21% at d14) → no-regret ship after W1/W2 d14, only if the field doesn't route.
