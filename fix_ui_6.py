import re

def clean_header(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to remove the <div class="actions">...</div> inside <header class="wrap nav">
    header_match = re.search(r'<header class="wrap nav">(.*?)</header>', content, flags=re.DOTALL)
    if header_match:
        header_content = header_match.group(1)
        # Find the actions div
        actions_match = re.search(r'<div class="actions">.*?</div>\s*(?:<!--.*?-->\s*)*$', header_content, flags=re.DOTALL)
        if not actions_match:
            actions_match = re.search(r'<div class="actions">.*?</button>\s*</div>', header_content, flags=re.DOTALL)
        if actions_match:
            new_header_content = header_content.replace(actions_match.group(0), '')
            content = content.replace(header_match.group(0), f'<header class="wrap nav">{new_header_content}</header>')
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)

for f in ['index.html', 'support.html', 'privacy.html', 'preview.html', 'device-preview.html']:
    clean_header(f)
