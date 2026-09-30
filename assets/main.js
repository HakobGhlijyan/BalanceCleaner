/**
 * BalanceCleaner — main.js
 * Handles: i18n, theme switching (ripple), language switcher, scroll reveal, coverflow carousel.
 */

// =========================================================================
// i18n DICTIONARIES
// =========================================================================
const dictionaries = {
  en: {
    about: 'About', screens: 'Screens', video: 'Video', features: 'Features',
    support: 'Support', privacy: 'Privacy',
    subHeaderText: 'Available for iPhone', subHeaderBtn: 'Download',
    eyebrow: 'A calmer digital life',
    title: 'Make room for what matters.',
    lead: 'BalanceCleaner brings clarity to your digital world with thoughtful tools, a quiet interface, and privacy at its core.',
    explore: 'Explore the product →',
    ideaLabel: 'The idea',
    storyTitle: 'Less noise.<br>More balance.',
    storyLead: 'A calm product story built around clarity, control and a respectful digital experience.',
    storyCardTitle: 'Your digital space, understood.',
    storyText: 'BalanceCleaner helps people see what is taking up space, make confident decisions and keep their everyday devices feeling lighter.',
    demoNotice: 'The website currently presents demo screens. Final App Store materials will be added after launch.',
    understand: 'Understand', choose: 'Choose', balance: 'Balance',
    thoughtful: 'Built thoughtfully',
    simple: 'Simple from the first tap.',
    simpleText: 'Focused tools, transparent choices and privacy at the centre of every interaction.',
    talk: 'Talk to the developer →',
    screenLabel: 'Product screens',
    screenTitle: 'See the app<br>before it ships.',
    videoLabel: 'Product demo',
    videoTitle: 'See how it works.',
    videoLead: 'Demo across all supported iPhone models.',
    why: 'Why BalanceCleaner',
    featuresTitle: 'Thoughtfully simple.',
    clear: 'Clear by design', clearText: 'Focused tools that feel easy from the first tap.',
    private: 'Privacy first', privateText: 'Transparent choices and respect for your information.',
    quiet: 'Quietly powerful', quietText: 'Useful insights without unnecessary complexity.',
    improve: 'Made to improve', improveText: 'Send feedback directly to the developer.',
    listening: 'We\'re listening', idea: 'Have an idea?',
    ideaText: 'Send feedback, report a problem or ask a question through our support page.',
    openSupport: 'Open support →',
    faqTitle: 'Frequently Asked Questions',
    faq1q: 'What is BalanceCleaner?',
    faq1a: 'BalanceCleaner lets you easily select or enter the exact custom amount to zero out your Apple ID account balance — no account registration required.',
    faq2q: 'How does the balance split work?',
    faq2a: 'See the precise breakdown of your remaining balance and calculated parts before confirming any operation. Everything is shown clearly before you proceed.',
    faq3q: 'Is my data safe?',
    faq3a: 'Yes. All processing happens locally on your device via Apple\'s StoreKit framework. We do not collect, store or upload any personal data.',
    faq4q: 'Do I need an account?',
    faq4a: 'No account is required. Download and start immediately.',
    faq5q: 'What is Pro?',
    faq5a: 'Pro unlocks full transaction history, PDF export, and advanced settings. The core cleaner is free for everyone.',
    faq6q: 'What is the Region Checklist?',
    faq6a: 'A step-by-step guide to prepare your account for a region change. It checks if your Apple ID balance is zero, subscriptions are canceled, and Family Sharing is left.',
    faq7q: 'What Pro customization is available?',
    faq7a: 'Pro users can change the App background to Starfield and customize the Amount Ring Apple Glow Intent Design.',
    proFeaturesTitle: 'Premium Features',
    proFeaturesDesc: 'Unlock full transaction history, export records to PDF, customize the Amount Ring glow, and set a Starfield background.'
  }
};

function fill(code, overrides) {
  dictionaries[code] = Object.assign({}, dictionaries.en, overrides);
}

