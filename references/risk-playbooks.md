# Common Risk Playbooks — SE Action Guide

**Purpose:** When the agent surfaces a risk, these playbooks define what the SE should do next. Reference these when generating acceleration opportunities, drafting status updates, or advising on next steps. Each playbook includes: when to escalate severity, immediate SE actions, what to communicate, and how to update the tracker.

---

## Playbook 1 — Hardware Delivery Delayed

**Triggers:** Hardware ETA is unknown, later than expected, or pushes within 10 days of go-live.

**Severity escalation:**
- Med → High if delivery ETA is less than 14 days before go-live
- High → Critical if delivery ETA is less than 7 days before go-live (no time for setup and testing)

**Immediate SE actions:**
1. Get a firm delivery date from the partner today — "in transit" is not an ETA
2. Calculate minimum time needed: hardware delivery → device setup → firewall/MDM checks → hardware testing. Minimum realistic buffer = 5 business days
3. If delivery ETA + 5 days > go-live date: raise the go-live date risk with the merchant immediately, don't wait
4. Ask partner if any devices can be sourced locally as a backup (retail Apple Store for iPads, for example)
5. Confirm whether Tap to Pay (on iPhone or Android) can serve as a temporary fallback for card payments if hardware arrives late

**What to communicate:**
- To partner: "We need a confirmed delivery date today. If hardware arrives after [date], we won't have enough time for setup and testing before [go-live date]."
- To merchant: "Hardware is in transit but we don't have a confirmed delivery date yet. We're monitoring this closely — if the ETA slips past [date], we'll need to discuss options for [go-live date]."

**Tracker update:** Escalate severity on the hardware risk. Add a due date on the risk entry. Log the ETA confirmation (or lack of one) as an update in the risk log.

---

## Playbook 2 — Shopify Payments Not Approved / Delayed

**Triggers:** Shopify Payments application not submitted, under review, or rejected.

**Severity escalation:**
- Med → High if approval is pending with < 21 days to go-live (approval can take 1-2 weeks)
- High → Critical if approval is pending with < 10 days to go-live (not enough time to test payments)

**Immediate SE actions:**
1. Confirm the application was actually submitted — not just "started"
2. If not submitted: get the merchant to submit today. The clock starts at submission, not at "we're working on it"
3. If under review: check for any outstanding document requests from Shopify — these are the most common cause of delays
4. Explore a temporary fallback: can the merchant use a third-party processor (Stripe, Square via integration) for the first few days while Payments approves? This is not ideal but preserves the go-live date
5. If rejected: escalate to your Shopify account team immediately — rejections are sometimes resolvable with additional documentation

**What to communicate:**
- To merchant: "Shopify Payments approval typically takes 1-2 weeks. If we don't have approval by [date], we won't be able to test payment flows before go-live. Has there been any communication from Shopify requesting additional documents?"

**Tracker update:** Mark the "Payments configured" milestone as Blocked if approval is pending. Update risk severity and due date. Note any document requests or rejection reason in the risk log.

---

## Playbook 3 — Implementation Partner Unresponsive or Behind Schedule

**Triggers:** Partner not completing milestones, not responding to communications, or missing agreed dates.

**Severity escalation:**
- Med if partner is 3-5 days behind on a non-critical milestone
- High if partner is behind on a critical-path milestone or not responding to communications for 3+ business days
- Critical if partner has gone dark for 5+ business days with critical milestones unstarted

**Immediate SE actions:**
1. Document the last confirmed communication date and what was outstanding
2. Escalate within the partner org — reach out to the partner's account lead or project manager, not just the implementation contact
3. If partner is a Shopify Partner, you can escalate to your Shopify Partner Manager for visibility
4. Assess which milestones are blocked by the partner and which the merchant could action directly (e.g., adding POS Sales Channel, configuring locations — these are Shopify Admin tasks the merchant can do)
5. Determine whether an alternative partner needs to be identified — this is a last resort but sometimes necessary

**What to communicate:**
- Internal: Flag to your team lead. Partner capacity issues can affect other merchants and the account team may have leverage.
- To merchant: "We're following up with [partner] on [specific milestone]. In the meantime, there are a few things your team can move forward on directly — [specific tasks]."

**Tracker update:** Add a new risk or escalate the existing scope/partner-capacity risk. Set due date for next expected response. Log all communication attempts with dates in the risk log.

---

## Playbook 4 — Merchant Wants to Postpone Go-Live

**Triggers:** Merchant expresses hesitation, requests a delay, or goes quiet as go-live approaches.

**Severity escalation:** Assess the reason — not all postponements are equal:
- Operational readiness (training not done, staff not hired): High — solvable, needs a plan
- Technology not ready (hardware not arrived, Payments not approved): High — external dependency
- Business decision / change of direction: Critical — may require contract or scope conversation

**Immediate SE actions:**
1. Get the reason in writing — "we're not ready" is not enough to act on
2. If it's a training or operational gap: propose a revised go-live date with a specific remediation plan. A 1-2 week delay with a clear plan is far better than a rushed launch
3. If it's a hardware or Payments issue: see Playbooks 1 and 2
4. If it's a business decision: involve your account team. This may be a signals issue (merchant cold feet) or a real scope change
5. Always propose a new concrete date in the same conversation — don't leave it as "we'll reassess later"

