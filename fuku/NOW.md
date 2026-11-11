# NOW — Fuku's working memory
_Last updated: 2026-11-11 20:02 WIB (cloud heartbeat: quiet run; groundwork → Wave 1 launch checklist for Markus)_
_Rules: rewrite, never append. Max 45 lines. History lives in the journal. See `protocols/heartbeat.md` (quiet-run rule)._

## Current focus
- **M-001 (P0):** 7d Fab (11/04–11/10) **CPL Rp 106.8k** *(calc)* ❌ vs 95k, improving (112.4k → 106.8k); spend Rp 336k/day vs 1M. PEIKIRA 118.9k (17 leads), BC 65.7k (5 leads).
- **No ad-account ask live.** PEIKIRA2 pause dropped (2 leads on 11/10). Item 1 (cut IG Stories) retired: 7d Stories 119k, Feed 166k, Reels 48k *(calc)*. Items 2 (WA Status junk gone, freq 1.11; WA+Threads 9.9% of BC spend, `2026-11-11_bc_item2_revalidate.md`), 3 (BC keep-5) and 5 (dead PEIKIRA ads, 0.9% of spend) retired 11/11. **Only item 4 remains** (087 Copy 7 cap 94,250 → 105k).
- **Ad015:** 7d CTR 1.73%, CPL 98,955, freq 1.36 → no fallback trigger; 94% of control spend.
- **W4 answered (17:02):** Lead = PYS event on `/thank-you-self-storage-lead/` only (24 h window); Form #10 routes some answers to a no-Lead page → the ~1 in 3 gap is by design. W3 held (field may drive routing). Lead definition stays (`2026-11-11_w4_lead_trigger.md`).
- **Ad destinations (19:02):** 13 ads = 88% of 7d spend *(calc)* all land on `/sewa-gudang-self-storage-jakarta/` (→ Form #10 only). Homepage/Form #8 risk closed. **W1 = that one page** (still "Jakarta Pusat" ×9, "Kelapa Gading" ×2, "Rp 800.000" ×3). `2026-11-11_ad_destination_check.md`.
- **Pixel Leads are ≈ 73% ad-attributed** *(calc)* (~30 unique/7d vs Meta 22; stats sum browser+server, `2026-11-11_pixel_lead_ad_share.md`), so a site fix mostly reaches ad CPL.
- **The only real levers left need Alvian:** W1/W2 site fixes and phone photos + 750/800 (OUTBOX asks #1, #2). Reels being cheapest supports vertical phone-photo ads.
- **Wave 1 launch checklist** (20:02, `fab_advertising/creatives/2026-11-11_wave1_launch_checklist.md`): gates, optional dead-ad tidy, build spec (inside control ad set, `?ad={{ad.name}}` URL, WAVE1 names), one-line INBOX handback, read rules. Photo drop → launch in one sitting.
- **11/20 gate brief** (`fab_advertising/reports/2026-11-20_gate_brief.md`): only W1+W2 can open the gate alone (≈ 94.6k / 85.0k *(calc)*); item 4 alone ≈ 104k; Wave 1 only if ≤ 70k. Must be live by 11/12 evening to count.
- **M-002 (P1):** weekly report Mon 11/16 07:00; skeleton `fab_advertising/reports/weekly/2026-11-16.md`. Incess 019 = 1 ad, 8-wk sawtooth, 2-wk CPL 34–39k → keep; judge on 2-wk (`2026-11-11_incess_019_split.md`). 019 Copy 5: 2-wk Rp 175.5k / 3 *(calc)*, post-click not fatigue; 11/16 rule: propose pause if 3-wk CPL > 105k (`2026-11-11_incess_019_copy5.md`).

## Next actions (dated or triggered)
1. **Polls:** next is inside the 11/12 07:00 readout (13:00 + 19:00 done today, both empty).
2. **11/12 07:00 readout:** tracker row; Ad015 triggers (7d CTR < 1.30% / CPL > 120k / freq > 2.5); placement split again only if Feed stays > 150k for a 2nd week (then consider proposing a Feed→Reels test, not an exclusion).
3. **Every run:** check INBOX/OUTBOX for "W1 W2 done", photos, 750 vs 800, "applied N". Log applied changes in `fab_advertising/reports/m001_tracker.md`.
4. **When W1/W2 are applied:** re-curl the 3 Jakarta pages, run `fab_advertising/reports/w1w2_lift_template.md` (day-7 + day-14 pixel reads vs 27-d baseline 3.72% VC→Lead).
5. **If OUTBOX asks stay unanswered by 11/12 07:00 (> 48h):** shrink to ONE line: fix the 2 site lines today (location → Kuningan/Sudirman, price → whichever is true, 750 or 800). Covers W1+W2+price fact (gate brief).
6. **Retro #3:** ~11/18 or at 15 new lessons (Retro #2 done 11/11; new playbook `meta-tests-and-proposals.md`).
7. **11/20:** if 7d CPL > 95k, tell Alvian criterion 2 is out of reach by 12/05.

## Groundwork backlog (for quiet runs; needs nothing from Alvian)
1. **Item 4 apply-ready card:** 087 Copy 7 cap 94,250 → 105k with the 5-day revert rule and read rule, one screen, for the 11/12 re-ask if site asks stay stuck.
2. **11/12 07:00 re-ask line, pre-written:** one-line site ask: fix ONE page `/sewa-gudang-self-storage-jakarta/` (location → Kuningan/Sudirman Jakarta Selatan; price → 750 or 800, whichever is true).
3. **W1 replacement text, paste-ready:** exact before → after lines for the 9 "Jakarta Pusat", 2 "Kelapa Gading", 3 "Rp 800.000" hits on that page, so the site fix is copy-paste.

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
- Parked in OUTBOX: M-001 item 4, W3/W4 + WA follow-up script, 4 disabled ad accounts, Incess bid-cap, lead-value questions.
