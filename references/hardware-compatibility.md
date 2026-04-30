# Shopify POS Hardware Compatibility

**Source:** Shopify Help Center (help.shopify.com/en/manual/sell-in-person/hardware)
**Purpose:** Reference when assessing hardware risks, reviewing the "Hardware ordered" and "Hardware connected" milestones, and advising on firewall/MDM configuration.

---

## Card Readers

| Device | Connectivity | Notes |
|---|---|---|
| Tap & Chip Card Reader | Bluetooth | Contactless (NFC), chip, and swipe. Available in US, CA, UK, IE, AU, and others. Recommended for most merchants. |
| WisePad 3 | Bluetooth | Chip and PIN focus. Common in markets outside the US. |
| Tap to Pay on iPhone | Built-in (no hardware needed) | Accepts contactless cards and digital wallets directly on iPhone. No card reader required. Available in US, CA, UK, AU, and others. Useful as a backup or for mobile staff. |
| Tap to Pay on Android | Built-in (no hardware needed) | Same as above but on Android devices. |
| Shopify POS Go | Built-in | All-in-one Android device with built-in card reader and barcode scanner. **⚠️ Discontinued — existing units supported until September 2026 only. Do not recommend for new orders.** |

**Risk signal:** If a merchant's hardware order includes Shopify POS Go units, flag immediately — support ends September 2026 and they should be ordering the Tap & Chip Reader + separate device instead.

---

## Receipt Printers

| Device | Connectivity | Notes |
|---|---|---|
| Star Micronics mC-Print3 | Bluetooth, USB, LAN | Most commonly deployed. Compact and reliable. |
| Star Micronics TSP143III | Bluetooth, USB, LAN | Widely used alternative. |
| Epson TM-m30II | Bluetooth, USB, LAN | Compact design, works well in tight counter setups. |

**Note:** Most receipt printers also have a cash drawer port — the cash drawer is triggered by the printer, not connected directly to the device.

---

## Cash Drawers

Cash drawers connect to a supported receipt printer via a cable (RJ11/RJ12 port) — they are not independently paired to the iPad or POS app. When configuring cash tracking, confirm that:
1. A compatible receipt printer is already set up
2. The cash drawer cable is connected to the printer's DK port
3. Cash tracking is enabled in POS Settings

There is no standalone USB or Bluetooth cash drawer that works directly with Shopify POS without a printer.

---

## Barcode Scanners

| Device | Connectivity | Notes |
|---|---|---|
| Socket Mobile CHS 7Ci | Bluetooth | Wireless, 1D barcodes. Lightweight, retail-friendly form factor. |
| Socket Mobile S700 | Bluetooth | 2D barcodes (QR codes + standard barcodes). |
| Zebra CS6080 | Bluetooth/USB | 2D barcode scanner. Handheld, common in higher-volume retail. |

**Alternative:** The Shopify POS app supports camera-based barcode scanning on iPhone/iPad at no extra cost — available on both Lite and Pro. For low-volume merchants, this may be sufficient without purchasing a dedicated scanner.

---

## Device Requirements

### iPad (recommended primary device)
- iPadOS 16 or later required
- Compatible models: iPad (6th gen+), iPad mini (5th gen+), iPad Air (3rd gen+), iPad Pro (all models)
- Shopify recommends a dedicated stand (Shopify Stand, or third-party compatible stand) for fixed checkout stations

### iPhone
- iOS 16 or later required
- Best suited for mobile or floor staff, not primary checkout stations

### Android
- Android 8.0 (Oreo) or later required
- Used primarily for Tap to Pay on Android and POS Go (discontinued)

---

## Network Requirements

### Domains to Whitelist (add all ports)

The following domains must be on the firewall allow list for Shopify POS to function:

```
shopify.com
shopifyapps.com
shopifycs.com
shopifysvc.com
shopifyinc.com
shopifycloud.com
myshopify.com
pos.api.myshopify.com
cdn.shopify.com
extensions.shopifycdn.com
stripe.com
stripecdn.com
stripe.network
hcaptcha.com
bbpos.com
bugsnag.com
clients3.google.com
storage.googleapis.com
[merchant's custom domain(s)]
```

### Ports to Keep Open

```
4443
8080
27000
27001
```

### Geographic IP Filtering

**Must be disabled.** Shopify POS services are hosted globally — geographic IP blocking will intermittently break POS functionality even if all domains are whitelisted.

### DNS

If DNS errors occur, configure devices to use:
- Cloudflare: `1.1.1.1` and `1.0.0.1`
- Google: `8.8.8.8` and `8.8.4.4`

### WiFi Recommendations

- Dedicate a separate SSID for POS devices where possible — prevents consumer/guest traffic from competing with payment processing
- Minimum recommended: stable 10 Mbps connection per active POS station
- Test offline mode: confirm the POS app can process cash sales when WiFi is disconnected

---

## MDM Considerations

For merchants with 5+ locations or corporate IT policies:

| Consideration | Guidance |
|---|---|
| Auto-lock policy | MDM-enforced device lock can override POS and lock devices mid-transaction. Disable auto-lock for POS devices, or set a long timeout (30+ minutes). |
| App management | POS app must be on the approved app list. Ensure MDM won't block updates. |
| VPN | Corporate VPN on POS devices can interfere with payment processing. Test with VPN on and off; most merchants exclude POS devices from VPN policy. |
| App whitelisting | Confirm Shopify POS app ID is on the MDM approved list before device setup begins. |

The "Firewall and MDM checks complete" milestone in the launch tracker should not be marked Complete until all of the above have been verified for each Phase 1 location.

---

## Hardware Risk Signals

Flag these as risks during intake processing:

| Signal | Risk | Category | Severity |
|---|---|---|---|
| Hardware order not yet placed with < 4 weeks to go-live | Delivery timeline at risk | hardware | Med |
| Hardware ETA not confirmed | Can't validate setup timeline | hardware | Med |
| Hardware ETA within 10 days of go-live | No buffer for setup/testing | hardware | High |
| Shopify POS Go units ordered | Support ends Sept 2026 | hardware | High |
| No dedicated WiFi for POS | Network stability risk | hardware | Med |
| IT team hasn't reviewed firewall requirements | Potential launch-day connectivity failure | hardware | Med |
| MDM policy not assessed for POS devices | Auto-lock or VPN may break POS | hardware | Med |
| Corporate VPN on POS devices | Payment processing interference | hardware | Med |
