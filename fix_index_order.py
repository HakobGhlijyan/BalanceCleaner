import re

with open('index.html', 'r') as f:
    html = f.read()

# Extract the <main> block
main_match = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
if not main_match:
    print("Main not found")
    exit(1)

main_content = main_match.group(1)

# Split sections
section_regex = r'(<section[^>]*>.*?</section>)'
sections = re.findall(section_regex, main_content, re.DOTALL)

print(f"Found {len(sections)} sections")

# We want this order based on the IDs/classes:
# 1. hero
# 2. banner
# 3. story
# 4. screens
# 5. video
# 6. features
# 7. faq
# 8. contact

order_map = {
    'hero': 1,
    'banner': 2,
    'story': 3,
    'screens': 4,
    'video': 5,
    'features': 6,
    'faq': 7,
    'contact': 8
}

def get_order(section_html):
    for key, val in order_map.items():
        if f'id="{key}"' in section_html or f'class="{key}"' in section_html or f'class="wrap {key}"' in section_html:
            return val
    return 99

sections.sort(key=get_order)

new_main_content = "\n\n    ".join(sections)
new_html = html[:main_match.start(1)] + "\n    " + new_main_content + "\n  " + html[main_match.end(1):]

with open('index.html', 'w') as f:
    f.write(new_html)

print("index.html sections reordered successfully.")
