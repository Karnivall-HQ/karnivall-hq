# Read card: PEIKIRA-FAB-20261109-ADSET-3 (team launch, 11/13)
_Written 2026-11-13 07:02 WIB by Fuku, before the ad set has spent (playbook `meta-tests-and-proposals.md` §A). Propose-only: Fuku reads, Alvian/Markus apply._

## What launched (activity log, account data)
- **Ad set** `120254400251570572` "PEIKIRA-FAB-20261109-ADSET-3" in **PEIKIRA-BID-CAP-LEADS-CAMPAIGN** `120254051672440572` (CBO Rp 300,000/day, campaign bid strategy shows "Highest volume"). Created 11/13 00:04 WIB, **ACTIVE 04:05 WIB**; Rp 0 spent at 07:02.
- Built by actor **"TourHub Shared Office for Tour Travel Business" (61557670947597, Power Editor)**: new actor in this account. Markus Reynaldo (1684366339) renamed the ad set and added ad 016. ❓ Who is the TourHub actor? (FYI, not blocking.)
- Settings: optimise Lead on pixel 405755485775053; Jakarta city, 18–65+, **Advantage+ audience on** (`expansion_all`), Instagram only (Feed, Stories, Reels, profile feed, search).
- **6 ads**, all ACTIVE after 1–3 creative swaps each overnight: FAB-20261109-003 / 007 / 010 v03 / 018 / S30 v04 (creative name "Sewa Unit Self-storage Bersih & Terang di Jakarta, di Fab") + AKIRA-FAB-20261103-016 ("…mulai Rp750rb/bulan"). 15 images added to the library → likely new photos (INFERRED).
- Sample copy (S30 v04, account data): "Dari Rp750rb/bulan + gratis pickup 1x hingga Rp150.000 · 📍 Jakarta Selatan (Kuningan and Sudirman)", CTA SEE_DETAILS.
- Advantage+ enhancements ON in all 6 creatives: `cv_transformation`, `image_animation`, `image_touchups` (016 also `audio`, `video_filtering`, `media_liquidity_animated_image`).

## Message-match vs the landing page (curl 11/13 07:02, visible text)
| Claim in new ads | `/sewa-gudang-self-storage-jakarta/` | Risk |
|---|---|---|
| Rp750rb/bulan | "750" ×24, "Rp 800.000" ×1 (FAQ) | low; W2 removes the last 800 |
| Jakarta Selatan (Kuningan, Sudirman) | "Jakarta Pusat" ×9, "Jakarta Selatan" ×2, Sudirman ×9 | **high**: the new ads now say Selatan while the page mostly says Pusat → W1 |
| "Kuningan and Sudirman" (reads as 2 sites) | page names one site (ITC Kuningan Ambasador, Sudirman); Kuningan ×1 | medium: same issue our Wave 2 rows avoid (one-site line) |
| gratis pickup 1x hingga Rp150.000 | "Gratis: Pickup barang" ×7, "150.000" ×0 | low: ad is narrower than the page (page has no cap) |

→ The team's copy already follows the W1/W2 direction; the page is now the only place the old facts remain. That makes W1/W2 more valuable, not less.

## Read rules (fixed now; apply as written)
Target CPL 95k. Projection: CBO Rp 300k/day over 3 ad sets → ~Rp 70–130k/day to ADSET-3 if it gets a fair share *(calc)*; PEIKIRA2 took 78% on its day 2 (11/06), so it could take far more.
1. **Share watch (daily, from 11/14 07:00):** if ADSET-3 > 70% of PEIKIRA spend on a full day with 0 leads → flag in the readout (no ask yet; ad sets often front-load).
2. **Early kill:** cumulative spend ≥ Rp 190k (2×) with 0 leads, or ≥ Rp 285k (3×) with ≤ 1 lead → propose pausing ADSET-3 (budget flows back to control + PEIKIRA2).
3. **Comparative (day 7, 11/20 readout, full days 11/13–11/19):** ADSET-3 CPL vs the control ad set's CPL in the same window. ADSET-3 ≤ control → KEEP; > 1.3× control with ≥ Rp 400k spent → propose pause.
4. **Verdict on day 14 (11/27)**, 2-week block, per playbook: winner only if ≤ 95k on ≥ 4 leads. Fill-in: `2026-11-27_adset3_verdict_template.md`.
5. Per-ad: judge the pooled ad set first; per-ad reads only for ads with ≥ Rp 95k spend.
6. Starvation check: any of the 6 ads < Rp 5k in 7d = untested, not a loser.

