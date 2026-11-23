# Incess (OMO ADVLeads): landing page check + placement split, 2026-11-23 09:01 WIB

Read-only. Follows `2026-11-23_incess_drift_decomposition.md` (CPL ×1.43; ≈ 65% after the click; LPV ÷ click slid to 78–83%).
Campaign `120233576079370222`, account `2017038114993984`. Weeks: W1 11/09–11/15, W2 11/16–11/22.

## 1. Landing page: not the cause
- All 4 picks (042, 047, 026D Copy 3, 030) link to **one URL**: `https://omorental.com/sewa-mobil-rental-bali` (Bali self-drive car rental, "from 175.000"). CTA SEE_DETAILS / BOOK_TRAVEL.
- curl ×3 (mobile UA, `?fbclid=`): **200, 0 redirects**, TTFB 0.82–1.22 s, total 1.70–1.93 s, 264,753 bytes. Measured from a cloud box outside Indonesia, so Indonesian mobile timing is unknown.
- **No changes:** page `dateModified` 2024-11-28; WA form page (`/booking-form-whatsapp`, Fluent Form #3) 2025-07-15; WP Rocket cache stamp 2026-02-13. Nothing on the site moved around 11/19.
- Funnel: no form on the landing page. CTAs ("Pesan via Whatsapp ➜", "Sewa Mobil Rental di Bali via WA ➜", floating WA button) → `/booking-form-whatsapp`. Pixel 209989004433191 via PixelYourSite Pro (PageView + ViewContent static, "Form" dynamic event, Lead set up as an event).
- ⚠️ Structural, not new: WP Rocket "delay JS" (`rocketlazyloadscript`, 40 scripts incl. jQuery + PixelYourSite) holds the pixel until the visitor's first touch or scroll. A visitor who bounces without touching never counts as an LPV. That explains why LPV ÷ click sits below 100% on FB placements, but it has been live since at least Feb, so it can't explain the 11/19 slide (INFERRED).

## 2. Placement split (tool output; ratios *(calc)*)

| Placement | Spend W1 → W2 | LPV÷click W1 → W2 | Lead÷LPV W1 → W2 | CPL W1 → W2 |
|---|---|---|---|---|
| IG feed | 2,294,048 → 2,793,667 | 95.6 → 91.8% | 7.45 → 7.83% | 29.0k → 34.1k |
| **IG reels** | 1,034,456 → 1,487,395 | **92.6 → 83.8%** | **4.68 → 3.33%** | **19.5k → 36.3k** |
| IG stories | 1,086,829 → 1,640,951 | 102.4 → 97.3% | 5.69 → 5.06% | 27.9k → 42.1k |
| **FB reels** | 304,939 → 527,335 | 74.8 → 70.3% | 5.21 → 2.87% | 27.7k → 52.7k |
| FB feed | 212,831 → 318,311 | 73.2 → 72.0% | 6.67 → 4.03% | 35.5k → 53.1k |
| Threads | 201,146 → 299,362 | 72.6 → 69.6% | 2.93 → 3.64% | 28.7k → 27.2k |
| FB search | 9,647 → 14,660 | 62.0 → 62.3% | 0 → 0 | n/a |
| Total (8 rows) | 5,170,217 → 7,121,201 (×1.38) | 90.6 → 84.0% | 5.61 → 4.80% | 26.4k → 37.7k |

- **Mix:** IG share of clicks 77.9% → 72.6% *(calc)*; FB/Threads placements carry LPV ÷ click of 52–72% vs 84–102% on IG.
- **Mix alone:** W2 clicks at W1 per-placement rates → 4,189 LPV, 230 leads, **CPL 30.9k** *(calc)* vs actual 37.7k. So in log terms **≈ 45% of the rise is mix** (more spend going to weaker placements) and **≈ 55% is decline inside placements** *(calc)*, led by IG reels (CPL ×1.86) and FB reels (×1.90).

## 3. Read
- Spend rose ×1.38 at unchanged caps. The extra delivery went to weaker inventory (FB reels/feed, Threads) and to weaker IG reels users. Same "volume expansion" pattern as the 11/20 pick split (INFERRED). It is not the site and not auction price.
- Implication: a cut list of ads won't fix it, but a **placement lever** could (e.g. pull FB reels/feed out of the pick ad sets). It's an ad-account change, so propose-only, and the 7d isn't settled yet. **No ask today**; the 11/30 weekly decides.
- **11/30 rule (adds to NOW #5):** if 7d CPL is still > 35k and FB reels + FB feed CPL is > 1.4× IG feed for a 2nd week → write a placement-exclusion proposal (Alvian applies). If IG reels CPL is back ≤ 25k → close the watch. Trend/peers tools: trend window is lifetime (not usable for W1 vs W2); peers returned "empty peer_set" for all ad sets.
