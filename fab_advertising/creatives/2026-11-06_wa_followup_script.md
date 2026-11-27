# Fab: WA follow-up script for "Form submitted, never chatted" (W4)
_2026-11-06 08:02 WIB · Fuku draft · NOT sent. Nothing goes out until Alvian approves and the Fab team sends it from the Fab WA number._

**Why:** 7d pixel shows 101 Form events vs 61 Lead events (~40% gap) [data, `2026-11-06_landing_page_audit.md`]. If Lead fires only when WhatsApp opens, the gap = people who left a name + WA number in Fluent Form #10 but never sent the chat. They raised a hand; a same-day reply is the cheapest lead Fab can get (no ad spend). [INFERRED until W4 confirms how Lead fires.]

**Facts used (only those already on the live site/ads):** "Harga Promo Launching" Rp750.000/bulan (the site's own wording; the site never mentions a code, the PEIKIRA ads say "kode FAB750") (⚠️ the WA form page + 1 FAQ line still say Rp800.000 = W2; confirm before sending) · ITC Kuningan Ambasador, Sudirman, Jakarta Selatan · no minimum rental, monthly payment, **can be** no deposit (page: "Bisa tanpa uang deposit/ jaminan"), free pickup · Small 3.8 m³ / Medium 7.6 m³ / Large 15.2 m³ (ad landing page, 11/12 curl; an older read said 4.75/9.5/19). ⚠️ Confirm all with Alvian before use.

## How to run it (for the Fab team)
1. Daily, export Fluent Form #10 entries from WP admin (Fluent Forms → Entries).
2. Match against the WA chat list. Anyone with no chat within 2 h of submitting → send Message 1.
3. No reply after 24 h → Message 2. No reply after 3 days → Message 3, then stop. Never more than 3 messages.
4. Only message people who submitted the form themselves (they gave the number to be contacted). Respect "stop".
5. Log: submitted → messaged → replied → survey → closed. This gives the close rate Fuku still needs.

## Messages (Bahasa Indonesia, casual-polite, short)
Placeholders: `{nama}`, `{kebutuhan}` (from the form's "Kebutuhan" field), `{ruangan}` ("Untuk merapikan ruangan dimana?").

**Message 1 (≤ 2 h after submit)**
> Halo Kak {nama}, ini Fab Self-storage 👋 Tadi Kakak isi form di website kami untuk {kebutuhan}. Mau kami bantu cek ukuran unit yang pas?
> Unit kami di ITC Kuningan Ambasador (Sudirman, Jaksel), lagi harga promo launching Rp750rb/bulan. Bisa tanpa deposit, tanpa minimal sewa, pickup gratis.
> Barangnya kira-kira apa aja, Kak? 😊

**Message 2 (+24 h, no reply)**
> Kak {nama}, biar gampang pilihnya: Small 3,8 m³ (± isi 1 kamar kos), Medium 7,6 m³, Large 15,2 m³. Mau kami kirim foto unitnya dulu?

**Message 3 (+3 days, last one)**
> Kak {nama}, kalau masih butuh tempat simpan barang, harga promo launching Rp750rb/bulan masih berlaku. Mau survei langsung ke gudang Fab di ITC Kuningan Ambasador minggu ini? Balas "survei" nanti kami atur jamnya. Kalau sudah tidak perlu, tidak apa-apa, terima kasih ya Kak 🙏

## Notes
- "± isi 1 kamar kos" is Fuku's sizing analogy [INFERRED], not a site claim. Have the team check it against real units, or drop it.
- **Price wording (2026-11-12 11:01):** Messages 1 and 3 now use the site's own phrase "harga promo launching Rp750rb/bulan" instead of "kode FAB750" (`fab_advertising/reports/2026-11-12_wave1_price_wording_check.md`). Reason: a form-filler arrives from the site, so the WA reply should echo the site. If a lead quotes "FAB750" from an ad, the team just confirms it (same 750 price). Message 3 no longer claims "slot" scarcity, which nothing on the site backs. If **800 is real**, change the number in Messages 1, 3 and Reply A.
- Message 2's "foto unit" ties in with the phone photo shoot (the same real photos double as ad creative).
- Measure: replies ÷ messaged and surveys ÷ messaged for 2 weeks. If reply rate < 10%, rewrite Message 1 (lead with the price, not the question).

## Page check (playbook `ad-copy-page-check.md`, 11/12 18:02, live `/sewa-gudang-self-storage-jakarta/`, HTTP 200)
| Claim in the script | On page | Verdict |
|---|---|---|
| harga promo launching Rp750rb/bulan (M1, M3) | ✔ "Harga Promo Launching: Rp750.000 /bulan" (750 ×9; "Rp 800" ×1 = W2) | ✔ STATED |
| ITC Kuningan Ambasador (Sudirman, Jaksel) (M1) | ✔ ×1: "**akan launching** di ITC Kuningan Ambasador Sudirman, Jakarta Selatan" | ⚠️ see gate below |
| tanpa deposit · tanpa minimal sewa · pickup gratis (M1) | ✔ deposit/jaminan ×2, "tanpa minimal lama sewa" ×8, "Gratis: Pickup barang dari tempat-mu" | ✔ STATED |
| Small 3,8 / Medium 7,6 / Large 15,2 m³ (M2) | ✔ each ×1 | ✔ STATED |
| "± isi 1 kamar kos" (M2) | ✗ 0 ("kos" hits are all "Kosong") | ⚠️ INFERRED, already flagged; team checks or drops |
| survei ke gudang (M3) | ✔ "Cara Sewa: 01 Chat via WhatsApp · 02 Datang survey ke warehouse · 03 Booking unit" | ✔ STATED; M3 mirrors the page's own step 02 |
| "masih berlaku" (M3) | 0 (no end date on the page) | ✔ OK: no deadline is claimed, only "still valid now". Don't add a deadline. |
| "bayarnya cuma Rp750rb bulan ini aja" (Reply A) | "per 1 bulan" ✔; "Harga sudah All-in" ×1 (table row, no detail) | ⚠️ "cuma … aja" implies no other fee; true only if "All-in" holds. Gate: Alvian confirms what All-in covers. |

**Fixed (18:02):** M3 "survei langsung ke Kuningan" → "ke gudang Fab di ITC Kuningan Ambasador" (one named site, same line as the ads).
**New gate (G6), before any message that offers a survey or a move-in:** the page says the site **"akan launching"** (will launch). If units are not open yet, M3's survey offer and "unit gudangmu siap dipakai" (Wave 2 B5) can't be kept. Confirm with Alvian: is ITC Kuningan Ambasador open for survey and move-in now? If not, M3 becomes "Mau kami kabari begitu unit siap disurvei?" and B5's last line drops "siap dipakai".

## Page re-check 11/21 10:01 (playbook step 8: sheet > 3 days old; live `/sewa-gudang-self-storage-jakarta/`, HTTP 200, 271 visible lines)
| Claim in the script | On page 11/21 (visible lines) | Verdict |
|---|---|---|
| harga promo launching Rp750rb/bulan (M1, M3) | 750 ×9, "Promo Launching" ×10; FAQ still "mulai dari Rp 800.000" ×1 (W2 unapplied) | ✔ STATED; 800 gate stays |
| ITC Kuningan Ambasador (Sudirman, Jaksel) (M1, M3) | ITC Kuningan ×1, FAQ: "**akan launching** di ITC Kuningan Ambasador Sudirman, Jakarta Selatan"; "Jakarta Pusat" ×9 (W1 unapplied) | ⚠️ G6 open (open for survey?) |
| tanpa deposit (M1, Reply A) | only "**Bisa** tanpa uang deposit/ jaminan" (comparison table) | ❌→ fixed to "bisa tanpa deposit" |
| tanpa minimal sewa · per bulan (M1) | "tanpa minimal lama sewa" ×6, "per 1 bulan" ×6 | ✔ STATED |
| pickup gratis (M1, Reply A) | "Gratis: Pickup" ×6 + "Bantu Pickup barang dari Apartemen/ Rumah/ Kantor-mu" | ✔ STATED; **no area or Rp cap on page** (150 ×0): the ads' Rp150k pickup cap must not appear in WA until Alvian confirms it |
| Small 3,8 / Medium 7,6 / Large 15,2 m³ (M2) | each ×1 | ✔ STATED |
| "± isi 1 kamar kos" (M2) | 0 (all 6 "kos" hits = "kosong/Kosongkan") | ⚠️ INFERRED, unchanged |
| survei ke gudang (M3) | "Datang survey ke warehouse Fab" ×1 | ✔ STATED (G6 still applies) |
| "cuma Rp750rb … aja" (Reply A) | "Harga sudah All-in" ×1 (table) | ⚠️ All-in gate unchanged |

**Don't claim (page contradicts itself, 11/21):** security setting. Line 68 "Berlokasi di dalam Building … security 1×24 jam" vs line 155 "Satpam **Komplek Ruko** yang aktif 24/7". No message mentions security; if a lead asks, the team answers from the real site, not the page. Access hours: 0× on page, don't promise any.
**If a lead asks "Jakarta Pusat?"** (page says it ×9): "Lokasinya di ITC Kuningan Ambasador, area Sudirman, Jakarta Selatan Kak" (= the page FAQ's own wording, STATED).
**What changed and why:** "tanpa deposit" → "bisa tanpa deposit" in M1 + Reply A: the page only says deposit-free is *possible*; a flat promise could break if the team asks a deposit for some units. Everything else still matches. Script stays **NOT sent**; gates left: 750 vs 800 (W2), open for survey (G6), All-in (Reply A).

## Page re-check 11/27 14:01 (playbook step 8: 11/21 check > 3 days old; live `/sewa-gudang-self-storage-jakarta/`, HTTP 200, 288,285 B, 272 visible lines)
| Claim in the script | On page 11/27 | Verdict vs 11/21 |
|---|---|---|
| harga promo launching Rp750rb/bulan (M1, M3) | 750 ×9, "Promo Launching" ×10; FAQ line 250 still "mulai dari Rp 800.000" | = unchanged; W2 gate stays |
| ITC Kuningan Ambasador (M1, M3) | ×1, line 248 "**akan launching** di ITC Kuningan Ambasador Sudirman, Jakarta Selatan"; "Jakarta Pusat" ×9 | = G6 open |
| bisa tanpa deposit (M1, Reply A) | line 200 "Bisa tanpa uang deposit/ jaminan" (only deposit wording) | = ✔ STATED as "bisa" |
| tanpa minimal sewa · per bulan (M1) | "tanpa minimal (lama) sewa" lines 65/93/131/148/224/245 + "Tidak ada Kontrak Minimal Sewa" | = ✔ STATED |
| pickup gratis (M1, Reply A) | "Gratis: Pickup" lines 81/244 + "Bisa & Gratis" table; 150 ×0 | = ✔; still no Rp150k cap in WA |
| Small 3,8 / Medium 7,6 / Large 15,2 m³ (M2) | each ×1 | = ✔ STATED |
| "± isi 1 kamar kos" (M2) | 0 (all "kos" hits = kosong) | = ⚠️ INFERRED |
| survei ke gudang (M3) | line 206 "Datang survey ke warehouse Fab Self-storage" | = ✔ (G6 applies) |
| "cuma Rp750rb … aja" (Reply A) | line 185 "sudah All-in" ×1 | = ⚠️ All-in gate |

**Security (don't claim, unchanged):** line 139 "di dalam building dengan security 1x24 jam di area Sudirman, Jakarta Pusat" vs line 154 "Satpam Komplek Ruko yang aktif 24/7". Still contradictory; no message mentions security.
**What changed and why:** nothing. Page text identical on every script claim since 11/21, so no copy edit. Script stays **NOT sent** and is paste-ready the moment 3 gates close: 750 vs 800 (W2), Kuningan open for survey (G6), what "All-in" covers (Reply A only). Next re-check due ≥ 11/30 if still unsent.

## Objection reply: "Kok lebih mahal dari yang 400rb?" (added 2026-11-10 18:02, draft, NOT sent)
**Context:** SpaceHub (Thamrin, ~10 min away) advertises "From Rp 400k / month" for its smallest unit, but asks a **security deposit**, needs **online self-booking + pay first**, and you **move your stuff yourself** (its own FAQ, `fab_advertising/research/2026-11-10_competitor_angles.md`). Rule: compare **total cost and effort**, never knock the competitor by name, never discount on the spot.
**Gate:** use only after Alvian confirms 750 vs 800, no deposit, free pickup (+ pickup area), and the Small unit size. Unit size of SpaceHub's 400k unit is **unknown**, so the reply does not claim "ours is bigger".

**Reply A (default, short)**
> Betul Kak, ada yang mulai 400rb 🙏 Bedanya di Fab: barang Kakak **kami jemput gratis**, **bisa tanpa deposit**, dan **tanpa minimal sewa**, jadi bayarnya cuma Rp750rb bulan ini aja.
> Jadi Kakak nggak perlu sewa mobil bak, cari tenaga angkut, atau siapkan uang deposit di depan. Tinggal tunjuk barangnya 😊
> Barangnya kira-kira berapa banyak, Kak? Biar kami cek unit yang pas.

**Reply B (if they push on price again)**
> Kami paham Kak 🙏 Supaya adil, coba bandingkan dari ukurannya juga ya: unit Small kami 3,8 m³. Kalau barangnya sedikit, kami bantu cek dulu apakah memang perlu unit itu.
> Mau kami kirim foto unitnya + estimasi jadwal jemput?

**Notes**
- Reply A makes no "total cost is the same" claim: no Jakarta pickup-truck price is checked, and deposits are usually refundable. If a lead asks for a cost comparison, the team should not quote a number.
- Reply B hands the sizing question back instead of discounting: protects the promo-launching 750 price and moves to a photo/pickup step (the same next step as Message 2).
- Measure: tag chats that raise the 400rb objection; if > 20% of chats raise it in 2 weeks, test a price-led reply (and tell Fuku).
