# PEIKIRA2 read (Tue 2026-11-10): pre-staged
_Prepared 2026-11-06 13:02 WIB (cloud heartbeat). Read-only. On 11/10 you only need to run the pulls, fill the table, and apply the rules._

## Objects
| What | Name | ID |
|---|---|---|
| Campaign (CBO, Rp 300k/day, bid cap) | PEIKIRA-BID-CAP-LEADS-CAMPAIGN | `120254051672440572` |
| Old ad set (control) | PEIKIRA-FAB-20261023-ADSET | `120254051672430572` |
| New ad set (test, launched by Markus 11/05 14:40 WIB) | AKIRA-FAB-20261031-WAVE-PEIKIRA2 | `120254276298070572` |

Account `484578521394893`. Window: **2026-11-05 → 2026-11-09** (5 full days; 11/05 is a partial launch day for PEIKIRA2, so read it with and without 11/05).

## Pulls (run in this order)
1. **Activity log** `start_time=2026-11-05T07:40:00Z`, `object_id=120254051672440572`, limit 40. Note any edit to either ad set (an edit resets learning and breaks the comparison).
2. **Ad sets** `ads_get_ad_entities` level=adset, filter `campaign.name CONTAIN PEIKIRA`, `time_range {"since":"2026-11-05","until":"2026-11-09"}`, fields: id, name, effective_status, amount_spent, impressions, link_click, ctr, lead, cost_per_lead, learning_stage_info. Repeat with `since 2026-11-06`.
3. **Ads in PEIKIRA2** level=ad, filter `adset.id IN [120254276298070572]` (verify the field with `ads_get_field_context` first), same window, fields: id, name, effective_status, amount_spent, ctr, lead, cost_per_lead. Sort by amount_spent descending.
4. **Placement breakdown** for both ad sets (`breakdowns: ["publisher_platform","platform_position"]`), same window. Check whether IG Stories is still eating PEIKIRA spend (item 1).
5. Campaign total for 11/05–11/09 → feeds the tracker's 7d row.

## Table to fill
| Ad set | Spend | Leads | CPL | CTR | Learning | Share of campaign spend |
|---|---|---|---|---|---|---|
| Old (control) | | | | | | |
| PEIKIRA2 (test) | | | | | | |
| Campaign total | | | | | | 100% |

### Mid-flight snapshot (11/05–11/06 13:02 WIB, partial; context only, not a verdict)
| Ad set | Spend | Leads | CPL | CTR | Learning |
|---|---|---|---|---|---|
| Old (control) | Rp 307,284 | 4 | Rp 76,821 | 1.68% | LEARNING (23 conv.) |
| PEIKIRA2 (test) | Rp 168,108 | 1 | Rp 168,108 | 1.67% | LEARNING (1 conv.) |
| Campaign | Rp 475,392 *(calc)* | 5 | Rp 95,078 *(calc)* | | |

PEIKIRA2 took 35% *(calc)* of campaign spend in its first ~1.5 days. Meta trend (old ad set, full history): CPR improving (−54%, GOOD), CVR +136%, CTR down 8%; industry benchmark: old ad set CTR 54% **below** peers. The test ad set has too little data for trend/benchmark.

### Mid-flight snapshot #2 (11/05–11/06 19:01 WIB, partial; context only)
| Ad set | Spend | Leads | CPL | CTR |
|---|---|---|---|---|
| Old (control) | Rp 314,403 | 4 | Rp 78,601 | 1.70% |
| PEIKIRA2 (test) | Rp 279,085 | 1 | Rp 279,085 | 1.56% |

Today alone (11/06 to 19:01): PEIKIRA2 Rp 239,487 / 1 lead at CPM Rp 54,048; control Rp 68,588 / 2 leads at CPM Rp 37,236. PEIKIRA2 took **77.7%** *(calc)* of today's campaign spend (was 35% at 13:02). Cumulative PEIKIRA2 spend = **97.9% of the Rp 285k pause threshold** *(calc)* with 1 lead → the pre-set pause rule will almost certainly trip tonight. Plan: if PEIKIRA2 is still ≤ 1 lead at ≥ Rp 400k at the 11/07 07:00 readout, make "pause PEIKIRA2" the single ask (it replaces, not stacks on, item 1). Otherwise keep the 11/10 read.