## Optional (not an ask yet)
- Enhancements: `cv_transformation` / `image_touchups` change the raw-photo look this test is about (INFERRED). Turning them off means editing live ads (re-review). Revisit only if day-7 CTR < control's.

## Effect on the 11/20 gate
- 7d CPL 11/06–11/12 = Rp 103,286 *(calc)*. With W1+W2 (same lift ratio 1.129 as the gate brief) ≈ **91.5k** *(calc)* → opens the gate. Without a site fix, ADSET-3 alone opens the gate at ≤ Rp 83.5k CPL on a 1/3 share, or ≤ 95.7k on a 60% share *(calc, 11/13 09:01 gate refresh in `2026-11-20_gate_brief.md`)*.

## Day-1 share check (for the 11/14 07:00 readout; added 11/13 10:01)
Pull level=adset, campaign `120254051672440572`, time_range 11/13→11/13 (and 11/13→yesterday from 11/15 on).
- **Share** s = ADSET-3 spend ÷ PEIKIRA campaign spend, same day(s) *(calc)*.
- **Break-even CPL** (opens the 11/20 gate with no site fix; base 11/06–11/12, PEIKIRA Rp 299,363/day + 2.571 leads/day, gate needs +2.006 leads over the 23 already in base) *(calc)*:
  `BE(s, d) = s·d·299,363 ÷ (2.006 + s·d·2.571)`, d = days ADSET-3 delivers inside 11/13–11/19.

| share s | d = 6 (from 11/14) | d = 5 (from 11/15) | d = 4 (from 11/16) |
|---|---|---|---|
| 20% | 70.6k | 65.4k | 58.9k |
| 25% | 76.6k | 71.7k | 65.4k |
| 33% | 83.8k | 79.3k | 73.4k |
| 40% | 87.9k | 83.8k | 78.3k |
| 50% | 92.4k | 88.7k | 83.8k |
| 60% | 95.7k | 92.4k | 87.9k |
| 70% | 98.2k | 95.2k | 91.1k |
| 80% | 100.1k | 97.4k | 93.6k |
- Readout line template: "ADSET-3 day N: Rp ⟨spend⟩ = ⟨s⟩% of PEIKIRA, ⟨leads⟩ leads; break-even at that share = ⟨BE⟩ *(calc)*; rule 1 (>70% & 0 leads) ⟨ok/flag⟩; rule 2 (≥ Rp 190k & 0 leads) ⟨ok/flag⟩."
- Late start costs margin: every day ADSET-3 stays at 0 impressions lowers the bar by ~4–6k at a 1/3 share. Low share (< 25%) means ADSET-3 can't open the gate alone, whatever its CPL: W1+W2 then carries it.

