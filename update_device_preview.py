import re

with open('device-preview.html', 'r') as f:
    html = f.read()

# Change .device-grid styles
html = html.replace('.device-grid {\n      display: grid;\n      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));\n      gap: 40px 24px;\n      padding: 40px 0 80px;\n    }',
'''.device-grid {
      display: flex;
      flex-direction: column;
      gap: 60px;
      padding: 40px 0 80px;
    }''')

# Change size of cards to be larger
html = html.replace('.device-card {\n      position: relative;\n      flex-shrink: 0;\n      scroll-snap-align: start;\n      width: 160px;\n    }',
'''.device-card {
      position: relative;
      flex-shrink: 0;
      scroll-snap-align: start;
      width: 320px;
    }''')

# Make the device screens container larger
html = html.replace('.device-screen-scroll {\n      display: flex;\n      gap: 12px;\n      overflow-x: auto;\n      scroll-snap-type: x mandatory;\n      padding-bottom: 6px;\n    }',
'''.device-screen-scroll {
      display: flex;
      gap: 24px;
      overflow-x: auto;
      scroll-snap-type: x mandatory;
      padding-bottom: 12px;
    }''')

# Ensure we use contain for screen images so they aren't cropped
html = html.replace('.device-card .screen {\n      position: absolute;\n      z-index: 1;\n      object-fit: cover;\n    }',
'''.device-card .screen {
      position: absolute;
      z-index: 1;
      object-fit: contain;
      background: #000;
    }''')

html = html.replace('.device-card .screen-placeholder {\n      position: absolute;\n      z-index: 1;\n      background: var(--surface2);\n      display: flex;\n      align-items: center;\n      justify-content: center;\n      color: var(--muted);\n      font-size: 11px;\n      text-align: center;\n    }',
'''.device-card .screen-placeholder {
      position: absolute;
      z-index: 1;
      background: var(--surface2);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--muted);
      font-size: 14px;
      text-align: center;
    }''')

# Insert Video card at the beginning of each group
video_18 = '''<div class="device-card frame-18pro">
            <img class="frame" src="assets/mockups/iPhone 18 Pro.png" alt="iPhone 18 Pro">
            <video preload="metadata" class="screen" controls style="background:#000;">
              <source src="#" type="video/mp4">
            </video>
          </div>
          '''
html = html.replace('<div class="device-card frame-18pro">\n            <img class="frame" src="assets/mockups/iPhone 18 Pro.png" alt="iPhone 18 Pro">\n            <img class="screen" src="assets/screenshots/Screenshot iPhone 18 Pro 1.png" alt="Screen 1">\n          </div>',
video_18 + '<div class="device-card frame-18pro">\n            <img class="frame" src="assets/mockups/iPhone 18 Pro.png" alt="iPhone 18 Pro">\n            <img class="screen" src="assets/screenshots/Screenshot iPhone 18 Pro 1.png" alt="Screen 1">\n          </div>')

# 17
video_17 = '''<div class="device-card frame-17">
            <img class="frame" src="assets/mockups/iPhone 17.png" alt="iPhone 17">
            <video preload="metadata" class="screen" controls style="background:#000;">
              <source src="#" type="video/mp4">
            </video>
          </div>
          '''
html = html.replace('<div class="device-card frame-17">\n            <img class="frame" src="assets/mockups/iPhone 17.png" alt="iPhone 17">\n            <div class="screen-placeholder placeholder-label">Coming soon</div>\n          </div>',
video_17 + '<div class="device-card frame-17">\n            <img class="frame" src="assets/mockups/iPhone 17.png" alt="iPhone 17">\n            <div class="screen-placeholder placeholder-label">Coming soon</div>\n          </div>', 1)

# 16 Pro
video_16 = '''<div class="device-card frame-16pro">
            <img class="frame" src="assets/mockups/iPhone 16 pro.png" alt="iPhone 16 Pro">
            <video preload="metadata" class="screen" controls style="background:#000;">
              <source src="#" type="video/mp4">
            </video>
          </div>
          '''
html = html.replace('<div class="device-card frame-16pro">\n            <img class="frame" src="assets/mockups/iPhone 16 pro.png" alt="iPhone 16 Pro">\n            <div class="screen-placeholder placeholder-label">Coming soon</div>\n          </div>',
video_16 + '<div class="device-card frame-16pro">\n            <img class="frame" src="assets/mockups/iPhone 16 pro.png" alt="iPhone 16 Pro">\n            <div class="screen-placeholder placeholder-label">Coming soon</div>\n          </div>', 1)

# SE
video_se = '''<div class="device-card frame-se">
            <img class="frame" src="assets/mockups/iPhone SE.png" alt="iPhone SE">
            <video preload="metadata" class="screen" controls style="background:#000;">
              <source src="#" type="video/mp4">
            </video>
          </div>
          '''
html = html.replace('<div class="device-card frame-se">\n            <img class="frame" src="assets/mockups/iPhone SE.png" alt="iPhone SE">\n            <div class="screen-placeholder placeholder-label">Coming soon</div>\n          </div>',
video_se + '<div class="device-card frame-se">\n            <img class="frame" src="assets/mockups/iPhone SE.png" alt="iPhone SE">\n            <div class="screen-placeholder placeholder-label">Coming soon</div>\n          </div>', 1)

with open('device-preview.html', 'w') as f:
    f.write(html)

print("device-preview updated")
