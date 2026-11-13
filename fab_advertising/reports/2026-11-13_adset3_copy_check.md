# ADSET-3 copy check: 6 live ads vs the landing page
_2026-11-13 08:01 WIB, Fuku (cloud). Playbook: `fuku/memory/playbooks/ad-copy-page-check.md`. Propose-only: nothing here is applied by Fuku._

**Bottom line:** no ad needs pulling. The copy is clean on price (750) and close to the page. The gaps are **on the page**, not in the ads: 3 claims the ads make that the page never states (access hours, own key, pickup cap), and one page line that now **contradicts** the ads ("akan launching" vs "ini penampakan aslinya… datang dan lihat sendiri"). No new ask: these fold into W1/W2 + the photos question.

## Sources
- Ad text: `primaryText` from the Meta ad previews (Instagram Feed) for all 6 ads. The API `body` field is empty for the 5 multi-image creatives; the preview iframe carries the real text. Headline empty on all 6. (account data)
- Page: curl `https://fabwarehouses.com/sewa-gudang-self-storage-jakarta/` at 08:0x, scripts/styles stripped, counts lower-cased. (STATED, site)
- ⚠️ Destination URL of the new ads is **not exposed** by the preview or creative API. I assume the same page as every other PEIKIRA ad (11/11 destination check: 13 ads = 88% of spend). INFERRED; confirm in Ads Manager if needed.

## The 6 hooks
| Ad | Hook (opening line) | Body claims |
|---|---|---|
| S30 v04 | "Kalo barangmu butuh tempat sendiri, ada Gudang Fab." | own key ("kunci pegang sendiri"), 750, pickup ≤150k, Jaksel (Kuningan and Sudirman) |
| 003 | "Bingung gudang ukuran apa yang cukup? Lihat denahnya dulu." | Small/Medium/Large with scale picture, 750, pickup ≤150k, Jaksel |
| 007 | "Barang 'numpang' di rumah orang tua sudah berapa tahun?" | 750, pickup ≤150k, Jaksel |
| 010 v03 | "Barangmu, kuncimu sendiri." | solid panel unit, CCTV, **come any day 07.00–19.00**, 750, Jaksel |
| 018 | "Ini penampakan aslinya, bukan gambar render." | solid panel, own key, clean corridor, CCTV + building security, **"datang dan lihat sendiri"**, 750, pickup ≤150k, Jaksel |
| 016 (AKIRA) | "Gudang Self-storage Jakarta: gudang pribadi…" | apartment/office/home, **office space for employees**, **renovation / furniture**, Kuningan & Sudirman, pickup 1× ≤ Rp150rb, 750 |

## Page check
| Claim | Ads | Page count | Verdict |
|---|---|---|---|
| Rp750rb/bulan | all 6 | "750" ×9, "Rp 800.000" ×1 (FAQ) | ✔ (W2 removes the last 800) |
| Jakarta Selatan | 5 of 6 | "Jakarta Selatan" ×2, **"Jakarta Pusat" ×9** | ❌ page side → **W1** (already asked) |
| "Kuningan and/& Sudirman" | all 6 | Kuningan ×1, Sudirman ×9; page names one site (ITC Kuningan Ambasador, Sudirman) | ⚠️ reads as 2 sites; low risk, no change asked |
| Gratis pickup 1× hingga Rp150.000 | 5 of 6 | "Gratis: Pickup barang" (pickup ×9), "150.000"/"150rb" ×0 | ⚠️ ad is narrower than page; fine for the ad, but a lead may meet a cap the page never mentioned → page line suggested below |
| CCTV / building security | 010, 018 | CCTV ×6, keamanan ×5, "24 jam" ×10 | ✔ |
| Own key ("kunci pegang sendiri", "kuncimu sendiri") | S30, 010, 018 | "kunci" ×0, "pribadi" ×15, "private & tertutup" | ⚠️ INFERRED physical fact (private unit); page never says you hold the key |
| Solid panel unit, clean corridor | 010, 018 | "panel" ×0, "koridor" ×0 | ⚠️ backed by the photos themselves (INFERRED) |
| **Access every day 07.00–19.00** | 010 | "07.00"/"19.00"/"setiap hari"/"akses"/"buka" ×0; page only has "CCTV 1×24 jam", "security 1×24 jam" | ⚠️ the one hard operating fact the page never states. "24 jam" ×10 on the page could be read as 24h access → a lead may expect 24h. Needs a page line |
| Small/Medium/Large with scale picture | 003 | Small/Medium/Large unit images present (3 PNGs), sizes 3.8 m³ etc. | ✔ |
| **"Ini penampakan aslinya… datang dan lihat sendiri"** | 018 (010: "bisa datang setiap hari") | FAQ: "Fab Self Storage **akan launching** di ITC Kuningan Ambasador" ×1; steps: "Datang survey" ×1 | ❌ **page contradicts ad**: the ad says the site is real and visitable now; the FAQ says it will launch. This is open gate G6 |
| Office "ruang kosong untuk karyawan" | 016 | kantor ×14, karyawan ×0 | ✔ office angle on page; "employees" wording only in ad, low risk |
| Renovation / furniture | 016 | renovasi ×0, furniture ×0 | ⚠️ situation unsupported on page (lesson 11/12); 016 lists it as 1 of 4 bullets, low risk |
| "Rumah orang tua" / "numpang" | 007 | ×0 / ×0; rumah many | ⚠️ angle only, no factual claim; fine |

## Meta site links (FYI)
The previews show Meta-suggested site links: the WA form, About Us and the **homepage** (whose form sells the Rp 5jt warehouse+coworking product, 11/11 check). `site_links_opt_in: false` on all 6 → INFERRED not shown. No action.

## Proposed page lines (for whoever applies W1/W2; not ad changes)
Use the page's own wording; each needs the fact confirmed by Alvian/Markus first (they wrote it into the ads, so they likely know).
- **P1 (G6, only if the site is open now):** FAQ "Saat ini Fab Self Storage akan launching di ITC Kuningan Ambasador Sudirman, Jakarta Selatan." → "Fab Self Storage sudah buka di ITC Kuningan Ambasador Sudirman, Jakarta Selatan."
- **P2 (access hours, if 07.00–19.00 is true):** after "Gudang yang aman, dgn CCTV 1x24 jam." add "Jam akses gudang: setiap hari 07.00–19.00."
- **P3 (pickup cap):** "Gratis: Pickup barang dari tempat-mu." → "Gratis: Pickup barang 1x dari tempat-mu (hingga Rp150.000)."

## Ads: proposed changes for Markus
- **None now.** The ads are consistent with each other and with the team's chosen facts. Only revisit 010's hours line if the 07.00–19.00 fact is wrong.
- Delivery note: all 6 ads at **Rp 0 / 0 impressions** at 08:0x, ~4h after ACTIVE (04:05). Normal for a new ad set early morning; 13:00 poll checks again, and if still 0 then, check review/delivery status.
