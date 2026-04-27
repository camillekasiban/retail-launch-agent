# Shopify VTP Template — Reference

**Source:** Shopify internal "Vetted Technical Plan" template V2.2
**Purpose:** This template documents the technical strategy agreed between a merchant and Shopify during the pre-sales/pre-implementation phase. When a merchant has a filled-in VTP, it is the highest-quality source of ground truth for scope, integration landscape, go-live dates, and POS specifics.

---

## Document Structure

A VTP is organized into these major sections. When reading a merchant's VTP, extract signal from each section as noted below.

---

### Project Description
Free-text paragraph. Extract:
- Customer identity and core business (brand, vertical, scale)
- Strategic initiative (replatforming, expansion, adding POS, etc.)
- Current platform if replatforming

---

### Project Scope
Bullet list of what is and is not in scope. Extract:
- **Brands in scope** — how many brands, which ones
- **Implementation partner** — name of SI; if none, flag as a risk (merchant self-implementing)
- **Markets and currencies** launching
- **Target initial go-live date** — authoritative date; supersedes any other source
- **Explicitly out of scope** — note anything that could resurface as a scope risk later

---

### Key Timelines
Table: Store/Brand Name | Estimated Launch Date | High Level Product Areas | Scoped. Extract:
- All phase dates and which brands/channels they cover
- Whether each item was formally scoped (Yes/No)
- Flag any launch dates that appear in the timeline but are marked "not scoped"

---

### Solution Outline — Retail & POS
**This is the most important section for POS launch tracking.** Extract:
- **Number of retail locations** and whether they also fulfill online orders
- **POS customizations required** — any custom tile, UI extension, or non-native POS behavior
- **Custom app development** — what partner is building, who owns it
- **Commission or employee discount logic** — custom POS workflows that add configuration complexity
- **Unique POS policies** — cash handling, holds, item alerts, ship-to-home routing, etc.
- Any limitation callouts Shopify flagged (e.g., "Shopify supports only 1 salesperson per item")

Risk signals:
- Custom tiles or UI extensions = integration/scope risk if not already built
- Multiple complex POS workflows = training and testing risk
- No named partner for POS customizations = delivery risk

---

### Solution Outline — Payments, Taxes & Checkout
Extract:
- **Primary payment gateway** — Shopify Payments (preferred), or third-party processor
- **Countries/markets** for payment processing
- **Gift card provider** — native Shopify or third-party (GiveX, Cashstar, etc.)
- **Tax provider** — Shopify Tax, Avalara, Vertex, other
- Any non-standard payment methods (ACH, PO, invoicing) — note if unsupported natively

POS-specific signals:
- Non-Shopify gift card provider = gift card migration/integration milestone required
- Third-party processor = Tap to Pay may not apply; hardware setup more complex

---

### Solution Outline — Inventory & Locations
Extract:
- **Total inventory location count** — relevant for Shopify's 1000-location limit
- **Inventory system of record** — Shopify native, IMS, ERP
- **Update frequency** — real-time, batch, hourly
- **BOPIS configuration** — yes/no, which locations
- **Order routing rules** — any custom routing logic (extensions, middleware)

---

### Solution Outline — Data Migration & Integrations
Extract:
- **ERP** — name, integration method (Celigo, custom middleware, etc.)
- **OMS** — if separate from Shopify
- **Loyalty program** — name, whether it extends to POS
- **Historical order migration** — yes/no, scope
- **Customer migration** — yes/no, from where
- **Gift card migration** — legacy balances to migrate (yes/no, provider)

For POS: loyalty, gift cards, and historical orders are the migration milestones most likely to block go-live if not scoped early.

---

### Solution Outline — Subscriptions, B2B, Order Management, Customer Accounts
Extract only if relevant to POS:
- Subscriptions: usually not POS-relevant; note if subscription orders can be placed in-store
- B2B: note if POS is expected to support B2B pricing or draft orders for sales reps
- Customer accounts: note if in-store login uses SSO or a third-party identity provider

---

### Professional Services Summary
Extract:
- **Service tier** — Complimentary Implementation Consulting (Enterprise) vs. Partner Powered (Plus)
- **SA name** if assigned
- This determines how much Shopify involvement to expect post-sale

---

### RACI Chart
Extract:
- Implementation partner name (in column header)
- For Retail & POS row: who is R (responsible) — merchant, partner, or Shopify
- Flag if Shopify is marked R on any Retail & POS item (unusual, worth noting)

---

### Merchant Stakeholders
Extract contact names for:
- Executive Sponsor
- Lead Technical Stakeholder
- Project Manager

These become relevant for escalation paths if risks go unresolved.

---

## How the Agent Uses a VTP

When `merchants/[Name]/vtp.md` exists:

1. **During `add merchant`**: Read the VTP to pre-populate launch target date, partner name, brand count, and any known POS customizations into `launch-tracker.md` frontmatter and the Decisions Log.

2. **During `process intake`**: Before extracting signals from intake documents, read `vtp.md` for context. Use it to:
   - Validate whether a mentioned integration was in scope
   - Identify whether a "new" risk is actually a known VTP constraint
   - Catch scope creep (intake mentions something that was explicitly out of scope in the VTP)

3. **During `update health` and `show acceleration opportunities`**: Reference the VTP's Retail & POS section to understand what custom work is in flight vs. still to be built.

4. **Never overwrite VTP data with intake data.** The VTP is a baseline; intake tracks changes from that baseline. If an intake document contradicts the VTP (e.g., a new partner, a changed go-live date), log it as a Decision and flag it as a scope risk if appropriate.
