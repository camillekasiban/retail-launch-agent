# Shopify POS Pro vs POS Lite — Feature Reference

**Source:** Shopify internal retail-launch resource
**Purpose:** Use this to identify plan gaps during intake processing, flag scope risks when a merchant's requirements exceed POS Lite, and confirm plan eligibility before milestone completion.

---

## Pricing

| Plan | Cost |
|---|---|
| POS Lite | Free — included with every Shopify plan |
| POS Pro | $89/month per location (or discounted annually) |

Perry Ellis example: 5 Phase 1 locations × $89 = $445/month for Pro. Factor this into conversations when a merchant hasn't confirmed their plan.

---

## Feature Comparison

| Feature | Lite | Pro |
|---|---|---|
| Integrated payment hardware (Shopify Payments) | ✅ | ✅ |
| Non-payment retail hardware (printers, scanners, cash drawers) | ✅ | ✅ |
| Customizable smart grid | ✅ | ✅ |
| Add/edit customer profiles | ✅ | ✅ |
| Customer View app (customer-facing display) | ✅ | ✅ |
| Multi-location inventory, orders, and customer management | ✅ | ✅ |
| Email/SMS receipts | ✅ | ✅ |
| **Custom printed receipts** | ❌ | ✅ |
| Discount codes and manual discounts | ✅ | ✅ |
| **Automatic discounts** | ❌ | ✅ |
| Sell and redeem gift cards | ✅ | ✅ |
| Camera barcode scanning | ✅ | ✅ |
| Custom sales | ✅ | ✅ |
| Offline cash payments | ✅ | ✅ |
| Staff PINs | ✅ | ✅ |
| **Retail staff permissions and role management** | ❌ | ✅ |
| **Unlimited POS-only staff** | ❌ | ✅ |
| **Sales attribution** | ❌ | ✅ |
| Refunds | ✅ | ✅ |
| **Exchanges** | ❌ | ✅ |
| Cash tracking | ✅ | ✅ |
| **Save/retrieve cart (draft orders at POS)** | ❌ | ✅ |
| Email carts | ✅ | ✅ |
| **Ship to home (ship from store)** | ❌ | ✅ |
| **Local pickup (BOPIS)** | ❌ | ✅ |
| **Local delivery fulfillment** | ❌ | ✅ |
| **Advanced inventory management (Stocky)** | ❌ | ✅ |
| **Daily sales reports** | ❌ | ✅ |
| **In-app retail store analytics** | ❌ | ✅ |

---

## Risk Signals — Flag These During Intake

If a merchant mentions any of the following and their plan is not confirmed as POS Pro, flag as a **Medium scope risk**:

| Merchant says... | Requires | Risk if on Lite |
|---|---|---|
| "Staff will have different permission levels" | Staff permissions | Admin-level access for all staff — security risk |
| "Managers need override capabilities" | Staff permissions | No role differentiation possible |
| "We want exchanges at POS" | Exchanges | Can only do refund + new sale — friction for staff and customers |
| "We want BOPIS / buy online, pick up in store" | Local pickup | Not available — blocks omnichannel fulfillment milestone |
| "Ship to home from store" | Ship to home | Not available — blocks ship-from-store milestone |
| "Automatic promotions / tiered discounts" | Automatic discounts | Only manual discount codes — can't automate buy X get Y |
| "We want custom branded receipts" | Custom printed receipts | Email/SMS receipts only |
| "Sales reps need to save carts / put things on hold" | Save/retrieve cart | No cart holds at POS |
| "We want to see store-level analytics in the app" | In-app analytics | No reporting in POS app |
| "We have commission tracking" | Sales attribution | Can't attribute sales to staff members |
| Many store staff members | Unlimited POS-only staff | Lite has a staff limit |

---

## Common Plan Scenarios

**Scenario: Merchant is D2C-live and adding POS for the first time**
- Their Shopify plan is likely Plus or Basic — POS Lite is included
- They almost certainly need Pro for staff permissions, exchanges, and BOPIS
- Flag plan upgrade as a milestone dependency before POS Set Up phase begins

**Scenario: Merchant already has POS Lite from a previous pilot**
- Confirm which features they're actually using
- If they're running pilot stores without staff permissions, that works on Lite — but enterprise rollout needs Pro
- Upgrade is per-location, so they can upgrade Phase 1 locations now and Phase 2 later

**Scenario: Merchant asks "do we need Pro?"**
Answer YES if they need ANY of: exchanges, BOPIS, ship-to-home, staff roles/permissions, automatic discounts, save cart, custom receipts, or analytics.
Answer MAYBE if they're a simple single-location cash-and-carry with no complex requirements — but most retailers at this scale need Pro.

---

## Milestone Dependencies

These milestones in the launch tracker require POS Pro to complete:

| Milestone | Why Pro is required |
|---|---|
| POS staff roles and permissions created | Feature is Pro-only |
| Delivery and BOPIS configured | Local pickup is Pro-only |
| POS checkout requirements configured | Exchanges and save/retrieve cart are Pro-only |
| Receipts customized | Custom printed receipts are Pro-only |
| Daily operations tested | Analytics and sales attribution require Pro |

If a merchant is on Lite and these milestones are marked In Progress or Complete, flag as a data integrity issue — they may not actually have access to those features.
