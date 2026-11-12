# Fab: WA follow-up script for "Form submitted, never chatted" (W4)
_2026-11-06 08:02 WIB · Fuku draft · NOT sent. Nothing goes out until Alvian approves and the Fab team sends it from the Fab WA number._

**Why:** 7d pixel shows 101 Form events vs 61 Lead events (~40% gap) [data, `2026-11-06_landing_page_audit.md`]. If Lead fires only when WhatsApp opens, the gap = people who left a name + WA number in Fluent Form #10 but never sent the chat. They raised a hand; a same-day reply is the cheapest lead Fab can get (no ad spend). [INFERRED until W4 confirms how Lead fires.]

**Facts used (only those already on the live site/ads):** "Harga Promo Launching" Rp750.000/bulan (the site's own wording; the site never mentions a code, the PEIKIRA ads say "kode FAB750") (⚠️ the WA form page + 1 FAQ line still say Rp800.000 = W2; confirm before sending) · ITC Kuningan Ambasador, Sudirman, Jakarta Selatan · no minimum rental, monthly payment, no deposit, free pickup · Small 4.75 m³ / Medium 9.5 m³ / Large 19 m³. ⚠️ Confirm all with Alvian before use.

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
> Unit kami di ITC Kuningan Ambasador (Sudirman, Jaksel), lagi harga promo launching Rp750rb/bulan. Tanpa deposit, tanpa minimal sewa, pickup gratis.
> Barangnya kira-kira apa aja, Kak? 😊

**Message 2 (+24 h, no reply)**
> Kak {nama}, biar gampang pilihnya: Small 4,75 m³ (± isi 1 kamar kos), Medium 9,5 m³, Large 19 m³. Mau kami kirim foto unitnya dulu?

**Message 3 (+3 days, last one)**
> Kak {nama}, kalau masih butuh tempat simpan barang, harga promo launching Rp750rb/bulan masih berlaku. Mau survei langsung ke Kuningan minggu ini? Balas "survei" nanti kami atur jamnya. Kalau sudah tidak perlu, tidak apa-apa, terima kasih ya Kak 🙏

## Notes
- "± isi 1 kamar kos" is Fuku's sizing analogy [INFERRED], not a site claim. Have the team check it against real units, or drop it.
- **Price wording (2026-11-12 11:01):** Messages 1 and 3 now use the site's own phrase "harga promo launching Rp750rb/bulan" instead of "kode FAB750" (`fab_advertising/reports/2026-11-12_wave1_price_wording_check.md`). Reason: a form-filler arrives from the site, so the WA reply should echo the site. If a lead quotes "FAB750" from an ad, the team just confirms it (same 750 price). Message 3 no longer claims "slot" scarcity, which nothing on the site backs. If **800 is real**, change the number in Messages 1, 3 and Reply A.
- Message 2's "foto unit" ties in with the phone photo shoot (the same real photos double as ad creative).
- Measure: replies ÷ messaged and surveys ÷ messaged for 2 weeks. If reply rate < 10%, rewrite Message 1 (lead with the price, not the question).

## Objection reply: "Kok lebih mahal dari yang 400rb?" (added 2026-11-10 18:02, draft, NOT sent)
**Context:** SpaceHub (Thamrin, ~10 min away) advertises "From Rp 400k / month" for its smallest unit, but asks a **security deposit**, needs **online self-booking + pay first**, and you **move your stuff yourself** (its own FAQ, `fab_advertising/research/2026-11-10_competitor_angles.md`). Rule: compare **total cost and effort**, never knock the competitor by name, never discount on the spot.
**Gate:** use only after Alvian confirms 750 vs 800, no deposit, free pickup (+ pickup area), and the Small unit size. Unit size of SpaceHub's 400k unit is **unknown**, so the reply does not claim "ours is bigger".

**Reply A (default, short)**
> Betul Kak, ada yang mulai 400rb 🙏 Bedanya di Fab: barang Kakak **kami jemput gratis**, **tanpa deposit**, dan **tanpa minimal sewa**, jadi bayarnya cuma Rp750rb bulan ini aja.
> Jadi Kakak nggak perlu sewa mobil bak, cari tenaga angkut, atau siapkan uang deposit di depan. Tinggal tunjuk barangnya 😊
> Barangnya kira-kira berapa banyak, Kak? Biar kami cek unit yang pas.

**Reply B (if they push on price again)**
> Kami paham Kak 🙏 Supaya adil, coba bandingkan dari ukurannya juga ya: unit Small kami 4,75 m³. Kalau barangnya sedikit, kami bantu cek dulu apakah memang perlu unit itu.
> Mau kami kirim foto unitnya + estimasi jadwal jemput?

**Notes**
- Reply A makes no "total cost is the same" claim: no Jakarta pickup-truck price is checked, and deposits are usually refundable. If a lead asks for a cost comparison, the team should not quote a number.
- Reply B hands the sizing question back instead of discounting: protects the promo-launching 750 price and moves to a photo/pickup step (the same next step as Message 2).
- Measure: tag chats that raise the 400rb objection; if > 20% of chats raise it in 2 weeks, test a price-led reply (and tell Fuku).
