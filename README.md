# Awaken BJJ — Private Jiu-Jitsu Coaching Landing Page

Premium, bilingual (EN/PT-BR) landing page for private Jiu-Jitsu lessons in João Pessoa, Brazil.

## Structure

```
awaken-bjj/
├── index.html          # Single-page landing (all sections)
├── assets/
│   └── img/
│       ├── hero.png    # Hero section background
│       ├── logo.png    # Awaken brand mark
│       └── mat.png     # CTA section background
└── README.md
```

## Features

- **Bilingual Toggle** — Full EN/PT-BR with localStorage persistence
- **WhatsApp Integration** — All CTAs link to WhatsApp with pre-filled messages
- **SEO Optimized** — Meta tags, OG tags, structured data (JSON-LD), semantic HTML
- **Mobile-First** — Responsive design with mobile navigation overlay
- **Scroll Animations** — Lightweight IntersectionObserver-based reveals
- **Floating WhatsApp Button** — Persistent CTA with pulse animation

## Tech Stack

- HTML5 (semantic)
- Vanilla CSS (custom properties design system)
- Vanilla JS (language toggle, scroll effects, mobile menu)
- Google Fonts: Bebas Neue + Barlow

## Deployment

This is a fully static site. Deploy to any static host:

### Hostinger
1. Upload the entire `awaken-bjj/` folder to `public_html/`
2. Done — no build step required

### GitHub Pages
1. Push to a GitHub repo
2. Enable Pages from Settings → Pages → main branch
3. Site will be live at `https://username.github.io/awaken-bjj/`

### Netlify / Vercel
1. Connect the repository
2. No build command needed — set publish directory to `/`

## Customization

- **Colors**: Edit CSS custom properties in `:root` at the top of `index.html`
- **Content**: Edit the `translations` object in the `<script>` section
- **WhatsApp Number**: Search and replace `5583999619497`
- **Images**: Replace files in `assets/img/`

## Future Integration Ready

- **Supabase**: Add lead capture forms connected to Supabase tables
- **Analytics**: Add GA4 / Plausible script tag
- **Domain**: Configure custom domain on your hosting provider

## License

© 2026 Awaken BJJ. All rights reserved.
