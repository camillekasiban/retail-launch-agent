---
merchant: "Greenleaf Home Goods"
launch_target: "2026-05-15"
launch_health: "YELLOW"
last_updated: "2026-04-08"
se_owner: "Camille Kasiban"
partner: "Pixel Commerce Agency"
---

# Greenleaf Home Goods — Launch Tracker

**Launch Health:** 🟡 YELLOW — Needs Attention
**Target Go-Live:** 2026-05-15
**SE Owner:** Camille Kasiban
**Implementation Partner:** Pixel Commerce Agency
**Last Updated:** 2026-04-08

---

## Milestone Progress

| Phase | Milestone | Status | Owner | Due Date | Notes |
|---|---|---|---|---|---|
| Getting Started | Admin access configured | Complete | Pixel Commerce Agency | 2026-04-01 | All stakeholders added; SE and partner have admin access |
| Getting Started | Sandbox / dev environment created | Complete | Pixel Commerce Agency | 2026-04-01 | Dev store confirmed active |
| Getting Started | POS Sales Channel added | Complete | Pixel Commerce Agency | 2026-04-01 | POS channel live in Admin |
| Getting Started | Locations configured | Complete | Pixel Commerce Agency | 2026-04-05 | Chicago IL, Austin TX, Portland OR — all 3 active |
| Getting Started | Hardware ordered | Complete | Pixel Commerce Agency | 2026-04-03 | 3x POS Go, 3x Tap to Pay on iPhone, 3x Star TSP100 printers |
| Data Migration & Integrations | Products migrated | Complete | Pixel Commerce Agency | 2026-04-08 | 1,240 SKUs migrated from Lightspeed CSV; barcodes verified |
| Data Migration & Integrations | Inventory quantities migrated | Complete | Pixel Commerce Agency | 2026-04-08 | Counts match Lightspeed export at time of migration |
| Data Migration & Integrations | Customers migrated | In Progress | Pixel Commerce Agency | 2026-04-12 | Chicago done; Austin and Portland pending |
| Data Migration & Integrations | Orders migrated | Not Started | | | Not in scope for Phase 1 — manual CSV migration only |
| Data Migration & Integrations | Discounts and promotions configured | Not Started | Pixel Commerce Agency | 2026-04-15 | |
| Data Migration & Integrations | Software integrations connected | Not Started | | | No ERP/OMS/loyalty integration in scope for Phase 1 |
| Admin Set Up | Payments configured | In Progress | Camille Kasiban | 2026-04-15 | Application submitted 2026-04-03; under review — see R-001 |
| Admin Set Up | Delivery and BOPIS configured | Not Started | Pixel Commerce Agency | 2026-04-18 | |
| Admin Set Up | Order routing rules configured | Not Started | Pixel Commerce Agency | 2026-04-18 | |
| Admin Set Up | Tax IDs and exemptions set up | Complete | Pixel Commerce Agency | 2026-04-08 | IL, TX, OR rates configured and spot-checked |
| Admin Set Up | Email notifications reviewed | Not Started | Pixel Commerce Agency | 2026-04-18 | |
| Admin Set Up | POS staff roles and permissions created | Complete | Pixel Commerce Agency | 2026-04-08 | 3 roles defined: Store Manager, Senior Staff, Staff |
| Admin Set Up | POS staff accounts created | In Progress | Pixel Commerce Agency | 2026-04-15 | Chicago done; Austin and Portland pending |
| Admin Set Up | Receipts customized | Complete | Pixel Commerce Agency | 2026-04-07 | Merchant approved via email 2026-04-07 |
| Admin Set Up | POS checkout requirements configured | Complete | Pixel Commerce Agency | 2026-04-08 | No tipping (merchant preference confirmed) |
| Admin Set Up | POS terminal view configured | Not Started | Pixel Commerce Agency | 2026-04-20 | Waiting on all hardware to arrive |
| Admin Set Up | Product availability confirmed on POS | Complete | Pixel Commerce Agency | 2026-04-08 | All 1,240 SKUs visible on POS Sales Channel |
| Admin Set Up | Third-party apps installed | Not Started | Pixel Commerce Agency | 2026-04-20 | Matrixify and Rewind to be installed |
| POS Set Up (On Device) | POS app installed on all devices | In Progress | Pixel Commerce Agency | 2026-04-20 | Chicago done; Austin and Portland hardware arrives Apr 18 |
| POS Set Up (On Device) | Firewall and MDM checks complete | Complete | Tom Nakamura (Merchant IT) | 2026-04-05 | All 3 locations on ethernet; firewall allows Shopify POS |
| POS Set Up (On Device) | Hardware connected | In Progress | Pixel Commerce Agency | 2026-04-20 | Chicago fully connected; Austin and Portland pending delivery |
| POS Set Up (On Device) | Gift cards enabled | Not Started | Pixel Commerce Agency | 2026-04-20 | |
| POS Set Up (On Device) | Custom payment methods set up | Not Started | Pixel Commerce Agency | 2026-04-22 | Store credit to be configured |
| Testing | Login and permissions tested | Not Started | Pixel Commerce Agency | 2026-04-25 | Blocked on staff accounts for Austin and Portland |
| Testing | Sales flows tested | Not Started | Pixel Commerce Agency | 2026-04-28 | Blocked on Payments approval (R-001) |
| Testing | Draft orders and holds tested | Not Started | Pixel Commerce Agency | 2026-04-28 | |
| Testing | Returns and exchanges tested | Not Started | Pixel Commerce Agency | 2026-04-28 | |
| Testing | Gift card tested | Not Started | Pixel Commerce Agency | 2026-04-28 | |
| Testing | Third-party app tiles tested | Not Started | Pixel Commerce Agency | 2026-04-28 | |
| Testing | Daily operations tested | Not Started | Pixel Commerce Agency | 2026-05-02 | |
| Testing | Hardware verified per location | Not Started | Pixel Commerce Agency | 2026-05-02 | All 3 locations must be verified independently |
| POS Staff Training | Test results reviewed and processes documented | Not Started | Camille Kasiban | 2026-05-04 | |
| POS Staff Training | Training materials organized | Not Started | Camille Kasiban | 2026-05-04 | |
| POS Staff Training | Staff training completed | Not Started | Camille Kasiban | 2026-05-10 | See R-002 — scheduling not confirmed; SE OOO May 5–9 |
| Launch | Delta data migration complete | Not Started | Pixel Commerce Agency | 2026-05-14 | |
| Launch | Gift cards migrated | Not Started | | | Lightspeed has no gift cards to migrate — confirmed kickoff |
| Launch | Device launch readiness check complete | Not Started | Pixel Commerce Agency | 2026-05-14 | Per store: Chicago, Austin, Portland |
| Launch | First transaction processed | Not Started | | 2026-05-15 | Chicago flagship only for Phase 1 |

