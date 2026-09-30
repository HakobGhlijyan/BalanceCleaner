import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Add FAQs to FAQ section
faq_addition = '''          <details class="faq-item">
            <summary data-i18n="faq6q">What is the Region Checklist?</summary>
            <div class="faq-content" data-i18n="faq6a">A step-by-step guide to prepare your account for a region change. It checks if your Apple ID balance is zero, subscriptions are canceled, and Family Sharing is left.</div>
          </details>
          <details class="faq-item">
            <summary data-i18n="faq7q">What Pro customization is available?</summary>
            <div class="faq-content" data-i18n="faq7a">Pro users can change the App background to Starfield and customize the Amount Ring Apple Glow Intent Design.</div>
          </details>'''
html = html.replace('</details>\n        </div>', '</details>\n' + faq_addition + '\n        </div>')

# 2. Move SUB-HEADER banner above footer
banner_block = """  <!-- SUB-HEADER: App Store Banner -->
  <div class="sub-header-banner wrap">
    <div class="sub-header-left">
      <img src="assets/app-store/app-store-badge.svg" alt="App Store" style="height: 28px;">
      <span data-i18n="subHeaderText">Available for iPhone</span>
    </div>
    <a href="#" class="button" style="padding: 8px 20px; font-size: 14px;" data-i18n="subHeaderBtn">Download</a>
  </div>
"""

# First, remove it from its current location if it exists
html = re.sub(r'  <!-- SUB-HEADER: App Store Banner -->\n  <div class="sub-header-banner wrap">.*?</div>\n  </div>\n', '', html, flags=re.DOTALL)

# Now, insert it just before the FOOTER
html = html.replace('  <!-- FOOTER -->', banner_block + '\n  <!-- FOOTER -->')

# 3. Save
with open('index.html', 'w') as f:
    f.write(html)
print("Index recreated perfectly")
