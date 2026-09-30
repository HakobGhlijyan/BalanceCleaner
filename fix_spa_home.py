with open('assets/main.js', 'r') as f:
    js = f.read()

home_logic = """
  // Logo brings back to home
  const brand = document.querySelector('.brand');
  if (brand && window.location.pathname.endsWith('index.html') || window.location.pathname === '/') {
    brand.addEventListener('click', e => {
      e.preventDefault();
      document.querySelectorAll('main > section').forEach(sec => {
        sec.style.display = 'block';
      });
      // But keep our display:flex for regular sections?
      // Actually let's just reload the page for Home to be safe and reset state
      window.location.href = 'index.html';
    });
  }
"""

js = js.replace("if (!document.querySelector('main > section.hero')) return;", "if (!document.querySelector('main > section.hero')) return;\n" + home_logic)

with open('assets/main.js', 'w') as f:
    f.write(js)
print("Home logic fixed")
