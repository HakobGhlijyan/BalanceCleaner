import re
import markdown

with open('PRIVACY.md', 'r') as f:
    md = f.read()

# Find all language sections
languages = [
    ('en', 'English'), ('ru', 'Русский'), ('fr', 'Français'), 
    ('de', 'Deutsch'), ('es', 'Español'), ('it', 'Italiano')
]

tabs_html = '<div class="lang-tabs">\n'
for code, name in languages:
    active = ' class="active"' if code == 'en' else ''
    tabs_html += f'  <button data-lang="{code}"{active}>{name}</button>\n'
tabs_html += '</div>\n\n'

content_html = ''
for code, name in languages:
    active = ' active' if code == 'en' else ''
    content_html += f'<div id="policy-{code}" class="policy-section{active}">\n'
    
    # Extract section
    pattern = f'## {name}.*?(?=## |$)'
    match = re.search(pattern, md, re.DOTALL)
    if match:
        section_md = match.group(0)
        # Convert to HTML (simple replace for now)
        html_str = markdown.markdown(section_md)
        content_html += html_str + '\n'
    content_html += '</div>\n'

with open('privacy.html', 'r') as f:
    html = f.read()

# Replace main content
main_regex = r'<main.*?</main>'
new_main = f'''<main class="wrap" style="padding-top: 20px;">
  <section class="hero" style="text-align: center;">
    <div class="eyebrow">Privacy</div>
    <h1>Privacy Policy</h1>
  </section>
  <div class="privacy-content">
    {tabs_html}
    {content_html}
  </div>
</main>'''

html = re.sub(main_regex, new_main, html, flags=re.DOTALL)

with open('privacy.html', 'w') as f:
    f.write(html)

print("privacy.html content updated")
