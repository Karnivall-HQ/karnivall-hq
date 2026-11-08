# M-001 tracker: Fab / Warehouse Storage `484578521394893`
Goal: 7d avg CPL ≤ Rp 95,000 AND sustained Rp 1,000,000/day. Deadline 2026-12-05.
Numbers come from Rudi MCP (read-only). *(calc)* = Fuku's arithmetic. Proposed changes are applied by Alvian, never by Fuku.

## Weekly readouts (7d windows)
| Readout (WIB) | Window | Spend 7d | Spend/day | Leads | 7d CPL | Gate (≤95k)? | Notes |
|---|---|---|---|---|---|---|---|
| 2026-11-08 07:02 | 11-01 → 11-07 | Rp 2,531,551 *(calc)* | Rp 362k *(calc)* | 22 | Rp 115,070 *(calc)* | ❌ | Better than 11/07 (121.9k) on paper, but driven by the control ad set. PEIKIRA Rp 2,095,244 / 19 (Rp 110,276); BC CBO Copy Rp 436,307 / 3 (Rp 145,436). PEIKIRA2 cumulative 11/05–11/07 Rp 539,027 / 2 (Rp 269.5k) vs control Rp 350,414 / 5 (Rp 70.1k) → re-trigger rule (≥ Rp 500k, ≤ 2 leads) hit → pause-PEIKIRA2 ask. No human edits overnight. |
| 2026-11-07 07:02 | 10-31 → 11-06 | Rp 2,560,776 *(calc)* | Rp 366k *(calc)* | 21 | Rp 121,942 *(calc)* | ❌ | Slightly better than 11/06 (125.2k). PEIKIRA 19 leads @ Rp 109,956 (Rp 2.09M); BC CBO Copy 2 @ Rp 235,806 (Rp 472k). No proposals applied; no human edits overnight. |
| 2026-11-06 07:01 | 10-30 → 11-05 | Rp 2,503,323 | Rp 358k | 20 | Rp 125,166 *(calc)* | ❌ | Worse than yesterday's readout. PEIKIRA 18 leads @ Rp 112.6k (Rp 2.03M); BC CBO Copy 2 leads @ Rp 238k (Rp 477k). No proposals applied yet. Pixel funnel: LP→Lead 3.9% → `2026-11-06_landing_page_audit.md` |
| 2026-11-05 19:09 | 10-29 → 11-04 | Rp 2,483,302 | Rp 355k | 22 | Rp 112,877 *(calc)* | ❌ | PEIKIRA 19 leads @105k; BC CBO 3 leads @163k (stalled under bid cap). Placement breakdown → `2026-11-05_m001_breakdown.md` |

## Daily snapshots (partial day unless noted)
| Date (WIB) | Spend | Leads | CPL | Notes |
|---|---|---|---|---|
| 2026-11-07 (full day) | Rp 278,661 *(calc)* | 2 | Rp 139,331 *(calc)* | PEIKIRA Rp 231,092 / 1; BC CBO Copy Rp 47,569 / 1. Inside PEIKIRA: PEIKIRA2 Rp 202,368 / 0 *(calc)* = 87.6% of PEIKIRA spend; control Rp 28,745 / 1 *(calc)*. Single day, not a gate metric. |
| 2026-11-06 (full day) | Rp 413,498 *(calc)* | 5 | Rp 82,700 *(calc)* | PEIKIRA Rp 372,915 / 4 (Rp 93,229); BC CBO Copy Rp 40,583 / 1. PEIKIRA2 got its 2nd lead after 20:02 → cumulative 11/05–11/06 Rp 336,659 / 2 (Rp 168,330); control Rp 321,669 / 4 (Rp 80,417). Single day, not a gate metric. |
| 2026-11-06 (to 19:01) | Rp 337,101 *(calc, top 15 ad sets)* | 3 | Rp 112,367 *(calc)* | PEIKIRA2 Rp 239,487 / 1 (77.7% of PEIKIRA spend, CPM 54k); control Rp 68,588 / 2; BC Rp 29,026 / 0 (087 Copy 7 only Rp 9,791). Single day, not a gate metric. |
| 2026-11-06 (to 20:02) | PEIKIRA ad sets Rp 321,977 *(calc)* | 3 | Rp 107,326 *(calc)* | PEIKIRA2 Rp 252,984 / 1 (78.6%); control Rp 68,993 / 2. PEIKIRA2 cumulative Rp 292,582 / 1 → pause threshold tripped. No human edits 19:00–20:02. |
| 2026-11-05 (full day) | Rp 342,560 *(calc)* | 2 | Rp 171,280 *(calc)* | PEIKIRA Rp 285,413 / 2; BC CBO Copy Rp 57,147 / 0. |
| 2026-11-05 (to 22:01) | Rp 327,111 *(calc)* | 2 | Rp 163,556 *(calc)* | PEIKIRA Rp 272,991 / 2 leads (incl. PEIKIRA2 in learning); BC CBO Copy Rp 54,120 / 0. Single day, not a gate metric. |

## Change log (applied by Alvian)
| Date | Change | By | Effect read on |
|---|---|---|---|
| 2026-10-26 | PEIKIRA campaign budget Rp 5,000,000 → Rp 300,000/day | Markus Reynaldo (from activity log) | n/a (before mission) |
| 2026-11-05 14:40 WIB | New ad set **AKIRA-FAB-20261031-WAVE-PEIKIRA2** (`120254276298070572`) in PEIKIRA-BID-CAP-LEADS-CAMPAIGN; 23 image ads created (8 approved/active, 15 inactive after review). CBO budget unchanged at Rp 300k/day. | **Markus Reynaldo** via the "Rudi MCP" app (actor id 61594758338050; confirmed by Alvian) | 2026-11-10 (5 days) |
| 2026-11-05 17:06 WIB | Meta set ad **ImageAd 201B** (in winner ad set BCbatch201 Manny5) to "Update Required" (issue 4469003) → it stopped delivering | Meta (system) | ✅ checked 11/06 08:02: still WITH_ISSUES, but it spent **Rp 0 in all of 10/23–11/05**, so no real loss. The whole Manny5 ad set spent only Rp 18.2k in 7d (0 leads) [calc]. Its "winner" label is 30d data. Low priority. |
