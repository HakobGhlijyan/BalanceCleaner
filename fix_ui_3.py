import re
import os

# --- 1. Fix Privacy HTML ---
with open('privacy.html', 'r', encoding='utf-8') as f:
    privacy_content = f.read()

# Remove inline style block
privacy_content = re.sub(r'<style>.*?</style>', '', privacy_content, flags=re.DOTALL)

# Ensure header and footer match index.html exactly (assuming they were close but let's be sure)
# Actually, privacy.html currently has <main class="wrap" style="text-align: center;">? Let's just make sure.
# Wait, let's just do a regex replace to center main on privacy.html:
privacy_content = re.sub(r'<main class="wrap">', '<main class="wrap" style="text-align: center;">', privacy_content)
with open('privacy.html', 'w', encoding='utf-8') as f:
    f.write(privacy_content)


# --- 2. Fix Support HTML ---
with open('support.html', 'r', encoding='utf-8') as f:
    support_content = f.read()

# Make text centered
support_content = support_content.replace('<main class="wrap" style="margin-top: 10px;">', '<main class="wrap" style="margin-top: 10px; text-align: center;">')
support_content = support_content.replace('text-align: left', 'text-align: center')
with open('support.html', 'w', encoding='utf-8') as f:
    f.write(support_content)


# --- 3. Custom Language Switcher for all HTML files ---
lang_switcher_html = """
      <div class="custom-lang" id="customLangSwitcher">
        <button class="lang-btn" id="langBtn" aria-label="Select language">
          <span id="langCurrent">EN</span>
          <svg width="10" height="6" viewBox="0 0 10 6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M1 1L5 5L9 1"/></svg>
        </button>
        <div class="lang-menu" id="langMenu">
          <button data-val="en">EN</button>
          <button data-val="fr">FR</button>
          <button data-val="es">ES</button>
          <button data-val="it">IT</button>
          <button data-val="de">DE</button>
          <button data-val="ru">RU</button>
        </div>
      </div>
"""

def update_lang_switcher(filename):
    if not os.path.exists(filename): return
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    # Replace the <select> with the custom UI
    content = re.sub(r'<select class="select" id="language".*?</select>', lang_switcher_html.strip(), content, flags=re.DOTALL)
    
    # Also fix footer App Store icon (move it outside footer if it's inside, or just move it to the bottom)
    # The user said: "ты просто за пределами футера сделай эту иконку с гиперссылкой"
    # Current footer: <div class="wrap foot" style="display: flex;... <a href="#" ... app-store-badge.svg ...
    # Let's extract the badge and put it just before <footer>
    badge_html = '<div style="text-align: center; margin-bottom: 20px;"><a href="#" class="footer-app-store-link"><img src="assets/app-store/app-store-badge.svg" alt="Download on the App Store" style="height: 44px; display: inline-block;"></a></div>\n  <footer>'
    
    # First remove the badge from inside wrap foot if it's there
    content = re.sub(r'<a href="#" aria-label="Download on the App Store" style="transition: opacity 0\.3s; display: inline-block;">\s*<img src="assets/app-store/app-store-badge\.svg"[^>]*>\s*</a>', '', content)
    # Then insert it before footer
    if 'footer-app-store-link' not in content:
        content = content.replace('<footer>', badge_html)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

for f in ['index.html', 'support.html', 'privacy.html', 'preview.html', 'device-preview.html']:
    update_lang_switcher(f)

# --- 4. Update index.html Video Section (4 Mockups) and Carousel Indicators ---
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

# Add indicators to coverflow
indicators_html = """
          <div class="indicators" id="indicators">
              <div class="indicator active" data-index="0"></div>
              <div class="indicator" data-index="1"></div>
              <div class="indicator" data-index="2"></div>
              <div class="indicator" data-index="3"></div>
              <div class="indicator" data-index="4"></div>
          </div>
          <div class="coverflow-controls">
"""
idx = idx.replace('<div class="coverflow-controls">', indicators_html)

