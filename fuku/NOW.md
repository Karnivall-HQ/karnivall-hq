# NOW — Fuku's working memory
_Last updated: 2026-11-12 10:02 WIB (cloud heartbeat: groundwork, Wave 1 vs site price wording aligned)_
_Rules: rewrite, never append. Max 45 lines. History lives in the journal. See `protocols/heartbeat.md` (quiet-run rule)._

## Current focus
- **M-001 (P0):** 7d Fab (11/05–11/11) **CPL Rp 100.5k** *(calc)* ❌ vs 95k, best so far (112.4k → 106.8k → 100.5k); spend Rp 330k/day vs 1M. PEIKIRA 111.4k (18), BC 61.2k (5). Control 107.6k (9) vs PEIKIRA2 115.2k (9): now close.
- **No ad-account ask live; all 5 items of the 11/05 list are retired.** Item 4 retired 11/12 08:01: 087 Copy 7 runs 8-wk CPL 96.1k at the current Rp 94,250 cap (ratio 1.02, no bid edits since 09/01) → at 105k ≈ 107k *(calc)*. Only an optional BC204 probe is parked (59.8k, ratio 0.63, Rp 2.5k/day), with read rules in `fab_advertising/reports/2026-11-12_item4_bidcap_card.md`.
- **Ad015:** 7d CTR 1.96%, CPL 98,810, freq 1.34 → no fallback trigger; 92% of control spend.
- **W4 answered (17:02):** Lead = PYS event on `/thank-you-self-storage-lead/` only (24 h window); Form #10 routes some answers to a no-Lead page → the ~1 in 3 gap is by design. W3 held (field may drive routing). Lead definition stays (`2026-11-11_w4_lead_trigger.md`).
- **Ad destinations (19:02):** 13 ads = 88% of 7d spend *(calc)* all land on `/sewa-gudang-self-storage-jakarta/` (→ Form #10 only). Homepage/Form #8 risk closed. **W1 = that one page** (still "Jakarta Pusat" ×9, "Kelapa Gading" ×2, "Rp 800.000" ×3). `2026-11-11_ad_destination_check.md`.
- **Pixel Leads are ≈ 73% ad-attributed** *(calc)* (~30 unique/7d vs Meta 22; stats sum browser+server, `2026-11-11_pixel_lead_ad_share.md`), so a site fix mostly reaches ad CPL.
- **The only real levers left need Alvian:** W1/W2 site fixes and phone photos + 750/800 (OUTBOX asks #1, #2). Reels being cheapest supports vertical phone-photo ads.
- **W1/W2 paste-ready** (21:02, `fab_advertising/reports/2026-11-11_w1w2_paste_ready.md`): 9 "Jakarta Pusat" lines + 1 FAQ price line (800 ×3 = one FAQ answer + its schema copy); "Kelapa Gading" ×2 = footer address only (decide, don't auto-edit). 22:02: + B2 = WA form page heading `859f605` "mulai dari Rp 800.000 /bulan." (only other 800 in the flow; page also shows 750rb ×2) → 11 edits total. 11/12 10:02: W2/B2 replacement text now uses the site's own "Harga Promo Launching Rp750.000" (site has 0 × "FAB750"; `2026-11-12_wave1_price_wording_check.md`).
- **Wave 1 launch checklist** (20:02, `fab_advertising/creatives/2026-11-11_wave1_launch_checklist.md`): gates, optional dead-ad tidy, build spec (inside control ad set, `?ad={{ad.name}}` URL, WAVE1 names), one-line INBOX handback, read rules. Photo drop → launch in one sitting.
- **11/20 gate brief** (`fab_advertising/reports/2026-11-20_gate_brief.md`): only W1+W2 can open the gate alone (≈ 94.6k / 85.0k *(calc)*); item 4 now ≈ 107k+ (corrected 11/12); Wave 1 only if ≤ 70k. Must be live by 11/12 evening to count. **Scale plan S1/S2 have no lever left**: volume past ~Rp 330k/day needs new creative (photos).
- **M-002 (P1):** weekly report Mon 11/16 07:00; skeleton `fab_advertising/reports/weekly/2026-11-16.md` (static parts current as of 11/12 09:02: proposal retirements, gate levers, pre-ranked top 3). Incess 019 = 1 ad, 8-wk sawtooth, 2-wk CPL 34–39k → keep; judge on 2-wk (`2026-11-11_incess_019_split.md`). 019 Copy 5: 2-wk Rp 175.5k / 3 *(calc)*, post-click not fatigue; 11/16 rule: propose pause if 3-wk CPL > 105k (`2026-11-11_incess_019_copy5.md`).

## Next actions (dated or triggered)
1. **Polls:** ~13:00 and ~19:00 today (07:00 done: no human edits).
2. **11/13 07:00 readout:** tracker row; Ad015 triggers (7d CTR < 1.30% / CPL > 120k / freq > 2.5); placement split again only if Feed stays > 150k for a 2nd week (then consider a Feed→Reels test, not an exclusion).
3. **Every run:** check INBOX/OUTBOX for "W1 W2 done", photos, 750 vs 800, "applied N". Log applied changes in `fab_advertising/reports/m001_tracker.md`.
4. **When W1/W2 are applied:** re-curl the 3 Jakarta pages, run `fab_advertising/reports/w1w2_lift_template.md` (day-7 + day-14 pixel reads vs 27-d baseline 3.72% VC→Lead).
5. **W1/W2 re-ask sent 11/12 07:02 (+1 push).** No more pushes on it today. If still unanswered at 11/13 07:00, model the 11/20 gate without it and say so in the readout.
6. **Retro #3:** ~11/18 or at 15 new lessons (Retro #2 done 11/11; new playbook `meta-tests-and-proposals.md`).
7. **11/20:** if 7d CPL > 95k, tell Alvian criterion 2 is out of reach by 12/05.

## Groundwork backlog (for quiet runs; needs nothing from Alvian)
1. **Scale plan v2:** rebuild the Rp 1M/day path without BC cap levers: how many photo-ad waves at what CPL, and the per-wave capacity from the 8-week history.
2. **Partial-week pre-pull for 11/16:** after the 13:00 poll, nothing; on a quiet run 11/14–15, pull 11/09–11/13 Fab+Incess ad-set rows into the skeleton as a draft so Monday is a delta.
3. **WA follow-up script price wording:** align `2026-11-06_wa_followup_script.md` to "harga promo launching" + 750 the same way (draft only, nothing sent).

## Waiting on Alvian (asks live in OUTBOX "Needs you")
- Website W1 + W2, and who edits the site.
- Phone photos; price 750 vs 800rb. Later: close rate + months stayed; confirm no minimum rental / no deposit / free pickup.

## Standing facts
- Read `playbooks/meta-ads-algorithm.md` + `meta-cpl-diagnosis.md` + `meta-tests-and-proposals.md` before any ads work. Wave 1 is read with `fab_advertising/reports/wave1_read_template.md`.
- Cloud Fuku: routine trig_01NGMFnv9BpvRp1jQjkAwUVJ, hourly 07–22 WIB. Propose-only: never call Meta write tools, even when visible.
- Fab pixel/dataset id **405755485775053**. PEIKIRA campaign `120254051672440572`, control ad set `120254051672430572`, PEIKIRA2 `120254276298070572`, BC campaign `120236222888610572` (= "BC CBObass005").
- Markus (team) edits the Fab account via the Rudi MCP app (actor 61594758338050).

## Open loops (current state, one line each)
- Activity log: no human edits since the 11/09 14:11 ad-006 pause (last check 11/11 19:02). PEIKIRA2 ACTIVE, ~35% of PEIKIRA spend.
- Site: W1/W2 not applied (copy re-checked 11/09 07:02; tracking curl 11/11 17:02). W3 on hold pending the W4 routing rule.
- Parked in OUTBOX: optional BC204 cap probe, W3/W4 + WA follow-up script, 4 disabled ad accounts, Incess bid-cap, lead-value questions.
