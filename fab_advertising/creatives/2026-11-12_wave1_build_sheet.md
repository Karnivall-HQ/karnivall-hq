# Fab Wave 1 build sheet: S1 · B1 · B2 (+ fallback S6 · S2), copy rows
_Fuku, 2026-11-12 15:02 WIB · cloud heartbeat (groundwork). Draft for Markus. Nothing is created in the ad account (propose-only)._
_Sources: `2026-11-06_batch01_v2_home_clutter_shotlist.md` (S1 stickers), `2026-11-05_creative_batch_01.md` (A1→S1 copy), `2026-11-10_creative_batch_02.md` (B1, B2), `2026-11-12_shoot_card_v2.md` (P-photos), `2026-11-12_wave1_price_wording_check.md` (price line). Claims re-checked against the live landing page `/sewa-gudang-self-storage-jakarta/` (curl 11/12 15:02, HTTP 200)._

## How to use
Build = `2026-11-11_wave1_launch_checklist.md` §C (inside PEIKIRA control ad set `120254051672430572`, budget unchanged, single image 9:16, placements as Ad015, pixel `405755485775053` / Lead). This sheet replaces "stickers + copy: see the 3 source docs" with rows you can paste.
If free pickup / no deposit are **not** confirmed (checklist §A), run **S1 + S6 + S2** instead: S6/S2 rows are in `2026-11-12_wave2_build_sheet.md` (same format).

## The 3 rows (paste-ready; `\n` = line break; 750 case)
| Code | Ad name | Photo | Stickers (top · middle · bottom, yellow on bottom) | Primary text (hook + body) | Headline |
|---|---|---|---|---|---|
| S1 | `WAVE1-FAB-<YYYYMMDD>-S1` | P1 (bedroom/apartment corner: koper + kardus + kipas) | `Kamar apartemen jadi gudang? 😣` · `Pindahin aja ke Gudang Fab` · `mulai 750rb/bulan 👇` | 😣 Kamar apartemen malah jadi gudang?\nSewa apartemen di Jakarta itu mahal. Sayang kalau satu kamar cuma buat numpuk barang.\n📦 Pindahkan barang yang jarang dipakai ke gudang self-storage Fab. Unit pribadi, bersih, terkunci.\n📍 ITC Kuningan Ambasador, Sudirman, Jakarta Selatan\n💰 Harga promo launching Rp750rb/bulan (kode FAB750 via WhatsApp). | Kamar Kembali Lega, Barang Tetap Aman |
| B1 | `WAVE1-FAB-<YYYYMMDD>-B1` | P2 (suitcases + boxes by the front door / hallway) | `Mau beresin barang tapi males angkut?` · `Tim Fab yang jemput 🚚` · `Gudang mulai 750rb/bln 👇` | 🚚 Gudang self-storage yang barangnya kami jemput sendiri.\nNggak perlu sewa pickup, nggak perlu angkat-angkat. Tunjuk barangnya, tim Fab yang bawa ke unit gudangmu.\n🔒 Unit pribadi, bersih, terkunci\n📍 ITC Kuningan Ambasador, Sudirman, Jakarta Selatan\n💰 Harga promo launching Rp750rb/bulan (kode FAB750 via WhatsApp). | Sewa Gudang Jakarta, Barang Dijemput Gratis |
| B2 | `WAVE1-FAB-<YYYYMMDD>-B2` | P1 (same photo as S1) | `Kamar penuh barang? 😩` · `Tanpa deposit, langsung dijemput` · `mulai 750rb/bulan 👇` | 📦 Sewa gudang self-storage tanpa deposit, barang dijemput gratis.\nBayar per bulan, tanpa uang jaminan. Barangmu kami jemput dari rumah dan disimpan di unit pribadi yang terkunci.\n📍 ITC Kuningan Ambasador, Sudirman, Jakarta Selatan\n💰 Harga promo launching Rp750rb/bulan (kode FAB750 via WhatsApp). | Tanpa Deposit, Barang Dijemput, Mulai Rp750rb |

