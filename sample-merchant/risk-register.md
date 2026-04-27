---
merchant: "Greenleaf Home Goods"
last_updated: "2026-04-08"
---

# Greenleaf Home Goods — Risk Register

---

## Active Risks

| ID | Severity | Category | Risk Description | Owner | Due Date | Status |
|---|---|---|---|---|---|---|
| R-001 | 🟠 High | payments | Shopify Payments application has been under review for 5 days with no update. This blocks all card reader and Tap to Pay testing, which is on the critical path to go-live. | Camille Kasiban | 2026-04-15 | Open |
| R-002 | 🟡 Med | staff | Manager training dates are not confirmed. 3 store managers across 3 time zones must be trained before staff training can begin. SE is OOO May 5–9, compressing the scheduling window significantly. | Camille Kasiban | 2026-04-18 | Open |

---

## Risk Log

### R-001 — Shopify Payments application delayed, blocking payment testing

- **Severity:** High
- **Category:** payments
- **Identified:** 2026-04-08 from 2026-04-07-email-thread.md
- **Description:** Shopify Payments application was submitted on 2026-04-03. As of 2026-04-08, it has been 5 days with no approval or rejection communication. Standard review is 1–3 business days. Merchant contact Sarah Doyle flagged this via email asking for an update.
- **Impact if unresolved:** Card reader testing, Tap to Pay testing, refund flow testing, and cash handling configuration are all blocked until Payments is approved. These 5 milestones are on the critical path. If approval comes after April 15, there is less than 30 days of runway for testing — insufficient for 3 locations.
- **Mitigation plan:** 1) Camille to follow up with Shopify Payments team by April 10. 2) If not approved by April 12, escalate via SE escalation path. 3) In parallel, identify whether a Stripe or Square interim processing option could be configured as a contingency (discuss with Sarah).
- **Owner:** Camille Kasiban
- **Due Date:** 2026-04-15
- **Status:** Open
- **Updates:**
  - 2026-04-08: Application submitted 2026-04-03, still pending. Merchant flagged via email. Escalation path identified. Originally logged as Med; escalated to High given downstream blocking impact on payment testing milestones.

---

### R-002 — Manager training scheduling not confirmed, window is compressing

- **Severity:** Med
- **Category:** staff
- **Identified:** 2026-04-08 from intake note (Camille's implementation notes)
- **Description:** The 3 store managers (Chicago, Austin, Portland) need to be trained before frontline staff training can begin. No training dates have been confirmed. Camille is OOO May 5–9. The ideal window is April 25–May 2 to allow staff training to complete by May 8. If training slips past May 2, it creates a cascade risk for the May 15 go-live.
- **Impact if unresolved:** Staff training for 3 locations cannot begin until manager training is done. If manager training slips past May 9, staff training likely can't complete by May 15, potentially delaying go-live.
- **Mitigation plan:** 1) Propose joint virtual training session for all 3 managers on April 25. 2) If schedules conflict, do individual sessions the week of April 21. 3) Record session for async review by any manager who misses.
- **Owner:** Camille Kasiban
- **Due Date:** 2026-04-18 (training date confirmed by this date)
- **Status:** Open
- **Updates:**
  - 2026-04-08: Identified during intake review. No scheduling conflict exists yet, but proactive flagging needed given SE OOO window in May.
