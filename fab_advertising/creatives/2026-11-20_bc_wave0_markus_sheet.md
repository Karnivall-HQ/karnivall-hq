# BC Wave 0: cap ladder + N2 carousel, one page for Markus
_Fuku, 2026-11-20 11:01 WIB · cloud heartbeat groundwork · read-only pulls (account `484578521394893`). Propose-only: Fuku creates/edits nothing in the ad account. Markus builds (Ads Manager or Rudi MCP), Alvian approves._
_Merges `../reports/2026-11-20_bc_cap_ladder_card.md` (ladder) + `2026-11-20_bc_angle_scan_brief.md` (N2). This is the **BC variant header** for all later wave build sheets: from here, new creative waves go into their **own BC ad sets** (criterion-2 replan branch C), not into PEIKIRA. If a source and this page disagree, this page is newer; the sources keep the reasoning._
_Status: **held, not asked** (stalled-ask rule). Becomes the single swap-in ask at the 11/23 weekly if OUTBOX #2/#3 are still stalled: **"Build N2 in BC + apply the cap ladder?"**_

## 0. Before building (Fuku re-checks at ask time, Markus re-checks at build time)
| # | Check | If it fails |
|---|---|---|
| C1 | BC campaign activity log has no edits since 11/12 (11/20 08:02: empty) | someone touched BC → Fuku re-bases before anything (playbook §D) |
| C2 | The 4 ladder ad sets still at Rp 94,250 | already changed → skip that row in §1 |
| C3 | Landing page still says "Harga Promo Launching Rp750.000/bulan" (11/20 11:01 curl: "Promo Launching" ×10, "800" ×1 FAQ) | page moved to 800 → swap card 5 + body to "mulai Rp800rb/bulan" |
| C4 | Ladder table re-pulled on the latest 7d (CPL ÷ cap still < 0.85 per ad set) | an ad set fails → drop that row only |

