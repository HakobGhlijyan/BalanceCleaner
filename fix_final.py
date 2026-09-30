import re

# 1. Remove top SUB-HEADER from index.html
with open('index.html', 'r') as f:
    idx = f.read()
# Find the first one and delete it
idx = re.sub(r'  <!-- SUB-HEADER: App Store Banner -->\n  <div class="sub-header-banner wrap">.*?</div>\n  </div>\n', '', idx, count=1, flags=re.DOTALL)

# Also fix the Full Screen section snapping for index.html
# Add CSS classes or inline styles to make sections 100vh
# Actually, better to do this in CSS

with open('index.html', 'w') as f:
    f.write(idx)


# 2. Fix Support Page bottom gap
with open('support.html', 'r') as f:
    sup = f.read()
# Ensure no extra divs. The gap might be from CSS `body { min-height: 100vh }` combined with a dark gradient background that doesn't reach the bottom.
# We will fix the background in CSS.

# 3. Fix Privacy Page Tabs
with open('privacy.html', 'r') as f:
    priv = f.read()
# Change the lang-tabs structure to be centered pills
# The previous script might have messed up the 3 feature cards if they existed, but looking at the screenshot, they are in privacy.html. Let's see what's in privacy.html right now.

print("index.html top banner removed.")
