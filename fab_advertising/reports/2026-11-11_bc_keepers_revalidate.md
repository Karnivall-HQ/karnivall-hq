# BC 5-keeper re-validation (parked item 3 + 4), 7d 11/04–11/10
_2026-11-11 13:02 WIB · cloud heartbeat · read-only · campaign `120236222888610572`_

Rule applied: `meta-tests-and-proposals.md`, re-validate a parked ask on fresh 7d data before any re-ask.

## Numbers (account data, `ads_get_ad_entities` adset level, time_range 11/04–11/10)
| Group | Ad sets | Spend (Rp) | Leads | CPL |
|---|---|---|---|---|
| 5 "keepers" (087 Copy 7, 201 Manny5, batch101 Copy 21, BC204 Manny6, BC4-08 Usir) | 5 | 169,700 *(calc)* | 2 | 84,850 *(calc)* |
| Everything else in BC | 51 rows (incl. 0-spend) | 158,614 *(calc)* | 3 | 52,871 *(calc)* |
| BC total | | 328,314 *(calc)* | 5 | 65,663 *(calc)*, matches the 07:02 readout |

Per keeper: 087 Copy 7 Rp 98,776 / 2 (49,388) · 201 Manny5 29,754 / 0 · batch101 Copy 21 20,922 / 0 · BC204 Manny6 15,352 / 0 · BC4-08 Usir 4,896 / 0.
Leads from non-keepers: batch095 Copy 15 (19,516 / 1), BC208 UGC (18,835 / 1), BC3-21 Anak Copy 10 (16,459 / 1).
Tail: 10 non-keepers ≥ Rp 7k spent Rp 125,321 *(calc)*; the other ~41 together ≈ Rp 33k *(calc)*. Several are WITH_ISSUES (BC3-27, BC3-32, batch044–047, batch082) at 0 spend.

Supporting reads (required follow-ups): trend tool rates 087 Copy 7 CPR **GOOD** (−74.8% change, CTR +29.9%, CPM +27.4% BAD) and BC3-21 Copy 10 GOOD. Benchmark: 087 Copy 7 CPR **30.22% worse than its peer benchmark**.

## Verdict
- **Item 3 (keep 5, pause ~44): retire.** Its 11/05 basis ("the others: < Rp 30k each, 0 leads") no longer holds: last 7d, 3 of BC's 5 leads came from non-keepers, at a lower blended CPL than the keepers. Counts are tiny (2 vs 3 leads), so this does not prove the tail is better, only that "pause the tail" has no evidence behind it. The tail also spends only ≈ Rp 22.7k/day *(calc)*, so pausing it can't move the Fab blend much. INFERRED: with all ad sets on the same Rp 94,250 cap, the tail acts as extra auction coverage, not waste.
- **Item 4 (087 Copy 7 cap Rp 94,250 → 105,000): still stands, unchanged.** 087 delivers ≈ Rp 14.1k/day *(calc)*, the cap is still Rp 94,250 (confirmed), and it is BC's only multi-lead ad set. Gate-brief math (item 4 alone ≈ 104k) is unchanged, so it stays parked behind the site fix.
- Optional cleanup for whenever Alvian is in the account (no CPL effect): the 7 WITH_ISSUES ad sets at 0 spend.

No new ask. OUTBOX parked item 3 marked retired.