## 1. Cap ladder (4 fields, ~3 min) · campaign BC CBObass005 `120236222888610572`
Ads Manager → each ad set → Bid control → `105000` → Publish. Budget untouched (CBO Rp 5M, it doesn't bind: 1.94% used).

| # | Ad set | ID | Now → new |
|---|---|---|---|
| 1 | BCbatch201 Manny5 Bid94 JKTcity NoExcl | `120245708232080572` | 94,250 → **105,000** |
| 2 | BC204 Manny6 Slide APT Bid94 JKTcity NoExcl | `120246071060620572` | 94,250 → **105,000** |
| 3 | BC208 UGC JKTcity NoExcl | `120247180846830572` | 94,250 → **105,000** |
| 4 | BC3-21 Anak Tele JKTcity – Copy 10 | `120250479689810572` | 94,250 → **105,000** |

## 2. N2 carousel: new ad set + 1 ad

### 2a. Ad set = duplicate `BC208 UGC JKTcity NoExcl` (`120247180846830572`), then change only name + bid
Settings verified 11/20 11:01 (account data; all 4 ladder ad sets are identical):
| Field | Value |
|---|---|
| Name | `BC-W0-N2 Labirin Carousel JKTcity NoExcl` |
| Campaign | BC CBObass005 `120236222888610572` (CBO, no ad-set budget) |
| Performance goal | Conversions (`OFFSITE_CONVERSIONS`), pixel `405755485775053`, event **Lead** |
| Bid control | **Rp 94,250** (BC standard; keep it, so N2 is read on the same terms as its parent 204F) |
| Billing | Impressions |
| Attribution | 7-day click, 1-day view, 1-day engaged view |
| Location | Jakarta (city key 962899), people living in or recently there |
| Age | 18–65, Advantage+ audience on (age/gender may expand, geo locked) |
| Placements | Advantage+ (FB, IG, Messenger, Threads; as the parent) |
| Ads | **Delete the duplicated BC Image 208 ad** inside the copy. Only N2 in this ad set (ladder data: extra ads in a set get ≈ Rp 0). |

### 2b. Ad `BC-W0-N2-<YYYYMMDD>`: carousel, 5 cards
Identity (from 204F's creative `2022641311963133`, account data): Facebook Page `321292677733040` · Instagram `17841466480733343` · CTA **Learn more** · every card link + website URL:
`https://fabwarehouses.com/sewa-gudang-self-storage-jakarta/?ad={{ad.name}}`

Images are **already in the account** (reuse by hash; no upload, no new photos):
| Card | Image (source) | Image hash | Overlay text (burn in or as card headline) |
|---|---|---|---|
| 1 | BC208 clutter photo (creative `980979054320303`) | `55399a85bf180fa15460c3fa5232af05` | Kamar di rumah udah kayak labirin? 🤯 |
| 2 | 204F card 1, corridor | `3f7de728e05076a64b6d631ddbf15022` | Pindahkan barangnya ke Gudang Self-storage Fab ➡️ |
| 3 | 204F card 2, B16 | `91424e948d9a5c4675abbb473d79e626` | Muat barang besar: lemari, kulkas, sofa, tempat tidur, sepeda 💪 |
| 4 | 204F card 3, stools | `f4d9bd9e47279ab95b46ac9a65aa3cd8` | Bersih, aman, CCTV · Jakarta Selatan (Sudirman) |
| 5 | 204F card 5, C14/C15 | `6e4427de9624e73c31adaf0b2e924838` | Harga Promo Launching Rp750rb/bulan 👇 |

(204F card 4 `417149d2116e51af6515a674f0d3e38d` is not used; the brief picked cards 1, 2, 3, 5.)
If burning text into the images is not possible today: put the overlay line as each card's **headline** and leave the description empty. Note in the handback which one you did.

**Primary text** (paste as is):
```
Kamar jadi gudang? 🤯
Simpan barang-barang menumpuk dari apartemen, rumah, atau kantor di Gudang Self-storage Fab, Jakarta Selatan (Sudirman).
📦 Muat barang besar: lemari, kulkas, sofa, tempat tidur, sepeda.
🔒 Bersih, aman, CCTV.
🚚 Barangmu bisa kami pickup juga.
💰 Harga Promo Launching: Rp750rb/bulan.
```
**Headline (carousel-level / end card):** `Sewa Gudang Self Storage Jakarta (Promo: Rp750.000 /bulan)` — same as 201D's live headline.

**Advantage+ creative:** turn **off** `carousel_to_video` and `media_order` (204F has both on). *INFERRED:* the test is the card order "clutter → facility → price"; a reorder or a video conversion breaks that story. `profile_card` may stay.

Don't copy from the parents: "dari 800rb" (all 3 parent bodies; page says Promo Launching 750), "link ada di bio" (204F, 208: wrong for a link ad), BC208's headline "dari Rp800.000".

### Page check (curl 2026-11-20 11:01, tags/scripts stripped; `ad-copy-page-check.md`)
| Claim in N2 | Page | Verdict |
|---|---|---|
| Harga Promo Launching Rp750rb/bulan | "Promo Launching" ×10 | ✔ |
| Jakarta Selatan (Sudirman) | Sudirman ×9, Jakarta Selatan ×2 | ✔ (page also says Jakarta Pusat ×9 = site bug W1, not copied) |
| lemari / kulkas / sofa / tempat tidur / sepeda | 3 / 3 / 2 / 2 / 3 | ✔ |
| bersih / CCTV / pickup | 6 / 6 / 9 | ✔ |
| "labirin" (hook) | 0 | ⚠️ hook word only, backed by BC208 live ad data (Rp 363,096 / 6, 60.5k) → keep, INFERRED |
| Kuningan, "datang & lihat sendiri", "siap hari ini" | not used | page says "akan launching" ×1 → deliberately left out |

## 2c. N3 · 201D refresh with the apartment hook (build only on the N2 winner trigger, §4)
_Added 2026-11-20 13:02. Creatives re-read today (account data): 201D = creative `965339026357938`, 208 = `980979054320303`; both use Page `321292677733040`, IG `17841466480733343`, CTA Learn more, same landing page._

**Ad set:** §2a exactly (duplicate BC208 `120247180846830572`, delete the copied ad, cap 94,250), name `BC-W0-N3 201D Apartemen JKTcity NoExcl`.
**Ad** `BC-W0-N3-<YYYYMMDD>`: single image, **201D's image by hash `1bf532b9a01eeda4334da99ef6bf3005`** (unit row photo; its burned-in price already says "(Harga Promo) 750rb/bulan", so no edit). Link `https://fabwarehouses.com/sewa-gudang-self-storage-jakarta/?ad={{ad.name}}`.

**Primary text** (paste as is):
```
Apartemen malah jadi gudang? 😣
Sayang kalau kamar cuma dipakai buat simpan barang.
Gudang Self-storage Fab di Jakarta Selatan (Sudirman):
📦 Muat barang besar: lemari, kulkas, sofa, tempat tidur, sepeda.
🔒 Bersih, aman, CCTV.
🚚 Barangmu bisa kami pickup juga.
💰 Harga Promo Launching: Rp750rb/bulan.
```
**Headline:** `Sewa Gudang Self Storage Jakarta (Promo: Rp750.000 /bulan)` (= 201D's live headline).
**Advantage+ creative:** keep **the same as 201D** (image_animation, product_extensions, reveal_details_over_time, cv_transformation on). *INFERRED:* N3 is read against 201D, so the only difference should be the body (201D says "hanya dari 800rb" ×1 and "mulai dari Rp 800rb" ×1; N3 says the page's Promo Launching 750).
- Change vs the 10:01 brief: dropped "kamar yang **mahal**" (page 0×, an unbacked value claim) → "Sayang kalau kamar cuma dipakai buat simpan barang" (kamar 5× on page).

## 2d. N1 · Parents' hook on BC208's real photo (rank last; build after N3, or with N3 if the site gets a family line)
**Ad set:** §2a, name `BC-W0-N1 Ortu RealPhoto JKTcity NoExcl`.
**Ad** `BC-W0-N1-<YYYYMMDD>`: single image, **BC208's photo by hash `55399a85bf180fa15460c3fa5232af05`** (real photo: room packed with boxes, toys, stroller).
- **Default (no new upload): hook in text only.** The 208 image's own stickers say "Kamar di rumah udah kayak labirin?", which is fine with this body. 
- *Optional:* burn 3-21's line onto a clean copy of the 208 photo = a **new image upload** (Markus has the original). Only if it's quick; note it in the handback.

**Primary text** (paste as is):
```
Semua orang tua di Jakarta tahu rasanya: rumah penuh, tapi tidak ada yang mau dibuang… 😅
Ada solusinya: Gudang Self-storage Fab, Jakarta Selatan (Sudirman).
📦 Muat stroller, sepeda, lemari, kotak-kotak barang.
🔒 Bersih, aman, CCTV.
🚚 Barangmu bisa kami pickup juga.
💰 Harga Promo Launching: Rp750rb/bulan.
```
**Headline:** `Rumah penuh barang? Gudang Self-storage Fab (Promo Rp750rb/bulan)`
**Advantage+ creative:** same as BC208 (all 4 on), so N1 vs 3-21 differs in image (real vs staged), not in settings.
Don't copy from 208: "hanya dari 800rb" ×2, headline "dari Rp800.000", "(link ada di bio)", the hashtags.

### Page check N3 + N1 (curl 2026-11-20 13:02, scripts/styles/tags stripped)
| Claim | Page | Verdict |
|---|---|---|
| Harga Promo Launching Rp750rb/bulan | "promo launching" ×10, 750 ×9 (800 ×1 FAQ) | ✔ |
| Jakarta Selatan (Sudirman) | 2 / 9 | ✔ (Jakarta Pusat ×9 still on the page = W1 site bug, not copied) |
| apartemen / kamar | 9 / 5 | ✔ N3 hook backed |
| lemari / kulkas / sofa / tempat tidur / sepeda | 3 / 3 / 2 / 2 / 3 | ✔ |
| bersih / aman / CCTV / pickup | 6 / 14 / 6 / 9 | ✔ |
| stroller / mainan | 0 / 0 | ⚠️ physical fact (a stroller is in the 208 photo, units fit bikes and wardrobes) → keep, INFERRED |
| orang tua / anak / keluarga | 0 / 0 / 0 | ⚠️ message-match risk → N1 stays rank last; fix = one FAQ line "untuk keluarga dengan anak kecil" with W1/W2 |
| mahal | 0 | ❌ removed from N3 |
| Kuningan, "datang & lihat sendiri", "siap hari ini" | not used | page "akan launching" ×1 → left out |

**Read rules N3 / N1:** same as N2 in §4 (kill, starvation), but the day-14 comparative parent is **201D** for N3 and **BC Image 3-21** for N1 (keep if CPL ≤ parent × 1.15 or ≤ 70k, same window).

## 2e. Wave 1 (S1 / B1 / B2) as BC rows: build on the photo drop, zero re-assembly
_Added 2026-11-20 14:02. Source: `2026-11-12_wave1_markus_onepager.md` (gates G1–G6, photos P1/P2, stickers stand). This section replaces its §2–§3 "where/how" while the PEIKIRA caps hold; its copy was re-checked against the page today and **5 lines changed** (table below)._
**Needs:** the new phone photos P1 (apartment/bedroom corner) + P2 (suitcases + boxes by the door) from `2026-11-06_batch01_v2_home_clutter_shotlist.md`, stickers burned in (9:16). This is the only wave that needs a **new upload**.

**3 ad sets, each = §2a** (duplicate BC208 `120247180846830572`, delete the copied ad, cap Rp 94,250), one ad each:
| Ad set | Ad | Photo | Stickers (top · middle · bottom) | Headline |
|---|---|---|---|---|
| `BC-W1-S1 Apartemen P1 JKTcity NoExcl` | `BC-W1-S1-<YYYYMMDD>` | P1 | `Kamar apartemen jadi gudang? 😣` · `Pindahin aja ke Gudang Fab` · `mulai 750rb/bulan 👇` | Kamar Kembali Lega, Barang Tetap Aman |
| `BC-W1-B1 Pickup P2 JKTcity NoExcl` | `BC-W1-B1-<YYYYMMDD>` | P2 | `Mau beresin barang tapi males angkut?` · `Tim Fab yang pickup 🚚` · `Gudang mulai 750rb/bln 👇` | Sewa Gudang Jakarta, Pickup Barang Gratis |
| `BC-W1-B2 TanpaDeposit P1 JKTcity NoExcl` | `BC-W1-B2-<YYYYMMDD>` | P1 | `Kamar penuh barang? 😩` · `Bisa tanpa deposit, pickup gratis` · `mulai 750rb/bulan 👇` | Bisa Tanpa Deposit, Pickup Gratis, Mulai Rp750rb |

Identity = BC parent, not Ad015 (*INFERRED:* the read is against BC ads on the same Page): Page `321292677733040` · IG `17841466480733343` · CTA **Learn more** · link `https://fabwarehouses.com/sewa-gudang-self-storage-jakarta/?ad={{ad.name}}`.
**Advantage+ creative:** as BC208 except **`cv_transformation` off** and `image_text_translation` off if shown (the stickers are the copy; a crop/re-render or a translation would change the test, INFERRED, same reason as the 11/12 onepager).

**Primary text** (paste as is):

S1
```
😣 Kamar apartemen malah jadi gudang?
Sayang kalau satu kamar cuma buat numpuk barang.
📦 Pindahkan barang yang jarang dipakai ke gudang pribadi di Fab Self-storage. Private & tertutup, bersih, aman, CCTV.
📍 Sudirman, Jakarta Selatan
💰 Harga Promo Launching Rp750rb/bulan.
```
B1
```
🚚 Gudang self-storage yang barangnya bisa kami pickup gratis.
Nggak perlu sewa mobil, nggak perlu repot. Tim Fab pickup barang dari apartemen, rumah, atau kantormu, dan staff kami bantu loading.
🔒 Gudang pribadi, private & tertutup, CCTV
📍 Sudirman, Jakarta Selatan
💰 Harga Promo Launching Rp750rb/bulan.
```
B2
```
📦 Sewa gudang self-storage, bisa tanpa deposit, pickup barang gratis.
Bayar per 1 bulan, tanpa ikatan minimal lama sewa. Barangmu kami pickup dari rumah dan disimpan di gudang pribadi yang private & tertutup.
📍 Sudirman, Jakarta Selatan
💰 Harga Promo Launching Rp750rb/bulan.
```

### Changes vs the 11/12 copy (page curl 2026-11-20 14:02, scripts/styles/tags stripped)
| 11/12 line | Page count | Change |
|---|---|---|
| "Sewa apartemen di Jakarta itu **mahal**" (S1) | mahal 0 | ❌ dropped (same call as N3) |
| "(**kode FAB750** via WhatsApp)" (all 3) | FAB750 0, kode 0 | ❌ dropped (G2 never answered; page offers "Promo Launching" with no code) |
| "📍 **ITC Kuningan Ambasador**, Sudirman" (all 3) | 1×, inside "saat ini Fab **akan launching** di ITC Kuningan Ambasador" | → "Sudirman, Jakarta Selatan" (Sudirman 9, Jakarta Selatan 2); G6 stays open in parked OUTBOX |
| "**terkunci**", "**unit** pribadi" | terkunci 0, unit pribadi 0 | → "gudang pribadi, private & tertutup" (pribadi 15) |
| "**dijemput / jemput**", "angkat-angkat" | jemput 0, angkat 0 | → "pickup gratis" (gratis 7, all "Gratis: pickup barang dari tempatmu") + "staff bantu loading" |
| "**Tanpa deposit**" (B2) | tanpa deposit 0; comparison table: Fab "bisa tanpa uang deposit/jaminan" | → "**bisa** tanpa deposit" (STATED, hedged as the page is); G4 still asks if it's always true |

Kept as backed: apartemen 9, kamar 5, bersih 6, aman 14, CCTV 6, "per 1 bulan" + "tanpa ikatan minimal lama sewa" ✔, Promo Launching ×10 / 750 ×9 (800 ×1 FAQ = W2 site bug).

**Gates (from the onepager §1, re-mapped):** G1 price → C3 above. G2 → gone (no code). G3/G4 pickup + deposit: page-backed now (STATED), so B1/B2 no longer wait on Alvian; a "no" from him still swaps in S6/S2 (`2026-11-12_wave2_build_sheet.md`). G5 site: launch anyway. G6: not needed (no Kuningan line).
**Read rules:** §4 N2 rules per ad set; day-14 comparative parent = **BC208** (same home-clutter angle, real photo): keep if CPL ≤ BC208 × 1.15 or ≤ 70k, same window. Handback: `BC W1 done <date time>: S1/B1/B2 ad set IDs <…>, stickers burned <yes|no>, cv_transformation off <yes|no>`.

## 3. Handback (one line in `fuku/INBOX.md`)
`BC W0 done <date time>: ladder <4/4 | which>, N2 ad set <ID>, overlays <burned | headlines>, enhancements off <yes|no>`

## 4. Read rules (fixed now, from the two source cards)
- **Day 1:** split at the edit time (playbook §D3); read on full days at the 07:00 readout.
- **Ladder kill, per ad set:** back to 94,250 at ≥ Rp 190k with 0 leads, or ≥ Rp 285k with ≤ 1 lead. **Comparative:** revert all 4 if group 7d CPL > 1.3× the rest of BC **and** > 95k. **Day 7:** keep if group ≤ 95k on ≥ Rp 285k; spend < Rp 285k = cap wasn't the limiter → close the lever.
- **N2 kill:** pause at ≥ Rp 190k / 0 leads or ≥ Rp 285k / ≤ 1 lead. **Starvation:** < Rp 50k in 7 days = cap-limited, no creative verdict. **Day 14 comparative:** keep if CPL ≤ 204F × 1.15 or ≤ 70k, same window. **Winner (criterion 2):** ≥ Rp 285k in 7 days at ≤ 70k → N3 (§2c) then N1 (§2d), rows ready since 11/20 13:02.
- **Account guard:** Fab 7d CPL > 95k with the ladder group or N2 as the cause → revert the cause only.

## 5. Template for later BC waves (N3, N1, Wave 1–6 photos)
Each new concept = §2a (duplicate BC208, rename `BC-W<n>-<code> … JKTcity NoExcl`, delete the copied ad, cap 94,250) + §2b (one ad, page check, enhancements off, `?ad={{ad.name}}`). Older PEIKIRA-targeted build sheets (`2026-11-12_wave*_build_sheet.md`, `2026-11-13_wave5-6_build_sheet.md`) keep their copy; only their "where" line changes to this header while the PEIKIRA caps hold.

## Labels
- Account data: all IDs, ad-set settings, creative identity, image hashes, enhancements, parent copy.
- STATED (site): page counts above.
- INFERRED: enhancements-off, one-ad-per-ad-set, "labirin" keep, cap choice for N2.
