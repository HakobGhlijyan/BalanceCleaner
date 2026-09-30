with open('assets/main.js', 'r') as f:
    js = f.read()

active_state_logic = """
// =========================================================================
// ACTIVE NAV STATE ON SCROLL
// =========================================================================
function setupScrollSpy() {
  const sections = document.querySelectorAll('main > section');
  const navLinks = document.querySelectorAll('.links a[href^="index.html#"], .links a[href^="#"]');
  
  if (sections.length === 0 || navLinks.length === 0) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        let id = entry.target.getAttribute('id');
        if (!id) return;
        
        navLinks.forEach(link => {
          link.classList.remove('active');
          const href = link.getAttribute('href');
          if (href === '#' + id || href === 'index.html#' + id) {
            link.classList.add('active');
          }
        });
      }
    });
  }, { rootMargin: '-50% 0px -50% 0px' });

  sections.forEach(sec => observer.observe(sec));
}

document.addEventListener('DOMContentLoaded', () => {
  setupScrollSpy();
  
  // Static page active state (for Support and Privacy)
  const path = window.location.pathname;
  if (path.includes('support.html')) {
    const link = document.querySelector('.links a[href="support.html"]');
    if (link) link.classList.add('active');
  } else if (path.includes('privacy.html')) {
    const link = document.querySelector('.links a[href="privacy.html"]');
    if (link) link.classList.add('active');
  }
});
"""

if "ACTIVE NAV STATE" not in js:
    with open('assets/main.js', 'a') as f:
        f.write("\n" + active_state_logic)
    print("Active nav state added to main.js")
