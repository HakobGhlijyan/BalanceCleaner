# BalanceCleaner

> Smart Balance Cleaner for iPhone — clear your Apple ID balance before switching regions.

[![App Store](https://img.shields.io/badge/App_Store-Coming_Soon-0D96F6?logo=apple)](https://apps.apple.com)

---

## What is BalanceCleaner?

**BalanceCleaner** is a privacy-first iOS app that helps you easily select or enter the exact custom amount you want to zero out in your Apple ID account balance — with no account registration required.

Designed for users who need to clear a leftover App Store credit (e.g., before switching to a different App Store region), BalanceCleaner provides a transparent, step-by-step experience built around clarity, control, and respect for your data.

---

## Features

### Free Tier
- **Smart Balance Cleaner** — select or enter the exact amount to clear
- **Calculate & Split** — see the precise breakdown before confirming
- **Transaction History** — basic log of all balance operations
- **Privacy Dashboard** — overview of what data exists locally

### Pro (optional upgrade)
- Full transaction history (unlimited)
- PDF export of all operations
- Advanced settings & customization
- Priority support

---

## Onboarding Screens

| Screen | Title | Description |
|--------|-------|-------------|
| 1 | Smart Balance Cleaner | Choose the exact amount to zero out your Apple account balance |
| 2 | Calculate & Split | Preview the precise breakdown of remaining balance parts |
| 3 | Track Every Cleared Balance | Full history of all past operations in one place |
| 4 | How It Works & Support | Review conditions and how clears work |
| 5 | Free Tier Features | Standard tools available to all users |
| 6 | Unlock Pro & Export | PDF export, full history, and advanced settings |

---

## Privacy

BalanceCleaner is privacy-first by design:

- ✅ No account required
- ✅ No personal data collected
- ✅ No analytics transmitted
- ✅ No advertising SDKs
- ✅ All data stored locally on-device (UserDefaults + Core Data)
- ✅ All transactions processed by Apple's StoreKit

Full policy: [PRIVACY.md](./PRIVACY.md) | [balancecleaner.app/privacy](https://balancecleaner.app/privacy)

---

## Project Structure

```
BalanceCleaner/
├── index.html              # Main landing page
├── support.html            # Contact & support form
├── privacy.html            # Privacy policy (multi-language)
├── device-preview.html     # All iPhone mockups grid
├── preview.html            # Screenshot gallery
├── PRIVACY.md              # Privacy policy source (all 6 languages)
├── README.md               # This file
└── assets/
    ├── site.css            # Global design system
    ├── theme-fixes.css     # Light/dark theme tokens
    ├── main.js             # i18n, theme, carousel, reveal
    ├── app-store/          # App Store badge SVGs (6 languages)
    ├── icons/              # App icon (x1024.svg)
    ├── images/             # Tier/feature images
    ├── mockups/            # iPhone mockup PNGs (18 Pro, 17, 16 Pro, SE)
    ├── screenshots/        # App Store screenshots (Page 1–5) & iPhone 18 Pro (1–6)
    ├── translations/       # JSON translation files (en, ru, fr, de, es, it)
    └── videos/             # Demo video placeholder (add your .mp4 here)
```

---

## Supported Languages

| Code | Language  |
|------|-----------|
| en   | English   |
| ru   | Русский   |
| fr   | Français  |
| de   | Deutsch   |
| es   | Español   |
| it   | Italiano  |

---

## Development Notes

- **Video**: Add your screen recording as `assets/videos/demo.mp4` — the video mockup section will pick it up automatically.
- **Device Preview**: Add screenshots for iPhone 17, 16 Pro and SE to `assets/screenshots/` and update `device-preview.html`.
- **Apple Banner**: Generate your smart banner at [Apple Marketing Toolbox](https://toolbox.marketingtools.apple.com/en-us/app-store/us) and paste the HTML into the `#banner` section in `index.html`.
- **App Store URL**: When live, replace `href="#"` in the Download buttons with your real App Store link.

---

## License

© 2026 BalanceCleaner. All rights reserved.  
See [LICENSE](./LICENSE) for details.
