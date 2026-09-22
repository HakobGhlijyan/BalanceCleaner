# BalanceCleaner

## Модуль 1 — сайт

Одностраничный сайт-презентация BalanceCleaner в тёмном premium-стиле с красными акцентами, анимированным фоном, floating glass header, App Preview, поддержкой и футером.

## Страницы

- `index.html` — главная страница, hero, preview-заглушки, функции и футер.
- `support.html` — публичная страница поддержки для App Store Connect Support URL.
- `privacy.html` — политика конфиденциальности.
- `LICENSE` — Apache License 2.0.

## Папки и форматы

```text
assets/
├── screenshots/   # PNG/JPG: реальные экраны приложения
├── videos/        # MP4/H.264 или WebM + preview-poster.jpg
├── icons/         # SVG; PNG 512×512 или 1024×1024 с прозрачностью
├── images/        # WebP/JPG/PNG для маркетинговых материалов
└── app-store/     # локализованные материалы App Store Connect
    ├── en-US/
    ├── fr-FR/
    ├── es-ES/
    ├── it-IT/
    ├── de-DE/
    └── ru-RU/
```

В секции Preview сейчас стоят заглушки. Позже добавьте:

- `assets/screenshots/dashboard.png` — обзор;
- `assets/screenshots/cleaning.png` — очистка;
- `assets/screenshots/insights.png` — аналитика.

Имена файлов лучше писать в нижнем регистре через дефис. Не загружайте реальные персональные данные пользователей.

## Поддержка и App Store Connect

После публикации по HTTPS используйте:

```text
https://ваш-домен/support.html
https://ваш-домен/privacy.html
```

`support.html` содержит контакт разработчика, форму с именем, фамилией, email и сообщением, а также ссылку на политику. Перед публикацией проверьте адрес `support@balancecleaner.app`, активацию FormSubmit и соответствие App Privacy фактическому поведению приложения.

## Ветки

- `main` — текущая стабильная версия;
- `module-1-initial-website-state` — резервная точка модуля 1.

## Лицензия

Apache License 2.0. Подробности — в `LICENSE`.
