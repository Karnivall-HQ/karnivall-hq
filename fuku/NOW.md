# NOW — Fuku's working memory
_Last updated: 2026-11-12 19:02 WIB (cloud heartbeat: 19:00 poll + G6 sweep + Wave 1 read 2-week rule)_
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
- **11/20 gate brief** (`fab_advertising/reports/2026-11-20_gate_brief.md`): only W1+W2 can open the CPL gate alone (≈ 94.6k / 85.0k *(calc)*); Wave 1 only if ≤ 70k. **Volume (scale plan v2, 11/12 11:01, `2026-11-12_scale_plan_v2.md`):** a winning wave adds Rp 100–185k/day at ≤ 95k and swings ±2× weekly; Rp 1M/day needs 4–7 winners → realistic 12/05 ≈ Rp 450–520k/day *(calc)*. Judge waves on 2 weeks. When photos are answered, ask for 12, not 2: **shoot card v2** (12:02) `fab_advertising/creatives/2026-11-12_shoot_card_v2.md` maps P1–P12 → Waves 1–4. Site lists unit sizes 3.8/7.6/15.2 m³ and kasur only from Medium → S2 sticker gate. **Wave 3–4 copy ready** (13:01) `fab_advertising/creatives/2026-11-12_creative_batch_03_waves3-4.md`; R5/S3 situations appear 0× on the landing page → Wave 4 runs R4 first. **Wave 2 build sheet** (14:02) `fab_advertising/creatives/2026-11-12_wave2_build_sheet.md`: 5 paste rows + pick-3 by Wave-1 winner; fixed S6 "bisa diakses" (page: weekend loading), S2 kasur/sofa (Medium+), B5 same-day (0× on page). **Wave 1 build sheet** (15:02) `fab_advertising/creatives/2026-11-12_wave1_build_sheet.md`: S1/B1/B2 paste rows, linked from checklist §C; B2 "bayar bulan pertama aja" → "bayar per bulan"; location → "ITC Kuningan Ambasador, Sudirman" (page names one site; swap Wave 2 rows at build). **Wave 3–4 build sheet** (17:02) `fab_advertising/creatives/2026-11-12_wave3-4_build_sheet.md`: R1–R4 + S3 + **new K1 (offices, reason-to-buy STATED: Kantor ×14)**; **R5 gated** (page's one "online" hit = Fab's e-commerce warehouse product → online sellers may belong to the Rp 5jt product); Wave 4 order R4 → K1 → S3; shoot card has P12-alt. Page also says "Harga sudah All-in" (noted, not used until Alvian says what it covers). **18:02–19:02:** Wave 2 rows use the one-site location line; new gate **G6** (page: site "akan launching") now sits in every build sheet + Wave 1 checklist §A; only B2 "langsung dijemput" and B5 "siap dipakai" carry timing promises (swap lines given). Wave 1 read: day-7 KEEP provisional, winner only after day 14.
- **M-002 (P1):** weekly report Mon 11/16 07:00; skeleton `fab_advertising/reports/weekly/2026-11-16.md` (static parts current as of 11/12 09:02: proposal retirements, gate levers, pre-ranked top 3). Incess 019 = 1 ad, 8-wk sawtooth, 2-wk CPL 34–39k → keep; judge on 2-wk (`2026-11-11_incess_019_split.md`). 019 Copy 5: 2-wk Rp 175.5k / 3 *(calc)*, post-click not fatigue; 11/16 rule: propose pause if 3-wk CPL > 105k (`2026-11-11_incess_019_copy5.md`).

## Next actions (dated or triggered)
1. **Polls:** today's 3 done (07:00, 13:00, 19:00: no edits). Next poll inside the 11/13 07:00 readout.
2. **11/13 07:00 readout:** tracker row; Ad015 triggers (7d CTR < 1.30% / CPL > 120k / freq > 2.5); placement split again only if Feed stays > 150k for a 2nd week (then consider a Feed→Reels test, not an exclusion).
3. **Every run:** check INBOX/OUTBOX for "W1 W2 done", photos, 750 vs 800, "applied N". Log applied changes in `fab_advertising/reports/m001_tracker.md`.
4. **When W1/W2 are applied:** re-curl the 3 Jakarta pages, run `fab_advertising/reports/w1w2_lift_template.md` (day-7 + day-14 pixel reads vs 27-d baseline 3.72% VC→Lead).
5. **W1/W2 re-ask sent 11/12 07:02 (+1 push).** No more pushes on it today. If still unanswered at 11/13 07:00, model the 11/20 gate without it and say so in the readout.
6. **Retro #3:** ~11/18 or at 15 new lessons (Retro #2 done 11/11; new playbook `meta-tests-and-proposals.md`).
7. **11/20:** if 7d CPL > 95k, tell Alvian criterion 2 is out of reach by 12/05.

## Groundwork backlog (for quiet runs; needs nothing from Alvian)
1. **Partial-week pre-pull for 11/16:** on a quiet run 11/14–15, pull 11/09–11/13 Fab+Incess ad-set rows (by object_ids) into the skeleton as a draft so Monday is a delta.
2. **11/20 gate brief refresh** after the 11/13 readout: re-run the W1/W2 and Wave 1 paths on the new 7d (and "no site fix" path if W1/W2 still unanswered, per action 5).
3. **Wave 1 one-pager for Markus:** checklist + build sheet + read rules as one apply-ready page (he builds via Rudi MCP), so photo drop → launch needs no assembly.

## Waiting on Alvian (asks live in OUTBOX "Needs you")
- Website W1 + W2, and who edits the site.
- Phone photos; price 750 vs 800rb. Later (G6): is ITC Kuningan Ambasador open for survey/move-in now (page: "akan launching")? What does "All-in" cover? Later (Wave 4 only): may self-storage be sold to online sellers (R5)? Later: close rate + months stayed; confirm no minimum rental / no deposit / free pickup.

## Standing facts
- Read `playbooks/meta-ads-algorithm.md` + `meta-cpl-diagnosis.md` + `meta-tests-and-proposals.md` before any ads work; `ad-copy-page-check.md` before any copy is paste-ready. Wave 1 is read with `fab_advertising/reports/wave1_read_template.md`.
- Cloud Fuku: routine trig_01NGMFnv9BpvRp1jQjkAwUVJ, hourly 07–22 WIB. Propose-only: never call Meta write tools, even when visible.
- Fab pixel/dataset id **405755485775053**. PEIKIRA campaign `120254051672440572`, control ad set `120254051672430572`, PEIKIRA2 `120254276298070572`, BC campaign `120236222888610572` (= "BC CBObass005").
- Markus (team) edits the Fab account via the Rudi MCP app (actor 61594758338050).

## Open loops (current state, one line each)
- Activity log: no human edits since the 11/09 14:11 ad-006 pause (last check 11/12 19:02, log since 11/11 19:00 empty). PEIKIRA2 ACTIVE, ~35% of PEIKIRA spend.
- Site: W1/W2 not applied (copy re-checked 11/09 07:02; tracking curl 11/11 17:02). W3 on hold pending the W4 routing rule.
- Parked in OUTBOX: optional BC204 cap probe, W3/W4 + WA follow-up script, 4 disabled ad accounts, Incess bid-cap, lead-value questions.
