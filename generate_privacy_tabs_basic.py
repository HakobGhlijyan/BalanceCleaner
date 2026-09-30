import re

with open('PRIVACY.md', 'r') as f:
    md = f.read()

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
        # Very basic markdown conversion
        html_str = re.sub(r'### (.*?)\n', r'<h2>\1</h2>\n', section_md)
        html_str = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html_str)
        html_str = re.sub(r'## (.*?)\n', r'', html_str) # remove the title
        
        paragraphs = []
        for p in html_str.split('\\n\\n'):
            p = p.strip()
            if p and not p.startswith('<h'):
                if p.startswith('- '):
                    items = [f"<li>{i[2:]}</li>" for i in p.split('\\n- ')]
                    paragraphs.append("<ul>\\n" + "\\n".join(items) + "\\n</ul>")
                else:
                    paragraphs.append(f"<p>{p}</p>")
            elif p:
                paragraphs.append(p)
        content_html += "\\n".join(paragraphs) + '\n'
    content_html += '</div>\n'

with open('privacy.html', 'r') as f:
    html = f.read()

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
html = html.replace('\\n', '\n') # fix any literal escaped newlines

with open('privacy.html', 'w') as f:
    f.write(html)

print("privacy.html content updated")
