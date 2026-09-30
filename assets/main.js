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
    title: 'Zero your Apple ID balance.<br>Change region freely.',
    lead: 'BalanceCleaner lets you clear your Apple ID leftover balance using real in-app purchases — so you can switch your App Store region freely.',
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

    guideLabel: 'Overview',
    guideTitle: 'Clear Apple ID Balance',
    guideDesc: 'To change your Apple ID region, your account balance must be exactly zero.',
    step1Title: 'Check Your Remaining Balance',
    step1Desc: 'Open App Store account settings and find your exact remaining store credit.',
    step2Title: 'Calculate and Purchase',
    step2Desc: 'Buy an item or tip in the app. If price exceeds balance, Apple charges the rest from your credit card.',
    step3Title: 'Change Region Successfully',
    step3Desc: 'Once zeroed, return to Apple ID settings and freely switch to your new region.',
    donationTitle: 'Your Payment as a Donation',
    donationDesc: 'When you pay your remaining balance ($0.50, $1.00, etc.), you are donating directly to support independent iOS development.',
    donationFooter: 'Thank you for helping keep this tool alive and free of ads!',
    guideNeedHelp: 'Need Help?',
    guideSupportTitle: 'Contact Apple Support',
    guideSupportDesc: 'If your balance is lower than the lowest purchase price, contact Apple Support directly to manually zero it out.',
    guideSupportWeb: 'Apple Billing & Subscriptions',

    privacyEyebrow: 'YOUR PRIVACY MATTERS',
    privacyTitle: 'Privacy Policy',
    privCard1Title: 'Apple StoreKit Secure',
    privCard1Desc: 'All balance clearing operations run through official Apple In-App Purchase APIs.',
    privCard2Title: 'Zero Payment Access',
    privCard2Desc: 'We never see, collect, or store your Apple ID password, credit cards, or billing info.',
    privCard3Title: 'No Data Sales',
    privCard3Desc: 'Your personal details are never sold, rented, or shared with third-party advertisers.',
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
  title: 'Обнулите баланс Apple ID.<br>Смените регион свободно.',
  lead: 'BalanceCleaner позволяет очистить остаток на Apple ID через реальные покупки — чтобы вы могли сменить регион App Store без ограничений.',
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
  faq5a: 'Pro открывает полную историю транзакций, экспорт в PDF и расширенные настройки. Основной функционал бесплатен.',
  guideLabel: 'Обзор',
  guideTitle: 'Очистите баланс Apple ID',
  guideDesc: 'Для смены региона Apple ID баланс должен быть ровно нулевым.',
  step1Title: 'Проверьте остаток',
  step1Desc: 'Откройте настройки аккаунта App Store и найдите точный остаток кредита.',
  step2Title: 'Рассчитайте и купите',
  step2Desc: 'Купите товар или типовой предмет в приложении. Если цена превышает баланс — Apple спишет остаток с карты.',
  step3Title: 'Успешная смена региона',
  step3Desc: 'После обнуления вернитесь в настройки Apple ID и выберите новый регион.',
  donationTitle: 'Ваш платёж как поддержка',
  donationDesc: 'Оплачивая остаток ($0.50, $1.00 и т.д.), вы поддерживаете независимую разработку iOS-приложений.',
  donationFooter: 'Спасибо, что помогаете сохранять этот инструмент живым и без рекламы!',
  guideNeedHelp: 'Нужна помощь?',
  guideSupportTitle: 'Обратитесь в службу поддержки Apple',
  guideSupportDesc: 'Если ваш баланс меньше минимальной цены покупки — свяжитесь с Apple Support напрямую.',
  guideSupportWeb: 'Биллинг и подписки Apple',
  privacyEyebrow: 'ВАША ПРИВАТНОСТЬ ВАЖНА',
  privacyTitle: 'Политика конфиденциальности',
  privCard1Title: 'Защита Apple StoreKit',
  privCard1Desc: 'Все операции очистки баланса проходят через официальный Apple In-App Purchase API.',
  privCard2Title: 'Нет доступа к платежам',
  privCard2Desc: 'Мы никогда не видим, не собираем и не храним ваш пароль Apple ID, данные карт или платёжную информацию.',
  privCard3Title: 'Данные не продаются',
  privCard3Desc: 'Ваши личные данные никогда не передаются третьим лицам и рекламодателям.',
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
  faqTitle: 'Questions fréquentes',
  privacyEyebrow: 'VOTRE VIE PRIVÉE COMPTE',
  privacyTitle: 'Politique de confidentialité',
  privCard1Title: 'Apple StoreKit Sécurisé',
  privCard2Title: 'Zéro accès aux paiements',
  privCard3Title: 'Aucune vente de données',
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
  faqTitle: 'Häufige Fragen',
  privacyEyebrow: 'IHRE PRIVATSPHÄRE IST WICHTIG',
  privacyTitle: 'Datenschutzerklärung',
  privCard1Title: 'Apple StoreKit-Sicherheit',
  privCard2Title: 'Kein Zahlungszugriff',
  privCard3Title: 'Keine Datenweitergabe',
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
  faqTitle: 'Preguntas frecuentes',
  privacyEyebrow: 'TU PRIVACIDAD IMPORTA',
  privacyTitle: 'Política de privacidad',
  privCard1Title: 'Apple StoreKit seguro',
  privCard2Title: 'Sin acceso a pagos',
  privCard3Title: 'Sin venta de datos',
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
  faqTitle: 'Domande frequenti',
  privacyEyebrow: 'LA TUA PRIVACY CONTA',
  privacyTitle: 'Informativa sulla privacy',
  privCard1Title: 'Apple StoreKit sicuro',
  privCard2Title: 'Nessun accesso ai pagamenti',
  privCard3Title: 'Nessuna vendita di dati',
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

