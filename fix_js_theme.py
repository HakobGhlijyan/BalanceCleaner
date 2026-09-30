import re

with open('assets/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix Theme Logic to be 2 seconds and originate from click
theme_logic = """
    const root = document.documentElement;
    const themeBtns = document.querySelectorAll('.theme');

    function applyTheme(mode) {
      root.classList.toggle('light', mode === 'light');
      themeBtns.forEach(btn => {
         const icon = btn.querySelector('.theme-icon');
         if(icon) icon.textContent = mode === 'light' ? '☾' : '☼';
         btn.setAttribute('aria-label', mode === 'light' ? 'Switch to dark theme' : 'Switch to light theme');
      });
      localStorage.setItem('balance-theme', mode);
    }

    applyTheme(localStorage.getItem('balance-theme') || 'dark');

    themeBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        const next = root.classList.contains('light') ? 'dark' : 'light';
        const color = next === 'light' ? '#edf8f1' : '#07110d';
        
        // Ripple Animation
        const overlay = document.createElement('div');
        overlay.style.position = 'fixed';
        overlay.style.left = e.clientX + 'px';
        overlay.style.top = e.clientY + 'px';
        overlay.style.width = '0px';
        overlay.style.height = '0px';
        overlay.style.borderRadius = '50%';
        overlay.style.backgroundColor = color;
        overlay.style.transform = 'translate(-50%, -50%)';
        overlay.style.zIndex = '9999';
        overlay.style.transition = 'width 2s ease-in-out, height 2s ease-in-out';
        overlay.style.pointerEvents = 'none';
        
        document.body.appendChild(overlay);
        
        // Trigger expansion
        setTimeout(() => {
            const maxDim = Math.max(window.innerWidth, window.innerHeight) * 3;
            overlay.style.width = maxDim + 'px';
            overlay.style.height = maxDim + 'px';
        }, 10);
        
        setTimeout(() => {
            applyTheme(next);
            document.body.removeChild(overlay);
        }, 2000);
      });
    });
"""

js = re.sub(r'const root = document.documentElement;.*?(?=// Scroll Reveal)', theme_logic, js, flags=re.DOTALL)

# Fix Language logic for multiple dropdowns
lang_logic = """
    // Custom Language Switchers (can be multiple)
    const langSwitchers = document.querySelectorAll('.custom-lang');
    
    langSwitchers.forEach(switcher => {
        const btn = switcher.querySelector('.lang-btn');
        const menu = switcher.querySelector('.lang-menu');
        const currentLabel = switcher.querySelector('span');
        
        if (btn && menu) {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                // Close all others
                langSwitchers.forEach(s => {
                   if (s !== switcher) s.querySelector('.lang-menu')?.classList.remove('show');
                });
                menu.classList.toggle('show');
            });
            
            menu.querySelectorAll('button').forEach(menuBtn => {
                menuBtn.addEventListener('click', (e) => {
                    const code = e.target.getAttribute('data-val');
                    
                    // Update all switchers
                    langSwitchers.forEach(s => {
                        const lbl = s.querySelector('span');
                        if (lbl) lbl.textContent = code.toUpperCase();
                        const btns = s.querySelectorAll('.lang-menu button');
                        btns.forEach(b => b.style.fontWeight = 'normal');
                        const activeBtn = s.querySelector(`.lang-menu button[data-val="${code}"]`);
                        if(activeBtn) activeBtn.style.fontWeight = 'bold';
                    });
                    
                    applyLanguage(code);
                });
            });
        }
    });

    document.addEventListener('click', () => {
        langSwitchers.forEach(s => {
            s.querySelector('.lang-menu')?.classList.remove('show');
        });
    });

    const initialCode = localStorage.getItem('balance-language') || 'en';
    langSwitchers.forEach(s => {
        const lbl = s.querySelector('span');
        if (lbl) lbl.textContent = initialCode.toUpperCase();
    });
"""
js = re.sub(r'// Custom Language Switcher.*?(?=/\*\*|\n\s*const root =)', lang_logic, js, flags=re.DOTALL)

with open('assets/main.js', 'w', encoding='utf-8') as f:
    f.write(js)
