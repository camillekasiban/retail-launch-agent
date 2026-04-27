# Milestone Framework
# Shopify POS Implementation Plan — Camille Kasiban, Large Segment SE

<!-- Derived from: Shopify Launch Workbook V3 (POS Only Implementation Plan) -->
<!-- Last synced: 2026-04-13 -->
<!-- Owner: Camille Kasiban -->

## Framework Version
**Version:** 2.0 (Camille's actual framework — sourced from Launch Workbook V3)
**Last Updated:** 2026-04-13
**Owner:** Camille Kasiban

---

## Phase 1 — Getting Started

| Milestone | Description | Exit Criteria |
|---|---|---|
| Admin access configured | Project stakeholders added as Shopify user accounts with correct roles | All implementation team members can log in to Admin |
| Sandbox / dev environment created | Development store or sandbox set up for testing prior to production | Dev environment active and accessible to implementation team |
| POS Sales Channel added | POS Sales Channel installed in Shopify Admin | POS channel visible in Admin sidebar |
| Locations configured | All physical POS locations added in Admin | Locations match merchant's physical stores; inventory routing set correctly |
| Hardware ordered | All POS hardware ordered (terminals, card readers, receipt printers, barcode scanners) | PO or order confirmation on file; estimated delivery date confirmed |

## Phase 2 — Data Migration & Integrations

| Milestone | Description | Exit Criteria |
|---|---|---|
| Products migrated | Full product catalog migrated to Shopify; barcodes verified for POS scanning | Products visible in POS Sales Channel; barcodes scan correctly in POS app |
| Inventory quantities migrated | Opening inventory counts loaded per location | Inventory quantities match source of truth system at time of migration |
| Customers migrated | Customer records migrated to Shopify | Customer accounts accessible; loyalty data attached if applicable |
| Orders migrated | Historical orders migrated (if required; 3rd party app or API) | Order history accessible in Admin for returns/lookups |
| Discounts and promotions configured | All discount codes, automatic discounts, and gift card rules set up manually | Test discount applies correctly in POS |
| Software integrations connected | All tech stack integrations (ERP, OMS, loyalty, etc.) connected and tested | Bidirectional data flow confirmed; no duplicate records |

## Phase 3 — Admin Set Up

| Milestone | Description | Exit Criteria |
|---|---|---|
| Payments configured | Shopify Payments approved and activated, or 3rd party gateway connected | Test transaction successful; payout account confirmed |
| Delivery and BOPIS configured | Delivery methods, buy online pick up in store, and ship-to-customer rules set up | BOPIS order flows correctly from POS and online |
| Order routing rules configured | Routing rules set to assign fulfillment to correct locations | Test order routes to expected location |
| Tax IDs and exemptions set up | All applicable tax registration IDs and exemption rules configured | Test transaction shows correct tax in all states/regions |
| Email notifications reviewed | Email notification templates reviewed and customized if needed | Merchant has approved or accepted default templates |
| POS staff roles and permissions created | Custom POS staff roles defined with correct permission levels | Role definitions match merchant's management hierarchy |
| POS staff accounts created | All POS staff user accounts created and assigned to correct roles | Every staff member can log in with their own credentials |
| Receipts customized | Receipt header, footer, and return policy text approved by merchant | Merchant email approval on file |
| POS checkout requirements configured | Required customer info at checkout, receipt delivery preference set | Checkout flow matches merchant's operational requirements |
| POS terminal view configured | Homescreen tiles, product layout, and app customizations set up on all devices | Merchant or store manager has approved layout |
| Product availability confirmed on POS | All required products confirmed as available in POS Sales Channel | No missing products on POS; variants display correctly |
| Third-party apps installed | All agreed POS apps installed and configured (e.g., Matrixify, Rewind, loyalty apps) | Apps functional in both Admin and POS app |

## Phase 4 — Point of Sale Set Up (On Device)

| Milestone | Description | Exit Criteria |
|---|---|---|
| POS app installed on all devices | Shopify POS app installed and updated to latest version on all devices | Every device running current POS version |
| Firewall and MDM checks complete | Network firewall rules verified; MDM settings allow POS app to function | POS app connects to Shopify without restrictions |
| Hardware connected | All card readers, receipt printers, barcode scanners, and cash drawers connected | Each device has confirmed hardware connections |
| Gift cards enabled | Shopify Gift Cards enabled in Admin and POS | Test gift card purchase and redemption successful |
| Custom payment methods set up | Store credit, IOUs, external gift cards, or other custom payment types configured | Custom payment method appears and processes correctly in POS |

## Phase 5 — Testing

| Milestone | Description | Exit Criteria |
|---|---|---|
| Login and permissions tested | All staff log in with credentials and PINs; QR code login tested; location switching verified | Each role confirmed with expected permission level |
| Sales flows tested | All key sales scenarios tested: simple sale (cash + card), split payment, discount (code/manual/line item), ship-to-customer | All scenarios complete without errors; receipts accurate |
| Draft orders and holds tested | Draft order created, saved, emailed, and retrieved from POS | Draft order flow end-to-end confirmed |
| Returns and exchanges tested | Return and exchange processed; refund confirmed in Admin | Refund appears correctly; inventory adjusted |
| Gift card tested | Gift card sold, redeemed, and balance checked | Gift card balance accurate after purchase and partial redemption |
| Third-party app tiles tested | All POS app integrations tested from within POS | No errors; data flows between POS and app correctly |
| Daily operations tested | Register tracking session opened and closed; cash adjustments made; end-of-day report printed | Store manager can run full open-to-close process independently |
| Hardware verified per location | Card reader, receipt printer, barcode scanner, and cash drawer tested at each location | Every piece of hardware functional at every location |

## Phase 6 — POS Staff Training

| Milestone | Description | Exit Criteria |
|---|---|---|
| Test results reviewed and processes documented | Testing phase results reviewed; any unique merchant processes or workarounds documented for training | Documentation shared with trainer and store managers |
| Training materials organized | Training resources compiled (Shopify training links, merchant-specific process docs) | Training materials sent to store managers ahead of session |
| Staff training completed | All frontline POS staff trained; practice transactions completed | Training attendance log on file; store manager sign-off |

## Phase 7 — Launch

| Milestone | Description | Exit Criteria |
|---|---|---|
| Delta data migration complete | Final inventory counts, pricing changes, and new products synced since initial migration | Stock counts match source of truth on launch day |
| Gift cards migrated | Any legacy gift card balances loaded into Shopify (3rd party app or API required) | Gift card import confirmed; balances match legacy system |
| Device launch readiness check complete | Per-store device check: OS version, POS app version, app permissions, Bluetooth on, hardware connected | All devices green for every location going live |
| First transaction processed | First real customer transaction processed on Shopify POS | Transaction ID documented; receipt confirmed |
