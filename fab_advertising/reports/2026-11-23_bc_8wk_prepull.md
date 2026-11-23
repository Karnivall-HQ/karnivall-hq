# BC 8-week pre-pull (skeleton call 4a) — 2026-11-23 11:01 WIB
_Read-only. Fab 484578521394893, ad-set level, weekly rows 09/28–11/22 (8 weeks, pixel Lead, default attribution). Caps 94,250 on all 4 all 8 weeks (bid_amount read today), all ACTIVE._

| Ad set | 8-wk spend | Leads | CPL *(calc)* | CPL ÷ cap *(calc)* |
|---|---|---|---|---|
| BCbatch201 Manny5 `120245708232080572` | 623,508 | 11 | 56,683 | 0.60 |
| BC204 Manny6 `120246071060620572` | 345,735 | 7 | 49,391 | 0.52 |
| BC3-21 c10 `120250479689810572` | 593,217 | 8 | 74,152 | 0.79 |
| **W0 group (3)** | **1,562,460** | **26** | **60,095** | — |
| BC3-13 c2 `120250129960290572` | 321,360 | 2 | **160,680** | 1.70 |

Weekly rows (spend / leads), 09/28 → 11/16 week starts:
- 201: 161,721/2 · 188,458/6 · 15,464/0 · 76,743/0 · 26,526/0 · 26,997/0 · 48,386/1 · 79,213/2
- 204: 144,403/3 · 89,884/1 · 4,295/0 · 22,702/2 · 36,432/1 · 20,881/0 · 12,806/0 · 14,332/0
- 3-21: 275,794/3 · 130,154/0 · 10,566/0 · 46,532/0 · 69,066/2 · 17,437/1 · 19,632/0 · 24,036/2
- 3-13: 84,375/0 · 77,418/0 · 5,074/0 · 10,549/1 · 12,441/0 · 16,154/0 · 38,068/1 · 77,281/0

## Reads
- **Verify:** W0 group 60,095 = the 07:00 `bc_swapin_precheck.py` number in OUTBOX #1 ✓ (same window, independent pull).
- **R3 fires (pre-read):** BC3-13 c2 8-wk 160.7k > 120k line. Its last week (77,281 / 0) is its 3rd-largest week in 8 and 11.4% of BC 7d spend *(calc: 77,281 ÷ 677,675)*. Meta benchmark tool (own window): BC3-13 CPR 147,762 vs peer median 86,498 (STATED, tool); 3-21 30,910 and 201 70,261 beat the median.
- **Action:** per R3 + stage-less rule → a **pause line** in the 11/30 weekly Top 3 only (propose-only, no new OUTBOX ask while W0 is unapplied). Re-pull on 11/30 (window 10/05–11/29) before it's written: if 11/23–11/29 adds ≥ 1 lead at < 80k, re-check the line.
- Context (INFERRED): pausing 3-13 frees ≈ Rp 11k/day at the 94,250 cap — small; it's a tidy-up, not a volume lever. The W0 ask stays the lever.
