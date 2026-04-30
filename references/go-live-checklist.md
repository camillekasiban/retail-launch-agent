# POS Go-Live Checklist

**Purpose:** Use this during the final 48 hours before a merchant's go-live date to confirm launch readiness. The agent should reference this when generating next steps for merchants within 14 days of launch, and when the user asks "is [Name] ready to go live?"

Run each check per location, per brand where applicable. A single failing item in a required category should be flagged as a Critical risk.

---

## T-48 Hours (2 Days Before Launch)

### Staff Readiness
- [ ] All store staff accounts created in Shopify Admin
- [ ] All staff have logged into POS app on their device and confirmed access
- [ ] Staff PINs set and tested per device
- [ ] Manager override permissions tested (approve discounts, process refunds)
- [ ] Training completed and signed off — confirm no staff first touching POS on launch day

### Hardware
- [ ] All devices (iPads/phones) have Shopify POS app installed and updated to latest version
- [ ] Card readers paired, tested, and processing test transactions
- [ ] Receipt printers connected and printing test receipts
- [ ] Cash drawers connected and triggering on cash sales
- [ ] Barcode scanners connected and reading product barcodes
- [ ] All hardware tested per location — not just one device

### Connectivity
- [ ] WiFi confirmed stable at all POS stations
- [ ] Firewall and MDM checks complete — Shopify POS domains whitelisted
- [ ] Offline mode tested: device processes cash sales when WiFi is disconnected

### Inventory
- [ ] Product catalog visible and correct on POS Sales Channel per location
- [ ] Inventory quantities correct per location in Shopify
- [ ] Any products that should NOT be available on POS are excluded

---

## T-24 Hours (Day Before Launch)

### Payments
- [ ] Shopify Payments enabled for POS (not just D2C)
- [ ] Test transaction processed and refunded on each card reader
- [ ] Tap to Pay tested if applicable
- [ ] Gift card redemption tested end-to-end
- [ ] Custom payment methods configured (cash, store credit, check if applicable)

### Checkout Configuration
- [ ] Tipping settings confirmed (on/off, percentage options)
- [ ] Receipt delivery preference configured (email, SMS, print, no receipt)
- [ ] Tax rates confirmed correct for each store location
- [ ] Discount codes tested at POS — at least one manual and one automatic (if Pro)
- [ ] Exchanges flow tested end-to-end (Pro only)
- [ ] Returns flow tested — refund to original payment method

### Fulfillment (if applicable)
- [ ] BOPIS orders visible in POS and can be marked as picked up (Pro only)
- [ ] Ship to home orders can be initiated from POS (Pro only)
- [ ] Order routing rules confirmed — POS orders routing to correct location

### Data
- [ ] Customer profiles accessible in POS — search and pull up a customer
- [ ] Order history visible per customer
- [ ] Any loyalty program integration tested (customer earns/redeems points at POS)

---

## Launch Day Morning (Before Doors Open)

### Per Location Sign-Off
- [ ] Opening cash count entered in POS cash tracking
- [ ] At least one staff member confirmed signed in and ready per location
- [ ] Store manager has confirmed they can process a transaction
- [ ] SE or partner on standby contact info shared with store manager

### Final Sanity Check
- [ ] POS app version is current (no pending update that could disrupt launch day)
- [ ] Internet connectivity confirmed at each location
- [ ] Backup plan confirmed: if card reader fails, what's the fallback? (manual entry, Tap to Pay, etc.)
- [ ] Merchant knows how to reach Shopify support (help.shopify.com, in-app support)

---

## First Transaction

- [ ] First real transaction processed per location
- [ ] Receipt delivered correctly
- [ ] Order appears in Shopify Admin
- [ ] Inventory decremented correctly
- [ ] Payment captured correctly in Shopify Payments

**Note the time and order number of the first transaction per location in the merchant's launch-tracker.md Decisions Log.**

---

## End of Day 1

- [ ] Closing cash count completed and session closed in POS
- [ ] End-of-day sales report reviewed — figures look correct
- [ ] Any issues encountered documented in the merchant's risk register
- [ ] SE completes a quick debrief with merchant/partner: what worked, what didn't

---

## Post-Launch Hypercare (Days 2–14)

Check in with the merchant/partner every 2-3 days for the first 2 weeks:

- [ ] No transaction failures or payment processing errors
- [ ] Staff not encountering repeated login or permission issues
- [ ] Hardware performing reliably across all locations
- [ ] Inventory counts remaining accurate
- [ ] Any open risks from pre-launch resolved or formally accepted

**When to formally close the launch:**
- All go-live checklist items confirmed complete
- No Critical or High risks remain open
- Merchant has processed at least 3 days of transactions without incident
- End-of-day reporting confirmed working

Update `launch-tracker.md`: set "First transaction processed" to Complete, add a Decisions Log entry confirming go-live date and any notable issues, and update health to GREEN if criteria are met.

---

## Common Launch Day Issues and Quick Fixes

| Issue | First action |
|---|---|
| Card reader not pairing | Force-quit POS app, reopen, re-pair in Settings → Hardware |
| Staff can't log in | Confirm staff account exists in Admin and has POS access enabled |
| Products not showing at POS | Confirm products are available on POS Sales Channel and at the specific location |
| Payments not processing | Confirm Shopify Payments is enabled for POS in Admin → Settings → Payments |
| Receipt printer not printing | Check Bluetooth/network connection; confirm correct printer selected in POS Settings |
| Inventory not decrementing | Confirm product inventory tracking is enabled (not "Don't track inventory") |
| BOPIS orders not appearing | Confirm local pickup is enabled for the location in Admin → Settings → Shipping and delivery |
