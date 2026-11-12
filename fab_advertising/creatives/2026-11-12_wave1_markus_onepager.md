# Wave 1 — one page for Markus (photo drop → launch, nothing to assemble)
_Fuku, 2026-11-12 20:02 WIB · cloud heartbeat groundwork. Propose-only: Fuku creates/edits nothing in the ad account. Markus builds (Ads Manager or Rudi MCP)._
_Merges `2026-11-11_wave1_launch_checklist.md` + `2026-11-12_wave1_build_sheet.md` + `../reports/wave1_read_template.md`. If they ever disagree, this page is newer (11/12 20:02); the sources keep the reasoning and page checks._

## 1. Gates (Alvian answers; ✅ all before publish)
| # | Gate | If NO / unknown |
|---|---|---|
| G1 | Price 750 or 800? | 800 → swap 3 places per ad (bottom sticker, 💰 line → `Mulai Rp800rb/bulan via WhatsApp.`, B2 headline) |
| G2 | WA team uses code FAB750? | drop ` (kode FAB750 via WhatsApp)` from the 💰 line |
| G3 | Free pickup real? (B1, B2) | launch **S1 + S6 + S2** instead (rows in `2026-11-12_wave2_build_sheet.md`) |
| G4 | No deposit real? (B2) | same as G3 |
| G5 | Site W1/W2 fixed? | launch anyway; write `site fixed no` in the handback |
| G6 | ITC Kuningan Ambasador open for goods now? (page: "akan launching") | B2 middle sticker → `Tanpa deposit, barang dijemput gratis` |

## 2. Optional tidy (2 min)
Pause in control ad set `120254051672430572`: `KENJI-FAB-20261019-001 · v03`, `PEIKIRA-FAB-20261023-Ad003`, `Ad004`, `Ad005`, `Ad008` (lifetime Rp 251,806 / 0 leads). **Never touch** Ad015 (`120254063163810572`) or PEIKIRA2.

## 3. Build: 3 ads, same settings as Ad015
**Where:** inside ad set `120254051672430572` (campaign `120254051672440572`). No new ad set, no budget/bid change.
**Copy from Ad015's creative `1718772653590165` (read 11/12 20:02, account data):** Facebook Page = same as Ad015 · Instagram account `17841466480733343` · CTA `SEE_DETAILS` (Lihat Detail) · single image (object_type SHARE) · placements as the ad set.
**URL (all 3):** `https://fabwarehouses.com/sewa-gudang-self-storage-jakarta/?ad={{ad.name}}`
**Format:** vertical 9:16 phone photo, stickers burned into the image (top · middle · bottom; bottom one yellow).

**⚠️ Advantage+ creative enhancements: turn OFF `image_text_translation` and `cv_transformation` on the 3 new ads** (Ad015 has both on, plus `image_animation`). *INFERRED:* the stickers are the copy (Indonesian) and the test is "raw phone photo vs polished"; machine translation of sticker text or a crop/re-render would mix those up. Leave `image_animation` as on Ad015. Don't change Ad015.

| Name | Photo | Stickers (top · middle · bottom) | Headline |
|---|---|---|---|
| `WAVE1-FAB-<YYYYMMDD>-S1` | P1 bedroom/apartment corner (koper + kardus + kipas) | `Kamar apartemen jadi gudang? 😣` · `Pindahin aja ke Gudang Fab` · `mulai 750rb/bulan 👇` | Kamar Kembali Lega, Barang Tetap Aman |
| `WAVE1-FAB-<YYYYMMDD>-B1` | P2 suitcases + boxes by the door | `Mau beresin barang tapi males angkut?` · `Tim Fab yang jemput 🚚` · `Gudang mulai 750rb/bln 👇` | Sewa Gudang Jakarta, Barang Dijemput Gratis |
| `WAVE1-FAB-<YYYYMMDD>-B2` | P1 (same as S1) | `Kamar penuh barang? 😩` · `Tanpa deposit, langsung dijemput` (G6!) · `mulai 750rb/bulan 👇` | Tanpa Deposit, Barang Dijemput, Mulai Rp750rb |

**Primary text** (paste as is; line breaks as shown):

S1
```
😣 Kamar apartemen malah jadi gudang?
Sewa apartemen di Jakarta itu mahal. Sayang kalau satu kamar cuma buat numpuk barang.
📦 Pindahkan barang yang jarang dipakai ke gudang self-storage Fab. Unit pribadi, bersih, terkunci.
📍 ITC Kuningan Ambasador, Sudirman, Jakarta Selatan
💰 Harga promo launching Rp750rb/bulan (kode FAB750 via WhatsApp).
```
B1
```
🚚 Gudang self-storage yang barangnya kami jemput sendiri.
Nggak perlu sewa pickup, nggak perlu angkat-angkat. Tunjuk barangnya, tim Fab yang bawa ke unit gudangmu.
🔒 Unit pribadi, bersih, terkunci
📍 ITC Kuningan Ambasador, Sudirman, Jakarta Selatan
💰 Harga promo launching Rp750rb/bulan (kode FAB750 via WhatsApp).
```
B2
```
📦 Sewa gudang self-storage tanpa deposit, barang dijemput gratis.
Bayar per bulan, tanpa uang jaminan. Barangmu kami jemput dari rumah dan disimpan di unit pribadi yang terkunci.
📍 ITC Kuningan Ambasador, Sudirman, Jakarta Selatan
💰 Harga promo launching Rp750rb/bulan (kode FAB750 via WhatsApp).
```

**Before publish, check:** 3 ads named `WAVE1-…`, all in the control ad set, URL has `?ad={{ad.name}}`, 2 enhancements off, ad set budget unchanged.

## 4. Handback (one line in `fuku/INBOX.md`)
`Wave 1 live <date time>, ads S1/B1/B2, price <750|800>, site fixed <yes|no>, dead ads paused <yes|no>, enhancements off <yes|no>`

## 5. Read rules (fixed now; Fuku proposes, Markus/Alvian applies)
- **Day 2–3:** new ads < 10% of ad-set spend = starved → first fix is §2 tidy. Never pause Ad015 to force delivery.
- **Day 3–5, per ad:** pause if spend ≥ Rp 95k + 0 leads + CTR < 1.0%, or spend ≥ Rp 190k + 0 leads.
- **Day 7:** pooled ≥ 3 leads at CPL ≤ Rp 95k → provisional KEEP (kills may fire; no scale step yet). Pooled ≥ Rp 285k at CPL > Rp 142.5k → stop creative waves; the site is the lever.
- **Day 14 (or ≥ Rp 1.4M pooled):** winner call → Wave 2 pick-3 (`2026-11-12_wave2_build_sheet.md`).
- Any disapproval / "Update Required" → tell Alvian the same day.

## Labels
- Account data: IDs, Ad015 creative settings (CTA, IG account, enhancements), dead-ad spend.
- STATED (site, not confirmed by Alvian): free pickup, no deposit, per month, one site "akan launching".
- INFERRED: enhancements-off recommendation, naming scheme, 10% starvation line, early-kill CTR line.
