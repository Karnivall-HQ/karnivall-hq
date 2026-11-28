# Incess placement + 047 pre-pull — 11/23–11/26 (4 of 7 days)
_2026-11-27 08:01 WIB, cloud heartbeat. Read-only (Rudi MCP `ads_get_ad_entities`, 2 calls). Cross-check for the 11/30 weekly R2 + 047 flag; **no verdict < 7d**. *(calc)* = Fuku's arithmetic._

## Call 6a: Incess campaign `120233576079370222`, breakdowns publisher_platform × platform_position
`inline_link_clicks` is NOT supported at campaign level (tool said so) → use `link_click` on 11/30. LPV÷click column left empty here.

| Placement | Spend | LPV | Leads | Lead÷LPV *(calc)* | CPL *(calc)* | Prior wk CPL |
|---|---|---|---|---|---|---|
| IG feed | 1,459,965 | 439 | 49 | 11.16% | 29.8k | 34.1k |
| IG reels | 828,290 | 604 | 25 | 4.14% | 33.1k | 36.3k |
| IG stories | 896,767 | 418 | 32 | 7.66% | 28.0k | 42.1k |
| FB reels | 268,302 | 154 | 7 | 4.55% | 38.3k | 52.7k |
| FB feed | 204,694 | 79 | 3 | 3.80% | 68.2k | 53.1k |
| Threads | 177,491 | 134 | 8 | 5.97% | 22.2k | 27.2k |
| Other (9 small positions) | 46,274 | — | 1 | — | — | — |
| **Campaign** | **3,881,783** | | **125** | | **31.1k** | 37.8k (acct) |

- **R2 test so far:** FB reels+feed 472,996 / 10 = 47.3k ÷ IG feed 29.8k = **1.59** *(calc)* (prior 1.55), but campaign 4d CPL **31.1k ≤ 35k** → on track for **"close the watch"** on 11/30, not a proposal. Small FB counts (10 leads).
- Pace: 3.88M / 4 = 970k/day *(calc)* vs 1.02M/day last week: steady.

## 047 flag (ad set `120239723303450222`, daily)
| Day | Spend | Leads | CPL | CTR | Freq |
|---|---|---|---|---|---|
| 11/23 | 225,043 | 6 | 37,507 | 2.25% | 1.20 |
| 11/24 | 156,950 | 5 | 31,390 | 2.13% | 1.18 |
| 11/25 | 159,005 | 3 | 53,002 | 2.51% | 1.20 |
| 11/26 | 165,722 | 1 | 165,722 | 2.68% | 1.26 |
| **4d** | **706,720** | **15** | **47.1k** *(calc)* | | |

- Still above its 35.6k flag line (prior wk 40.1k), and worse. But CTR is **up** (2.13 → 2.68%) and freq ≈ 1.2 → not creative fatigue (INFERRED); the drop is post-click / lead rate, 2 days of small counts. Note only; the 11/30 weekly decides with 7d (R5 + the "picks > 35k → cut list" line from the 11/23 report).

## R7 pre-read + cut-list skeleton (15:01 WIB, 1 read-only ad-level call, 11/23–11/26)
Required follow-ups ran: trend (ad level, full history) + peers ("No benchmark data is available").

| Pick (ad set) | Live ads | Carrying ad | Spend 4d | Leads | CPL *(calc)* | CTR | Freq | Trend tool CPR |
|---|---|---|---|---|---|---|---|---|
| 042 `120239651281900222` | 1 | ImageAd042 `120239651281890222` | 808,366 | 28 | 28.9k | 2.72% | 1.29 | −20% GOOD |
| 026 `120244551313580222` | 6 | 026D Copy 3 `120244561032460222` (95.9% of 658,609 *(calc)*) | 658,609 | 34 | 19.4k | 2.70% (026D) | 1.39 | −9% GOOD |
| 047 `120239723303450222` | 1 | ImageAd047 `120239723303440222` | 706,723 | 15 | 47.1k | 2.35% | 1.42 | +74% BAD (CVR −30%, CTR +20%) |
| 030 `120239636846070222` | 1 | ImageAd030 `120239636846080222` | 249,236 | 2 | 124.6k | 2.33% | 1.20 | +29% BAD |
| **4 picks** | | | **2,422,934** | **79** | **30.7k** | | | |

