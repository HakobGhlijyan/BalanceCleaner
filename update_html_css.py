import re
import os

# 1. CSS Updates: Language Dropdown upwards
with open('assets/site.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('top: 100%;', 'top: auto;\n  bottom: 100%;')
css = css.replace('margin-top: 6px;', 'margin-bottom: 6px;')
css = css.replace('transform: translateY(-10px);', 'transform: translateY(10px);')

with open('assets/site.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. HTML Updates
subheader_new = """
  <!-- SUB-HEADER DOWNLOAD BANNER -->
  <div class="sub-header-banner wrap" style="display: flex; justify-content: space-between; align-items: center; padding: 12px 24px; background: var(--surface2); border: 1px solid var(--line); border-radius: 16px; margin: 20px auto;">
    <div style="display: flex; align-items: center; gap: 8px;">
      <span style="color: var(--text); font-size: 15px; font-weight: 500;">Available for iPhone</span>
    </div>
    <a href="#" aria-label="Download on the App Store" style="display: block; transition: opacity 0.2s;">
      <img src="assets/app-store/app-store-badge.svg" alt="Download on the App Store" style="height: 40px; display: block;">
    </a>
  </div>
"""

for filename in ['index.html', 'support.html', 'privacy.html', 'preview.html', 'device-preview.html']:
    if not os.path.exists(filename): continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace Sub-header
    content = re.sub(r'<!-- SUB-HEADER DOWNLOAD BANNER -->.*?</div>\s*(<!--|$)', subheader_new + r'\n\1', content, flags=re.DOTALL)
    
    # Remove App Store badge from Footer
    # Wait, the footer App Store badge was already removed in some files or was placed right before footer.
    # In step 3 I placed it inside `<div style="text-align: center; margin-bottom: 20px;"><a href="#" class="footer-app-store-link">...</a></div>`
    content = re.sub(r'<div style="text-align: center; margin-bottom: 20px;">\s*<a href="#" class="footer-app-store-link">.*?</a>\s*</div>\n?', '', content, flags=re.DOTALL)

    # Ensure actions are in the header again (User said: "На странице главной сама иконка смены языка, смены темы на хедере маленькая... Универсальную сделай стандартную во всех страницах. И иконку самого перевода... также ту же иконку в хедере добавь.")
    # If <header> doesn't have .actions, add it back.
    if '<div class="actions"' not in content.split('</header>')[0]:
        actions_html = """
    <div class="actions" style="display: flex; gap: 12px; align-items: center;">
      <div class="custom-lang" id="customLangSwitcherHeader">
        <button class="lang-btn" id="langBtnHeader" aria-label="Select language" style="padding: 6px 10px; font-size: 13px;">
          <span id="langCurrentHeader">EN</span>
          <svg width="10" height="6" viewBox="0 0 10 6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M1 1L5 5L9 1"/></svg>
        </button>
        <div class="lang-menu" id="langMenuHeader" style="top: 100%; bottom: auto; transform: translateY(-10px);">
          <button data-val="en">EN</button>
          <button data-val="fr">FR</button>
          <button data-val="es">ES</button>
          <button data-val="it">IT</button>
          <button data-val="de">DE</button>
          <button data-val="ru">RU</button>
        </div>
      </div>
      <button class="theme" id="themeHeader" type="button" aria-label="Toggle theme" style="width: 32px; height: 32px; font-size: 18px;">
        <span class="theme-icon">☼</span>
      </button>
    </div>
"""
        # insert before </header>
        # find the <nav class="links">...</nav>
        content = re.sub(r'(</nav>\s*)</header>', r'\1' + actions_html + '</header>', content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
