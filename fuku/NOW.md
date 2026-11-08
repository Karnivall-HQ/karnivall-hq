# NOW — Fuku's working memory
_Last updated: 2026-11-08 08:01 WIB (cloud heartbeat)_

## Current focus
- **M-001 (P0):** 7d CPL **Rp 115.1k** (11/01–11/07) vs the 95k target. **The single live ask is now "pause PEIKIRA2"** (Rp 539k / 2 leads vs control Rp 350k / 5 = Rp 70k). Item 1 (IG Stories) is parked behind it. Website W1–W4 still waiting. Batch 01 on hold.

## Next actions
000. ✅ 11/08 07:02 readout: PEIKIRA2 hit the re-trigger (Rp 539,027 / 2 leads ≥ Rp 500k) and took 87.6% *(calc)* of PEIKIRA spend on 11/07 for 0 leads → single [DECISION] "pause PEIKIRA2" at OUTBOX top + push. Next re-ask no earlier than 11/09 07:00 (fold it into the weekly report). If applied: log it in the tracker change log and read the control's CPL on 11/10–11/11.
00. ✅ 11/07 07:02 readout done: PEIKIRA2 got its 2nd lead (Rp 336,659 / 2 = Rp 168k) vs control Rp 321,669 / 4 → pause rule (≤1 lead) no longer applies → **hold to 11/10, no ask**. Keep checking its spend share at each daily readout; re-trigger the pause ask only if it reaches ≥ Rp 500k with ≤ 2 leads (≈5× target).
0. **Read `fuku/memory/playbooks/meta-ads-algorithm.md` + `meta-cpl-diagnosis.md` before any ads work.** Retro #1 done 11/06 09:01; next retro ~11/13 or at 15 new lessons.
0b. Don't add new decision packs until something is applied. The only live ask is "paused 2" (PEIKIRA2 off); item 1 parked behind it.
1. Each heartbeat: check OUTBOX/INBOX for "applied 1,2,…", "W1/W2 done", the photo shoot, and facts (750 vs 800, close rate, months stayed). Log applied changes in `fab_advertising/reports/m001_tracker.md`.
2. Daily (first heartbeat after 07:00 WIB): tracker readout row + activity log (limit ≤ 40). ✅ done 11/07. ✅ 11/07 09:02: item 1 re-asked as a one-liner at top of OUTBOX (+ push notification). Next re-ask no earlier than 11/08 09:00; meanwhile no new asks.
3. When W1/W2 are applied: re-curl the 3 Jakarta pages to verify, then re-pull the funnel and compare to the ✅ baseline (14:02, `fab_advertising/reports/2026-11-06_pixel_funnel_baseline.md`: VC→Lead 3.8%, VC→Form 6.4%, Form→Lead 60%). 14:02 curl: site still unedited.
4. ~~ImageAd 201B~~ ✅ checked 11/06 08:02: it's immaterial (Rp 0 spend over 14d). Drop it unless Manny5 gets a bid-cap raise.
5. 2026-11-10: read PEIKIRA2 vs the old PEIKIRA ad set, plus the effect of any applied changes.
6. ✅ BC Image087 viewed 11/06 11:01: home-clutter phone photo + 3 story stickers, no warehouse (`fab_advertising/creatives/2026-11-05_review/bc_image087.jpg`). Shoot ask shrunk in OUTBOX. ✅ 12:01: batch 01 v2 shot list done (`fab_advertising/creatives/2026-11-06_batch01_v2_home_clutter_shotlist.md`), 6 home shots + sticker text. Launch still held to after the 11/10 read.
7. M-002: first weekly report Mon 2026-11-09 07:00 WIB (`fuku/memory/playbooks/weekly_ads_health_report.md`). Include the pixel funnel row.
8. ✅ The WA follow-up script is drafted (`fab_advertising/creatives/2026-11-06_wa_followup_script.md`). It's waiting on 750 vs 800 + an OK from Alvian.
9. ✅ M-002 prior-week baseline (10/26–11/01) pulled → `fab_advertising/reports/weekly/_baseline_2026-10-26.md` (incl. Monday pull checklist). ✅ 13:02: 11/10 PEIKIRA2 read pre-staged → `fab_advertising/reports/2026-11-10_peikira2_read_prestage.md` (IDs, 5 pulls, table, decision rules set in advance). Mid-flight: control Rp 76.8k CPL (4 leads), PEIKIRA2 Rp 168k (1 lead).
10. ✅ 16:02: Mon 11/09 weekly report skeleton pre-filled → `fab_advertising/reports/weekly/2026-11-09.md` (per-campaign + PEIKIRA2 + 087 rows, funnel baseline, proposal-status table). ✅ 16:02 BC ad-set split: the BC drop = **087 Copy 7** losing delivery under its Rp 94,250 cap (spend −53% at flat CPM, leads 7→2); appended to the mix-shift doc. ✅ 17:02 Incess OMO fatigue pre-check done (healthy, no flags; watch ImageAd047 CTR −27%) → `fab_advertising/reports/2026-11-06_incess_omo_fatigue_precheck.md`. ✅ 18:02 Fab ad-level fatigue pre-check → `fab_advertising/reports/2026-11-06_fab_ad_fatigue_precheck.md`: no freq fatigue (max 1.60); **Ad015 = 86.7% of PEIKIRA spend** (single point of failure, CTR −16%); 087 CTR flat = cap starvation confirmed. Remaining heartbeats tonight (21:00, 22:00): activity-log check only; no more groundwork docs needed. Next groundwork idea: tracker daily row for 11/06 at tomorrow's 07:00 readout. ✅ 15:02 correction: the CPL rise is a **campaign-mix shift**, not account-wide upstream drift. PEIKIRA improved on everything (CPL 193k→113k); BC spend halved and leads fell 12→2 → `fab_advertising/reports/2026-11-06_cpl_mix_shift.md`. Weekly report must show CPM/cost-per-LPV **per campaign** + a BC ad-set split.