fill('ru', {
  about: 'О продукте', screens: 'Экраны', video: 'Видео', features: 'Возможности',
  support: 'Поддержка', privacy: 'Приватность',
  subHeaderText: 'Доступно для iPhone', subHeaderBtn: 'Загрузить',
  eyebrow: 'Более спокойная цифровая жизнь',
  title: 'Освободите место для важного.',
  lead: 'BalanceCleaner помогает навести порядок в цифровом мире, ставя приватность в основу.',
  explore: 'Открыть продукт →',
  ideaLabel: 'Идея',
  storyTitle: 'Меньше шума.<br>Больше баланса.',
  storyLead: 'Спокойный продукт, построенный на ясности, контроле и уважении к пользователю.',
  storyCardTitle: 'Ваше цифровое пространство — понятно.',
  storyText: 'BalanceCleaner помогает увидеть, что занимает место, и принимать уверенные решения.',
  demoNotice: 'Сайт пока показывает demo-экраны. Финальные материалы App Store будут добавлены после запуска.',
  understand: 'Понять', choose: 'Выбрать', balance: 'Сбалансировать',
  thoughtful: 'Продумано с заботой',
  simple: 'Просто с первого нажатия.',
  simpleText: 'Понятные инструменты, прозрачные решения и приватность в центре.',
  talk: 'Связаться с разработчиком →',
  screenLabel: 'Экраны продукта',
  screenTitle: 'Посмотрите приложение<br>до запуска.',
  videoLabel: 'Демо продукта',
  videoTitle: 'Посмотрите, как это работает.',
  videoLead: 'Демо на всех поддерживаемых моделях iPhone.',
  why: 'Почему BalanceCleaner',
  featuresTitle: 'Продумано и просто.',
  clear: 'Понятный дизайн', clearText: 'Инструменты, которыми легко пользоваться с первого нажатия.',
  private: 'Приватность прежде всего', privateText: 'Прозрачные решения и уважение к информации.',
  quiet: 'Тихая мощь', quietText: 'Полезная аналитика без лишней сложности.',
  improve: 'Становится лучше', improveText: 'Отправляйте отзывы разработчику.',
  listening: 'Мы слушаем', idea: 'Есть идея?',
  ideaText: 'Отправьте отзыв или задайте вопрос через поддержку.',
  openSupport: 'Открыть поддержку →',
  faqTitle: 'Часто задаваемые вопросы',
  faq1q: 'Что такое BalanceCleaner?',
  faq1a: 'BalanceCleaner позволяет выбрать точную сумму для обнуления остатка Apple ID — без регистрации аккаунта.',
  faq2q: 'Как работает разбивка баланса?',
  faq2a: 'Перед подтверждением операции вы видите точную разбивку остатка и расчётных частей. Всё прозрачно.',
  faq3q: 'Безопасны ли мои данные?',
  faq3a: 'Да. Вся обработка происходит локально на устройстве через StoreKit от Apple. Мы не собираем и не загружаем данные.',
  faq4q: 'Нужен ли аккаунт?',
  faq4a: 'Аккаунт не нужен. Скачайте и начните сразу.',
  faq5q: 'Что такое Pro?',
  faq5a: 'Pro открывает полную историю транзакций, экспорт в PDF и расширенные настройки. Основной функционал бесплатен.'
});

fill('fr', {
  about: 'À propos', screens: 'Écrans', video: 'Vidéo', features: 'Fonctions',
  support: 'Assistance', privacy: 'Confidentialité',
  subHeaderText: 'Disponible pour iPhone', subHeaderBtn: 'Télécharger',
  eyebrow: 'Une vie numérique plus calme',
  title: 'Faites de la place à l\'essentiel.',
  lead: 'BalanceCleaner apporte clarté et sérénité à votre univers numérique.',
  explore: 'Découvrir le produit →',
  ideaLabel: 'L\'idée',
  storyTitle: 'Moins de bruit.<br>Plus d\'équilibre.',
  talk: 'Parler au développeur →',
  openSupport: 'Ouvrir l\'assistance →',
  faqTitle: 'Questions fréquentes'
});

fill('de', {
  about: 'Über uns', screens: 'Screens', video: 'Video', features: 'Funktionen',
  support: 'Support', privacy: 'Datenschutz',
  subHeaderText: 'Verfügbar für iPhone', subHeaderBtn: 'Laden',
  eyebrow: 'Ein ruhigeres digitales Leben',
  title: 'Schaffe Raum für das Wesentliche.',
  lead: 'BalanceCleaner bringt Klarheit in deine digitale Welt.',
  explore: 'Produkt entdecken →',
  ideaLabel: 'Die Idee',
  storyTitle: 'Weniger Lärm.<br>Mehr Balance.',
  talk: 'Entwickler kontaktieren →',
  openSupport: 'Support öffnen →',
  faqTitle: 'Häufige Fragen'
});