URL for all 3: `https://fabwarehouses.com/sewa-gudang-self-storage-jakarta/?ad={{ad.name}}`

**If the price is 800:** change 3 places per row: bottom sticker, the 💰 line (→ `Mulai Rp800rb/bulan via WhatsApp.`, drop "promo launching" and the code), and the headline where it says Rp750rb (B2). S1/B1 headlines carry no price.
**If the WA team doesn't use FAB750:** drop ` (kode FAB750 via WhatsApp)` from the 💰 line.

## What changed vs the source docs (and why)
1. **B2 "Bayar bulan pertama aja" → "Bayar per bulan, tanpa uang jaminan".** The page backs per-month payment ("dibayar per 1 bulan" ×6) and no deposit ("Bisa tanpa uang deposit/ jaminan"), but never says the first month is the *only* upfront payment ("bulan pertama" 0, "biaya"/"admin" 0). If there is an admin fee, the old line becomes a broken promise in the WA chat.
2. **Location line → "ITC Kuningan Ambasador, Sudirman, Jakarta Selatan"** (was "Kuningan & Sudirman"). The page names **one** site ("akan launching di ITC Kuningan Ambasador Sudirman"); "Kuningan & Sudirman" can read as two branches. Same wording as the W1 site replacement, so ad and page match word for word once W1 lands. Wave 2 rows were swapped the same way on 11/12 18:02.
3. **Price line** already aligned 11/12 10:02 (site says "Harga Promo Launching"; 0× "FAB750").

## Page check (each ad's claims vs the live page, 11/12 15:02)
| Code | Claims used | On page | Note |
|---|---|---|---|
| S1 | apartemen, unit pribadi, bersih | ✔ "Apartemen" ×9, "Gudang Pribadi" ×15, "bersih" ×6 | reason-to-buy ✔ ("Penghuni Apartemen… barang menumpuk") |
| B1 | free pickup, no lifting | ✔ "Pickup" ×9 ("Gratis: Pickup barang dari rumahmu"), "Staff Bersama untuk bantu Loading" | "jemput"/"angkut" 0× on page: ad-copy verb only, no new claim |
| B2 | no deposit, per month, pickup | ✔ "Bisa tanpa uang deposit/ jaminan", "per 1 bulan" ×6, Pickup ×9 | first-month-only claim removed (change 1) |
| all | "terkunci" | ⚠️ 0× on page (page says "aman", "CCTV 1×24 jam") | **kept**: the live winner Ad015 already says "pintunya terkunci" (≈ 94% of control spend) and a private unit with a door is locked by nature *(INFERRED)*. If Alvian says units aren't individually locked, swap to "aman, CCTV 1×24 jam". |

Still on the page at 15:02: "Jakarta Pusat" ×9, "Rp 800" ×1 → W1/W2 not applied (gate G5).

## Gates (✅ before that ad runs)
| Ad | Gate | State 11/12 15:02 |
|---|---|---|
| all | Price 750 / 800 | ❓ Alvian |
| all | Site W1/W2 fixed | ❌ (launch anyway if needed; note "site not fixed") |
| B1, B2 | Free pickup | STATED on site, not confirmed |
| B2 | No deposit | STATED on site, not confirmed |
| B2 (`langsung dijemput`), WA M3 | G6: site open for goods/survey now? Page: "akan launching" | ❓ Alvian (added 19:02); if not open, sticker → `Tanpa deposit, barang dijemput gratis` |

## Read rules
Fixed before launch: checklist §E + `../reports/wave1_read_template.md`. Hand back in INBOX: `Wave 1 live <date time>, ads S1/B1/B2, price <750|800>, site fixed <yes|no>, dead ads paused <yes|no>`.

## Labels
- Account data: IDs, Ad015 share and its "terkunci" copy, Reels cheapest placement.
- STATED (site curl 11/12 15:02): pickup, no deposit, per-month, single location ITC Kuningan Ambasador.
- INFERRED: units are individually locked; "Kuningan & Sudirman" reads as two sites to some users.
