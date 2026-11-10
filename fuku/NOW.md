# NOW — Fuku's working memory
_Last updated: 2026-11-10 21:02 WIB (cloud heartbeat: shoot-day card)_
_Rules: rewrite, never append. Max 45 lines. History lives in the journal. See `protocols/heartbeat.md` (quiet-run rule)._

## Current focus
- **M-001 (P0):** 7d Fab (11/03–11/09) **CPL Rp 112.4k** *(calc)* ❌ vs 95k; spend Rp 337k/day *(calc)* vs 1M. 11/10 PEIKIRA2 read done: PEIKIRA2 Rp 869,690 / 5 (Rp 174k) vs control Rp 573,084 / 7 (Rp 82k) *(calc)*. After the 11/09 14:11 ad-006 pause, spend flowed back to the control. Pause-ad-set ask downgraded.
- **Scale plan done** (`fab_advertising/reports/scale_plan.md`): proven capacity ≈ Rp 590k/day at ≤ 95k (BC 290k + PEIKIRA 300k) *(calc)*; the last ~410k needs new creative. Gate (7d ≤ 95k) must open by **11/20** to hit 1M by 12/05. Bid cap max Rp 105k on 087 Copy 7.
- **Ad015 fallback done** (`fab_advertising/reports/2026-11-10_ad015_fallback.md`): Ad015 = 93% of control 7d spend *(calc)*, CPL 88.2k; the rest of the ad set does Rp 182k/lead over 30d *(calc)*, so there's no proven backup. Early CTR slide 1.82% → 1.55% *(calc)*. Triggers: 7d CTR < 1.30%, CPL > 120k, or freq > 2.5.
- **Competitor angles done** (`fab_advertising/research/2026-11-10_competitor_angles.md`): only SpaceHub + Gudangku advertise; SpaceHub Thamrin "from Rp 400k" but deposit + self-move. Lead batch 02 with pickup / no deposit, price second.
- **WA price-objection reply done** (in `fab_advertising/creatives/2026-11-06_wa_followup_script.md`): lead with pickup / no deposit / no minimum, then a sizing question; no discount, no cost-parity claim. Same gates as batch 02.
- **Price-copy audit done** (`fab_advertising/reports/2026-11-10_price_copy_audit.md`): all 59 live BC ads say "dari 800rb" (9.8% of 7d spend), all 11 PEIKIRA ads say 750rb (80.6%) *(calc)*. If 750 is real → no ad change, site W2 only; if 800 → PEIKIRA copy is the problem.
- **Shoot-day card done** (`fab_advertising/creatives/2026-11-10_shoot_day_card.md`): 6 home photos → 8 ads (batch 01 + 02). Wave 1 = S1, B1, B2 from just 2 photos; price-only fallback = S1, S6, S2. Gates per ad.
- **Incess bid-cap proposal done** (`fab_advertising/reports/2026-11-10_incess_bidcap_proposal.md`): caps binding, spend −30% at unchanged caps, CPL flat 35k. Raise 4 cheapest ad sets → Rp 51k/50k; parked until lead value known.
- **M-002 (P1):** next weekly report Mon 11/16 07:00 (`playbooks/weekly_ads_health_report.md`; include the pixel funnel row, CPM/cost-per-LPV per campaign, and a BC ad-set split).

## Next actions (dated or triggered)
1. **11/11 07:00 readout:** tracker row + activity log. PEIKIRA2 share of PEIKIRA spend on 11/10 full day: if ≥ 30% with ≤ 1 lead → one-line re-ask "pause ad set PEIKIRA2"; else drop the ask. Check which old "Rp800.000" Fab ads still deliver (Ad Library lists ≥ 8 ACTIVE); if any spend, add to W2. Check **Ad015** against the fallback triggers (7d CTR < 1.30% / CPL > 120k / freq > 2.5); if one fires → the contingency list becomes the single ad ask.
2. **After 11/11 settles:** re-raise item 1 (remove Instagram Stories from the PEIKIRA ad set) as the single ad ask, with fresh numbers.
3. **Every run:** check INBOX/OUTBOX for "W1 W2 done", photos, 750 vs 800, "applied N". Log applied changes in `fab_advertising/reports/m001_tracker.md`.
4. **When W1/W2 are applied:** re-curl the 3 Jakarta pages, re-pull the funnel, compare to `fab_advertising/reports/2026-11-06_pixel_funnel_baseline.md` (VC→Lead 3.8%, VC→Form 6.4%, Form→Lead 60%).
5. **Retro #2:** ~11/13 or at 15 new lessons.
6. **Each daily readout:** check the 11/20 gate date from the scale plan; on 11/20, if 7d CPL > 95k, tell Alvian criterion 2 is out of reach by 12/05.

## Groundwork backlog (for quiet runs; needs nothing from Alvian)
_Seeded 2026-11-10 by the local session. Take the top one, finish it as an artifact, delete it here._
1. **M-002 prep:** pre-fill the 11/16 weekly report skeleton (sections + queries; add the Incess 4-ad-set baseline 12.9 leads/day @ Rp 28.4k) so Monday's run is one pull.
2. **Incess ad-set 019 (Rp 53k CPL, 22% of spend):** ad-level split to see which of its 15 ads drag it, for the 11/16 weekly.
3. **Wave 1 read template:** pre-write the 5–7 day per-ad read for S1/B1/B2 (queries, keep/pause rules, wave-2 mapping) so launch day needs no prep.

## Waiting on Alvian (asks live in OUTBOX "Needs you")
- Website W1 + W2, and who edits the site.
- Phone photos; price 750 vs 800rb. Later: close rate + months stayed; confirm no minimum rental / no deposit / free pickup.

## Standing facts
- Read `playbooks/meta-ads-algorithm.md` + `meta-cpl-diagnosis.md` before any ads work.
- Cloud Fuku: routine trig_01NGMFnv9BpvRp1jQjkAwUVJ, hourly 07–22 WIB. Propose-only: never call Meta write tools, even when visible.
- Fab pixel/dataset id **405755485775053** (PixelYourSite Pro on WordPress; browser + server events).
- Markus (team) edits the Fab account via the Rudi MCP app (actor 61594758338050).
- ImageAd 201B "Update Required" is immaterial (Rp 0 spend over 14d).

## Open loops (current state, one line each)
- Activity log: no human edits since the 11/09 14:11 ad-006 pause (last check 11/10 19:02). PEIKIRA2 ad set still ACTIVE.
- Site: W1/W2/W3 not applied (last curl 11/09 07:02).
- Parked in OUTBOX: M-001 items 1–5, W3/W4 + WA follow-up script, 4 disabled ad accounts, lead-value questions.
- Incess has unpublished Ads Manager drafts ("FIX OMO CostCap Increm", Rp 5M/day draft); nothing delivers from them.
