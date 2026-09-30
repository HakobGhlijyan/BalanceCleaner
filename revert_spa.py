import re

with open('assets/main.js', 'r') as f:
    js = f.read()

# Remove SPA logic
spa_regex = r'// =========================================================================\n// SPA SECTION TOGGLING \(For index\.html\).*'
js = re.sub(spa_regex, '', js, flags=re.DOTALL)

with open('assets/main.js', 'w') as f:
    f.write(js)
print("SPA removed")