- **R7 so far: 4-pick 30.7k ≤ 35k → line heading to "closed"** *(calc, 4 of 7 days)*. 026 is now the cheapest pick (19.4k) after 2 weeks of Meta shrinking it.
- **Shape fact for the cut list:** 3 of 4 picks run **one ad**, and 026's spend is 96% on 026D. So a "per-ad cut" inside a pick = pausing the pick. The cut list is written at ad-set level.
- **Two watch lines for 11/30 (no ask on < 7d):** 047 (post-click drop; trend tool agrees: CVR −30%, CTR up) and 030 (Rp 249k / 2; its ≥ 10-lead flag line is 46.1k; small counts).

### Cut list — fill only if R7 fires on 11/30 (4-pick 7d > 35k). Propose-only: Alvian applies.
> **Dry-run 11/27 22:01:** the rules below now live in `fuku/bin/incess_r7.py` (`--pick 042 S L --pick 047 S L --pick 030 S L --pick 026 S L --ctr 047=<pct>`; exit 0 = R7 closed, 2 = cut list printed). 2 fixes: (1) 026 has 6 live ads, so "its only live ad" was wrong for 026 → the script names all 6; (2) 026's cap is 45,000, not 46k → spend multiples use each pick's own cap. 4 dry runs (closed on the 4d numbers, 030 cut, 030 skipped at 2.5× cap with 1 lead → 047 cut, 026 cut) ✓.

Pick rule (pre-set now): cut the pick with the highest 7d CPL among picks with **spend ≥ 2× its own bid cap (46k; 026 45k)**; if its 7d leads < 3, cut only if spend ≥ 3× cap (Rp 138k) (spend-multiple kill, `meta-tests-and-proposals.md`). Never cut 2 picks in one go.
```
Proposed changes for Alvian to apply (Incess, OMO ADVLeads 120233576079370222):
1. Pause ad set ⟨name⟩ ⟨id⟩ (its only live ad ⟨ad id⟩). 7d 11/23–11/29: Rp ⟨spend⟩ / ⟨leads⟩ = ⟨CPL⟩ (flag line ⟨line⟩); 4-pick 7d ⟨x⟩ > 35k.
   Where the spend goes: campaign budget unchanged; Meta re-routes to the other picks (cheapest 7d: ⟨pick⟩ ⟨CPL⟩). (INFERRED: campaign-level budget; confirm daily_budget at campaign level in call 5 before sending.)
   Expected: 4-pick CPL → ⟨(S − s_cut) ÷ (L − l_cut)⟩ *(calc)*, if the moved spend converts at the remaining picks' average.
   Undo: re-activate if the other 3 picks' 3-day CPL > 35k after the pause.
```
If R7 does **not** fire: write "R7 closed: 4-pick 7d ⟨x⟩ ≤ 35k" and carry 047/030 as watch lines only.

## 11/28 10:02 WIB — 5d pre-read 11/23–11/27 (2 read-only calls) + full script dry-run
_Not a verdict (5 of 7 days). Both rows below are script output, copied verbatim._

- **Campaign (sum of all 16 placement rows):** Rp 4,881,434 / 154 = **31.7k** *(calc)* (4d was 31.1k; prior wk 37.8k).
- **R2 (`incess_r2.py`, exit 0):** IG feed 30.3k · IG reels 28.2k · IG stories 30.6k · FB reels 51.4k · FB feed 81.3k · Threads 27.6k. FB reels+feed 603,524 / 10 = 60.4k ÷ IG feed 30.3k = **1.99** (prior 1.55) → **CLOSE** (campaign 31.7k ≤ 35k; IG reels 28.2k is above the 25k alt line). FB gap is widening but on 10 leads.
- **R7 (`incess_r7.py`, exit 0):** 042 1,015,499 / 36 = 28.2k · 047 871,299 / 22 = **39.6k OVER 35.6k** · 030 296,408 / 3 = **98.8k OVER 46.1k** · 026 901,959 / 40 = 22.5k → 4 picks 3,085,165 / 101 = **30.5k → R7 CLOSED** *(calc)*. Watch: 047 CTR 2.47% (ad set) vs 3.02% = −18% → post-click drop, not fatigue; 030 small counts.
- **Read for 11/30:** both lines heading to close; 030 is the only pick moving the wrong way (124.6k → 98.8k on 2 → 3 leads; 6.4× cap). If 030 stays > 46.1k at 7d with ≥ 3 leads it gets a named watch line in Top 3, still no cut (R7 closed = no cut list).
