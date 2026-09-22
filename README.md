# BalanceCleaner

The landing page is a self-contained HTML site.

## Adding app screenshots

The screenshot gallery is in `index.html`, under the section with `id="screenshots"`. It currently contains three polished placeholders so the layout is visible before the final images are ready.

When screenshots are available, add them to:

```text
assets/screenshots/dashboard.png
assets/screenshots/cleaning.png
assets/screenshots/insights.png
```

Then replace each `.shot-frame` placeholder with an image, for example:

```html
<div class="shot-frame">
  <img src="assets/screenshots/dashboard.png" alt="BalanceCleaner dashboard">
</div>
```

The gallery is responsive and includes light/dark theme support, nine languages, and captions.
