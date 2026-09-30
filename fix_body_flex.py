import re

with open('assets/site.css', 'r') as f:
    css = f.read()

# Add display flex to body
css = css.replace('body {\n  margin: 0;', 'body {\n  margin: 0;\n  display: flex;\n  flex-direction: column;\n  min-height: 100vh;')

# Add flex: 1 to main
if 'main {' not in css:
    css += '\nmain {\n  flex: 1;\n}\n'

with open('assets/site.css', 'w') as f:
    f.write(css)

print("Body flex applied.")
