# Missions

> **Alvian:** add missions here (or run `/mission <goal>` in Claude Code). Give each one a goal, success criteria, priority, and deadline if any.
> **Fuku** owns the strategy, keeps the Status/Progress lines current, and moves finished missions to "Completed".

## Active

<!-- Template:
### M-001 · <Mission name>
- **Goal:** what outcome you want
- **Success criteria:** how we know it's done (measurable)
- **Priority:** P0 (now) / P1 (this week) / P2 (whenever)
- **Deadline:** YYYY-MM-DD or none
- **Constraints:** budget, brand, no-gos
- **Status:** not started | in progress | blocked | done   ← Fuku
- **Strategy:** ← Fuku's current approach
- **Progress:** ← Fuku's latest update (dated)
-->

### M-001 · Fab ad account: cut CPL and scale to Rp 1M/day
- **Goal:** Make the Fab ad account (Meta "Warehouse Storage" `484578521394893`, The North Case Indonesia) profitable at scale: cheaper leads, then more spend.
- **Success criteria (both must hold):**
  1. 7-day average CPL ≤ **Rp 95,000** (baseline 2026-11-05: ~Rp 133k blended, last 30d).
  2. The account sustainably spends **Rp 1,000,000/day** with a 7-day average CPL of around Rp 95k (baseline: ~Rp 411k/day).
- **Priority:** P0
- **Deadline:** 2026-12-05 (30 days from 2026-11-05)
- **Constraints:** **Propose-only.** Fuku never touches the ad account (no pauses, budget changes, or launches). Every change is proposed to Alvian as an apply-ready checklist, and **Alvian applies it himself**. The metric is the 7-day average CPL, never a single day.
- **Status:** in progress (diagnosis ✅, waiting on Alvian to apply proposals; PEIKIRA2 mostly throttled via the 11/09 ad-006 pause; residual check 11/11)
- **Strategy (Fuku, 2026-11-05):**
  1. *Diagnose* (now): ad-set/ad/placement/audience breakdown; find which ads, audiences, and placements produce leads ≤ Rp 95k.
  2. *Cut waste*: propose to Alvian which CTR-collapsed FAB ads and losing ad sets to pause, so spend concentrates in the winners (BC CBObass005-type setups at ~Rp 83k).
  3. *Fix fatigue*: fresh creative batch (new angles/hooks) and a fresh or broader audience for the frequency-8 winner.
  4. *Scale*: propose budget raises of ~20–30% every 3–4 days, only while the 7d CPL ≤ Rp 95k. Alvian applies them. Fuku verifies the effect in the next readouts. Path: ~Rp 411k → 500k → 650k → 800k → 1M/day (≈ 10–11 leads/day at Rp 95k).
  5. Track daily in `fab_advertising/reports/m001_tracker.md` (spend, leads, 7d CPL).
