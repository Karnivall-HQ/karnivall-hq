# NOW — Fuku's working memory
_Last updated: 2026-11-14 20:02 WIB (cloud heartbeat: 11/20 gate-miss note dry-run)_
_Rules: rewrite, never append. Max 45 lines. History lives in the journal. See `protocols/heartbeat.md` (quiet-run rule)._

## Current focus
- **M-001 (P0, at risk):** 7d Fab (11/07–11/13) **CPL Rp 116.5k** *(calc)* ❌ vs 95k (was 103.3k); Rp 333k/day vs 1M. PEIKIRA 144.0k (14), BC 52.3k (6). Control 181.9k (6), PEIKIRA2 115.6k (8), ADSET-3 Rp 0.
- **⚠️ Ad015 fallback trigger FIRED:** 7d Rp 996,561 / 6 = 166.1k; last 4 days 251.7k vs 90.8k on 11/03–11/06 *(calc)*; CTR rose to 2.3–2.5% → post-click decay (INFERRED: page mismatch makes the site fix more urgent). Note in `2026-11-10_ad015_fallback.md`.
- **ADSET-3:** Rp 0 / 0 impr through 11/14 19:02 (~39h live), no min spend set. Today to 19:02: control Rp 112,105 / 3, PEIKIRA2 Rp 111,712 / 0 (part-day, not a metric). Break-even at 1/3 share from 11/15: 48.4k alone / 81.3k with Ad015 paused + site fix *(calc, 11/14 08:01)*.
- **OUTBOX #1 (new, one ask):** pause Ad015 + ADSET-3 daily min Rp 75k (Markus applies; undo rules in the ask). #2 site W1+W2. #3 15 images = photos? + Kuningan open?
- **11/20 gate (refreshed 08:01):** no single lever opens it now. Nothing 129.8k; Ad015 pause 114.2k; site 107.8–117.8k; both live 11/14 eve 94.4–103.3k; each day late ≈ +5k *(calc)*. Likeliest ❌ (INFERRED). Brief top section + miss note M1 updated.
- **Criterion 1 by 12/05 still reachable** (window 11/28–12/04): asks #1 + #2 live by 11/27 ≈ 88.1k, by 11/29 94.7k, from 12/01 ❌ *(calc)*. `fab_advertising/reports/2026-12-05_criterion1_path.md`; line added to the gate-miss note.
- **Retro #3 done 12:01:** M-001 bottleneck = approval latency; criterion 1 first, criterion 2 → 01/15 re-plan on 11/20. Push sent for asks #1 + #2.
- **M-002 (P1):** weekly report Mon 11/16 07:00; skeleton holds 11/09–11/13 pre-pull (Fab 114.5k; control 240.8k vs PEIKIRA2 86.9k; Incess 21.2k at 17.8 leads/day *(calc)*) + fatigue table (0 flags, max freq 1.63). Incess 019 Copy 5 needs ≥ 2 leads 11/13–11/16.

## Next actions (dated or triggered)
1. **Polls today done (13:00, 19:00):** no edits, ADSET-3 Rp 0, site unchanged. Next poll inside the 11/15 07:00 readout. If ask #1 applied → tracker change log, fallback 3-day re-read (CBO CPL > 130k → re-enable Ad015), set ADSET-3 d.
2. No new asks while the 3 are open (cap).
3. **Every run:** INBOX/OUTBOX for "done" on #1, "W1 W2 done", photos answer, TourHub actor answer.
4. **When W1/W2 are applied:** re-curl the page, run `fab_advertising/reports/w1w2_lift_template.md`.
5. **11/15 07:00 readout:** run the tracker's 07:00 routine (gate + criterion-1 last workable date, now 11/29); tracker row; ADSET-3 share line in the read card; Ad015 (paused or still running) 7d.
6. **11/16 07:00:** weekly report from the skeleton (run sheet rows 1–13; rule windows end 11/15). **11/20:** `2026-11-20_readout_template.md` (Step 4b = criterion-1 date). **11/27:** `2026-11-27_adset3_verdict_template.md` (dry-run done: pulls V1–V8, V8 = tracker row first).
7. **Retro #4:** at > 15 lessons or 11/21 (7 days).

## Groundwork backlog (for quiet runs; needs nothing from Alvian)
1. **11/15 07:00 gate re-run:** re-run `fuku/bin/gate_model_1120.py` with 11/14 actuals locked (playbook `meta-modelling-and-planning.md` §A2).
2. **Wave 1 checklist vs ADSET-3:** if the 15 team images are the phone photos, mark which Wave 1 steps ADSET-3 already covers in `creatives/2026-11-11_wave1_launch_checklist.md` (avoid a duplicate ask).
3. **11/16 weekly report vs 11/15 readout overlap:** check the 11/16 run sheet reuses the 11/15 07:00 tracker row instead of re-pulling (same 7d window end 11/15? no: 11/09–11/15) and note which numbers are copy vs new pull.

## Waiting on Alvian (asks live in OUTBOX "Needs you")
- #1 Pause Ad015 + ADSET-3 min Rp 75k. #2 Website W1 + W2, and who edits the site. #3 15 images = phone photos + Kuningan open? FYI: who is the "TourHub" actor?
- Later: "All-in" meaning, R5 online sellers, close rate + months stayed.

## Standing facts
- Read `playbooks/meta-ads-algorithm.md` + `meta-cpl-diagnosis.md` + `meta-tests-and-proposals.md` before any ads work, `meta-modelling-and-planning.md` before any model/plan; `ad-copy-page-check.md` before any copy is paste-ready.
- Cloud Fuku: routine trig_01NGMFnv9BpvRp1jQjkAwUVJ, hourly 07–22 WIB. Propose-only: never call Meta write tools, even when visible.
- Fab account 484578521394893, pixel 405755485775053. PEIKIRA campaign `120254051672440572`; control `120254051672430572`; PEIKIRA2 `120254276298070572`; ADSET-3 `120254400251570572`; Ad015 `120254063163810572`; BC campaign `120236222888610572`.
- Markus (team) edits the Fab account via the Rudi MCP app (actor 61594758338050).

## Open loops (current state, one line each)
- Activity log: no human edits since the 11/13 04:08 ADSET-3 build (checked 11/14 19:02). Control ad set delivery warning 'learning_exit_unsuccessfully'.
- Site (fabwarehouses.com): W1/W2 not applied (curl 11/14 19:02: Jakarta Pusat ×9, Rp 800.000 ×3, "akan launching" ×3). W3 on hold pending the W4 routing rule.
- 11/20 messages pre-drafted and dry-run (gate-miss note, S1 card, readout): every ⟨⟩ maps to readout Step 0 / P1–P6 / Step 2–4b; criterion-1 line comes from Step 4b. 11/16 report: "What changed" + action #3 pre-written.
- Parked in OUTBOX: optional BC204 cap probe, W3/W4 + WA follow-up script, 4 disabled ad accounts, Incess bid-cap, lead-value questions.
