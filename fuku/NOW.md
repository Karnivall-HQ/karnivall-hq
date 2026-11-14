# NOW — Fuku's working memory
_Last updated: 2026-11-14 11:02 WIB (cloud heartbeat: groundwork → criterion-1 path to 12/05)_
_Rules: rewrite, never append. Max 45 lines. History lives in the journal. See `protocols/heartbeat.md` (quiet-run rule)._

## Current focus
- **M-001 (P0, at risk):** 7d Fab (11/07–11/13) **CPL Rp 116.5k** *(calc)* ❌ vs 95k (was 103.3k); Rp 333k/day vs 1M. PEIKIRA 144.0k (14), BC 52.3k (6). Control 181.9k (6), PEIKIRA2 115.6k (8), ADSET-3 Rp 0.
- **⚠️ Ad015 fallback trigger FIRED:** 7d Rp 996,561 / 6 = 166.1k; last 4 days 251.7k vs 90.8k on 11/03–11/06 *(calc)*; CTR rose to 2.3–2.5% → post-click decay (INFERRED: page mismatch makes the site fix more urgent). Note in `2026-11-10_ad015_fallback.md`.
- **ADSET-3:** Rp 0 for its whole first day (11/13 share 0%), no min spend set, no errors. Break-even at 1/3 share from 11/15: 48.4k alone / 81.3k with Ad015 paused + site fix *(calc, 11/14 08:01)*.
- **OUTBOX #1 (new, one ask):** pause Ad015 + ADSET-3 daily min Rp 75k (Markus applies; undo rules in the ask). #2 site W1+W2. #3 15 images = photos? + Kuningan open?
- **11/20 gate (refreshed 08:01):** no single lever opens it now. Nothing 129.8k; Ad015 pause 114.2k; site 107.8–117.8k; both live 11/14 eve 94.4–103.3k; each day late ≈ +5k *(calc)*. Likeliest ❌ (INFERRED). Brief top section + miss note M1 updated.
- **Criterion 1 by 12/05 still reachable** (window 11/28–12/04): asks #1 + #2 live by 11/27 ≈ 88.1k, by 11/29 94.7k, from 12/01 ❌ *(calc)*. `fab_advertising/reports/2026-12-05_criterion1_path.md`; line added to the gate-miss note.
- **M-002 (P1):** weekly report Mon 11/16 07:00; skeleton holds 11/09–11/13 pre-pull (Fab 114.5k; control 240.8k vs PEIKIRA2 86.9k; Incess 21.2k at 17.8 leads/day *(calc)*) + fatigue table (0 flags, max freq 1.63). Incess 019 Copy 5 needs ≥ 2 leads 11/13–11/16.

## Next actions (dated or triggered)
1. **11/14 ~13:00 poll:** activity log (Ad015 pause? min spend? site?) + ADSET-3 delivery today. If ask #1 applied → log in tracker change log, start the fallback's 3-day re-read (CBO CPL > 130k → re-enable Ad015) and set ADSET-3 d.
2. **11/14 ~19:00 poll:** same checks. No new asks while the 3 are open (cap).
3. **Every run:** INBOX/OUTBOX for "done" on #1, "W1 W2 done", photos answer, TourHub actor answer.
4. **When W1/W2 are applied:** re-curl the page, run `fab_advertising/reports/w1w2_lift_template.md`.
5. **11/15 07:00 readout:** tracker row; ADSET-3 share line in the read card; Ad015 (paused or still running) 7d.
6. **11/16 07:00:** weekly report from the skeleton. **11/20:** `2026-11-20_readout_template.md`. **11/27:** `2026-11-27_adset3_verdict_template.md`.
7. **Retro #3:** next quiet run (12:00).

## Groundwork backlog (for quiet runs; needs nothing from Alvian)
1. **Retro #3 — DUE (16 lessons since 11/11, over the 15 cap):** run `fuku/protocols/retro.md` on the 12:00 run (quiet, before the 13:00 poll).
2. **11/15 07:00 gate re-run:** re-run `fuku/bin/gate_model_1120.py` with 11/14 actuals locked (rule from 11/14 lesson).
3. **11/27 template:** add the criterion-1 re-run (`fuku/bin/criterion1_model_1205.py`) + the 12/19 re-plan branch to `2026-11-27_adset3_verdict_template.md`.

## Waiting on Alvian (asks live in OUTBOX "Needs you")
- #1 Pause Ad015 + ADSET-3 min Rp 75k. #2 Website W1 + W2, and who edits the site. #3 15 images = phone photos + Kuningan open? FYI: who is the "TourHub" actor?
- Later: "All-in" meaning, R5 online sellers, close rate + months stayed.

## Standing facts
- Read `playbooks/meta-ads-algorithm.md` + `meta-cpl-diagnosis.md` + `meta-tests-and-proposals.md` before any ads work; `ad-copy-page-check.md` before any copy is paste-ready.
- Cloud Fuku: routine trig_01NGMFnv9BpvRp1jQjkAwUVJ, hourly 07–22 WIB. Propose-only: never call Meta write tools, even when visible.
- Fab account 484578521394893, pixel 405755485775053. PEIKIRA campaign `120254051672440572`; control `120254051672430572`; PEIKIRA2 `120254276298070572`; ADSET-3 `120254400251570572`; Ad015 `120254063163810572`; BC campaign `120236222888610572`.
- Markus (team) edits the Fab account via the Rudi MCP app (actor 61594758338050).

## Open loops (current state, one line each)
- Activity log: no human edits since the 11/13 04:08 ADSET-3 build (checked 11/14 07:02). Control ad set delivery warning 'learning_exit_unsuccessfully'.
- Site: W1/W2 not applied (last curl 11/13 18:02). W3 on hold pending the W4 routing rule.
- 11/20 messages pre-drafted (gate-miss note + ADSET-3 clause table); numbers current as of 11/14 08:01.
- Parked in OUTBOX: optional BC204 cap probe, W3/W4 + WA follow-up script, 4 disabled ad accounts, Incess bid-cap, lead-value questions.
