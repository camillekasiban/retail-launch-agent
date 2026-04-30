# Post-Launch Hypercare Protocol

**Purpose:** Defines what the SE does after go-live. Reference this when a merchant has processed their first transaction and the agent needs to guide the SE through the hypercare period, risk closure, and formal launch close-out.

---

## Overview

A Shopify POS launch isn't complete at "first transaction processed." The hypercare period (Days 1–14 post-launch) is when most operational issues surface. The SE's job in this period shifts from unblocking milestones to monitoring stability, closing resolved risks, and ensuring the merchant is self-sufficient.

---

## Hypercare Schedule

### Days 1–3: Active Monitoring

Check in with the merchant/partner **daily** — a quick message or call is enough.

What to ask:
- Any transaction failures or payment processing errors?
- Any staff login or permission issues?
- Any hardware problems (disconnects, printer failures, card reader pairing)?
- Any inventory count discrepancies?
- Any customer-facing issues (receipts not arriving, checkout errors)?

What to watch in the tracker:
- Are any risks that were "accepted at launch" showing up as actual problems?
- If a new issue surfaces, add it to the risk register immediately — don't let issues live in email threads

### Days 4–7: Stabilization Check

Check in every 2 days.

What to confirm:
- End-of-day cash reconciliation is working
- Daily sales reports are generating correctly (POS Pro)
- Staff are comfortable with common flows: exchanges, returns, gift cards, discounts
- Any integration issues (ERP, loyalty, OMS) that surfaced post-launch

If no issues by Day 7: move to weekly check-ins for the second week.

### Days 8–14: Wind-Down

Weekly check-in. Focus on:
- Any outstanding risks that haven't resolved
- Staff independently handling edge cases (the merchant shouldn't need to call the partner for a return)
- Confirming next phase planning if applicable (Phase 2 brands, additional locations)

---

## Risk Closure Criteria

Close a risk when **all three** are true:
1. The issue it described has been resolved and confirmed working in production
2. The merchant has confirmed — either verbally on a call or in writing
3. At least 3 business days have passed since resolution without recurrence

**Do not close risks based on:** partner saying it's done, a single successful test, or assumption that time has passed.

When closing a risk in `risk-register.md`:
- Change Status from `Open` to `Closed`
- Add a closing update: `YYYY-MM-DD: Closed. [One sentence on how it was resolved and who confirmed.]`
- Move the entry from Active Risks to a `## Closed Risks` section at the bottom of the file

---

## Launch Close-Out Criteria

Formally close the launch when **all** of the following are true:

| Criterion | How to confirm |
|---|---|
| All Testing phase milestones Complete | Milestone table in launch-tracker.md |
| All Launch phase milestones Complete | Including "First transaction processed" |
| No Critical or High risks remain Open | Risk register |
| Merchant has processed 5+ business days of transactions without incident | Ask merchant directly |
| End-of-day reporting confirmed working | Ask partner or check with merchant |
| Staff training completed and signed off | POS Staff Training phase milestones |
| Any Phase 2 dates confirmed or formally deferred | Decisions Log |

If all criteria are met: update launch-tracker.md health to GREEN and add a Decisions Log entry:
`YYYY-MM-DD: Launch formally closed. All close-out criteria met. Phase 1 go-live confirmed successful.`

---

## `close launch for [Name]` Command

When the user says `close launch for [Name]`, run through the close-out criteria above:
1. Read the merchant's `launch-tracker.md` and `risk-register.md`
2. Check each criterion against current state
3. If all criteria are met: update health to GREEN, add the Decisions Log close-out entry, and report success
4. If criteria are not met: list which ones are outstanding and what's needed to close them
5. Never close a launch with open Critical or High risks — flag them and ask the user to confirm they're intentionally accepting the risk

---

## Handoff Considerations

After formal close-out, consider:
- **Knowledge transfer:** Is there anything unusual about this merchant's setup that a colleague would need to know for future support? Document it in the Decisions Log.
- **Phase 2 kickoff:** If more brands or locations are in scope, start a new intake cycle — don't treat Phase 2 as a continuation of Phase 1 tracking.
- **Retrospective:** What went well? What would you do differently? Patterns worth capturing for future merchants (especially for the `references/risk-playbooks.md`).

---

## Health Transitions Post-Launch

| Situation | Expected health |
|---|---|
| Launch day, first transaction processed, no open Critical/High risks | 🟢 GREEN |
| Launch day, open High risk (e.g., one integration not working) | 🟡 YELLOW |
| Significant transaction failures, data integrity issues, or hardware down across locations | 🔴 RED |

A post-launch RED is a genuine incident. Treat it as: identify the issue, determine if it's a Shopify platform issue (contact Shopify Support) or a configuration issue (partner resolves), and communicate a timeline to the merchant within 2 hours.
