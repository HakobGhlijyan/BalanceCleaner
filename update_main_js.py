with open('assets/main.js', 'r') as f:
    js = f.read()

# Update Theme Animation
old_anim = "'transition:width 2s ease, height 2s ease'"
new_anim = "'transition:width 0.8s ease, height 0.8s ease, opacity 0.4s ease 0.4s'"
js = js.replace(old_anim, new_anim)

js = js.replace("setTimeout(() => applyTheme(next), 600);", "setTimeout(() => applyTheme(next), 300);\n  setTimeout(() => { overlay.style.opacity = '0'; }, 400);")
js = js.replace("setTimeout(() => overlay.remove(), 2100);", "setTimeout(() => overlay.remove(), 850);")

# Update Translations with New Content
js = js.replace("faq5a: 'Pro unlocks full transaction history, PDF export, and advanced settings. The core cleaner is free for everyone.'", 
"""faq5a: 'Pro unlocks full transaction history, PDF export, and advanced settings. The core cleaner is free for everyone.',
    faq6q: 'What is the Region Checklist?',
    faq6a: 'A step-by-step guide to prepare your account for a region change. It checks if your Apple ID balance is zero, subscriptions are canceled, and Family Sharing is left.',
    faq7q: 'What Pro customization is available?',
    faq7a: 'Pro users can change the App background to Starfield and customize the Amount Ring Apple Glow Intent Design.',
    proFeaturesTitle: 'Premium Features',
    proFeaturesDesc: 'Unlock full transaction history, export records to PDF, customize the Amount Ring glow, and set a Starfield background.'""")

with open('assets/main.js', 'w') as f:
    f.write(js)

print("JS updated")
