# Shopify POS — Native Capabilities vs. Requires Extension

**Purpose:** Use this when a merchant's VTP or intake documents describe POS requirements to quickly assess whether something is natively supported, needs a third-party app, or requires custom development. Informs scope risk flagging and partner capacity assessment.

---

## How to Use This Reference

When a merchant describes a POS requirement, find it in the table below:
- **Native** — configurable in Shopify Admin or POS settings, no development needed
- **App** — available via a third-party app from the Shopify App Store (see `references/pos-app-ecosystem.md`)
- **UI Extension** — requires a custom tile or extension built by a Shopify Partner developer (scope + delivery risk)
- **Not supported** — not currently possible on Shopify POS; needs a workaround or acceptance

If a requirement is UI Extension or Not Supported, flag it as a `scope` risk with High severity and confirm the partner has POS extension experience.

---

## Payments & Checkout

| Requirement | Support Level | Notes |
|---|---|---|
| Accept credit/debit cards via Shopify Payments | Native | Card reader required |
| Tap to Pay (contactless on iPhone/Android) | Native | No card reader needed |
| Third-party payment processor | Native | Configure in Admin → Settings → Payments |
| Manual/custom payment methods (cash, check, store credit) | Native | Add in POS settings |
| Split tender (multiple payment methods per transaction) | Native | Built into POS checkout |
| Tipping | Native | Configure % options in POS settings |
| Discount codes | Native (Lite + Pro) | |
| Manual discounts ($ or %) | Native (Lite + Pro) | |
| Automatic discounts (BOGO, spend thresholds) | Native (Pro only) | |
| Gift card sell and redeem | Native (Lite + Pro) | Shopify native gift cards only |
| Gift card redemption from third-party provider (GiveX, Cashstar) | UI Extension | Custom integration to query external gift card balance |
| Exchanges | Native (Pro only) | |
| Refunds | Native (Lite + Pro) | |
| Layaway / deposits | Not natively supported | Workaround: draft order with partial payment |
| Order holds / save cart | Native (Pro only) — Save/retrieve cart | Basic cart hold; no storage location tracking |
| Item holds with custom storage location tracking | UI Extension | Custom tile to assign and track hold location |

---

## Staff & Permissions

| Requirement | Support Level | Notes |
|---|---|---|
| Staff PINs | Native (Lite + Pro) | |
| Staff roles and permissions | Native (Pro only) | |
| Manager override (discounts, refunds) | Native (Pro only) | Tied to staff permissions |
| Unlimited POS-only staff | Native (Pro only) | |
| Sales attribution (which staff made the sale) | Native (Pro only) | Single staff per transaction |
| Split commission (multiple staff per transaction) | UI Extension | Custom tile required; data sent to external commission system |
| Employee discount with annual balance tracking | UI Extension | Custom tile + backend to track and decrement balance |
| Staff scheduling and payroll | App | e.g., Easyteam, Deputy |
| Staff performance dashboards beyond POS analytics | App | e.g., Better Reports |

---

## Inventory & Products

| Requirement | Support Level | Notes |
|---|---|---|
| Inventory lookup across locations | Native (Lite + Pro) | |
| Real-time inventory sync with ERP | Requires integration | Celigo, Patchworks, or custom middleware — not a POS setting |
| Stock transfers between locations | Native (Pro only) — via Stocky | |
| Stocktakes / cycle counts | Native (Pro only) — via Stocky | |
| Barcode scanning | Native (camera) or Hardware | Camera scan is free; dedicated scanner for high volume |
| Product bundles at POS | App | Shopify Bundles app (native app, free) |
| Endless aisle (browse full catalog, not just in-store stock) | Native (Pro only) — Ship to home | Customers can order out-of-stock items for home delivery |
| Product holds with inventory decrement | UI Extension | Custom tile to place hold and adjust inventory state |
| Product alert popup when specific item added to cart | UI Extension | Custom tile to trigger contextual alerts |
| Virtual product options / combined listings at POS | Limited | Test carefully; combined listings behavior at POS can differ from online |

---

## Fulfillment

| Requirement | Support Level | Notes |
|---|---|---|
| Ship to home from store | Native (Pro only) | |
| Local pickup (BOPIS) | Native (Pro only) | |
| Local delivery | Native (Pro only) | |
| Curbside pickup | Native (Pro only) | Variant of local pickup |
| Custom order routing rule (e.g., always route ship-to-home back to originating store) | UI Extension | Custom attribute on order + custom routing rule via extension |
| In-store pickup notifications to customer | Native | Via Shopify order notifications |

---

## Customer Experience

| Requirement | Support Level | Notes |
|---|---|---|
| Customer profiles (view/edit) | Native (Lite + Pro) | |
| Customer purchase history | Native (Lite + Pro) | Online + in-store unified if on same store |
| Email/SMS receipts | Native (Lite + Pro) | |
| Custom printed receipts | Native (Pro only) | |
| Customer-facing display (Customer View app) | Native (Lite + Pro) | Shows cart total to customer during checkout |
| Loyalty points earn/redeem | App | Requires a POS-compatible loyalty app (see app ecosystem reference) |
| Email capture / SMS opt-in at checkout | App or UI Extension | Some loyalty apps include this; custom via UI Extension |
| Signature capture on refunds | UI Extension | Customer-facing via Customer Extensions (customer display) |
| Age verification prompt | UI Extension | Custom tile to prompt and confirm age before proceeding |
| Gift card consolidation / balance top-up | UI Extension | Custom tile to look up balance, add top-up to cart |

---

## Reporting & Analytics

| Requirement | Support Level | Notes |
|---|---|---|
| Daily sales reports | Native (Pro only) | |
| In-app retail store analytics | Native (Pro only) | |
| End-of-day cash reconciliation | Native (Lite + Pro) — Cash tracking | |
| Advanced reporting (custom date ranges, staff performance, product) | App | e.g., Better Reports, Polar Analytics |
| Real-time cash drawer balance alerts to LP team | UI Extension / Custom App | Custom app to query Cash Tracking API and push notifications |

---

## Integrations

| Requirement | Support Level | Notes |
|---|---|---|
| ERP sync (products, inventory, orders) | Integration required | Celigo, Patchworks, Acumatica, custom middleware |
| OMS integration | Integration required | Typically via webhooks or middleware |
| Loyalty platform (external) | App or UI Extension | POS-compatible loyalty apps exist; deep integrations may need extension |
| External gift card provider | UI Extension | Custom tile to query and update external gift card system |
| Loss prevention / cash monitoring alerts | Custom App | Query Cash Tracking API; push to email or Teams |
| Appointment booking tied to POS checkout | App | e.g., Sesami, Appointo — some integrate with POS |

---

## Risk Signals for Scope Assessment

Flag as **High scope risk** if any of the following appear in intake or the VTP:

- Commission split between multiple staff per transaction
- Employee discount with annual balance cap
- External gift card provider (GiveX, Cashstar, etc.) needing POS redemption
- Item holds with storage location tracking
- Custom popup alerts on specific product types
- Age verification at POS
- Signature capture on refunds
- Cash drawer balance alerts to a security or LP team
- Custom ship-to-home routing logic
- Any "we currently do X in our existing POS" that isn't in the Native column above

Each of these requires a UI Extension or custom app. The partner must confirm:
1. They have POS UI Extension development experience
2. The custom work is scoped and in their SOW
3. A timeline exists before configuration milestones begin