**Completion:** 13 / 43 milestones (30%)

---

## Open Risks Summary

| Severity | Risk | Category | Owner | Due |
|---|---|---|---|---|
| 🟠 High | Shopify Payments application still under review after 5 days — blocks all payment and sales testing | payments | Camille Kasiban | 2026-04-15 |
| 🟡 Med | Manager training dates not confirmed — SE OOO May 5–9 compresses scheduling window | staff | Camille Kasiban | 2026-04-18 |

Full risk register: [risk-register.md](./risk-register.md)

---

## Open Questions

- 2026-04-07: Is Tap to Pay on iPhone primary or backup reader at each location? Sarah leaning toward backup but hasn't confirmed. Source: 2026-04-07-email-thread.md
- 2026-04-08: When can all 3 store managers attend joint training? Propose April 25. SE OOO May 5–9. Source: intake note

---

## Decisions Log

- 2026-04-01: Go-live May 15 for Chicago flagship only. Austin and Portland to follow within 30 days. Source: 2026-04-01-kickoff-transcript.md
- 2026-04-01: No ERP/OMS/loyalty integration in scope for Phase 1. Manual CSV inventory management. Source: 2026-04-01-kickoff-transcript.md
- 2026-04-01: No historical order migration required. Source: 2026-04-01-kickoff-transcript.md
- 2026-04-07: No tipping configured — merchant preference for home goods retail. Source: 2026-04-07-email-thread.md
- 2026-04-08: Lightspeed contract runs to May 31 — provides rollback window post go-live. Source: 2026-04-07-email-thread.md
- 2026-04-08: No legacy gift cards to migrate from Lightspeed. Source: kickoff confirmed.

---

## Next Steps

| Action | Owner | Due | Source |
|---|---|---|---|
| Follow up with Shopify Payments on application status — escalate if no update by Apr 10 | Camille Kasiban | 2026-04-10 | 2026-04-07-email-thread.md |
| Confirm manager training dates with Sarah Doyle — propose Apr 25 joint session | Camille Kasiban | 2026-04-12 | 2026-04-08 intake note |
| Complete staff account setup for Austin and Portland | Pixel Commerce Agency | 2026-04-15 | 2026-04-01-kickoff-transcript.md |
| Verify Austin and Portland hardware on arrival (Apr 18) | Pixel Commerce Agency | 2026-04-20 | 2026-04-07-email-thread.md |

---

## Intake Log

| Date Processed | File | Changes Made |
|---|---|---|
| 2026-04-08 | 2026-04-01-kickoff-transcript.md | 10 milestones updated, 5 decisions logged, 1 open question added |
| 2026-04-08 | 2026-04-07-email-thread.md | 3 milestones updated, R-001 escalated to High, R-002 added, 1 decision logged, 1 open question added, 4 next steps added |
