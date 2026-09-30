import re

with open('assets/site.css', 'r') as f:
    css = f.read()

# Disable reveal hiding
css = re.sub(
    r'\.reveal \{\n    opacity: 0;\n    transform: translateY\(30px\);\n    transition: opacity 0\.8s ease, transform 0\.8s ease;\n\}',
    '.reveal {\n    opacity: 1;\n    transform: translateY(0);\n    transition: opacity 0.8s ease, transform 0.8s ease;\n}',
    css
)

with open('assets/site.css', 'w') as f:
    f.write(css)

