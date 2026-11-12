# Wave 1 launch checklist for Markus (one screen)
_Fuku, 2026-11-11 20:02 WIB · cloud heartbeat groundwork. Propose-only: Fuku does not create, pause or edit anything in the ad account. Markus or Alvian applies every step below._
_Sources: `2026-11-10_shoot_day_card.md`, `../reports/wave1_read_template.md`, `../reports/2026-11-11_peikira_item5_revalidate.md`, `../reports/2026-11-11_ad_destination_check.md`._

**Goal:** when the photos arrive, launch in one sitting, with nothing left to decide.

## A. Gates (all ✅ before you press publish)
- [ ] **Price confirmed:** 750rb or 800rb → the same number on the last sticker of every ad. If 800: also swap it in the body price line + headline (3 places per ad). Body price wording matches the site since 11/12 ("Harga promo launching", `../reports/2026-11-12_wave1_price_wording_check.md`); drop "(kode FAB750 via WhatsApp)" if the WA team doesn't use the code.
- [ ] **Website W1/W2 fixed** on `/sewa-gudang-self-storage-jakarta/` (location → ITC Kuningan / Sudirman, Jakarta Selatan; price = the confirmed number). Every ad lands here (88% of 7d spend checked). If it isn't fixed, launch anyway, but write "site not fixed" in the launch note so the read isn't confused.
- [ ] **B1 needs free pickup ✅; B2 needs free pickup + no deposit ✅** (Alvian). If they're not confirmed, launch **S1 + S6 + S2** instead (price only).

## B. Tidy first (2 min, optional, ~0 CPL effect)
Pause the 5 known-dead ads in the control ad set `120254051672430572` (lifetime Rp 251,806 / 0 leads, 7d only Rp 18k):
`KENJI-FAB-20261019-001 · v03` · `PEIKIRA-FAB-20261023-Ad003` · `Ad004` · `Ad005` · `Ad008`.
Do **not** touch Ad015 (≈ 94% of the ad set, 7d CPL ≈ 99k) or PEIKIRA2.

## C. Build (3 new ads, nothing else changes)
| Setting | Value |
|---|---|
| Where | **Inside** the existing PEIKIRA control ad set `120254051672430572` (campaign `120254051672440572`). No new ad set, no budget change. |
| Ads | **S1** (photo P1) · **B1** (P2) · **B2** (P1). Paste rows (stickers, text, headline, name): **`2026-11-12_wave1_build_sheet.md`**. |
| Format | Single image, vertical 9:16 (Reels is the cheapest placement: 7d Rp 48k/lead *(calc)*). Placements: same as Ad015 (don't customise). |
| Destination URL | `https://fabwarehouses.com/sewa-gudang-self-storage-jakarta/?ad={{ad.name}}`, the same pattern as Ad015, so site visits can be traced to the ad. |
| Names | `WAVE1-FAB-<YYYYMMDD>-S1` / `-B1` / `-B2`, so Fuku can find them in the log. |
| Optimisation / pixel | Inherited from the ad set (pixel `405755485775053`, Lead). |

## D. After publish (send to Fuku via INBOX: one line)
`Wave 1 live <date time>, ads S1/B1/B2, price <750|800>, site fixed <yes|no>, dead ads paused <yes|no>`
Fuku fills the inputs table in `../reports/wave1_read_template.md` and reads it with no further work from you.

## E. Read rules (fixed before launch; Fuku proposes, you apply)
- **Day 2–3:** the new ads get < 10% of the ad set's spend → "starved". First fix: step B (if skipped). Never pause Ad015 to force delivery.
- **Day 3–5, per ad:** pause if spend ≥ Rp 95k + 0 leads + CTR < 1.0%; or spend ≥ Rp 190k + 0 leads.
- **Day 7 (up to 14):** pooled ≥ 3 leads at CPL ≤ Rp 95k → the format works → Wave 2. Pooled spend ≥ Rp 285k at CPL > Rp 142.5k → stop creative waves; the site is the lever.
- Any ad disapproved / "Update Required" → tell Alvian the same day.

## Labels
- Account data: ad set/campaign IDs, the 5 dead ads' spend, Ad015 share, destination URLs, Reels CPL.
- STATED (site, not confirmed by Alvian): free pickup, no deposit, no minimum.
- INFERRED: the naming scheme, the 10% starvation line, the early-kill CTR line.