// =========================================================================
// TIER TRANSLATIONS (from assets/translations/*.json)
// =========================================================================
const tierI18n = {
  en: {
    tiersLabel: "Purchase Tiers",
    tiersTitle: "How Balance Clearing Works",
    tiersDesc: "Each tier is a donation that simultaneously zeros your Apple ID balance. Buy the tier that matches your balance — Apple charges balance first, then card.",
    tiersNote: "💡 Smart Balance Matcher automatically selects the optimal combination of tiers to reach exactly $0.00.",
    tier1Price: "~$0.99 / 1 coin",  tier1Desc: "Clears a balance of ~$0.99.",
    tier2Price: "~$1.99 / 2 coins", tier2Desc: "Clears a balance of ~$1.99.",
    tier3Price: "~$2.99 / 3 coins", tier3Desc: "Use when your balance is around $2–3.",
    tier4Price: "~$3.99 / 4 coins", tier4Desc: "Best for a $3–4 leftover balance.",
    tier5Price: "~$4.99 / 5 coins", tier5Desc: "Handles balances around $4–5.",
    tier10Price: "~$9.99 / 10 coins", tier10Desc: "Clears larger balances up to $10.",
  },
  ru: {
    tiersLabel: "Уровни покупок",
    tiersTitle: "Как работает обнуление баланса",
    tiersDesc: "Каждый тир — это донат, который одновременно обнуляет ваш баланс Apple ID. Выберите тир, соответствующий вашему остатку.",
    tiersNote: "💡 Smart Balance Matcher автоматически подберёт оптимальную комбинацию тиров до $0.00.",
    tier1Price: "~99 ₽ / 1 монета",   tier1Desc: "Обнуляет баланс ~99 ₽.",
    tier2Price: "~199 ₽ / 2 монеты",  tier2Desc: "Для баланса ~199 ₽.",
    tier3Price: "~299 ₽ / 3 монеты",  tier3Desc: "Подходит для остатка 200–300 ₽.",
    tier4Price: "~399 ₽ / 4 монеты",  tier4Desc: "Оптимально для 300–400 ₽.",
    tier5Price: "~499 ₽ / 5 монет",   tier5Desc: "Для остатка до 500 ₽.",
    tier10Price: "~999 ₽ / 10 монет", tier10Desc: "Для больших остатков до 1000 ₽.",
  },
  fr: {
    tiersLabel: "Niveaux d'achat",
    tiersTitle: "Comment fonctionne le solde",
    tier1Price: "~0,99 € / 1 pièce", tier1Desc: "Solde ~0,99 €.",
    tier2Price: "~1,99 € / 2 pièces",tier2Desc: "Solde ~1,99 €.",
    tier3Price: "~2,99 € / 3 pièces",tier3Desc: "Solde ~2–3 €.",
    tier4Price: "~3,99 € / 4 pièces",tier4Desc: "Solde ~3–4 €.",
    tier5Price: "~4,99 € / 5 pièces",tier5Desc: "Solde ~4–5 €.",
    tier10Price: "~9,99 € / 10 pièces",tier10Desc: "Solde ~9–10 €.",
  },
  de: {
    tiersLabel: "Kaufstufen",
    tiersTitle: "Wie das Guthaben-Clearing funktioniert",
    tier1Price: "~0,99 € / 1 Münze", tier1Desc: "Guthaben ~0,99 €.",
    tier2Price: "~1,99 € / 2 Münzen",tier2Desc: "Guthaben ~1,99 €.",
    tier3Price: "~2,99 € / 3 Münzen",tier3Desc: "Guthaben ~2–3 €.",
    tier4Price: "~3,99 € / 4 Münzen",tier4Desc: "Guthaben ~3–4 €.",
    tier5Price: "~4,99 € / 5 Münzen",tier5Desc: "Guthaben ~4–5 €.",
    tier10Price: "~9,99 € / 10 Münzen",tier10Desc: "Guthaben ~9–10 €.",
  },
  es: {
    tiersLabel: "Niveles de compra",
    tiersTitle: "Cómo funciona la compensación de saldo",
    tier1Price: "~0,99 € / 1 moneda", tier1Desc: "Saldo ~0,99 €.",
    tier2Price: "~1,99 € / 2 monedas",tier2Desc: "Saldo ~1,99 €.",
    tier3Price: "~2,99 € / 3 monedas",tier3Desc: "Saldo ~2–3 €.",
    tier4Price: "~3,99 € / 4 monedas",tier4Desc: "Saldo ~3–4 €.",
    tier5Price: "~4,99 € / 5 monedas",tier5Desc: "Saldo ~4–5 €.",
    tier10Price: "~9,99 € / 10 monedas",tier10Desc: "Saldo ~9–10 €.",
  },
  it: {
    tiersLabel: "Livelli di acquisto",
    tiersTitle: "Come funziona la pulizia del saldo",
    tier1Price: "~0,99 € / 1 moneta", tier1Desc: "Saldo ~0,99 €.",
    tier2Price: "~1,99 € / 2 monete", tier2Desc: "Saldo ~1,99 €.",
    tier3Price: "~2,99 € / 3 monete", tier3Desc: "Saldo ~2–3 €.",
    tier4Price: "~3,99 € / 4 monete", tier4Desc: "Saldo ~3–4 €.",
    tier5Price: "~4,99 € / 5 monete", tier5Desc: "Saldo ~4–5 €.",
    tier10Price: "~9,99 € / 10 monete",tier10Desc: "Saldo ~9–10 €.",
  }
};

// Merge tier keys into main i18n dict on language load
(function mergeTierTranslations() {
  for (const lang in tierI18n) {
    if (window.i18n && window.i18n[lang]) {
      Object.assign(window.i18n[lang], tierI18n[lang]);
    }
  }
})();
