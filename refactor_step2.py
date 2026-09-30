import os
import re

# 1. Update support.html spacing
with open('support.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('<main class="wrap">', '<main class="wrap" style="margin-top: 10px;">')
content = content.replace('<section class="hero" style="text-align: left;">', '<section class="hero" style="text-align: left; padding-top: 20px;">')
with open('support.html', 'w', encoding='utf-8') as f:
    f.write(content)

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

# 2.1 Remove "See device variants" button
idx = re.sub(r'<a class="button ghost" href="device-preview.html"[^>]*>.*?</a>', '', idx)

# 2.2 Replace App Store CTA with Apple Banner Placeholder
banner_placeholder = """
    <!-- SECTION 2.2: APPLE BANNER PLACEHOLDER -->
    <section class="wrap" style="margin: 60px auto; text-align: center; border: 2px dashed var(--line); border-radius: 20px; padding: 60px 20px; color: var(--muted);">
      <h3 style="margin-bottom: 10px; color: var(--text);">Apple App Store Banner</h3>
      <p>Place your generated HTML from <a href="https://toolbox.marketingtools.apple.com/en-us/app-store/us" target="_blank" style="color: var(--green);">Apple Marketing Toolbox</a> here.</p>
    </section>
"""
idx = re.sub(r'<!-- SECTION 2\.2: APP STORE CTA.*?</section>', banner_placeholder, idx, flags=re.DOTALL)

# 2.3 Replace Screens section with Coverflow Carousel
coverflow_html = """
    <!-- SECTION: SCREENS CAROUSEL -->
    <section class="section reveal" id="screens">
      <div class="wrap">
        <div class="heading">
          <div>
            <div class="eyebrow" data-i18n="screenLabel">Product screens</div>
            <h2 data-i18n="screenTitle">See the app<br>before it ships.</h2>
          </div>
        </div>
      </div>
      
      <div class="coverflow-wrapper">
          <div class="coverflow-container" id="coverflowContainer">
              <div class="coverflow-item" data-index="0">
                  <img src="assets/screenshots/Page 1ai-store-black.png" class="portfolio-image" alt="Screen 1">
              </div>
              <div class="coverflow-item" data-index="1">
                  <img src="assets/screenshots/Page 2ai-store-black.png" class="portfolio-image" alt="Screen 2">
              </div>
              <div class="coverflow-item" data-index="2">
                  <img src="assets/screenshots/Page 3ai-store-black.png" class="portfolio-image" alt="Screen 3">
              </div>
              <div class="coverflow-item" data-index="3">
                  <img src="assets/screenshots/Page 4ai-store-black.png" class="portfolio-image" alt="Screen 4">
              </div>
              <div class="coverflow-item" data-index="4">
                  <img src="assets/screenshots/Page 5ai-store-black.png" class="portfolio-image" alt="Screen 5">
              </div>
          </div>
          
          <div class="coverflow-controls">
              <button class="control-btn" id="prevBtn">‹</button>
              <button class="control-btn" id="playPauseBtn">❚❚</button>
              <button class="control-btn" id="nextBtn">›</button>
          </div>
      </div>
    </section>
"""
idx = re.sub(r'<section class="section" id="screens">.*?(<section class="section" id="video">)', coverflow_html + r'\n    \1', idx, flags=re.DOTALL)

# 2.4 Replace Video section with Mockup wrapper and placeholder video
video_mockup_html = """
    <section class="section reveal" id="video">
      <div class="wrap">
        <div class="heading">
          <div>
            <div class="eyebrow" data-i18n="videoLabel">Product demo</div>
            <h2 data-i18n="videoTitle">See how it works.</h2>
          </div>
          <p data-i18n="videoLead">Video demo wrapped in an iPhone 18 Pro mockup.</p>
        </div>

        <figure class="video" style="max-width: 320px; margin: 0 auto; position: relative; background: transparent;">
          <!-- Mockup Frame (Top Layer) -->
          <img src="assets/mockups/iPhone 18 Pro.png" alt="iPhone Mockup" style="position: relative; width: 100%; z-index: 10; pointer-events: none; display: block;">
          
          <!-- Video Layer (Underneath the mockup frame) -->
          <!-- Adjust top/left/width/height % to fit the screen window of the mockup perfectly -->
          <video controls preload="metadata" style="position: absolute; top: 2.5%; left: 6.5%; width: 87%; height: 95%; z-index: 1; border-radius: 36px; object-fit: cover; background: #000;">
            <source src="#" type="video/mp4">
          </video>
        </figure>
      </div>
    </section>
"""
idx = re.sub(r'<section class="section" id="video">.*?</section>', video_mockup_html, idx, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)

print("index.html and support.html updated.")
