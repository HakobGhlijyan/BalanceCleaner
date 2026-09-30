with open('assets/site.css', 'r') as f:
    css = f.read()

css = css.replace('html {\n  scroll-behavior: smooth;\n  scroll-snap-type: y mandatory;\n}', 
'html {\n  scroll-behavior: smooth;\n  scroll-snap-type: y mandatory;\n  background: var(--bg);\n  min-height: 100vh;\n}')

with open('assets/site.css', 'w') as f:
    f.write(css)

print("HTML background fixed")
