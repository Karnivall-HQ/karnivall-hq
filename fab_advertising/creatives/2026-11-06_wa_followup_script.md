# Fab: WA follow-up script for "Form submitted, never chatted" (W4)
_2026-11-06 08:02 WIB · Fuku draft · NOT sent. Nothing goes out until Alvian approves and the Fab team sends it from the Fab WA number._

**Why:** 7d pixel shows 101 Form events vs 61 Lead events (~40% gap) [data, `2026-11-06_landing_page_audit.md`]. If Lead fires only when WhatsApp opens, the gap = people who left a name + WA number in Fluent Form #10 but never sent the chat. They raised a hand; a same-day reply is the cheapest lead Fab can get (no ad spend). [INFERRED until W4 confirms how Lead fires.]

**Facts used (only those already on the live site/ads):** Promo Rp750.000/bulan with code FAB750 (⚠️ the form page says Rp800.000; confirm before sending) · ITC Kuningan Ambasador, Sudirman, Jakarta Selatan · no minimum rental, monthly payment, no deposit, free pickup · Small 4.75 m³ / Medium 9.5 m³ / Large 19 m³. ⚠️ Confirm all with Alvian before use.

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
> Unit kami di ITC Kuningan Ambasador (Sudirman, Jaksel), promo Rp750rb/bulan pakai kode FAB750. Tanpa deposit, tanpa minimal sewa, pickup gratis.
> Barangnya kira-kira apa aja, Kak? 😊

**Message 2 (+24 h, no reply)**
> Kak {nama}, biar gampang pilihnya: Small 4,75 m³ (± isi 1 kamar kos), Medium 9,5 m³, Large 19 m³. Mau kami kirim foto unitnya dulu?

**Message 3 (+3 days, last one)**
> Kak {nama}, kalau masih butuh tempat simpan barang, slot promo FAB750 masih bisa dipakai. Mau survei langsung ke Kuningan minggu ini? Balas "survei" nanti kami atur jamnya. Kalau sudah tidak perlu, tidak apa-apa, terima kasih ya Kak 🙏

## Notes
- "± isi 1 kamar kos" is Fuku's sizing analogy [INFERRED], not a site claim. Have the team check it against real units, or drop it.
- Message 2's "foto unit" ties in with the phone photo shoot (the same real photos double as ad creative).
- Measure: replies ÷ messaged and surveys ÷ messaged for 2 weeks. If reply rate < 10%, rewrite Message 1 (lead with the price, not the question).
