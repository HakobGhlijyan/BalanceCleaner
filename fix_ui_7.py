import re

for filename in ['index.html', 'support.html', 'privacy.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    header_match = re.search(r'<header class="wrap nav">(.*?)</header>', content, flags=re.DOTALL)
    if header_match:
        h = header_match.group(1)
        # Find everything from <div class="actions"> to the matching closing </div> 
        # Since it's nested (the lang switcher has divs inside), regex is tricky.
        # Let's just string split or use a known substring.
        if '<div class="actions">' in h:
            start = h.find('<div class="actions">')
            # It ends near the end of the header
            # Or we can just cut from <div class="actions"> to the end of the header content
            new_h = h[:start].strip()
            content = content.replace(header_match.group(0), f'<header class="wrap nav">\n{new_h}\n</header>')
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)

