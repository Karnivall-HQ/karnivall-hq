# Fab pixel funnel baseline (before W1/W2) — pulled 2026-11-06 14:02 WIB

Dataset 405755485775053, `ads_get_dataset_stats` aggregation=event_total_counts. Counts are browser + server summed (each event arrives ~twice; ÷2 ≈ unique, INFERRED from the Lead source split). URL breakdown strips paths, so this is site-wide.

| Window (UTC 07:02 → 07:02) | PageView | ViewContent | Form | Lead | VC→Form *(calc)* | Form→Lead *(calc)* | VC→Lead *(calc)* |
|---|---|---|---|---|---|---|---|
| 10/23 → 10/30 (prior wk) | 1,728 | 1,376 | 59 | 41 | 4.3% | 69% | 3.0% |
| 10/30 → 11/06 (baseline) | 2,187 | 1,642 | 105 | 63 | 6.4% | 60% | 3.8% |

## Read (account data + INFERRED)
- Post-click conversion **improved** wk/wk (VC→Lead 3.0% → 3.8%) while Meta 7d CPL rose (113k → 125k). So the CPL drift this week is **upstream (cost per landing-page view / delivery mix)**, not a worsening site. INFERRED; the site is still the cheapest lever (3.8% is low), but don't blame the recent drift on it.
- Form→Lead fell 69% → 60%: more form submits are not firing Lead. Supports W4 (how Lead fires; uncalled Fluent Form entries).
- Site check 14:02 WIB: `/sewa-gudang-self-storage-jakarta/` still contains "Kelapa Gading" ×2 and "Jakarta Pusat" ×9 → W1 not applied.

## After W1/W2 go live
Re-pull the same call for the 7d after the edit date; compare VC→Form and VC→Lead against the **baseline row**. Success = VC→Lead ≥ 4.5% (≈ −15% CPL at same LP cost, calc). Small samples: ±1pt is noise below ~1,500 VC.
