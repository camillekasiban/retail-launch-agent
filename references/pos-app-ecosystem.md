# Shopify POS App Ecosystem

**Source:** Shopify App Store — "Works with Shopify POS" collection (90+ apps)
**Purpose:** Reference when reviewing the "Third-party apps installed" milestone, when a merchant's VTP lists integrations, or when generating acceleration opportunities around extending POS capabilities. All apps listed here are verified to work with Shopify POS.

**Important:** App availability, pricing, and POS compatibility change frequently. Always verify on the Shopify App Store before recommending to a merchant.

---

## Loyalty & Rewards

The most commonly requested POS extension category. A loyalty app is required for any earn/redeem at POS — this is not native Shopify POS functionality.

| App | What it does | Notes |
|---|---|---|
| **Smile: Loyalty & Rewards** | Points, VIP tiers, referrals — earns and redeems at POS | One of the most widely deployed; strong POS integration |
| **Yotpo: Loyalty & Rewards** | Points, rewards, referrals | Often paired with Yotpo Reviews; good for brands wanting a single vendor |
| **BON Loyalty** | Points, VIP tiers, referral programs | POS-compatible; often chosen for value at lower GMV |
| **Rivo: Loyalty & Rewards** | Retain customers with loyalty, rewards, and referrals | Built for Shopify; POS supported |
| **Marsello** | Omnichannel loyalty + email/SMS | Designed specifically for brands with both online and in-store; strong POS focus |
| **Growave** | Loyalty, wishlist, reviews, referrals | All-in-one; POS loyalty supported |

**When to flag:** If a merchant has an existing loyalty program (especially on a legacy POS) and expects customers to earn/redeem points on day one, this app must be installed, configured, and tested before go-live. Flag it as a milestone dependency under "Third-party apps installed."

---

## Returns & Exchanges

Native Shopify POS handles basic refunds (Lite) and exchanges (Pro). For more complex return flows (return portals, automated restocking rules, cross-channel returns), a returns app is commonly used.

| App | What it does | Notes |
|---|---|---|
| **Loop Returns** | Self-serve return portal, automated rules, exchange workflows | Used by KEEN (referenced in case studies). Strong for brands with high return volume |
| **AfterShip Returns** | Return portal, automated notifications, analytics | Good alternative to Loop; integrates with POS for in-store return visibility |
| **Return Prime** | Omnichannel returns including in-store | POS-specific return workflows |

**When to flag:** If a merchant mentions "our current system handles returns differently" or they have complex exchange/credit workflows, confirm whether native POS exchanges cover their needs or if a returns app is required.

---

## Appointments & Bookings

Required for any merchant offering in-store services, consultations, alterations, or events alongside retail.

| App | What it does | Notes |
|---|---|---|
| **Sesami** | Appointment booking, staff scheduling, service products | Integrates with POS for booking and checkout |
| **Appointo** | Appointment booking on calendar | POS-compatible booking app |
| **Evey Events & Tickets** | Create, sell, and scan event tickets | POS ticket scanning supported |
| **BookThatApp** | Bookings, rentals, tours, classes | POS integration for service checkout |

