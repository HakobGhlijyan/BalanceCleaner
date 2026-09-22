# Project structure

```text
BalanceCleaner/
├── index.html
├── privacy.html
├── README.md
├── LICENSE
└── assets/
    ├── screenshots/       # PNG/JPG app screenshots for the preview section
    ├── videos/            # MP4/WebM product demos; poster image recommended
    ├── icons/             # SVG preferred; PNG fallback at 512x512 or larger
    ├── images/            # JPG/PNG/WebP marketing images
    └── app-store/         # final App Store Connect exports
```

## Asset guidelines

- App screenshots: PNG or JPG, exactly matching the source device capture; use descriptive names such as `dashboard.png`, `cleaning.png`, and `insights.png`.
- Videos: MP4 (H.264) or WebM, with a lightweight poster such as `preview-poster.jpg`. Do not upload private user data.
- Icons: SVG is preferred for the website; use a square transparent PNG fallback, ideally 1024×1024 or at least 512×512.
- Images: WebP or JPG for photos; PNG for transparency. Keep filenames lowercase with hyphens.
- App Store screenshots: keep final localized exports in `assets/app-store/<locale>/`.

The site now includes a six-language dropdown: English, French, Spanish, Italian, German, and Russian. The theme control uses an animated sun/moon transition and the header is a floating glass panel.

The feedback form collects first name, last name, email, and message through FormSubmit. Keep `privacy.html` synchronized with the actual provider and fields before publishing.
