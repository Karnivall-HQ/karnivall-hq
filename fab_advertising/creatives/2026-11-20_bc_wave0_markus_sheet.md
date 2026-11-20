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

## 3. Handback (one line in `fuku/INBOX.md`)
`BC W0 done <date time>: ladder <4/4 | which>, N2 ad set <ID>, overlays <burned | headlines>, enhancements off <yes|no>`

## 4. Read rules (fixed now, from the two source cards)
- **Day 1:** split at the edit time (playbook §D3); read on full days at the 07:00 readout.
- **Ladder kill, per ad set:** back to 94,250 at ≥ Rp 190k with 0 leads, or ≥ Rp 285k with ≤ 1 lead. **Comparative:** revert all 4 if group 7d CPL > 1.3× the rest of BC **and** > 95k. **Day 7:** keep if group ≤ 95k on ≥ Rp 285k; spend < Rp 285k = cap wasn't the limiter → close the lever.
- **N2 kill:** pause at ≥ Rp 190k / 0 leads or ≥ Rp 285k / ≤ 1 lead. **Starvation:** < Rp 50k in 7 days = cap-limited, no creative verdict. **Day 14 comparative:** keep if CPL ≤ 204F × 1.15 or ≤ 70k, same window. **Winner (criterion 2):** ≥ Rp 285k in 7 days at ≤ 70k → N3 + N1 next, same template (§2a duplicate, §2b one ad).
- **Account guard:** Fab 7d CPL > 95k with the ladder group or N2 as the cause → revert the cause only.

## 5. Template for later BC waves (N3, N1, Wave 1–6 photos)
Each new concept = §2a (duplicate BC208, rename `BC-W<n>-<code> … JKTcity NoExcl`, delete the copied ad, cap 94,250) + §2b (one ad, page check, enhancements off, `?ad={{ad.name}}`). Older PEIKIRA-targeted build sheets (`2026-11-12_wave*_build_sheet.md`, `2026-11-13_wave5-6_build_sheet.md`) keep their copy; only their "where" line changes to this header while the PEIKIRA caps hold.

## Labels
- Account data: all IDs, ad-set settings, creative identity, image hashes, enhancements, parent copy.
- STATED (site): page counts above.
- INFERRED: enhancements-off, one-ad-per-ad-set, "labirin" keep, cap choice for N2.
