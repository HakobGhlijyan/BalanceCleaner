import re

# ------------------------------------------------------------------
# 1. FIX INDEX.HTML SECTION ORDER
# ------------------------------------------------------------------
with open('index.html', 'r') as f:
    idx_html = f.read()

# Extract sections
def extract_section(html, section_id=None, class_name=None):
    if section_id:
        # Match <section id="XYZ"...> ... </section> or <section class="..." id="XYZ"> ... </section>
        # Needs to handle nested divs
        # We'll use a simpler regex for the known structure
        regex = r'<section[^>]*id="' + section_id + r'"[^>]*>.*?</section>'
        match = re.search(regex, html, re.DOTALL)
        if match: return match.group(0)
    if class_name:
        regex = r'<section[^>]*class="[^"]*' + class_name + r'[^"]*"[^>]*>.*?</section>'
        match = re.search(regex, html, re.DOTALL)
        if match: return match.group(0)
    return ""

hero = extract_section(idx_html, class_name="hero")
banner = extract_section(idx_html, section_id="banner")
story = extract_section(idx_html, section_id="story")
screens = extract_section(idx_html, section_id="screens")
video = extract_section(idx_html, section_id="video")
features = extract_section(idx_html, section_id="features")
faq = extract_section(idx_html, section_id="faq")
contact = extract_section(idx_html, class_name="contact")

# Remove them from main
idx_html = re.sub(r'<main>.*?</main>', '<main>\n    <!-- SECTIONS GO HERE -->\n  </main>', idx_html, flags=re.DOTALL)

# Reassemble in correct order
sections_ordered = [hero, banner, story, screens, video, features, faq, contact]
sections_html = "\n\n    ".join([s for s in sections_ordered if s])

idx_html = idx_html.replace('<!-- SECTIONS GO HERE -->', sections_html)

with open('index.html', 'w') as f:
    f.write(idx_html)
print("index.html order fixed")

# ------------------------------------------------------------------
# 2. FIX PRIVACY.HTML WRAP & TABS
# ------------------------------------------------------------------
with open('privacy.html', 'r') as f:
    priv_html = f.read()

# Make the language tabs full width
tabs_regex = r'<div class="lang-tabs".*?</div>'
match = re.search(tabs_regex, priv_html, re.DOTALL)
if match:
    old_tabs = match.group(0)
    # The CSS for lang-tabs might be missing or not full width.
    # In privacy.html, there's a script block. But let's check what the tabs look like.
    # We will just inject CSS to make it full width.

with open('assets/site.css', 'r') as f:
    css = f.read()

priv_css = """
/* Privacy page specific */
.privacy-card {
  max-width: 800px;
  margin: 0 auto;
}
.lang-tabs {
  display: flex;
  justify-content: space-between;
  width: 100%;
  gap: 8px;
  border-bottom: 1px solid var(--line);
  padding-bottom: 20px;
  margin-bottom: 30px;
}
.lang-tabs button {
  flex: 1;
  text-align: center;
  padding: 10px 0;
}
@media (max-width: 600px) {
  .lang-tabs {
    flex-wrap: wrap;
  }
  .lang-tabs button {
    flex: 1 1 45%;
  }
}
"""
if "Privacy page specific" not in css:
    css += "\n" + priv_css

# ------------------------------------------------------------------
# 3. FIX VIDEO DEMO GRID (ALL 4 IN A ROW)
# ------------------------------------------------------------------
video_grid_css = """
.video-grid {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 20px !important;
  width: 100%;
  max-width: 100%;
}
.video-mockup .mockup-wrap {
  width: 100% !important;
  max-width: 280px;
  margin: 0 auto;
}
@media (max-width: 1024px) {
  .video-grid { grid-template-columns: repeat(2, 1fr) !important; }
}
@media (max-width: 600px) {
  .video-grid { grid-template-columns: 1fr !important; }
}
"""
if ".video-grid {" in css:
    css = re.sub(r'\.video-grid\s*\{[^}]*\}', '', css) # remove old

css += "\n" + video_grid_css

with open('assets/site.css', 'w') as f:
    f.write(css)

print("CSS updated for Video Grid and Privacy Tabs")