### Mid-flight snapshot #3 (11/05–11/06 20:02 WIB, partial; context only)
| Ad set | Spend | Leads | CPL | CTR |
|---|---|---|---|---|
| Old (control) | Rp 314,808 | 4 | Rp 78,702 | 1.70% |
| PEIKIRA2 (test) | Rp 292,582 | 1 | Rp 292,582 | 1.54% |

Today (11/06 to 20:02): PEIKIRA2 Rp 252,984 / 1; control Rp 68,993 / 2 (CPL Rp 34,497). PEIKIRA2 = 78.6% *(calc)* of today's PEIKIRA spend. **Pause threshold (Rp 285k, ≤1 lead) tripped: 102.7% *(calc)*.** Per the 19:01 plan the ask fires at the 11/07 07:00 readout (if still ≤1 lead at ≥ Rp 400k), not tonight — the campaign has already spent ~Rp 322k *(calc)* of today's Rp 300k, so little more can be lost before morning.

### 11/07 07:02 readout (11/05–11/06 full days; context only)
| Ad set | Spend | Leads | CPL | CTR | Learning |
|---|---|---|---|---|---|
| Old (control) | Rp 321,669 | 4 | Rp 80,417 | 1.72% | LEARNING (23 conv.) |
| PEIKIRA2 (test) | Rp 336,659 | 2 | Rp 168,330 | 1.64% | LEARNING (2 conv.) |

PEIKIRA2 got a 2nd lead after 20:02, so the pause rule (≤ 1 lead) **no longer applies**; it sits in the "in between" band (CPL 95–150k+ / < 3 leads) → **hold**, no ask. Share of campaign spend 51% *(calc)*. The 11/10 read stands.

### 11/08 07:02 readout (11/05–11/07 full days) → early trigger
| Ad set | Spend | Leads | CPL |
|---|---|---|---|
| PEIKIRA2 (`120254276298070572`) | Rp 539,027 | 2 | Rp 269,514 *(calc)* |
| Control PEIKIRA-FAB-20261023-ADSET (`120254051672430572`) | Rp 350,414 | 5 | Rp 70,083 *(calc)* |
| Campaign (both) | Rp 889,441 *(calc)* | 7 | Rp 127,063 *(calc)* |

11/07 alone: PEIKIRA2 Rp 202,368 / 0 leads *(calc)* = 87.6% of PEIKIRA spend; control Rp 28,745 / 1. PEIKIRA2 is ≈ 5.7× target spend *(calc)* with 2 leads → the 11/07 re-trigger rule (≥ Rp 500k with ≤ 2 leads) fired, and the "either way" rule also fires: campaign CPL (127k) is worse than the control alone (70k), so the split is costing money. **Ask (replaces item 1 as the single live ask): pause ad set PEIKIRA2; budget flows back to the control.** The 11/10 read becomes a check of the post-pause effect.

## Decision rules (set now, so the read isn't biased by the result)
Target CPL Rp 95k. Five days at ~Rp 300k/day ≈ Rp 1.5M, ~15 leads at target.
- **PEIKIRA2 spent ≥ Rp 285k (3× target) with ≤ 1 lead** → propose: pause PEIKIRA2's ads with 0 leads and Rp ≥ 95k spend; spend returns to the control.
- **PEIKIRA2 7d-window CPL ≤ Rp 95k with ≥ 3 leads** → keep; propose pausing control ads with CTR collapse instead (old item 5) and give batch 01 v2 a slot.
- **In between (CPL 95–150k or < 3 leads)** → hold 3 more days, no new creative test.
- **Either way:** if the campaign CPL for the window is worse than the control alone, the split itself is costing money, so propose consolidating into the better ad set.
- Every proposal goes to OUTBOX as a one-line yes/no (stalled-asks rule). Fuku applies nothing.

## Caveats
- 1–5 leads per side is noise-level. Treat ±1 lead as a coin flip; lean on spend-per-lead thresholds above, not CTR.
- Placement item 1 (IG Stories) may be applied mid-window. If the activity log shows it, split the read at the change time.
