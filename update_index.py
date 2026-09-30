import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Move sub-header-banner from top to just above footer
banner_regex = r'<!-- SUB-HEADER: App Store Banner -->.*?</div>\s*</div>'
match = re.search(banner_regex, html, re.DOTALL)
if match:
    banner = match.group(0)
    html = html.replace(banner, '')
    
    footer_idx = html.find('<!-- FOOTER -->')
    html = html[:footer_idx] + banner + '\n\n  ' + html[footer_idx:]

# 2. Add new FAQs
faq_addition = '''          <details class="faq-item">
            <summary data-i18n="faq6q">What is the Region Checklist?</summary>
            <div class="faq-content" data-i18n="faq6a">A step-by-step guide to prepare your account for a region change. It checks if your Apple ID balance is zero, subscriptions are canceled, and Family Sharing is left.</div>
          </details>
          <details class="faq-item">
            <summary data-i18n="faq7q">What Pro customization is available?</summary>
            <div class="faq-content" data-i18n="faq7a">Pro users can change the App background to Starfield and customize the Amount Ring Apple Glow Intent Design.</div>
          </details>'''
html = html.replace('</details>\n        </div>', '</details>\n' + faq_addition + '\n        </div>')

# 3. Add Video to About/Features or Split Screen?
# User says "Используй также, как на том проекте Split 616, пусть на весь экран как бы секция отображается."
# I will just write it to the file.
with open('index.html', 'w') as f:
    f.write(html)

print("Index updated")
