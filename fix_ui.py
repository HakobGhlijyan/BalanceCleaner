import re
import os

# 1. Extract JS to main.js
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

script_match = re.search(r'<script>(.*?)</script>', index_content, re.DOTALL)
if script_match:
    js_content = script_match.group(1).strip()
    with open('assets/main.js', 'w', encoding='utf-8') as f:
        f.write(js_content)

# 2. Define the unified header without 'All demos' button
def get_header(is_index):
    link_prefix = "" if is_index else "index.html"
    return f"""  <header class="wrap nav">
    <a class="brand" href="index.html">
      <img class="brand-icon" src="assets/icons/x1024.svg" alt="BalanceCleaner icon">
      <span>BalanceCleaner</span>
    </a>
    <nav class="links">
      <a href="{link_prefix}#story" data-i18n="about">About</a>
      <a href="{link_prefix}#screens" data-i18n="screens">Screens</a>
      <a href="{link_prefix}#video" data-i18n="video">Video</a>
      <a href="{link_prefix}#features" data-i18n="features">Features</a>
      <a href="support.html" data-i18n="support">Support</a>
      <a href="privacy.html" data-i18n="privacy">Privacy</a>
    </nav>
    <div class="actions">
      <select class="select" id="language" aria-label="Language">
        <option value="en">EN</option>
        <option value="fr">FR</option>
        <option value="es">ES</option>
        <option value="it">IT</option>
        <option value="de">DE</option>
        <option value="ru">RU</option>
      </select>
      <button class="theme" id="theme" type="button" aria-label="Toggle theme">
        <span class="theme-icon">☼</span>
      </button>
    </div>
  </header>"""

# 3. Update HTML files
def update_html(filename):
    if not os.path.exists(filename): return
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    is_index = filename == 'index.html'
    new_header = get_header(is_index)
    
    # Replace header
    content = re.sub(r'<header class="wrap nav">.*?</header>', new_header, content, flags=re.DOTALL)
    
    # Remove 'All demos' from footer
    content = re.sub(r'<a href="preview\.html"( data-i18n="demos")?>[^<]+</a>\s*·\s*', '', content)
    content = re.sub(r'<a href="preview\.html".*?Open all demos.*?</a>\s*·\s*', '', content)

    # In index.html, remove script content and use src
    if is_index:
        content = re.sub(r'<script>.*?</script>', '<script src="assets/main.js"></script>', content, flags=re.DOTALL)
        
        # Replace empty screenshot images in index.html
        content = content.replace('assets/screenshots/dashboard_free.PNG', 'assets/screenshots/Page 1ai-store-black.png')
        content = content.replace('assets/screenshots/cleaning.PNG', 'assets/screenshots/Page 2ai-store-black.png')
        content = content.replace('assets/screenshots/dashboard_premium.PNG', 'assets/screenshots/Page 3ai-store-black.png')
    else:
        # In other files, inject script if missing
        if '<script src="assets/main.js"></script>' not in content:
            content = content.replace('</body>', '  <script src="assets/main.js"></script>\n</body>')
            
        # Also ensure theme-fixes.css is included in other pages
        if 'theme-fixes.css' not in content:
            content = content.replace('</head>', '  <link rel="stylesheet" href="assets/theme-fixes.css">\n</head>')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

for f in ['index.html', 'support.html', 'privacy.html', 'preview.html', 'device-preview.html']:
    update_html(f)

# 4. Update CSS (site.css)
with open('assets/site.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make transition smoother for theme switching globally
css = css.replace(
    'transition: background .4s, color .4s;',
    'transition: background 0.6s ease, background-color 0.6s ease, color 0.6s ease, border-color 0.6s ease;'
)

# Shrink App Store button
css = re.sub(r'width: min\(100%, 620px\);', 'width: min(100%, 320px);', css)
css = re.sub(r'padding: 26px 30px;', 'padding: 12px 16px;', css)
css = re.sub(r'width: 76px;\s*height: 76px;\s*border-radius: 20px;\s*background: #f6f8f8;\s*color: #0c0d0f;\s*font-size: 56px;',
             'width: 48px; height: 48px; border-radius: 12px; background: #f6f8f8; color: #0c0d0f; font-size: 32px;', css)

css = css.replace('font-size: 20px;', 'font-size: 14px;') # for button-text small
css = css.replace('font-size: 3.4rem;', 'font-size: 1.8rem;') # for button-text strong

# Add transition to all common containers
if '.card {' in css and 'transition:' not in css.split('.card {')[1].split('}')[0]:
    css = css.replace('.card {\n', '.card {\n  transition: background-color 0.6s ease, border-color 0.6s ease, color 0.6s ease;\n')

# Make screenshots and video vertical aspect ratio (9:16)
if '.card img' in css:
    css = css.replace('.card img {\n', '.card img {\n  aspect-ratio: 9/16;\n  object-fit: cover;\n')

# For video
if '.video {' in css:
    css = css.replace('.video {\n', '.video {\n  max-width: 400px;\n  margin: 0 auto;\n  aspect-ratio: 9/16;\n')

if '.video video {' in css:
    css = css.replace('.video video {\n', '.video video {\n  aspect-ratio: 9/16;\n  object-fit: cover;\n')
else:
    css += "\n.video video { aspect-ratio: 9/16; object-fit: cover; width: 100%; border-radius: inherit; }"

with open('assets/site.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Done")
