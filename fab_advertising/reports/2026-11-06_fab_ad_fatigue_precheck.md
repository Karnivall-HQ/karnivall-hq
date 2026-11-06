# Fab (Warehouse Storage) — ad-level fatigue pre-check (for Mon 11/09 weekly)
_2026-11-06 18:02 WIB cloud heartbeat · account `484578521394893` · source: ads_get_ad_entities, level=ad, time_increment=7, spend > Rp 50k over 10/23–11/05_

Weeks: **W1 = 10/23–10/29**, **W2 = 10/30–11/05**. 13 ads qualified (PEIKIRA2 ads started 11/05, below threshold).
Totals for these 13 ads *(calc)*: W1 Rp 1,612,651 / 14 leads / Rp 115,189 → W2 Rp 2,255,300 / 20 / Rp 112,765.

## Verdict
**No classic fatigue (max freq 1.60), but a concentration risk.** In W2, **AKIRA-FAB-20261016-Ad015** took Rp 1,661,844 = **86.7%** *(calc)* of PEIKIRA ad-level spend and 16 of the 20 leads (CPL Rp 103,865). CTR 1.93% → 1.63% (−16% calc), freq 1.60. If Ad015 fatigues, PEIKIRA has no second ad carrying volume, which is why the 11/10 PEIKIRA2 read and the batch 01 v2 shoot matter.
BC Image087: CTR flat 1.51% → 1.51%, freq 1.22, CPM flat → **not fatigue**; confirms the 16:02 finding (auction loss under the Rp 94,250 cap → item 4).

## Per ad (account data)
| Ad | Campaign | Spend W1 → W2 (Rp) | Leads | CTR W1 → W2 | Freq W2 | Flag |
|---|---|---|---|---|---|---|
| AKIRA-…-Ad015 | PEIKIRA | 29,643 → 1,661,844 | 0 → 16 | 1.93% → 1.63% (−16%) | 1.60 | ⚠️ concentration; watch CTR |
| BC Image087 Post | BC Copy 7 | 555,204 → 260,770 | 7 → 2 | 1.51% → 1.51% | 1.22 | bid-cap starvation, not fatigue |
| PEIKIRA-…-Ad001 | PEIKIRA | 140,249 → 95,519 | 1 → 1 | 1.72% → 0.74% (**−57%**) | 1.09 | 🚩 CTR flag (≥30%); CPL 95.5k so low priority |
| PEIKIRA-…-Ad007 | PEIKIRA | 70,609 → 63,312 | 1 → 1 | 1.74% → 1.22% (**−30%**) | 1.08 | 🚩 borderline CTR flag |
| KENJI-…-001 v03 | PEIKIRA | 58,190 → 25,071 | 0 → 0 | 1.02% → 0.49% (**−52%**) | 1.22 | 🚩 already in item 5 (pause) |
| KENJI-…-020 v03 | PEIKIRA | 33,501 → 51,181 | 1 → 0 | 1.92% → 2.02% | 1.25 | ok |
| PEIKIRA-…-Ad003 | PEIKIRA | 48,256 → 19,123 | 0 → 0 | 1.15% → 2.09% | 1.06 | in item 5 |
| AKIRA-…-Ad014 / Ad002 | PEIKIRA | 252,130 / 202,981 → 0 | 1 / 0 → 0 | — | — | paused (by team) |
| BC 3-21, 201D, 204F, 208 | BC | 92,631 / 60,403 / 38,993 / 29,861 → ≤ 20k each | 3 → 0 | rising (2.3–3.5%) | ≤ 1.30 | starved by caps, not fatigued |

## For Monday
- Re-pull W3 (11/06–11/12 partial → use 11/02–11/08). Flag Ad015 if CTR < 1.4% or freq > 2.5 with CPL > Rp 120k.
- Fatigue table rows: Ad015 (concentration), Ad001/Ad007/KENJI-001 (CTR flag).
- No new proposal (stalled-asks rule). It strengthens the existing creative ask: one ad = 87% of PEIKIRA spend.
- Skipped the MCP's suggested trend/benchmark follow-ups: the WoW split answers the fatigue question; its candidate actions are write tools (propose-only).
