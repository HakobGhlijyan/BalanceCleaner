import re

with open('assets/site.css', 'r') as f:
    css = f.read()

if ".privacy-card" in css:
    css = css.replace('.privacy-card {', '.policy-card {')

# Let's ensure the padding inside policy card looks good and background is there
if ".policy-card {" not in css:
    css += "\n.policy-card {\n  max-width: 800px;\n  margin: 0 auto;\n  background: var(--surface2);\n  padding: 40px;\n  border-radius: 16px;\n  border: 1px solid var(--line);\n}\n"

with open('assets/site.css', 'w') as f:
    f.write(css)

print("Fixed policy-card CSS")