**What to communicate:**
- "Understood — let's make sure the launch goes well rather than rushing it. Can you help me understand what specifically isn't ready? I'd like to propose a revised date that gives us the buffer we need."

**Tracker update:** Update the go-live date if confirmed. Recalculate health. Add a Decisions Log entry with the original date, new date, and reason. Add a `go-live-logistics` risk if the delay creates downstream scheduling issues.

---

## Playbook 5 — ERP / Integration Failing or Behind Schedule

**Triggers:** Integration between Shopify and an ERP, OMS, loyalty platform, or inventory system is not working, not started, or blocked on a third party.

**Severity escalation:**
- Med if the integration is nice-to-have or post-launch
- High if the integration is required for accurate inventory, pricing, or order management at launch
- Critical if inventory or pricing data can't flow into Shopify without it

**Immediate SE actions:**
1. Clarify what "failing" means — is it a configuration issue, a data format mismatch, an API credential problem, or a capacity issue on the integration partner's side?
2. Separate what's blocking launch from what can be done post-launch. Ask: "Can we go live with manual processes for [X days] while the integration is completed?"
3. If the integration partner is a third party (Celigo, Patchworks, custom middleware): the implementation partner should own the escalation, not the SE directly — but confirm this is happening
4. If inventory is the core issue: can inventory be manually uploaded via CSV for Phase 1 while the integration is resolved? This is a common short-term mitigation.

**What to communicate:**
- "Which data flows are required on day one vs. can be deferred? Let's identify what the minimum viable integration looks like for go-live and what we can clean up in week 2."

**Tracker update:** Flag the specific integration milestone as Blocked. Add a risk with the integration category. Note the third party involved and their expected resolution date.

---

## Playbook 6 — Key Decision-Maker Unavailable

**Triggers:** The merchant's executive sponsor, IT lead, or project manager is OOO, unresponsive, or not attending calls as go-live approaches.

**Severity escalation:**
- Med if the person is unavailable for < 1 week and decisions can wait
- High if unresolved decisions (brand architecture, payment setup, staff structure) are gated on this person
- Critical if the merchant has no one empowered to make decisions with < 2 weeks to launch

**Immediate SE actions:**
1. Identify a backup decision-maker — who has authority in their absence?
2. Document every open decision that is gated on this person and communicate it clearly: "These three things need a decision before [date] or they will push the go-live date."
3. If a decision can be made with a reasonable default, propose the default clearly and ask for confirmation or override rather than leaving it open
4. Don't let the absence create ambiguity — treat no response after 48 hours as a risk escalation trigger

**Tracker update:** Log as a `merchant-readiness` risk. List the specific decisions that are blocked. Set a due date tied to the earliest downstream milestone that depends on those decisions.

---

## Playbook 7 — Staff Training Not Scheduled

**Triggers:** Go-live is within 14 days and no training session is on the calendar.

**Severity escalation:**
- Med if go-live is 14+ days away
- High if go-live is within 14 days and training is not scheduled
- Critical if go-live is within 7 days and staff have not been trained

**Immediate SE actions:**
1. Get a training date on the calendar today — not "this week"
2. Confirm who is delivering training (SE, partner, or merchant self-serve). If SE: block the time now
3. Ask: how many staff, across how many locations? A single virtual session can cover multiple locations if the training is for managers who then cascade to staff
4. Remind merchant: PAIGE reduced training from 2 weeks to 1-2 days, RUDSAK trained staff in 2 hours. Shopify POS is fast to learn — the risk is not complexity, it's not scheduling time

**What to communicate:**
- "Training is one of the last things that tends to get scheduled, and one of the first things that creates stress on launch day. Can we lock in a date this week? A 2-hour session for managers is usually enough to get stores ready."

**Tracker update:** Flag the `POS Staff Training` phase milestones as at-risk. Add a `staff` risk if no date is confirmed. Update once training is scheduled.

---

## Playbook 8 — Scope Creep (New Requirements Appearing Late)

**Triggers:** Merchant or partner introduces a new requirement not in the original scope (custom integrations, custom POS features, additional locations, new brands).

**Severity escalation:**
- Med if the requirement is post-launch and doesn't affect the go-live milestone
- High if the requirement affects a Phase 1 milestone or needs to be built before go-live
- Critical if the requirement is a blocker that was not scoped and has no clear owner or timeline

**Immediate SE actions:**
1. Confirm whether the requirement was in the VTP. If yes, flag that it was already scoped and ask why it's coming up now. If no, this is formal scope creep.
2. Assess: is this a "nice to have" or a "can't go live without it"? Most late requirements are nice-to-have — document them for Phase 2
3. If it's a genuine blocker: who builds it? The partner needs to confirm capacity and provide a timeline before it can be added to the tracker
4. Protect the go-live date: add the new item to the risk register as a `scope` risk and make it explicit that it does not affect the Phase 1 date unless the partner confirms capacity and timeline by [specific date]

**Tracker update:** Add a `scope` risk. Log the new requirement as an Open Question pending partner/merchant confirmation. Do not add new milestones until the requirement is formally confirmed in scope.