- **Progress:**
  - 2026-11-10 18:02: Groundwork: WA price-objection reply ("kok lebih mahal dari 400rb?") added to `fab_advertising/creatives/2026-11-06_wa_followup_script.md`: answer with free pickup / no deposit / no minimum + a sizing question, no discount, no cost-parity claim. Draft, gated on the same facts as batch 02. No new ask.
  - 2026-11-10 17:02: Groundwork: creative batch 02 copy → `fab_advertising/creatives/2026-11-10_creative_batch_02.md`. 5 phone-photo ads on objections (B1 free pickup, B2 no deposit + pickup, B3 monthly/no deposit, B4 "titip sebulan", B5 rapi 1 hari), stickers + copy + gates G1–G5 (pickup/deposit/minimum/price/site). Same shoot as batch 01; top-3 pick B1, B2, A1. No new ask.
  - 2026-11-10 19:02: Activity log 13:00–19:02 empty. Price-copy audit → `fab_advertising/reports/2026-11-10_price_copy_audit.md`: 83 delivering ads; 750rb copy = 11 PEIKIRA ads, Rp 1,902,877 (80.6%); 800rb copy = all 59 BC ads, Rp 230,262 (9.8%) *(calc)*. No ad change proposed while 750 is assumed; the 750/800 answer decides it. No new ask.
  - 2026-11-10 16:02: Groundwork: competitor angles → `fab_advertising/research/2026-11-10_competitor_angles.md`. Only 2 storage rivals advertise on Meta (SpaceHub, Gudangku); SpaceHub (Thamrin) headlines **from Rp 400k/month** but needs a deposit + self-move. Fab angle = free pickup / no deposit / home clutter, price second. ≥ 8 old "Rp800.000" Fab ads listed ACTIVE in the Ad Library. No new ask.
  - 2026-11-10 15:02: Groundwork: Ad015 fallback → `fab_advertising/reports/2026-11-10_ad015_fallback.md`. Ad015 7d Rp 1,058,606 / 12 / CPL Rp 88,217 = 93% of control spend *(calc)*; all other control ads 30d Rp 1,273,316 / 7 = Rp 181,902 *(calc)* → no proven backup. CTR 1.82% → 1.55% *(calc)*, freq 1.40. Triggers + 3-step contingency written; no new ask.
  - 2026-11-10 14:04: Groundwork: scale plan → `fab_advertising/reports/scale_plan.md`. Proven capacity at ≤ 95k ≈ **Rp 590k/day** *(calc)* (BC 09/14–10/11 Rp 288k/day @ 89.7k; PEIKIRA 300k). 10/12–10/18 the account ran Rp 919k/day at CPL Rp 201k *(calc)*, so 1M is creative-bound. Gate must open by **11/20** for 5 × +25% steps by 12/05. 087 Copy 7 cap: CPL/cap 0.889 → Rp 105k cap ≈ 93.4k CPL *(calc)*; 110k would overshoot.
  - 2026-11-10 07:02: ✅ PEIKIRA2 read (11/05–11/09): PEIKIRA2 Rp 869,690 / 5 (Rp 173,938) vs control Rp 573,084 / 7 (Rp 81,869) *(calc)* → test lost. The 11/09 ad-006 pause moved spend back to the control (67% of PEIKIRA on 11/10 so far), so the ad-set pause ask is downgraded; re-check 11/11. 7d (11/03–11/09) Rp 2,359,757 / 21 / **CPL Rp 112,369** *(calc)* ❌. New risk: control relies on Ad015.
  - 2026-11-09 15:02: Activity log: ad **AKIRA-FAB-20261031-006** (83% of PEIKIRA2 spend) was PAUSED at 14:11 WIB via the Rudi MCP app (presumed Markus, not Fuku). The **ad set PEIKIRA2 is still ACTIVE** (today Rp 107,014 / 0 leads). Logged in the tracker, FYI in OUTBOX + push. Read where the spend shifts on 11/10 07:00.
  - 2026-11-09 07:02: Daily + weekly readout: 7d (11/02–11/08) Rp 2,406,326 / 23 leads / **CPL Rp 104,623** *(calc)* ❌ (best yet; 115.1k yesterday, −22% WoW). PEIKIRA2 cum. Rp 739,973 / 4 (Rp 185k) vs control Rp 450,290 / 6 (Rp 75k). 11/08 was PEIKIRA2's best day (2 leads), but the split still costs the campaign ~119k vs 75k → pause ask re-sent (24h open) + push. Site still unedited (curl). No human edits.
  - 2026-11-08 07:02: Daily readout: 7d (11/01–11/07) Rp 2,531,551 / 22 leads / **CPL Rp 115,070** *(calc)* ❌ (121.9k yesterday). 11/07 Rp 278,661 / 2. PEIKIRA2 cumulative Rp 539,027 / 2 (Rp 269.5k) vs control Rp 350,414 / 5 (Rp 70.1k); 11/07 PEIKIRA2 took 87.6% *(calc)* of PEIKIRA spend for 0 leads → pre-set re-trigger fired. Single ask switched to "pause PEIKIRA2" (item 1 parked). No human edits overnight.
  - 2026-11-07 09:02: Activity log 07:55–09:02 empty; item 1 unapplied at 48h. Re-asked as a single one-line [DECISION] at OUTBOX top + push notification. No new packs.
  - 2026-11-07 07:02: Daily readout: 7d (10/31–11/06) Rp 2,560,776 / 21 leads / **CPL Rp 121,942** *(calc)* ❌ (125.2k yesterday). 11/06 full day Rp 413k / 5 leads. PEIKIRA2 got a 2nd lead overnight (Rp 336,659 / 2) → pause rule no longer applies; hold to 11/10, no ask. No human edits overnight; item 1 still unapplied.
  - 2026-11-06 20:02: Activity log empty (item 1 not applied). PEIKIRA2 cumulative Rp 292,582 / 1 lead → Rp 285k pause threshold tripped; control Rp 314,808 / 4. Ask scheduled for 11/07 07:00 readout.
  - 2026-11-06 19:01: Activity log 18:00–19:01 empty (item 1 not applied). Intraday: PEIKIRA2 took 77.7% *(calc)* of PEIKIRA spend today (Rp 239k / 1 lead) vs control Rp 69k / 2. Cumulative PEIKIRA2 Rp 279,085 / 1 lead, at 97.9% of the pre-set Rp 285k pause threshold. OUTBOX [RISK]; becomes the single ask at 11/07 07:00 if still ≤1 lead at ≥ Rp 400k.
  - 2026-11-06 18:02: Activity log 16:13–18:02 empty (item 1 not applied). Ad-level check: PEIKIRA depends on one ad (Ad015: Rp 1.66M / 16 leads / Rp 103,865 in W2 = 86.7% of PEIKIRA ad spend *(calc)*); BC Image087 CTR flat 1.51% at freq 1.22, so its drop is the bid cap, not fatigue. No new ask.
  - 2026-11-06 16:02: Activity log 15:00–16:02 empty. BC ad-set split: the BC drop is **one ad set**, BC batch087 Copy 7 (55–59% of BC spend): spend 555k → 261k (−53%, calc) at flat CPM 13.7k → 14.2k, leads 7 → 2. Lost auctions under the Rp 94,250 cap → item 4 on 087 is the single BC lever. Mon 11/09 weekly report skeleton pre-filled (`fab_advertising/reports/weekly/2026-11-09.md`). No new ask.
  - 2026-11-06 15:02: Activity log 14:00–15:02 empty. **Correction to 14:02:** the CPL rise (112k → 125k, wk 10/23 vs 10/30) is a campaign-mix shift. PEIKIRA improved (CPM 53.8k → 37.9k, CPL 193k → 113k *(calc)*); BC CBO Copy spend halved (937k → 477k) and leads fell 12 → 2 at a stable CPM. BC starvation is the CPL gap, which backs items 3+4. → `fab_advertising/reports/2026-11-06_cpl_mix_shift.md`. No new ask.
  - 2026-11-06 13:02: Activity log 12:00–13:02 empty. Pre-staged the 11/10 PEIKIRA2 read (`fab_advertising/reports/2026-11-10_peikira2_read_prestage.md`) with decision rules fixed in advance. Mid-flight 11/05–11/06: control ad set Rp 307k / 4 leads (Rp 76.8k), PEIKIRA2 Rp 168k / 1 lead, campaign ≈ Rp 95.1k *(calc)*. Too early to judge; no new ask.
  - 2026-11-06 14:02: Activity log 13:00–14:02 empty. Pixel funnel baseline before W1/W2 (`fab_advertising/reports/2026-11-06_pixel_funnel_baseline.md`): VC→Lead 3.0% (wk 10/23) → 3.8% (wk 10/30) *(calc)*, so this week's CPL drift is upstream (traffic cost), not the site. Form→Lead fell 69% → 60% (supports W4). Site still unedited (W1 not applied).
  - 2026-11-06 12:01: Activity log 11:01–12:01 empty (nothing applied). Groundwork: batch 01 v2 shot list in the Image087 pattern (6 home-clutter phone shots + exact sticker text, only S4 needs the site) → `fab_advertising/creatives/2026-11-06_batch01_v2_home_clutter_shotlist.md`. No new ask.
  - 2026-11-06 11:01: Activity log 10:02–11:01 empty. Viewed BC Image087 (#1 ad, 30d Rp 1.36M / 15 leads ≈ Rp 90.8k *(calc)*, Meta trend CPR −53% improving) at full size: home-clutter phone photo + story stickers, no warehouse. So the creative shoot doesn't need the warehouse; ask shrunk in OUTBOX (no new decision).
  - 2026-11-06 09:01: No account changes since 07:00 WIB (activity log empty). Retro #1 scored M-001 **at risk**: 7d CPL 125k vs 95k, and the bottleneck is applying changes, not analysis. Strategy tweak: no new decision packs; re-asked only item 1 (PEIKIRA: remove IG Stories, calc 30d CPL ≈ 94.9k).
  - 2026-11-06 07:01: Daily readout: 7d (10/30–11/05) Rp 2.50M / 20 leads / **CPL Rp 125k** ❌ (up from 113k); no proposals applied, no human edits overnight. Landing page + lead-flow audit (E4) done → `fab_advertising/reports/2026-11-06_landing_page_audit.md`: LP→Lead 3.9%, location contradictions (Kelapa Gading text on Jakarta Selatan pages), Rp800k on the form page vs 750 in ads, 40% Form→no-Lead gap. [DECISION] W1–W4 in OUTBOX.
  - 2026-11-06 08:02: ImageAd 201B check: still WITH_ISSUES, but Rp 0 spend over 14d → immaterial. BCbatch201 Manny5 spent Rp 18.2k / 0 leads in 7d (bid cap starving it). Its industry benchmark CPR is 14% better than peers (30d). Groundwork: WA follow-up script for Form-but-no-Lead contacts → `fab_advertising/creatives/2026-11-06_wa_followup_script.md` (draft, not sent).
  - 2026-11-05 (local session, ~19:00–23:00): Creative review of 13 ads → raw phone photos Rp 18–68k CPL vs AI-look renders Rp 200–372k (`fab_advertising/creatives/2026-11-05_creative_brief.md`). Funnel/attribution hypothesis tested: no remarketing layer; bid caps confirmed Rp 80k/94.25k (`2026-11-05_funnel_hypothesis.md`). Meta algorithm playbook built (`fuku/memory/playbooks/meta-ads-algorithm.md`).
  - 2026-11-05 22:01: No new outside edits. Today (partial): Rp 327k, 2 leads (PEIKIRA 2 @ Rp 136k; BC CBO 0). Daily snapshot section added to tracker. Proposals still unapplied.
  - 2026-11-05 21:03: Activity log shows a third-party launch at 14:40 WIB via the "Rudi MCP" app: new ad set AKIRA-FAB-20261031-WAVE-PEIKIRA2 (23 ads, 8 live) inside PEIKIRA, budget unchanged at Rp 300k. Logged in tracker; [RISK] in OUTBOX. Batch 01 on hold until the 11/10 read so two creative tests don't overlap. ImageAd 201B (winner ad set) flagged "Update Required" by Meta. Landing page audit blocked (cloud network).
  - 2026-11-05 20:02: Creative batch 01 drafted → `fab_advertising/creatives/2026-11-05_creative_batch_01.md` (6 ads, Indonesian copy). Basis: 14d ad-level data + Meta trend (6 PEIKIRA FAB ads CTR −40…−99%; Ad015 carries volume, 14 leads @ Rp 104.5k). [DECISION] in OUTBOX: launch A1/A2/A4 in the PEIKIRA ad set; 3 facts needed from Alvian.
  - 2026-11-05 19:09: Diagnosis done → `fab_advertising/reports/2026-11-05_m001_diagnosis.md`. 7d (10/29–11/04): Rp 355k/day, 22 leads, **CPL Rp 113k** (gate ≤95k closed). PEIKIRA (highest volume, Rp 300k/day) = volume @Rp 105k. BC CBO bid-cap = cheapest (Rp 60k CPL 10/19–28) but stalled to ~Rp 70k/day. 3 proposals sent to OUTBOX (consolidate BC ad sets, raise bid cap on 2 winners to Rp 105k, hold PEIKIRA). Tracker started: `m001_tracker.md`.
  - 2026-11-05 18:51 (local session): Placement breakdown done (`fab_advertising/reports/2026-11-05_m001_breakdown.md`). 7d CPL Rp 112.9k at ~Rp 355k/day. The main waste is placements (PEIKIRA IG Stories Rp 332k CPL; BC WA Status + Threads). Proposed 5 changes; top 3 are in OUTBOX. Tracker started.
  - 2026-11-05: Rule: propose-only, Alvian executes all ad changes.
  - 2026-11-05: Mission set by Alvian. Baseline scan done (`fab_advertising/reports/2026-11-05_meta_account_scan.md`).

### M-002 · Weekly ads health report
- **Goal:** Every Monday, a concise health report across all Meta ad accounts so Alvian sees spend, CPL, fatigue, and problems at a glance.
- **Success criteria:** A report in `fab_advertising/reports/weekly/YYYY-MM-DD.md` every Monday by 09:00 WIB (spend, leads, CPL, 7d trend, fatigue flags, disabled/limited accounts, top 3 recommended actions), plus a one-line summary in OUTBOX.
- **Priority:** P1
- **Deadline:** ongoing; first report Monday 2026-11-09
- **Constraints:** read-only. Recommendations go to OUTBOX.
- **Status:** in progress
- **Strategy:** The cloud heartbeat runs it on the first Monday run (07:00 WIB). Turn it into a playbook after the first report.
- **Progress:**
  - 2026-11-09 07:02: ✅ First weekly report delivered → `fab_advertising/reports/weekly/2026-11-09.md` (Fab 104.6k CPL −22% WoW; Incess 35.2k −3.7%; no fatigue; no new disabled accounts; Incess unpublished drafts noted as FYI). [REPORT] in OUTBOX. Next: Mon 11/16 07:00.
  - 2026-11-06 18:02: Fab ad-level fatigue pre-check → `fab_advertising/reports/2026-11-06_fab_ad_fatigue_precheck.md`. Max freq 1.60, no frequency fatigue; CTR flags Ad001 (−57%), KENJI-001 (−52%), Ad007 (−30%); ⚠️ Ad015 carries 86.7% *(calc)* of PEIKIRA W2 spend. Row added to the 11/09 skeleton.
  - 2026-11-06 17:02: Incess OMO ad-level fatigue pre-check → `fab_advertising/reports/2026-11-06_incess_omo_fatigue_precheck.md`. Healthy: CPL 35.5k → 36.3k *(calc)*, max freq 1.78, no flags; watch ImageAd047 (CTR −27%).
  - 2026-11-06 10:02: Prior-week baseline (10/26–11/01) pulled → `fab_advertising/reports/weekly/_baseline_2026-10-26.md`. Fab Rp 2.56M / 19 leads / CPL Rp 134.6k *(calc)*; Incess Rp 4.42M / 121 / Rp 36.5k. Monday only needs the current week + fatigue + logs.
  - 2026-11-05 22:01: Playbook + template ready → `fuku/memory/playbooks/weekly_ads_health_report.md`; folder `fab_advertising/reports/weekly/` created.
  - 2026-11-05: Approved by Alvian.

## Completed
