import re

with open('assets/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace <select> event listener with Custom Dropdown logic
# Find: const langSelect = document.getElementById('language');
# We will just inject the new logic.
new_lang_logic = """
    const langSelect = document.getElementById('language');
    if(langSelect) {
        langSelect.addEventListener('change', e => applyLanguage(e.target.value));
    }
    
    // Custom Language Switcher
    const langBtn = document.getElementById('langBtn');
    const langMenu = document.getElementById('langMenu');
    const langCurrent = document.getElementById('langCurrent');
    
    if (langBtn && langMenu) {
        langBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            langMenu.classList.toggle('show');
        });
        
        document.addEventListener('click', () => {
            langMenu.classList.remove('show');
        });
        
        langMenu.querySelectorAll('button').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const code = e.target.getAttribute('data-val');
                if(langCurrent) langCurrent.textContent = code.toUpperCase();
                applyLanguage(code);
                
                // Keep selected class sync (optional)
                langMenu.querySelectorAll('button').forEach(b => b.style.fontWeight = 'normal');
                e.target.style.fontWeight = 'bold';
            });
        });
        
        // Init visual
        const initialCode = localStorage.getItem('balance-language') || 'en';
        if(langCurrent) langCurrent.textContent = initialCode.toUpperCase();
    }
"""
js = js.replace("const langSelect = document.getElementById('language');\n\n    function applyLanguage(code) {", 
               "function applyLanguage(code) {")
js = js.replace("langSelect.addEventListener('change', e => applyLanguage(e.target.value));", new_lang_logic)

# In PhotoCoverflow class, add indicator click support
indicator_logic_injection = """
      // Indicators click
      this.indicators = document.querySelectorAll('.indicator');
      this.indicators.forEach((ind, index) => {
          ind.addEventListener('click', () => {
              this.stopAutoPlay();
              this.goTo(index);
          });
      });
"""
js = js.replace("this.setupEventListeners();", "this.setupEventListeners();\n      " + indicator_logic_injection)

# In updateCoverflow, update active indicator
indicator_update = """
      if (this.indicators) {
          this.indicators.forEach((ind, index) => {
              ind.classList.toggle('active', index === this.currentIndex);
          });
      }
"""
js = js.replace("item.style.pointerEvents = Math.abs(offset) > 2 ? 'none' : 'auto';\n      });", "item.style.pointerEvents = Math.abs(offset) > 2 ? 'none' : 'auto';\n      });\n" + indicator_update)

with open('assets/main.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("JS updated.")
