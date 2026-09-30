with open('assets/site.css', 'r') as f:
    css = f.read()

css = css.replace('object-fit: contain; background: #000;', 'object-fit: cover; background: #fff;')

with open('assets/site.css', 'w') as f:
    f.write(css)

print("Mockup object-fit fixed.")
