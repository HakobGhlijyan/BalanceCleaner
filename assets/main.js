/**
     * Slovari perevodov (i18n Dictionaries)
     * Базовые словари локализации. English используется как fallback.
     */
    const dictionaries = {
      en: {
        about: 'About', screens: 'Screens', video: 'Video', features: 'Features', support: 'Support', privacy: 'Privacy',
        demos: 'Open all demos', eyebrow: 'A calmer digital life', title: 'Make room for what matters.',
        lead: 'BalanceCleaner brings clarity to your digital world with thoughtful tools, a quiet interface, and privacy at its core.',
        explore: 'Explore the product →', devices: 'See device variants',
        cta: 'Designed for your device, and the app requires no account.',
        meta: 'Free to use • iPhone (iPad compatible) • Premium optional',
        ideaLabel: 'The idea', storyTitle: 'Less noise.<br>More balance.',
        storyLead: 'A calm product story built around clarity, control and a respectful digital experience.',
        storyCardTitle: 'Your digital space, understood.',
        storyText: 'BalanceCleaner helps people see what is taking up space, make confident decisions and keep their everyday devices feeling lighter.',
        demoNotice: 'The website currently presents demo screens and a demo video. Final App Store Connect materials can be added later.',
        understand: 'Understand', choose: 'Choose', balance: 'Balance', thoughtful: 'Built thoughtfully',
        simple: 'Simple from the first tap.', simpleText: 'Focused tools, transparent choices and privacy at the centre of every interaction.',
        talk: 'Talk to the developer →', screenLabel: 'Product screens', screenTitle: 'See the app<br>before it ships.',
        screenLead: 'These are temporary demo captures. Open the gallery for fullscreen viewing.',
        dashboard: 'Daily balance', dashboardText: 'See your digital space at a glance.',
        cleaning: 'Smart cleaning', cleaningText: 'Review suggestions with confidence.',
        premium: 'Premium dashboard', premiumText: 'A broader view for deeper control.',
        gallery: 'Open full screen gallery →', videoLabel: 'Product demo', videoTitle: 'See how it works.',
        videoLead: 'A separate demo video section, presented in the same visual system as the screens.',
        videoCaption: 'How to use BalanceCleaner · temporary demo', why: 'Why BalanceCleaner',
        featuresTitle: 'Thoughtfully simple.', clear: 'Clear by design', clearText: 'Focused tools that feel easy from the first tap.',
        private: 'Privacy first', privateText: 'Transparent choices and respect for your information.',
        quiet: 'Quietly powerful', quietText: 'Useful insights without unnecessary complexity.',
        improve: 'Made to improve', improveText: 'Send feedback directly to the developer.',
        listening: 'We’re listening', idea: 'Have an idea?',
        ideaText: 'Send feedback, report a problem or ask a question through our support page.',
        openSupport: 'Open support →'
      },
      fr: {
        about: 'À propos', screens: 'Écrans', video: 'Vidéo', features: 'Fonctions', support: 'Assistance', privacy: 'Confidentialité',
        demos: 'Toutes les démos', eyebrow: 'Une vie numérique plus calme', title: 'Faites de la place à l’essentiel.',
        lead: 'BalanceCleaner apporte clarté et sérénité à votre univers numérique, avec la confidentialité au cœur.',
        explore: 'Découvrir le produit →', devices: 'Voir les appareils',
        cta: 'Conçu pour votre appareil, sans compte requis.',
        meta: 'Gratuit • iPhone (compatible iPad) • Premium facultatif',
        ideaLabel: 'L’idée', storyTitle: 'Moins de bruit.<br>Plus d’équilibre.',
        storyLead: 'Une expérience calme fondée sur la clarté, le contrôle et le respect.',
        storyCardTitle: 'Votre espace numérique, en toute clarté.',
        storyText: 'BalanceCleaner vous aide à voir ce qui prend de la place et à faire des choix sereins.',
        demoNotice: 'Le site présente actuellement des écrans et une vidéo de démonstration temporaires.',
        understand: 'Comprendre', choose: 'Choisir', balance: 'Équilibrer', thoughtful: 'Pensé avec soin',
        simple: 'Simple dès le premier geste.', simpleText: 'Des outils ciblés, des choix transparents et la confidentialité au centre.',
        talk: 'Parler au développeur →', screenLabel: 'Écrans du produit', screenTitle: 'Découvrez l’app<br>avant son lancement.',
        screenLead: 'Captures temporaires. Ouvrez la galerie en plein écran.',
        dashboard: 'Équilibre quotidien', dashboardText: 'Une vue claire de votre espace numérique.',
        cleaning: 'Nettoyage intelligent', cleaningText: 'Examinez les suggestions en confiance.',
        premium: 'Tableau de bord premium', premiumText: 'Une vue plus large pour un meilleur contrôle.',
        gallery: 'Ouvrir la galerie →', videoLabel: 'Démo produit', videoTitle: 'Découvrez son fonctionnement.',
        videoLead: 'Une vidéo de démonstration dans le même style visuel.',
        videoCaption: 'Comment utiliser BalanceCleaner · démo temporaire', why: 'Pourquoi BalanceCleaner',
        featuresTitle: 'Pensé avec simplicité.', clear: 'Clair par nature', clearText: 'Des outils simples dès le premier geste.',
        private: 'Confidentialité d’abord', privateText: 'Des choix transparents et respectueux.',
        quiet: 'Discrètement puissant', quietText: 'Des informations utiles sans complexité.',
        improve: 'Toujours meilleur', improveText: 'Envoyez vos commentaires au développeur.',
        listening: 'Nous vous écoutons', idea: 'Une idée ?',
        ideaText: 'Envoyez un commentaire ou une question via l’assistance.',
        openSupport: 'Ouvrir l’assistance →'
      },
      es: {},
      it: {},
      de: {},
      ru: {}
    };

    const fallback = dictionaries.en;

    /**
     * Наполнение дополнительных языков поверх fallback значений
     */
    function fill(code, overrides) {
      dictionaries[code] = Object.assign({}, fallback, overrides);
    }

    fill('es', {
      about: 'Acerca de', screens: 'Pantallas', video: 'Vídeo', features: 'Funciones', support: 'Soporte', privacy: 'Privacidad',
      demos: 'Todas las demos', eyebrow: 'Una vida digital más tranquila', title: 'Haz espacio para lo importante.',
      lead: 'BalanceCleaner aporta claridad a tu mundo digital con privacidad en el centro.',
      explore: 'Explorar el producto →', devices: 'Ver dispositivos',
      cta: 'Diseñada para tu dispositivo y sin necesidad de cuenta.',
      meta: 'Gratis • iPhone (compatible con iPad) • Premium opcional'
    });

    fill('it', {
      about: 'Info', screens: 'Schermate', video: 'Video', features: 'Funzioni', support: 'Supporto', privacy: 'Privacy',
      demos: 'Tutte le demo', eyebrow: 'Una vita digitale più serena', title: 'Fai spazio a ciò che conta.',
      explore: 'Scopri il prodotto →', devices: 'Vedi dispositivi'
    });

    fill('de', {
      about: 'Über uns', screens: 'Screens', video: 'Video', features: 'Funktionen', support: 'Support', privacy: 'Datenschutz',
      demos: 'Alle Demos', eyebrow: 'Ein ruhigeres digitales Leben', title: 'Schaffe Raum für das Wesentliche.',
      explore: 'Produkt entdecken →', devices: 'Geräte ansehen'
    });

    fill('ru', {
      about: 'О продукте', screens: 'Экраны', video: 'Видео', features: 'Возможности', support: 'Поддержка', privacy: 'Приватность',
      demos: 'Все демо', eyebrow: 'Более спокойная цифровая жизнь', title: 'Освободите место для важного.',
      lead: 'BalanceCleaner помогает навести порядок в цифровом мире, ставя приватность в основу.',
      explore: 'Открыть продукт →', devices: 'Посмотреть устройства',
      cta: 'Создано для вашего устройства, аккаунт не требуется.',
      meta: 'Бесплатно • iPhone (совместимо с iPad) • Premium по желанию',
      ideaLabel: 'Идея', storyTitle: 'Меньше шума.<br>Больше баланса.',
      storyLead: 'Спокойный продукт, построенный на ясности, контроле и уважении к пользователю.',
      storyCardTitle: 'Ваше цифровое пространство — понятно.',
      storyText: 'BalanceCleaner помогает увидеть, что занимает место, и принимать уверенные решения.',
      demoNotice: 'Сайт пока показывает demo-экраны и видео. Финальные материалы App Store Connect будут добавлены позже.',
      understand: 'Понять', choose: 'Выбрать', balance: 'Сбалансировать', thoughtful: 'Продумано с заботой',
      simple: 'Просто с первого нажатия.', simpleText: 'Понятные инструменты, прозрачные решения и приватность в центре.',
      talk: 'Связаться с разработчиком →', screenLabel: 'Экраны продукта', screenTitle: 'Посмотрите приложение<br>до запуска.',
      screenLead: 'Временные demo-экраны. Откройте галерею на весь экран.',
      dashboard: 'Ежедневный баланс', dashboardText: 'Понятный обзор цифрового пространства.',
      cleaning: 'Умная очистка', cleaningText: 'Проверяйте предложения уверенно.',
      premium: 'Премиум-панель', premiumText: 'Расширенный обзор для большего контроля.',
      gallery: 'Открыть галерею →', videoLabel: 'Демо продукта', videoTitle: 'Посмотрите, как это работает.',
      videoLead: 'Отдельное видео в том же визуальном стиле.',
      videoCaption: 'Как использовать BalanceCleaner · временное demo', why: 'Почему BalanceCleaner',
      featuresTitle: 'Продумано и просто.', clear: 'Понятный дизайн',
      clearText: 'Инструменты, которыми легко пользоваться с первого нажатия.',
      private: 'Приватность прежде всего', privateText: 'Прозрачные решения и уважение к информации.',
      quiet: 'Тихая мощь', quietText: 'Полезная аналитика без лишней сложности.',
      improve: 'Становится лучше', improveText: 'Отправляйте отзывы разработчику.',
      listening: 'Мы слушаем', idea: 'Есть идея?',
      ideaText: 'Отправьте отзыв или задайте вопрос через поддержку.',
      openSupport: 'Открыть поддержку →'
    });

    /**
     * Логика смены языка
     */
    const langSelect = document.getElementById('language');

    function applyLanguage(code) {
      const t = dictionaries[code] || fallback;
      document.documentElement.lang = code;
      
      // Находим все элементы с атрибутом data-i18n и обновляем их контент
      document.querySelectorAll('[data-i18n]').forEach(el => {
        const value = t[el.dataset.i18n];
        if (value != null) {
          el.innerHTML = value;
        }
      });

      // Сохраняем выбор в localStorage
      localStorage.setItem('balance-language', code);
      langSelect.value = code;
    }

    // Инициализация языка при загрузке
    applyLanguage(localStorage.getItem('balance-language') || 'en');
    
    // Слушатель событий выбора языка
    langSelect.addEventListener('change', e => applyLanguage(e.target.value));

    /**
     * Логика переключения темы (Light / Dark Theme)
     */
    const root = document.documentElement;
    const themeBtn = document.getElementById('theme');

    function applyTheme(mode) {
      root.classList.toggle('light', mode === 'light');
      themeBtn.querySelector('.theme-icon').textContent = mode === 'light' ? '☾' : '☼';
      themeBtn.setAttribute('aria-label', mode === 'light' ? 'Switch to dark theme' : 'Switch to light theme');
      localStorage.setItem('balance-theme', mode);
    }

    // Инициализация темы при загрузке
    applyTheme(localStorage.getItem('balance-theme') || 'dark');

    // Обработчик нажатия на кнопку смены темы
    themeBtn.addEventListener('click', () => {
      const next = root.classList.contains('light') ? 'dark' : 'light';
      themeBtn.style.setProperty('--theme-transition-color', next === 'light' ? '#edf8f1' : '#07110d');
      themeBtn.classList.add('theme-transition');
      
      applyTheme(next);
      
      setTimeout(() => themeBtn.classList.remove('theme-transition'), 2000);
    });
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
