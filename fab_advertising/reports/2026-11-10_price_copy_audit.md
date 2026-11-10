# Fab price-in-copy audit: 750 vs 800 (2026-11-10 19:02 WIB, read-only)

Source: Meta account 484578521394893, every ad with spend > 0 in the last 7d (83 ads), creative body/title/description read via `ads_get_creatives`. Spend = 7d, from `ads_get_ad_entities`. Activity log 13:00–19:02 WIB: empty (no human edits).

## Result
| Copy says | Ads | 7d spend | Share | 7d leads |
|---|---|---|---|---|
| "dari Rp750rb" (FAB750) — all PEIKIRA / PEIKIRA2 ads | 11 | Rp 1,902,877 | 80.6% *(calc)* | 16 (Ad015 12, 006 4) |
| No price in creative text (incl. BC Image087, a boosted post; AKIRA 013/009; old PEIKIRA Ad00x/N0x) | 13 | Rp 226,649 | 9.6% *(calc)* | 3 (087 2, 013 1) |
| "dari 800rb" / "Mulai dari Rp800.000" — **every BC CBObass005 ad** | 59 | Rp 230,262 | 9.8% *(calc)* | 2 (095 1, 3-21 1) |

Total 7d spend Rp 2,359,788.

## What this changes
- The "old Rp800.000 ads" are not a stray 09/2026 batch: **the entire BC campaign (59 live ads, Feb–Sep 2026) says 800rb.** PEIKIRA (Oct–Nov) says 750rb. So the account itself runs two prices, split by campaign.
- BC is the bid-cap engine the scale plan counts on for ~Rp 290k/day (`scale_plan.md`). Editing 59 creatives would reset learning on every BC ad set; pausing them kills that engine. Neither is worth it for a price line.
- **If 750 is the real price (FAB750):** "dari 800rb" understates nothing that hurts the customer (they find a lower price in WA). → **No ad change.** Fix only the site form page (W2). New BC ads, if any, use 750.
- **If 800 is the real price:** the 80% of spend saying 750 is the problem, not BC. → PEIKIRA copy must change (Ad015 is the single point of failure: a copy edit = new ad, learning reset). That case would need its own plan.
- So the 750 vs 800 answer decides whether *any* ad needs touching. It stays inside ask #2; no new ask.

## Proposed changes for Alvian to apply
- None now. W2 (site form page → "Promo Rp750.000/bulan, kode FAB750") stays as written, assuming 750.