fill('es', {
  about: 'Acerca de', screens: 'Pantallas', video: 'Vídeo', features: 'Funciones',
  support: 'Soporte', privacy: 'Privacidad',
  subHeaderText: 'Disponible para iPhone', subHeaderBtn: 'Descargar',
  eyebrow: 'Una vida digital más tranquila',
  title: 'Haz espacio para lo importante.',
  lead: 'BalanceCleaner aporta claridad a tu mundo digital.',
  explore: 'Explorar el producto →',
  ideaLabel: 'La idea',
  storyTitle: 'Menos ruido.<br>Más balance.',
  talk: 'Hablar con el desarrollador →',
  openSupport: 'Abrir soporte →',
  faqTitle: 'Preguntas frecuentes'
});

fill('it', {
  about: 'Info', screens: 'Schermate', video: 'Video', features: 'Funzioni',
  support: 'Supporto', privacy: 'Privacy',
  subHeaderText: 'Disponibile per iPhone', subHeaderBtn: 'Scarica',
  eyebrow: 'Una vita digitale più serena',
  title: 'Fai spazio a ciò che conta.',
  lead: 'BalanceCleaner porta chiarezza nel tuo mondo digitale.',
  explore: 'Scopri il prodotto →',
  ideaLabel: 'L\'idea',
  storyTitle: 'Meno rumore.<br>Più equilibrio.',
  talk: 'Parla con lo sviluppatore →',
  openSupport: 'Apri supporto →',
  faqTitle: 'Domande frequenti'
});

// =========================================================================
// APPLY LANGUAGE
// =========================================================================
function applyLanguage(code) {
  const t = dictionaries[code] || dictionaries.en;
  document.documentElement.lang = code;
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const val = t[el.dataset.i18n];
    if (val != null) el.innerHTML = val;
  });
  localStorage.setItem('balance-language', code);
  // Update all lang labels
  document.querySelectorAll('.lang-label').forEach(lbl => {
    lbl.textContent = code.toUpperCase();
  });
  // Bold active in all menus
  document.querySelectorAll('.lang-menu button').forEach(btn => {
    btn.style.fontWeight = btn.dataset.val === code ? '700' : 'normal';
  });
}

// Initialize language
const savedLang = localStorage.getItem('balance-language') || 'en';
applyLanguage(savedLang);

// =========================================================================
// THEME SWITCHING — Ripple from click point, 2s
// =========================================================================
function applyTheme(mode) {
  document.documentElement.classList.toggle('light', mode === 'light');
  const icon = mode === 'light' ? '☾' : '☼';
  document.querySelectorAll('.theme-icon').forEach(el => el.textContent = icon);
  document.querySelectorAll('.theme').forEach(btn => {
    btn.setAttribute('aria-label', mode === 'light' ? 'Switch to dark theme' : 'Switch to light theme');
  });
  localStorage.setItem('balance-theme', mode);
}

applyTheme(localStorage.getItem('balance-theme') || 'dark');

document.addEventListener('click', function(e) {
  const btn = e.target.closest('.theme');
  if (!btn) return;

  const next = document.documentElement.classList.contains('light') ? 'dark' : 'light';
  const color = next === 'light' ? '#edf8f1' : '#07110d';

  const overlay = document.createElement('div');
  overlay.style.cssText = [
    'position:fixed',
    `left:${e.clientX}px`,
    `top:${e.clientY}px`,
    'width:0', 'height:0',
    'border-radius:50%',
    `background:${color}`,
    'transform:translate(-50%,-50%)',
    'z-index:9999',
    'pointer-events:none',
    'transition:width 0.8s ease, height 0.8s ease, opacity 0.4s ease 0.4s'
  ].join(';');
  document.body.appendChild(overlay);

  // Force reflow then expand
  overlay.getBoundingClientRect();
  const maxDim = (Math.max(window.innerWidth, window.innerHeight) * 3) + 'px';
  overlay.style.width = maxDim;
  overlay.style.height = maxDim;

  // Apply theme mid-transition for smooth feel
  setTimeout(() => applyTheme(next), 300);
  setTimeout(() => { overlay.style.opacity = '0'; }, 400);
  setTimeout(() => overlay.remove(), 850);
});

