# W4: where the Fab Lead event fires (2026-11-11 17:02 WIB, cloud, read-only curl)

**Answer:** Lead isn't fired by the form. It's a PixelYourSite Pro **custom static event on one thank-you page**, `/thank-you-self-storage-lead/` (post 5443, noindex), set to fire **once per visitor per 24 h** (`hasTimeWindow: true, timeWindow: 24`). Fluent Form #10 sends people there or to a second page, `/terima-kasih-non-self-storage-lead/`, which only fires PageView. So the "~1 in 3 Forms with no Lead" gap is **mostly by design (routing + 24 h dedup), not a technical leak.**

## Evidence (site HTML, account data)
| Page | PYS events | Notes |
|---|---|---|
| `/form-chat-fab-storage-via-whatsapp/` (Fluent Form #10) | PageView + automatic events (incl. **Form**, InternalClick, OutboundClick, scroll, time-on-page). `triggerEvents: []`. **No Lead.** | The PYS "Form" event fires on submit, before Fluent Form validation or routing (INFERRED from PYS automatic-event behaviour). |
| `/thank-you-self-storage-lead/` | PageView + **Lead** (custom_event, 24 h window) | Body: "Thank You. Chat via WA sekarang: Link WA Fab ➜" → `wa.me/628990332050?text=Hallo,Mas...+Saya+mau+sewa+self-storage+di+Fab`. `/thank-you/` 301s here. |
| `/terima-kasih-non-self-storage-lead/` | PageView only | Same layout, WA text "HaloMbak, Saya mau tanya tentang Fab Self-Storage". `/terima-kasih/` 301s here. |
| All 13 sitemap pages | No Lead anywhere | — |

Form #10 fields: Nama · Nomor WA · "Untuk merapikan ruangan dimana?" (Apartment / Rumah / Kantor / **Tidak ada**) · Kebutuhan (Mau sewa self-storage / Mau ambil harga promo / **Mau tanya-tanya dulu via WA**) · "Pernah chat WA ke Fab sebelumnya?" (**Sudah pernah** / Belum pernah).

## What I can't see from outside
- **The routing rule itself.** It lives in the Fluent Form #10 confirmation settings (server side). Candidates (INFERRED): "Tidak ada", "Mau tanya-tanya dulu via WA", or "Sudah pernah" → non-lead page. The non-lead page's WA text ("mau tanya") points at the **"tanya-tanya" answer** as the most likely rule.
- I didn't submit the form (that would put a fake lead in Fab's inbox).

## So what (for M-001)
1. **W4 changes from "find the leak" to "confirm the rule".** The gap is ~21 Forms/7d *(calc: server 51 − 30)*, minus 24 h repeats and validation-failed submits. Those people still reach a WA link; they just aren't counted as a Lead.
2. **⚠️ W3 is no longer zero-risk.** If routing uses "Pernah chat WA ke Fab sebelumnya?", deleting that field (W3) changes what counts as a Lead mid-mission. W3 must wait until the rule is known. W1/W2 (copy only) are unaffected.
3. **Don't redefine Lead to hit 95k.** Counting the non-lead page would cut measured CPL by up to ~⅓ without a single extra customer. The M-001 target was set on today's definition, so it stays. If Alvian wants "tanya-tanya" chats counted, that's a separate decision, and the target should be re-based with it.
4. **Optimisation angle (INFERRED, low priority):** Meta optimises on the Lead page only, which is right if "tanya-tanya" chats close worse. Only the close rate by answer can say. It's one more reason the lead-value question (close rate, months stayed) matters.

## Ask (folded into the parked W4 line, no new ask)
"Which Kebutuhan / field answer sends Form #10 to the non-self-storage thank-you page?" (one look in Fluent Forms → Form 10 → Settings → Confirmation).