# Update Video Section with 4 mockups side-by-side
video_grid_html = """
        <div class="video-grid" style="display: flex; gap: 20px; overflow-x: auto; padding: 20px 0; justify-content: center; flex-wrap: wrap;">
          
          <!-- Mockup: iPhone 18 Pro -->
          <div class="video-mockup" style="position: relative; width: 220px; flex-shrink: 0;">
            <img src="assets/mockups/iPhone 18 Pro.png" alt="iPhone 18 Pro" style="width: 100%; position: relative; z-index: 10; pointer-events: none; display: block;">
            <video controls preload="metadata" style="position: absolute; top: 2.5%; left: 6.5%; width: 87%; height: 95%; z-index: 1; border-radius: 28px; object-fit: cover; background: #000;">
              <source src="#" type="video/mp4">
            </video>
            <p style="text-align: center; margin-top: 10px; font-weight: 600; color: var(--muted);">iPhone 18 Pro</p>
          </div>

          <!-- Mockup: iPhone 17 -->
          <div class="video-mockup" style="position: relative; width: 220px; flex-shrink: 0;">
            <img src="assets/mockups/iPhone 17.png" alt="iPhone 17" style="width: 100%; position: relative; z-index: 10; pointer-events: none; display: block;">
            <video controls preload="metadata" style="position: absolute; top: 2%; left: 5%; width: 90%; height: 96%; z-index: 1; border-radius: 28px; object-fit: cover; background: #000;">
              <source src="#" type="video/mp4">
            </video>
            <p style="text-align: center; margin-top: 10px; font-weight: 600; color: var(--muted);">iPhone 17</p>
          </div>

          <!-- Mockup: iPhone 16 Pro -->
          <div class="video-mockup" style="position: relative; width: 220px; flex-shrink: 0;">
            <img src="assets/mockups/iPhone 16 pro.png" alt="iPhone 16 Pro" style="width: 100%; position: relative; z-index: 10; pointer-events: none; display: block;">
            <video controls preload="metadata" style="position: absolute; top: 2.5%; left: 6.5%; width: 87%; height: 95%; z-index: 1; border-radius: 28px; object-fit: cover; background: #000;">
              <source src="#" type="video/mp4">
            </video>
            <p style="text-align: center; margin-top: 10px; font-weight: 600; color: var(--muted);">iPhone 16 Pro</p>
          </div>

          <!-- Mockup: iPhone SE -->
          <div class="video-mockup" style="position: relative; width: 220px; flex-shrink: 0;">
            <img src="assets/mockups/iPhone SE.png" alt="iPhone SE" style="width: 100%; position: relative; z-index: 10; pointer-events: none; display: block;">
            <video controls preload="metadata" style="position: absolute; top: 12%; left: 7%; width: 86%; height: 76%; z-index: 1; object-fit: cover; background: #000;">
              <source src="#" type="video/mp4">
            </video>
            <p style="text-align: center; margin-top: 10px; font-weight: 600; color: var(--muted);">iPhone SE</p>
          </div>

        </div>
"""
# Replace the single mockup figure with the grid
idx = re.sub(r'<figure class="video".*?</figure>', video_grid_html, idx, flags=re.DOTALL)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)


# --- 5. Add CSS for Custom Lang Switcher, Indicators, and wider Carousel items ---
with open('assets/site.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update carousel sizes to reflect 1320x2868 (1:2.17) ratio
css = re.sub(r'width: clamp\(180px, 30vh, 320px\);', 'width: clamp(160px, 28vh, 300px);', css)
css = re.sub(r'height: clamp\(320px, 53vh, 560px\);', 'height: clamp(347px, 60.8vh, 651px);', css)

lang_and_indicator_css = """
/* =========================================================================
   CUSTOM LANGUAGE SWITCHER
   ========================================================================== */
.custom-lang {
  position: relative;
  display: inline-block;
}
.lang-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  background: var(--surface2);
  border: 1px solid var(--line);
  color: var(--text);
  padding: 8px 14px;
  border-radius: 12px;
  cursor: pointer;
  font-family: inherit;
  font-weight: 600;
  transition: background 0.3s;
}
.lang-btn:hover {
  background: var(--surface);
}
.lang-menu {
  position: absolute;
  top: 100%;
  right: 0;
  margin-top: 6px;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 12px;
  box-shadow: 0 10px 25px rgba(0,0,0,0.2);
  display: flex;
  flex-direction: column;
  min-width: 80px;
  opacity: 0;
  pointer-events: none;
  transform: translateY(-10px);
  transition: all 0.2s ease;
  z-index: 100;
}
.lang-menu.show {
  opacity: 1;
  pointer-events: auto;
  transform: translateY(0);
}
.lang-menu button {
  background: transparent;
  border: none;
  color: var(--text);
  padding: 10px 16px;
  text-align: left;
  cursor: pointer;
  font-family: inherit;
  transition: background 0.2s;
}
.lang-menu button:hover {
  background: var(--surface2);
}
.lang-menu button:first-child { border-radius: 12px 12px 0 0; }
.lang-menu button:last-child { border-radius: 0 0 12px 12px; }

/* =========================================================================
   CAROUSEL INDICATORS
   ========================================================================== */
.indicators {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-top: 20px;
}
.indicator {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--line);
  cursor: pointer;
  transition: all 0.3s;
}
.indicator.active {
  background: var(--text);
  transform: scale(1.3);
}
"""
with open('assets/site.css', 'a', encoding='utf-8') as f:
    f.write(lang_and_indicator_css)

print("HTML and CSS updated.")