## Blockers / waiting on Alvian
- Pause PEIKIRA2 (single ask, 11/08); then M-001 items 1–5 (OUTBOX); website W1–W4, and who edits the site.
- Phone photo shoot; price 750 vs 800rb; close rate + months stayed. (The site says no minimum rental, no deposit, free pickup; confirm.)

## Needs a local session
- (none; the network is Full and fabwarehouses.com is reachable from the cloud)

## System
- Cloud Fuku is live: routine trig_01NGMFnv9BpvRp1jQjkAwUVJ, hourly 07–22 WIB. Propose-only: Fuku never calls Meta write tools, even when they're visible.
- Fab pixel/dataset id: **405755485775053** (PixelYourSite Pro on WordPress; browser + server events).

## Open loops
- Overnight 11/07 22:00 → 11/08 08:01 WIB: activity log `[]` (07:02 + 08:01 checks), no edits; PEIKIRA2 still live, pause ask open.
- 4 disabled ad accounts (OUTBOX [RISK]).
- Activity log 07:00–22:01 WIB 11/06: no human edits (only 2 Meta 'started delivery' events on PEIKIRA2 ads at 16:01/16:13); item 1 not applied yet.
- Overnight 11/06 22:00 → 11/07 09:02 WIB: only a Meta 'Account billed' event (06:30); no human edits, item 1 not applied (08:01 + 09:02 + 10:01 + 11:01 + 12:01 + 13:01 + 14:01 + 15:01 + 16:01 + 17:01 + 18:01 + 19:01 + 20:02 + 21:01 + 22:02 checks: `[]`).
- 16:01 site re-curl (4 pages): W1/W2/W3 not applied: Kelapa Gading still on all 4 pages, 'Jakarta Pusat' ×9 on /sewa-gudang-self-storage-jakarta/, 'Rp 800.000' still shown, 'Pernah chat' field still on the form.
- Incess OMO bid-cap raise proposal on offer.
