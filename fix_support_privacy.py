import re

for filename in ['support.html', 'privacy.html']:
    with open(filename, 'r') as f:
        html = f.read()
    
    # Remove sub-header banner
    banner_regex = r'<!-- SUB-HEADER.*?<div class="sub-header-banner wrap.*?</div\s*>\s*</div\s*>'
    html = re.sub(banner_regex, '', html, flags=re.DOTALL)
    
    # Optional: also remove it if it's formatted differently
    html = re.sub(r'<div class="sub-header-banner wrap[^>]*>.*?</a>\s*</div>', '', html, flags=re.DOTALL)
    
    with open(filename, 'w') as f:
        f.write(html)
print("Removed subheader from support and privacy")
