with open('assets/main.js', 'r') as f:
    js = f.read()

spa_logic = """
// =========================================================================
// SPA SECTION TOGGLING (For index.html)
// =========================================================================
function activateSection(id) {
  const target = document.getElementById(id);
  if (!target || !target.classList.contains('section')) return;
  
  // Hide all sections, apple banner, hero
  document.querySelectorAll('main > section').forEach(sec => {
    sec.style.display = 'none';
  });
  
  // Show target
  target.style.display = 'flex';
  
  // Update nav active states
  document.querySelectorAll('.links a').forEach(a => {
    a.classList.toggle('active', a.getAttribute('href') === '#' + id);
  });
  
  // Trigger reveal on the newly visible section
  target.classList.add('active');
  window.scrollTo(0, 0);
}

document.addEventListener('DOMContentLoaded', () => {
  // Only apply on index.html where these sections exist
  if (!document.querySelector('main > section.hero')) return;

  const links = document.querySelectorAll('.links a[href^="#"]');
  links.forEach(link => {
    link.addEventListener('click', e => {
      e.preventDefault();
      const id = link.getAttribute('href').substring(1);
      activateSection(id);
    });
  });

  // Handle 'Explore the product' in Hero
  const exploreBtn = document.querySelector('a[href="#screens"]');
  if (exploreBtn) {
    exploreBtn.addEventListener('click', e => {
      e.preventDefault();
      activateSection('screens');
    });
  }
});
"""
if "SPA SECTION TOGGLING" not in js:
    with open('assets/main.js', 'a') as f:
        f.write("\n" + spa_logic)
    print("SPA logic added")
else:
    print("Already added")