// =========================================================================
// LANGUAGE SWITCHER DROPDOWNS (multiple on page)
// =========================================================================
document.addEventListener('click', function(e) {
  const btn = e.target.closest('.lang-btn');
  if (btn) {
    e.stopPropagation();
    const menu = btn.closest('.custom-lang').querySelector('.lang-menu');
    const isOpen = menu.classList.contains('show');
    // Close all
    document.querySelectorAll('.lang-menu').forEach(m => m.classList.remove('show'));
    if (!isOpen) menu.classList.add('show');
    return;
  }

  const menuBtn = e.target.closest('.lang-menu button');
  if (menuBtn) {
    const code = menuBtn.dataset.val;
    if (code) applyLanguage(code);
    document.querySelectorAll('.lang-menu').forEach(m => m.classList.remove('show'));
    return;
  }

  // Click outside — close all
  document.querySelectorAll('.lang-menu').forEach(m => m.classList.remove('show'));
});

// =========================================================================
// SCROLL REVEAL
// =========================================================================
function revealOnScroll() {
  document.querySelectorAll('.reveal').forEach(el => {
    if (el.getBoundingClientRect().top < window.innerHeight - 80) {
      el.classList.add('active');
    }
  });
}
window.addEventListener('scroll', revealOnScroll, { passive: true });
revealOnScroll();

// =========================================================================
// COVERFLOW CAROUSEL
// =========================================================================
class Coverflow {
  constructor() {
    this.items = Array.from(document.querySelectorAll('.coverflow-item'));
    if (!this.items.length) return;
    this.dots = Array.from(document.querySelectorAll('.indicator'));
    this.total = this.items.length;
    this.current = Math.floor(this.total / 2);
    this.playing = true;
    this.timer = null;
    this.speed = 3200;
    this.render();
    this.bindEvents();
    this.autoplay();
  }

  render() {
    const mobile = window.innerWidth < 768;
    const spacing = mobile ? 120 : 195;
    this.items.forEach((item, i) => {
      let off = i - this.current;
      if (off > this.total / 2) off -= this.total;
      if (off < -this.total / 2) off += this.total;
      const x = off * spacing;
      const z = off === 0 ? 160 : Math.abs(off) === 1 ? 0 : -120;
      const ry = off === 0 ? 0 : off * -35;
      const sc = off === 0 ? 1 : Math.abs(off) === 1 ? 0.85 : Math.abs(off) === 2 ? 0.7 : 0.5;
      const op = Math.abs(off) > 2 ? 0 : Math.abs(off) === 2 ? 0.45 : Math.abs(off) === 1 ? 0.78 : 1;
      item.style.transform = `translate(-50%,-50%) translateX(${x}px) translateZ(${z}px) rotateY(${ry}deg) scale(${sc})`;
      item.style.opacity = op;
      item.style.zIndex = this.total - Math.abs(off);
      item.style.pointerEvents = Math.abs(off) > 1 ? 'none' : 'auto';
    });
    this.dots.forEach((d, i) => d.classList.toggle('active', i === this.current));
  }

  prev() { this.current = (this.current - 1 + this.total) % this.total; this.render(); }
  next() { this.current = (this.current + 1) % this.total; this.render(); }
  goTo(i) { this.current = i; this.render(); }

  autoplay() {
    this.timer = setInterval(() => this.next(), this.speed);
    this.playing = true;
  }
  pause() {
    clearInterval(this.timer);
    this.playing = false;
    const btn = document.getElementById('playPauseBtn');
    if (btn) btn.innerHTML = '▶';
  }
  resume() {
    this.autoplay();
    const btn = document.getElementById('playPauseBtn');
    if (btn) btn.innerHTML = '❚❚';
  }

  bindEvents() {
    document.getElementById('prevBtn')?.addEventListener('click', () => { this.pause(); this.prev(); });
    document.getElementById('nextBtn')?.addEventListener('click', () => { this.pause(); this.next(); });
    document.getElementById('playPauseBtn')?.addEventListener('click', () => {
      this.playing ? this.pause() : this.resume();
    });
    this.dots.forEach((d, i) => d.addEventListener('click', () => { this.pause(); this.goTo(i); }));
    this.items.forEach((item, i) => item.addEventListener('click', () => {
      if (i !== this.current) { this.pause(); this.goTo(i); }
    }));

    // Swipe
    let sx = 0;
    const cnt = document.getElementById('coverflowContainer');
    if (cnt) {
      cnt.addEventListener('touchstart', e => { sx = e.touches[0].clientX; }, { passive: true });
      cnt.addEventListener('touchend', e => {
        const dx = sx - e.changedTouches[0].clientX;
        if (Math.abs(dx) > 40) { this.pause(); dx > 0 ? this.next() : this.prev(); }
      }, { passive: true });
    }

    window.addEventListener('resize', () => this.render());
  }
}

document.addEventListener('DOMContentLoaded', () => new Coverflow());


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
