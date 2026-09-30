import re

with open('privacy.html', 'r') as f:
    html = f.read()

# Remove inline <style> tag completely
html = re.sub(r'<style>.*?</style>', '', html, flags=re.DOTALL)

with open('privacy.html', 'w') as f:
    f.write(html)
print("Removed inline style from privacy.html")
