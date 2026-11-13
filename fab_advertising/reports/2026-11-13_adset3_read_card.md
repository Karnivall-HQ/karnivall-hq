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
4. **Verdict on day 14 (11/27)**, 2-week block, per playbook: winner only if ≤ 95k on ≥ 4 leads.
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
