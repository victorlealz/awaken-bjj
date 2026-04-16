# Awaken BJJ — Project Context

## Overview
Single-page, bilingual (EN/PT-BR) landing page promoting private Jiu-Jitsu lessons in João Pessoa, Brazil. Built as a static site — no frameworks, no build step.

## Tech Stack
- **HTML5** — semantic, single `index.html`
- **Vanilla CSS** — custom properties design system (no Tailwind, no preprocessors)
- **Vanilla JS** — language toggle, scroll animations, mobile menu
- **Fonts** — Bebas Neue (display) + Barlow (body) via Google Fonts CDN

## Architecture
- All code lives in `index.html` (styles in `<style>`, scripts in `<script>`)
- Images in `assets/img/`
- No dependencies, no `node_modules`, no build pipeline
- Designed for static hosting (Hostinger, GitHub Pages, Netlify, etc.)

## Design System
| Token | Value |
|-------|-------|
| Primary | `#C1C9D1` |
| Secondary | `#34AADC` |
| Accent | `#000000` |
| Background | `#FFFFFF` |
| Text | `#000000` |
| Display Font | `Bebas Neue` |
| Body Font | `Barlow` |

## Bilingual System
- Every translatable element has a `data-i18n="key"` attribute
- Translations live in the `translations` JS object (keys: `en`, `pt`)
- `setLanguage(lang)` updates all DOM text, meta tags, and WhatsApp message URLs
- Language preference persisted in `localStorage` under key `awaken-lang`

## WhatsApp Integration
- Primary conversion channel: `https://wa.me/5583999619497`
- Pre-filled messages switch language automatically
- Floating button (bottom-right) + inline CTAs in Hero, Pricing, and Final CTA sections

## SEO
- Target keywords: "private jiu jitsu João Pessoa", "BJJ private lessons Brazil", "jiu jitsu coach João Pessoa"
- JSON-LD structured data (LocalBusiness schema)
- Open Graph + Twitter Card meta tags
- Semantic HTML with proper heading hierarchy

## Conventions
- **No frameworks** — keep it vanilla unless explicitly approved
- **No generic fonts** — always use the established Bebas Neue + Barlow pairing
- **Sharp edges** — avoid border-radius; maintain the premium martial arts aesthetic
- **All CTAs → WhatsApp** — never add forms or email links without discussion
- **Bilingual parity** — every content change must include both EN and PT-BR translations
- **Mobile-first** — always test responsive behavior; breakpoints at 768px and 1024px

## Future Integration Points
- **Supabase** — lead capture, scheduling (not yet implemented)
- **Analytics** — GA4 or Plausible (add script tag when ready)
- **Instructor photo** — replace `assets/img/logo.png` in the About section with a real photo

## Local Development
```bash
# From the awaken-bjj/ directory:
python -m http.server 8080
# Then open http://localhost:8080
```
