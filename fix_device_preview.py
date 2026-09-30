import re
with open('device-preview.html', 'r') as f:
    html = f.read()

# 1. Change object-fit: contain to cover, background to white
html = html.replace('object-fit: contain;\n      background: #000;', 'object-fit: cover;\n      background: #fff;')
html = html.replace('style="background:#000;"', 'style="background:#fff;"')

# 2. Make them smaller
html = html.replace('width: 320px;', 'width: 260px;')

# 3. Add padding to device-screen-scroll so it doesn't crop at the edges, and hide scrollbars
scroll_css_old = '''.device-screen-scroll {
      display: flex;
      gap: 24px;
      overflow-x: auto;
      scroll-snap-type: x mandatory;
      padding-bottom: 12px;
    }'''
scroll_css_new = '''.device-screen-scroll {
      display: flex;
      gap: 24px;
      overflow-x: auto;
      scroll-snap-type: x mandatory;
      padding: 0 40px 20px 40px; /* Padding so cards aren't flush against edge */
      scrollbar-width: none; /* Firefox */
      -ms-overflow-style: none; /* IE/Edge */
    }
    .device-screen-scroll::-webkit-scrollbar {
      display: none;
    }
    .device-screen-scroll::before, .device-screen-scroll::after {
      content: '';
      flex: 0 0 1px; /* Extra space to ensure full scroll reach */
    }
'''
html = html.replace(scroll_css_old, scroll_css_new)

with open('device-preview.html', 'w') as f:
    f.write(html)
print("device-preview fixed.")
