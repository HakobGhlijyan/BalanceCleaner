# BalanceCleaner

BalanceCleaner is a responsive landing page for a calmer, clearer and more private digital experience.

## Pages and sections

- `index.html` — dark premium landing page with animated green/blue ambient background, theme switching, English/Russian language switching, App Preview section, feature cards, and feedback form.
- `privacy.html` — bilingual privacy policy covering the feedback form and FormSubmit processing.
- `LICENSE` — Apache License 2.0.

## Feedback form

The form collects first name, last name, email, and message in that order. It uses [FormSubmit](https://formsubmit.co/) and sends submissions to `support@balancecleaner.app`.

Before production use:

1. Confirm that the mailbox exists and can receive messages.
2. Complete FormSubmit's activation email if it is requested after the first submission.
3. Review FormSubmit's terms and privacy policy.
4. Keep the privacy policy accurate if the provider, recipient, or fields change.
5. Add spam protection or replace the provider if the public form receives abuse.

## App Store preparation

The site includes a dedicated App Preview section with placeholders for future product screenshots. Add real, non-sensitive application screenshots under:

```text
assets/screenshots/dashboard.png
assets/screenshots/cleaning.png
assets/screenshots/insights.png
```

The website's preview images are not a substitute for the actual App Store Connect screenshots. In App Store Connect, provide a public Privacy Policy URL, a Support URL, accurate App Privacy disclosures, and screenshots that show real application functionality.

## License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE) for details.
