import re
import os

# 1. Fix Support.html footer App Store badge removal
with open('support.html', 'r', encoding='utf-8') as f:
    support_content = f.read()

support_content = re.sub(r'<div style="text-align: center; margin-bottom: 20px;"><a href="#" class="footer-app-store-link">.*?</a></div>\n', '', support_content, flags=re.DOTALL)
with open('support.html', 'w', encoding='utf-8') as f:
    f.write(support_content)

# 2. Add FAQ section to index.html (before Footer)
faq_html = """
    <!-- SECTION: FAQ -->
    <section class="section reveal" id="faq">
      <div class="wrap">
        <div class="heading" style="text-align: center; margin-bottom: 40px;">
          <h2 data-i18n="faqTitle">Frequently Asked Questions</h2>
        </div>
        <div class="faq-list" style="max-width: 760px; margin: 0 auto; display: flex; flex-direction: column; gap: 16px;">
          <details class="faq-item">
            <summary>What is BalanceCleaner?</summary>
            <div class="faq-content">BalanceCleaner helps you free up space on your device by identifying large files, duplicates, and clutter, while strictly respecting your privacy.</div>
          </details>
          <details class="faq-item">
            <summary>Is my data safe?</summary>
            <div class="faq-content">Yes. We believe in privacy first. All processing happens locally on your device. We do not upload your photos or files to any server.</div>
          </details>
          <details class="faq-item">
            <summary>Do I need an account to use the app?</summary>
            <div class="faq-content">No account is required. You can download and start using BalanceCleaner immediately.</div>
          </details>
        </div>
      </div>
    </section>
"""
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

if 'id="faq"' not in idx:
    # Insert FAQ right before the Apple Banner Placeholder or footer
    idx = re.sub(r'(<!-- SECTION 2\.2: APPLE BANNER PLACEHOLDER -->)', faq_html + r'\n    \1', idx)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(idx)

# 3. Add Sub-Header Rectangle with Download Button
subheader_html = """
  <!-- SUB-HEADER DOWNLOAD BANNER -->
  <div class="sub-header-banner wrap" style="display: flex; justify-content: space-between; align-items: center; padding: 12px 24px; background: var(--surface2); border: 1px solid var(--line); border-radius: 16px; margin: 20px auto;">
    <div>
      <strong>BalanceCleaner</strong>
      <span style="color: var(--muted); margin-left: 8px; font-size: 14px;">Available for iPhone</span>
    </div>
    <a href="#" class="button" style="padding: 8px 16px; font-size: 14px; background: var(--green); color: #000; font-weight: 600;">Download App</a>
  </div>
"""
def add_subheader(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'sub-header-banner' not in content:
        content = content.replace('</header>', '</header>\n' + subheader_html)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

for f in ['index.html', 'support.html', 'privacy.html']:
    add_subheader(f)

# 4. Footer Redesign (Socials, Balance Cleaner Name, Language & Theme optionally moved)
# The user wants them in the footer on the right side.
new_footer_html = """
  <!-- NEW FOOTER REDESIGN -->
  <footer class="site-footer" style="padding: 40px 0; border-top: 1px solid var(--line); margin-top: 60px;">
    <div class="wrap" style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px;">
      <div class="footer-left" style="display: flex; align-items: center; gap: 16px;">
        <strong style="font-size: 18px; color: var(--text);">BalanceCleaner</strong>
        <span style="color: var(--muted);">© 2026</span>
        <a href="privacy.html" style="color: var(--muted); text-decoration: none;">Privacy</a>
      </div>
      
      <div class="footer-right" style="display: flex; align-items: center; gap: 16px;">
        <!-- Social Icons (Placeholders) -->
        <a href="#" aria-label="Twitter/X" style="color: var(--muted);">
          <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M22.46 6c-.77.35-1.6.58-2.46.69.88-.53 1.56-1.37 1.88-2.38-.83.5-1.75.85-2.72 1.05C18.37 4.5 17.26 4 16 4c-2.35 0-4.27 1.92-4.27 4.29 0 .34.04.67.11.98C8.28 9.09 5.11 7.38 3 4.79c-.37.63-.58 1.37-.58 2.15 0 1.49.75 2.81 1.91 3.56-.71 0-1.37-.2-1.95-.5v.05c0 2.08 1.48 3.82 3.44 4.21-.36.1-.74.15-1.13.15-.27 0-.54-.03-.8-.08.54 1.7 2.13 2.94 4 2.98C6.35 18.52 4.45 19.16 2.4 19.16c-.34 0-.68-.02-1.02-.06C3.25 20.29 5.57 21 8.08 21c8.08 0 12.5-6.69 12.5-12.5 0-.19 0-.38-.01-.57.86-.62 1.6-1.39 2.19-2.26z"/></svg>
        </a>
        <a href="#" aria-label="Instagram" style="color: var(--muted);">
          <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.16c3.2 0 3.58.01 4.85.07 3.25.15 4.77 1.69 4.92 4.92.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.15 3.23-1.67 4.77-4.92 4.92-1.27.06-1.65.07-4.85.07s-3.58-.01-4.85-.07c-3.25-.15-4.77-1.69-4.92-4.92-.06-1.27-.07-1.65-.07-4.85s.01-3.58.07-4.85C2.38 3.85 3.9 2.31 7.15 2.16c1.27-.06 1.65-.07 4.85-.07M12 0C8.74 0 8.33.01 7.05.07c-4.27.19-6.78 2.7-6.97 6.98C.01 8.33 0 8.74 0 12s.01 3.67.08 4.95c.19 4.28 2.7 6.79 6.97 6.98 1.28.06 1.69.07 4.95.07s3.67-.01 4.95-.07c4.27-.19 6.78-2.7 6.98-6.98.06-1.28.07-1.69.07-4.95s-.01-3.67-.07-4.95c-.19-4.28-2.7-6.79-6.98-6.98C15.67.01 15.26 0 12 0zm0 5.84a6.16 6.16 0 1 0 0 12.32 6.16 6.16 0 0 0 0-12.32zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm7.85-11.53a1.44 1.44 0 1 1-2.88 0 1.44 1.44 0 0 1 2.88 0z"/></svg>
        </a>
      </div>
    </div>
  </footer>
"""

def update_footer_all(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We will replace the current <footer>...</footer> completely.
    content = re.sub(r'<footer>.*?</footer>', new_footer_html, content, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

for f in ['index.html', 'support.html', 'privacy.html', 'preview.html', 'device-preview.html']:
    update_footer_all(f)

# 5. Add FAQ details styles to site.css
faq_css = """
/* FAQ Section */
.faq-item {
  background: var(--surface2);
  border: 1px solid var(--line);
  border-radius: 12px;
  overflow: hidden;
  transition: all 0.3s;
}
.faq-item summary {
  padding: 18px 24px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  list-style: none;
  outline: none;
  color: var(--text);
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.faq-item summary::-webkit-details-marker {
  display: none;
}
.faq-item summary::after {
  content: '+';
  font-size: 20px;
  color: var(--muted);
  transition: transform 0.3s;
}
.faq-item[open] summary::after {
  transform: rotate(45deg);
}
.faq-content {
  padding: 0 24px 24px;
  color: var(--muted);
  line-height: 1.6;
}
"""
with open('assets/site.css', 'a', encoding='utf-8') as f:
    f.write(faq_css)

print("Done updates")
