import re

with open('assets/site.css', 'r') as f:
    css = f.read()

# Remove the previously injected block for privacy
css = re.sub(r'/\* Privacy page specific \*/.*?@media \(max-width: 600px\) \{[^}]*\}[^}]*\}', '', css, flags=re.DOTALL)

with open('assets/site.css', 'w') as f:
    f.write(css)

print("Cleaned up duplicate privacy CSS")