## Delivery check 11/13 13:02 WIB (rule: still 0 impressions at 13:00 → check and flag)
- **ADSET-3 today: Rp 0 / 0 impressions, ~9h after ACTIVE (04:05).** Ad set delivery = active / `in_learning_phase` (0 conversions). 5 ads active / learning, ad FAB-20261109-007 `pending / preparing`. `ads_get_errors` on the ad set + 6 ads: **none**. All ads `ACTIVE` (= past review).
- Same campaign today: control Rp 101,228 / 2,102 impr; PEIKIRA2 Rp 76,028 / 1,448 impr → CBO has spent Rp 177,256 *(calc)* and given ADSET-3 nothing.
- Settings are not the blocker: same pixel/LEAD goal, same Jakarta city geo, Advantage+ audience, IG-only placements (a superset of the control's). No end time, no spend cap visible.
- **Diagnosis (INFERRED):** CBO starvation. Meta allocates to the two ad sets with conversion history (29 and 10) and has not yet tested the new one. Not an error, not a rejection.
- **Cost of waiting:** every 0-impression day lowers ADSET-3's 1/3-share break-even ~4–6k (table above). From 11/15 the bar is 79.3k, from 11/16 73.4k *(calc)*.
- **Conditional proposal (for Alvian/Markus to apply; Fuku does not touch the account):** if ADSET-3 is still at 0 impressions at the **19:00 poll**, set an ad-set **minimum daily spend of Rp 75,000** on PEIKIRA-FAB-20261109-ADSET-3 (Ads Manager → ad set → Budget & schedule → Ad set spend limits → Daily minimum), CBO total unchanged at Rp 300k. Remove the minimum at the 11/20 read or when rule 2 fires (≥ Rp 190k, 0 leads). Why 75k: 25% of the CBO, enough for ~1 expected lead every 1.3 days at 95k *(calc)*, without starving Ad015.
- **19:02 poll: trigger fired.** ADSET-3 still Rp 0 / 0 impressions (~15h live), delivery active / in_learning_phase, no `daily_min_spend_target` set. Same day: control Rp 149,615 / 3,793 impr (delivery warning: learning_exit_unsuccessfully), PEIKIRA2 Rp 113,540 / 2,433 impr → CBO Rp 263,155 *(calc)*. Activity log since 12:00: no human edits. → min-spend Rp 75k moved to OUTBOX "Needs you" #3. Delivery days d = 0 so far: if applied tonight, d starts 11/14 (break-even 83.8k at 1/3 share).

## Day-1 share check 11/14 07:02 WIB
- ADSET-3 day 1 (11/13 full day): **Rp 0 = 0% of PEIKIRA (Rp 293,851)**, 0 leads, 0 impr; still Rp 0 / 0 impr today at 07:0x; delivery active / in_learning_phase; no daily min spend set; activity log 11/13 19:00 → 11/14 07:02 empty. d = 0 → break-even from the table: 79.3k if it starts 11/15, 73.4k from 11/16 at 1/3 share *(calc)*. Rule 1 ok (no spend), rule 2 ok (no spend).
- New fact (tracker 11/14): Ad015 fallback trigger fired (7d CPL 166.1k *(calc)*). Pausing Ad015 removes ~91% of the control ad set's spend, which also gives the CBO room to test ADSET-3 → folded into one combined OUTBOX ask #1 with the min spend.

## 11/15 14:01 · Starvation cause check (day 3, under the Rp 105k cap)
- `ads_get_errors` on ADSET-3: **none**. All 6 ads ACTIVE, delivery `active / ad_set_in_learning_phase`, **lifetime impressions 0, Rp 0** (account data).
- Ad-set settings (account data): bid cap Rp 105,000 (same as control + PEIKIRA2), no `daily_min_spend_target`, optimization OFFSITE_CONVERSIONS (Lead), learning 0 conv since the 11/15 00:42 edit.
- **Targeting = PEIKIRA2's** (account data): Jakarta city, 18–65, Instagram only, Advantage+ audience on. Only difference: ADSET-3 adds IG profile feed + IG search.
- **Diagnosis (INFERRED):** two brakes stacked. (1) **Auction overlap:** same audience as PEIKIRA2, so in each auction Meta enters only one of the advertiser's ad sets, the one with the higher estimated value; ADSET-3 has 0 conversion history, so it loses that internal pick every time. (2) **Bid cap:** with no history its estimated action rate is low, so even when entered it rarely clears Rp 105k. CBO allocation (11/13 diagnosis) is the third layer. Benchmarks: no data. Trend tool: no rows for ADSET-3 (no delivery).
- **What fixes it (for the existing ask, no new one):** OUTBOX #2(b) daily minimum Rp 75k forces delivery past all three layers. Pausing Ad015 alone (#2a) frees budget but does **not** fix the overlap or the cap, so ADSET-3 may stay at 0 even if #2a is applied without #2b (INFERRED). Untested alternative if #2b is refused: duplicate ADSET-3 into its own campaign without a bid cap (proposal only, not raised).
- Cost so far: 3 days, d = 0 → 1/3-share break-even now 73.4k from 11/16 *(calc, table above)*: ADSET-3 can no longer open the 11/20 gate alone.

## 11/15 16:02 · Per-look read rules (added before ADSET-3 has spent; source `creatives/2026-11-15_adset3_vs_shoot_card.md`)
ADSET-3 mixes looks, and our account history splits sharply by look (raw phone photos Rp 18–68k vs polished/render Rp 200–372k CPL, 11/05 review, account data). A pooled ad-set CPL would hide which look won. So the day-7 and day-14 reads add one layer between rule 3/4 (ad set) and rule 5 (per ad):

| Look | Ads (mapping: account data, mapped 11/15 17:02) | Question it answers |
|---|---|---|
| L1a home photo + story stickers | **AKIRA-016** (2 images: 9:16 + 4:5, uploaded ~11/01): suitcases + boxes + fan in a tiled corner, stickers "Di Rumah butuh kamar kosong?" / "Kosongkan Kamar dengan simpan barang di…" / "Gudang Self-storage di Fab" (viewed) | does the BC Image087 formula (account's best look) work in PEIKIRA? |
| L1b home photo, big text overlay | S30 v04 (1 image, viewed) | home clutter without stickers |
| L2 real facility | 018 (v01 + v02 + 4:5, viewed) | does "real unit" proof work? |
| L3 designed graphic | 003 (size chart, 3 images), 007 (WA chat mock-up, 3 images) | graphics vs photos |
| L4 render-look | **010** (v03 + v04 + 4:5 v02): hand + key + brass padlock on white louvered/roll-up doors, glossy corridor (viewed; v03 = the a0a5 description re-uploaded as 6cc5…) | expected loser per history |

Mapping facts (account data, `ads_get_creatives` + `ads_get_ad_images`, 11/15 17:02): every ADSET-3 ad is a placement-customized asset feed of one look in 2–3 crops, so **per ad = per look** (no ad mixes looks). The no-text C1 photo (1110…) and the a0a5 file are **not used by any ADSET-3 ad**. All 6 ads: Rp 0 spend, 0 impressions lifetime. **016 history (account data, 11/15 18:01, `ads_get_ad_entities` name-search "016" lifetime + `ads_get_creatives`):** the same 2 image hashes (749b0f… + 708088…) and the same copy ran once before, as AKIRA-FAB-20261103-016 in **PEIKIRA2** (ad 120254276339950572, creative 1893364448770508): created 11/05 14:45, PAUSED 14:47, **Rp 0 / 0 impressions lifetime**. So this image has **no prior PEIKIRA CPL**; the L1a row's only benchmark is the BC Image087 *formula* (different image, BC campaign). KENJI-FAB-20261009-016 (Rp 933,870 / 3 = 311.3k) is a different image (74632d…, "muat kulkas" size copy), not a prior for L1a. Limit: there is no search by image hash, so a use under an ad name without "016" is not ruled out. ⚠️ 018 says "bukan gambar render" while 010 in the same ad set is render-look (copy risk, not an ad-account ask).

**L1a benchmark (account data, 11/15 19:01, `ads_get_ad_entities` ad 120241535471910572 "BC Image087 Post", BC batch087 Copy 7):** lifetime Rp 18,646,819 / 233 leads = **Rp 80.0k** *(calc)*; last 28d (10/18–11/14) Rp 1,264,452 / 16 = **Rp 79.0k** *(calc)*. So the formula holds ~80k over both windows, under the 95k target. L1a read rule: 016 "matches the formula" if its CPL ≤ Rp 95k on ≥ Rp 190k spend; ≤ 80k = beats its BC parent. Caveat: different campaign, image and bid setup (BC 087 runs under its own Rp 94,250 cap), so a gap is a signal, not proof (INFERRED).

7. **Map first.** At the read, pull `ads_get_creatives` for ADSET-3's ads (read-only) and fill the Ads column from image hashes; INFERRED rows become account data or move.
8. **Per-look call only when the look has ≥ Rp 95k spend** (same floor as rule 5). Below that: "untested look", not a loser.
9. **Look labels:** ≤ 95k on ≥ 2 leads = "look works" · > 1.5× the ad set's CPL on ≥ Rp 190k = "look fails" · else "unclear".
10. **Naming the wave:** call ADSET-3 a "photo wave" win/loss only from L1a + L1b + L2 pooled (≥ Rp 190k between them). If the ad set wins on L3/L4 spend, write "graphics/render won", which would contradict the 11/05 history and needs a second test before it changes the creative plan.
11. **Feeds Wave 2+:** a "look works" on L2 unlocks the clutter → C1 unit carousel option (`creatives/2026-11-12_wave2_build_sheet.md`, row B5-C).

## 11/20 day-7 pre-fill (added 11/17 11:01; rows copied from the tracker locks, no new pull)
Window = full days 11/13–11/19. Locked so far (account data via tracker; ADSET-3 = PEIKIRA total − control − PEIKIRA2):

| Day | PEIKIRA total | Control (spend / leads) | PEIKIRA2 | ADSET-3 (spend / impr) | Context |
|---|---|---|---|---|---|
| 11/13 | 293,851 | 168,405 / 0 | 125,446 / 0 | 0 / 0 | CBO Rp 300k, no cap |
| 11/14 | 309,404 | 166,269 / 3 | 143,135 / 0 | 0 / 0 | CBO Rp 300k, no cap |
| 11/15 | 153,555 | 100,930 / 0 | 52,625 / 1 | 0 / 0 | Rp 3M CBO + Rp 105k cap from 00:41 |
| 11/16 | 16,396 | 15,450 / 0 | 946 / 0 | 0 / 0 | capped, PEIKIRA ≈ off |
| 11/17 | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | lock at 11/18 07:00 |
| 11/18 | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | lock at 11/19 07:00 |
| 11/19 | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | pull at 11/20 07:00 |

Control 11/13–11/16: Rp 451,054 / 3 = **150.4k** *(calc)*. ADSET-3: Rp 0 on 4 of 7 days.

**Pre-resolved verdict branches (rules 1–6 above, unchanged):**
- **A. ADSET-3 still Rp 0 (or < Rp 5k) through 11/19** → rule 6: **UNTESTED, not a loser.** Rules 2–3 cannot fire. No keep/pause call; the 11/27 day-14 verdict is also void unless it spends ≥ Rp 95k by then. Message: "ADSET-3 got no delivery in 7 days (cap + overlap with PEIKIRA2, 11/15 diagnosis); it was never tested. Fix = ask #2(b) min spend, or ask #1 undo." Do not add a new ask; point to the existing ones.
- **B. Spends Rp 5k–94k** → still untested (rule 5/8 floor Rp 95k); report spend + leads only.
- **C. Spends ≥ Rp 95k** → rule 3: CPL vs control's full-window CPL (control base so far 150.4k): ≤ control → KEEP; > 1.3× control on ≥ Rp 400k → propose pause; rule 2 early-kill check first (≥ 190k / 0 leads).
- If ask #1 undo lands mid-window: split the window at the change day (re-base rule §D) and judge ADSET-3 only on post-undo days.
