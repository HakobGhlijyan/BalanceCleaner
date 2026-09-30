with open('assets/site.css', 'r') as f:
    css = f.read()

# Make sections 100vh and centered
fullscreen_css = """
/* Full-screen sections */
html {
  scroll-snap-type: y mandatory;
}
main > section {
  scroll-snap-align: start;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  scroll-padding-top: 80px; /* Offset for header */
}
/* Ensure the hero looks balanced with header above it */
.hero {
  min-height: calc(100vh - 80px) !important; 
}
"""

if "/* Full-screen sections */" not in css:
    css += "\n" + fullscreen_css

# Also FAQ adjustments: "слишком большие кнопки, сделай немножко поменьше"
css = css.replace('.faq-item {\n  background: var(--surface2);\n  border: 1px solid var(--line);\n  border-radius: 16px;\n  padding: 20px 24px;', 
'.faq-item {\n  background: var(--surface2);\n  border: 1px solid var(--line);\n  border-radius: 12px;\n  padding: 14px 18px;')
css = css.replace('.faq-item summary {\n  font-size: 16px;\n  font-weight: 600;', 
'.faq-item summary {\n  font-size: 15px;\n  font-weight: 500;')

with open('assets/site.css', 'w') as f:
    f.write(css)

print("Full screen and FAQ adjustments applied.")
