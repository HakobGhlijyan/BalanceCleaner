import re

with open('assets/site.css', 'r') as f:
    css = f.read()

# Fix subheader transition
css = css.replace('.sub-header-banner {', '.sub-header-banner {\n  width: 100%;\n  max-width: 1200px;')

# Fix footer alignment
css = css.replace('.footer-inner {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n  flex-wrap: wrap;\n  gap: 16px;\n}', 
'''.footer-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 20px;
}
.footer-left, .footer-right {
  display: flex;
  align-items: center;
  gap: 20px;
}
.footer-right .custom-lang, .footer-right .theme, .footer-right .social-icon {
  display: flex;
  align-items: center;
  justify-content: center;
}
''')

# Fix video mockup size on main screen
css = css.replace('.mockup-wrap {\n  position: relative;\n  width: 200px;\n}', 
'''.mockup-wrap {
  position: relative;
  width: 280px;
  max-width: 100%;
}''')

# Fix object-fit to avoid cropping
css = css.replace('object-fit: cover;', 'object-fit: contain; background: #000;')

# Make sections taller
css = css.replace('.section {\n', '.section {\n  min-height: 80vh;\n  display: flex;\n  flex-direction: column;\n  justify-content: center;\n')

with open('assets/site.css', 'w') as f:
    f.write(css)

print("CSS updated")
