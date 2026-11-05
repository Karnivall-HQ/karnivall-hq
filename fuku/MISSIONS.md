# Missions

> **Alvian:** add missions here (or run `/mission <goal>` in Claude Code). Give each one a goal, success criteria, priority, and deadline if any.
> **Fuku** owns the strategy, keeps the Status/Progress lines current, and moves finished missions to "Completed".

## Active

<!-- Template:
### M-001 · <Mission name>
- **Goal:** what outcome you want
- **Success criteria:** how we know it's done (measurable)
- **Priority:** P0 (now) / P1 (this week) / P2 (whenever)
- **Deadline:** YYYY-MM-DD or none
- **Constraints:** budget, brand, no-gos
- **Status:** not started | in progress | blocked | done   ← Fuku
- **Strategy:** ← Fuku's current approach
- **Progress:** ← Fuku's latest update (dated)
-->

### M-001 · Fab ad account: cut CPL and scale to Rp 1M/day
- **Goal:** Make the Fab ad account (Meta "Warehouse Storage" `484578521394893`, The North Case Indonesia) profitable at scale: cheaper leads, then more spend.
- **Success criteria (both must hold):**
  1. 7-day average CPL ≤ **Rp 95,000** (baseline 2026-11-05: ~Rp 133k blended, last 30d).
  2. The account sustainably spends **Rp 1,000,000/day** with a 7-day average CPL of around Rp 95k (baseline: ~Rp 411k/day).
- **Priority:** P0
- **Deadline:** 2026-12-05 (30 days from 2026-11-05)
- **Constraints:** **Propose-only.** Fuku never touches the ad account (no pauses, budget changes, or launches). Every change is proposed to Alvian as an apply-ready checklist, and **Alvian applies it himself**. The metric is the 7-day average CPL, never a single day.
- **Status:** in progress (diagnosis ✅, waiting on Alvian to apply proposals)
- **Strategy (Fuku, 2026-11-05):**
  1. *Diagnose* (now): ad-set/ad/placement/audience breakdown; find which ads, audiences, and placements produce leads ≤ Rp 95k.
  2. *Cut waste*: propose to Alvian which CTR-collapsed FAB ads and losing ad sets to pause, so spend concentrates in the winners (BC CBObass005-type setups at ~Rp 83k).
  3. *Fix fatigue*: fresh creative batch (new angles/hooks) and a fresh or broader audience for the frequency-8 winner.
  4. *Scale*: propose budget raises of ~20–30% every 3–4 days, only while the 7d CPL ≤ Rp 95k. Alvian applies them. Fuku verifies the effect in the next readouts. Path: ~Rp 411k → 500k → 650k → 800k → 1M/day (≈ 10–11 leads/day at Rp 95k).
  5. Track daily in `fab_advertising/reports/m001_tracker.md` (spend, leads, 7d CPL).
- **Progress:**
  - 2026-11-05 20:02: Creative batch 01 drafted → `fab_advertising/creatives/2026-11-05_creative_batch_01.md` (6 ads, Indonesian copy). Basis: 14d ad-level data + Meta trend (6 PEIKIRA FAB ads CTR −40…−99%; Ad015 carries volume, 14 leads @ Rp 104.5k). [DECISION] in OUTBOX: launch A1/A2/A4 in the PEIKIRA ad set; 3 facts needed from Alvian.
  - 2026-11-05 19:09: Diagnosis done → `fab_advertising/reports/2026-11-05_m001_diagnosis.md`. 7d (10/29–11/04): Rp 355k/day, 22 leads, **CPL Rp 113k** (gate ≤95k closed). PEIKIRA (highest volume, Rp 300k/day) = volume @Rp 105k. BC CBO bid-cap = cheapest (Rp 60k CPL 10/19–28) but stalled to ~Rp 70k/day. 3 proposals sent to OUTBOX (consolidate BC ad sets, raise bid cap on 2 winners to Rp 105k, hold PEIKIRA). Tracker started: `m001_tracker.md`.
  - 2026-11-05: Rule: propose-only, Alvian executes all ad changes.
  - 2026-11-05: Mission set by Alvian. Baseline scan done (`fab_advertising/reports/2026-11-05_meta_account_scan.md`).

### M-002 · Weekly ads health report
- **Goal:** Every Monday, a concise health report across all Meta ad accounts so Alvian sees spend, CPL, fatigue, and problems at a glance.
- **Success criteria:** A report in `fab_advertising/reports/weekly/YYYY-MM-DD.md` every Monday by 09:00 WIB (spend, leads, CPL, 7d trend, fatigue flags, disabled/limited accounts, top 3 recommended actions), plus a one-line summary in OUTBOX.
- **Priority:** P1
- **Deadline:** ongoing; first report Monday 2026-11-09
- **Constraints:** read-only. Recommendations go to OUTBOX.
- **Status:** in progress
- **Strategy:** The cloud heartbeat runs it on the first Monday run (07:00 WIB). Turn it into a playbook after the first report.
- **Progress:**
  - 2026-11-05: Approved by Alvian.

## Completed
