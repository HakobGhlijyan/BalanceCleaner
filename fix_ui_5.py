import re
import os

footer_actions = """
        <!-- Actions -->
        <div class="actions" style="display: flex; gap: 12px; align-items: center; margin-left: 20px;">
          <!-- Language Switcher -->
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
          <!-- Theme Switcher -->
          <button class="theme" id="theme" type="button" aria-label="Toggle theme">
            <span class="theme-icon">☼</span>
          </button>
        </div>
"""

def move_actions_to_footer(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract actions from header and delete
    # The actions block in header might look like: <div class="actions">...</div>
    # But wait, my custom language switcher is in it.
    
    # Just remove the entire <div class="actions"> from the header
    content = re.sub(r'<header class="wrap nav">.*?<div class="actions">.*?</div>\s*</header>', 
                     lambda m: m.group(0).replace(re.search(r'<div class="actions">.*?</div>', m.group(0), flags=re.DOTALL).group(0), ''), 
                     content, flags=re.DOTALL)

    # Insert into footer-right
    content = content.replace('</a>\n      </div>\n    </div>\n  </footer>', '</a>\n' + footer_actions + '      </div>\n    </div>\n  </footer>')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

for f in ['index.html', 'support.html', 'privacy.html', 'preview.html', 'device-preview.html']:
    move_actions_to_footer(f)
print("Actions moved to footer")
