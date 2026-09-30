import re

with open('support.html', 'r') as f:
    html = f.read()

# Make the hero section padding smaller
html = html.replace('<main class="wrap" style="padding-top: 20px;">', '<main class="wrap" style="padding-top: 0;">')
html = html.replace('<section class="hero" style="text-align: center;">', '<section class="hero" style="text-align: center; padding-top: 20px; padding-bottom: 20px;">')

# Convert the story panels to a grid to save vertical space
html = html.replace('<div class="story">', '<div class="story" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; align-items: start;">')

with open('support.html', 'w') as f:
    f.write(html)
print("support.html fixed")
