import os
import re

# 1. Update Footer in all HTML files
footer_badge = """
    <div class="wrap foot" style="display: flex; flex-direction: column; align-items: center; gap: 20px;">
      <a href="#" aria-label="Download on the App Store" style="transition: opacity 0.3s; display: inline-block;">
        <img src="assets/app-store/app-store-badge.svg" alt="Download on the App Store" style="height: 44px; display: block;">
      </a>
      <div>
        © 2026 BalanceCleaner · 
        <a href="privacy.html">Privacy</a>
      </div>
    </div>
"""
def update_footer(filename):
    if not os.path.exists(filename): return
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(r'<div class="wrap foot">.*?</div>', footer_badge, content, flags=re.DOTALL)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

for f in ['index.html', 'support.html', 'privacy.html', 'preview.html', 'device-preview.html']:
    update_footer(f)

# 2. Append CSS to site.css
coverflow_css = """
/* =========================================================================
   CAROUSEL / COVERFLOW STYLES
   ========================================================================== */
.coverflow-wrapper {
	width: 100%;
	position: relative;
	padding: 20px 0 60px;
    overflow: hidden;
}

.coverflow-container {
	width: 100%;
	height: clamp(350px, 60vh, 650px);
	position: relative;
	transform-style: preserve-3d;
	margin: 0 auto;
	perspective: 1200px;
}

.coverflow-item {
	position: absolute;
	width: clamp(180px, 30vh, 320px);
	height: clamp(320px, 53vh, 560px);
	left: 50%;
	top: 50%;
	transform-origin: center center;
	transition: transform 0.6s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.6s, z-index 0s;
	border-radius: 20px;
	overflow: hidden;
	box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
}

.coverflow-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.coverflow-controls {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 20px;
}

.control-btn {
    background: var(--surface2);
    border: 1px solid var(--line);
    color: var(--text);
    width: 44px;
    height: 44px;
    border-radius: 50%;
    cursor: pointer;
    font-size: 18px;
    display: grid;
    place-items: center;
    transition: all 0.3s;
}

.control-btn:hover {
    background: var(--green);
    color: #000;
}

/* Scroll Reveal */
.reveal {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.8s ease, transform 0.8s ease;
}
.reveal.active {
    opacity: 1;
    transform: translateY(0);
}
"""
with open('assets/site.css', 'a', encoding='utf-8') as f:
    f.write(coverflow_css)

# 3. Append JS to main.js
coverflow_js = """
// Scroll Reveal
function revealOnScroll() {
    const reveals = document.querySelectorAll('.reveal');
    for (let i = 0; i < reveals.length; i++) {
        const windowHeight = window.innerHeight;
        const elementTop = reveals[i].getBoundingClientRect().top;
        const elementVisible = 100;
        if (elementTop < windowHeight - elementVisible) {
            reveals[i].classList.add('active');
        }
    }
}
window.addEventListener('scroll', revealOnScroll);
revealOnScroll(); // Trigger on load

// Coverflow Logic
class PhotoCoverflow {
   constructor() {
      this.items = document.querySelectorAll('.coverflow-item');
      if (!this.items.length) return;
      this.totalItems = this.items.length;
      this.currentIndex = Math.floor(this.totalItems / 2);
      this.isPlaying = true;
      this.autoPlayInterval = null;
      this.autoPlaySpeed = 3000;

      this.init();
   }

   init() {
      this.updateCoverflow();
      this.setupEventListeners();
      this.startAutoPlay();
   }

   setupEventListeners() {
      document.getElementById('prevBtn')?.addEventListener('click', () => { this.stopAutoPlay(); this.prev(); });
      document.getElementById('nextBtn')?.addEventListener('click', () => { this.stopAutoPlay(); this.next(); });
      document.getElementById('playPauseBtn')?.addEventListener('click', () => this.toggleAutoPlay());

      // Click to go to item
      this.items.forEach((item, index) => {
         item.addEventListener('click', () => {
            if (this.currentIndex !== index) {
               this.stopAutoPlay();
               this.goTo(index);
            }
         });
      });

      // Swipe
      let startX = 0;
      const container = document.getElementById('coverflowContainer');
      if(container) {
          container.addEventListener('touchstart', (e) => { startX = e.touches[0].clientX; }, { passive: true });
          container.addEventListener('touchend', (e) => {
             const diffX = startX - e.changedTouches[0].clientX;
             if (Math.abs(diffX) > 50) {
                this.stopAutoPlay();
                if (diffX > 0) this.next();
                else this.prev();
             }
          }, { passive: true });
      }

      window.addEventListener('resize', () => this.updateCoverflow());
   }

   updateCoverflow() {
      const isMobile = window.innerWidth <= 768;
      let baseSpacing = isMobile ? 130 : 200;

      this.items.forEach((item, index) => {
         let offset = index - this.currentIndex;
         
         // Loop logic
         if (offset > this.totalItems / 2) offset -= this.totalItems;
         else if (offset < -this.totalItems / 2) offset += this.totalItems;

         let translateX = offset * baseSpacing;
         let translateZ = 0;
         let rotateY = 0;
         let scale = 1;
         let opacity = 1;

         if (offset === 0) {
            translateZ = 150;
            scale = 1;
         } else if (Math.abs(offset) === 1) {
            translateZ = 0;
            rotateY = offset * -35;
            scale = 0.85;
            opacity = 0.8;
         } else if (Math.abs(offset) === 2) {
            translateZ = -100;
            rotateY = offset * -45;
            scale = 0.7;
            opacity = 0.5;
         } else {
            translateZ = -200;
            rotateY = offset * -60;
            scale = 0.5;
            opacity = 0;
         }

         item.style.transform = `translate(-50%, -50%) translateX(${translateX}px) translateZ(${translateZ}px) rotateY(${rotateY}deg) scale(${scale})`;
         item.style.opacity = opacity;
         item.style.zIndex = this.totalItems - Math.abs(offset);
         
         // Fix visibility for far items to not block clicks
         item.style.pointerEvents = Math.abs(offset) > 2 ? 'none' : 'auto';
      });
   }

   toggleAutoPlay() {
      const btn = document.getElementById('playPauseBtn');
      if (this.isPlaying) {
         this.stopAutoPlay();
         if(btn) btn.innerHTML = '▶';
      } else {
         this.startAutoPlay();
         if(btn) btn.innerHTML = '❚❚';
      }
   }

   startAutoPlay() {
      this.isPlaying = true;
      this.autoPlayInterval = setInterval(() => this.next(), this.autoPlaySpeed);
   }

   stopAutoPlay() {
      this.isPlaying = false;
      if (this.autoPlayInterval) {
         clearInterval(this.autoPlayInterval);
         this.autoPlayInterval = null;
      }
   }

   prev() {
      this.currentIndex = (this.currentIndex - 1 + this.totalItems) % this.totalItems;
      this.updateCoverflow();
   }

   next() {
      this.currentIndex = (this.currentIndex + 1) % this.totalItems;
      this.updateCoverflow();
   }

   goTo(index) {
      this.currentIndex = index;
      this.updateCoverflow();
   }
}

document.addEventListener('DOMContentLoaded', () => {
   new PhotoCoverflow();
});
"""
with open('assets/main.js', 'a', encoding='utf-8') as f:
    f.write(coverflow_js)

print("Footer, CSS, and JS updated.")