**When to flag:** Apparel brands with tailoring/alteration services, bridal (see David's Bridal case study), and specialty retail (outdoor gear fitting sessions, etc.) commonly need an appointment app. Check the merchant's VTP or intake for any mention of "services," "consultations," or "alterations."

---

## Staff & Scheduling

Handles payroll, time tracking, shift scheduling, and commission calculations that go beyond what POS Pro's built-in sales attribution provides.

| App | What it does | Notes |
|---|---|---|
| **Easyteam** | POS time clock, commissions, staff payroll, schedules | Built specifically for Shopify POS; clocks in/out from the POS app |
| **Deputy** | Shift scheduling, time tracking, payroll integration | Broader workforce management; integrates with Shopify |
| **Homebase** | Scheduling, time tracking, team communication | Widely used in retail and food service |

**When to flag:** If a merchant mentions commission tracking, shift scheduling, or payroll that needs to tie into POS sales data, flag "Third-party apps installed" as requiring one of these apps before go-live.

---

## Reporting & Analytics

POS Pro includes daily sales reports and in-app analytics, but merchants with multi-location operations or complex reporting needs often require a dedicated analytics app.

| App | What it does | Notes |
|---|---|---|
| **Better Reports** | Custom reports on sales, inventory, staff, products | Widely used for POS-specific reporting beyond native analytics |
| **Polar Analytics** | Revenue analytics, cohort analysis, marketing attribution | More D2C-focused but useful for unified online + in-store view |
| **Mipler Reports** | Advanced custom reports and exports | Good for merchants needing CSV exports for external BI tools |

**When to flag:** Multi-location merchants or those with finance/operations teams that need more than end-of-day summaries. Ask in intake: "What does your current reporting look like, and who needs access to it?"

---

## Delivery, Pickup & BOPIS (Extended)

POS Pro includes native local pickup, local delivery, and ship-to-home. These apps extend those capabilities with date pickers, routing logic, and customer-facing scheduling.

| App | What it does | Notes |
|---|---|---|
| **Zapiet — Pickup + Delivery** | Order pickup and local delivery with date/time selection | Commonly used to add scheduling to native BOPIS |
| **Pickup Delivery Date Pickeasy** | Date/time picker for store pickup and local delivery | Good for merchants where customers need to schedule pickup windows |

**When to flag:** If a merchant wants customers to select a specific pickup time (not just "available for pickup"), they'll need one of these apps on top of native BOPIS.

---

## Gift Cards (Extended)

Native Shopify gift cards (sell, redeem, check balance) work out of the box. These apps extend gift card capabilities — bulk issuance, store credit programs, or bridging to external gift card systems.

| App | What it does | Notes |
|---|---|---|
| **Rise.ai** | Gift cards, store credit, referral rewards | Stronger bulk gifting and store credit workflows than native |
| **Govalo** | Digital gift card experience, scheduling, branding | Good for merchants wanting a branded gift card experience |

**When to flag:** If a merchant is migrating from a third-party gift card system (GiveX, Cashstar, etc.) or wants to issue store credit as a return option, confirm whether native gift cards are sufficient or if Rise.ai/Govalo is needed. For legacy gift card balance migration, this is a `data-migration` risk — see risk-playbooks.md.

---

## Product Bundles

| App | What it does | Notes |
|---|---|---|
| **Shopify Bundles** (native app) | Fixed and mix-and-match bundles, splits into component SKUs at checkout | Free, made by Shopify; good starting point |
| **Bundler — Product Bundles** | Volume discounts, bundle deals, quantity breaks | More flexible pricing rules than native Shopify Bundles |
| **Simple Bundles & Kits** | Build mix-and-match bundles for 3PL fulfillment | Useful when bundles need to flow correctly to a 3PL |

**When to flag:** If a merchant sells kits, gift sets, or bundled products in-store, confirm bundles are tested at POS specifically — bundle behavior at POS can differ from online.

---

## Invoicing & Order Documents

Relevant for B2B-at-POS scenarios or merchants who need printed documentation beyond standard receipts.

| App | What it does | Notes |
|---|---|---|
| **Order Printer Pro** | PDF invoices, quotes, packing slips | Works with POS orders; useful for B2B in-store sales |
| **Vify Order Printer** | Custom invoice and order document generation | POS-compatible alternative |

---

## App Installation Milestone

The "Third-party apps installed" milestone in the launch tracker covers all of the above. When processing intake for a merchant:

1. Note every app mentioned in the VTP or intake documents
2. Check whether each app is in this reference list (POS-compatible) or needs verification
3. Flag any app not confirmed as POS-compatible as an open question
4. Each app needs its own test in the Testing phase — "app tiles tested" covers POS UI integrations

**Common gap:** Merchants often have D2C apps that don't extend to POS. Check the Shopify App Store listing for "Works with Shopify POS" before assuming a D2C app will work in-store.
