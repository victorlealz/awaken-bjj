# CSS Skills & Techniques Used

A comprehensive reference of every CSS skill, pattern, and technique applied in the Awaken BJJ landing page.

---

## 1. Custom Properties (CSS Variables)

The entire design system is driven by CSS custom properties defined on `:root`, enabling centralized control of colors, fonts, spacing, and transitions.

```css
:root {
  --color-primary: #C1C9D1;
  --color-secondary: #34AADC;
  --color-accent: #000000;
  --font-display: 'Bebas Neue', Helvetica, Arial, sans-serif;
  --space-xl: 4rem;
  --transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
```

**Why**: Single source of truth for the design system. Change one variable and it cascades everywhere — colors, spacing, timing.

---

## 2. CSS Reset (Box Model Normalization)

```css
*, *::before, *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
```

**Why**: Eliminates browser inconsistencies. `border-box` ensures padding and borders are included in element dimensions.

---

## 3. Fluid Typography with `clamp()`

```css
.heading-xl { font-size: clamp(3.5rem, 10vw, 8rem); }
.heading-lg { font-size: clamp(2.5rem, 6vw, 5rem); }
```

**Why**: Creates responsive type that scales smoothly between a minimum and maximum size without media queries. The middle `vw` value is the preferred fluid size.

---

## 4. CSS Grid Layouts

Used for multi-column sections throughout the page:

```css
.about-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-3xl);
  align-items: center;
}

.method-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1px; /* 1px gap creates visible grid lines */
  background: rgba(255, 255, 255, 0.1); /* Grid line color */
}

.audience-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: var(--space-md);
}
```

**Why**: Grid provides precise two-dimensional layout control. The `1px gap + background` trick on `.method-grid` creates subtle grid lines without extra markup.

---

## 5. Flexbox

Used for navigation, button groups, inline elements, and centering:

```css
.nav-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.hero-cta-group {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-sm);
}
```

**Why**: One-dimensional alignment. Flex for rows/lists, Grid for complex layouts.

---

## 6. Fixed Positioning & Backdrop Blur

```css
.nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
}

.nav.scrolled {
  background: rgba(0, 0, 0, 0.95);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
}
```

**Why**: Sticky navigation with a frosted glass effect on scroll. `-webkit-` prefix needed for Safari support.

---

## 7. CSS Transitions with Custom Easing

```css
--transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1);

.btn {
  transition: all var(--transition);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(52, 170, 220, 0.3);
}
```

**Why**: `cubic-bezier(0.4, 0, 0.2, 1)` is Material Design's standard easing — fast start, gentle deceleration. More natural than `ease` or `linear`.

---

## 8. CSS Keyframe Animations

```css
@keyframes float {
  0%, 100% { transform: translateX(-50%) translateY(0); }
  50% { transform: translateX(-50%) translateY(-8px); }
}

@keyframes pulse-green {
  0%, 100% { box-shadow: 0 4px 20px rgba(37, 211, 102, 0.4); }
  50% { box-shadow: 0 4px 30px rgba(37, 211, 102, 0.6); }
}
```

**Why**: `float` draws attention to the scroll indicator. `pulse-green` makes the WhatsApp button gently breathe — attracting clicks without being annoying.

---

## 9. Pseudo-Elements (`::before`, `::after`)

```css
.hero-eyebrow::before {
  content: '';
  display: block;
  width: 40px;
  height: 1px;
  background: var(--color-secondary);
}

.section-divider::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--color-border);
}

.exp-list li::before {
  content: '—';
  color: var(--color-secondary);
  font-weight: 700;
}
```

**Why**: Decorative elements (lines, dashes) without polluting HTML markup. Clean separation of content and decoration.

---

## 10. Object-Fit for Image Control

```css
.hero-bg img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.4;
  filter: grayscale(30%);
}
```

**Why**: `object-fit: cover` crops images to fill their container proportionally (like `background-size: cover` but for `<img>` tags). Keeps images semantic and accessible with `alt` text.

---

## 11. Aspect Ratio

```css
.about-image-wrap img {
  aspect-ratio: 4/5;
  object-fit: cover;
}
```

**Why**: Forces a consistent portrait proportion on the image regardless of source dimensions. No padding-bottom hack needed.

---

## 12. CSS Filters

```css
.hero-bg img {
  opacity: 0.4;
  filter: grayscale(30%);
}

.about-image-wrap img {
  filter: grayscale(20%);
}
```

**Why**: Desaturates images slightly to maintain the premium, disciplined black-and-white aesthetic without fully removing color.

---

## 13. Multi-Layer Gradients

```css
.hero-overlay {
  background: linear-gradient(
    to top,
    rgba(0, 0, 0, 0.95) 0%,
    rgba(0, 0, 0, 0.5) 40%,
    rgba(0, 0, 0, 0.3) 100%
  );
}
```

**Why**: Three-stop gradient creates a natural darkening toward the bottom where text sits, ensuring readability over any hero image.

---

## 14. RGBA & Transparency System

Used extensively for layered depth:

```css
background: rgba(255, 255, 255, 0.1);   /* Subtle grid lines */
background: rgba(255, 255, 255, 0.03);  /* Hover state on dark bg */
color: rgba(255, 255, 255, 0.7);        /* Muted text on dark bg */
color: rgba(255, 255, 255, 0.4);        /* Very muted text */
```

**Why**: Creates visual hierarchy on dark backgrounds through opacity levels rather than multiple gray color tokens.

---

## 15. Responsive Design with Media Queries

```css
@media (max-width: 1024px) {
  .about-grid { grid-template-columns: 1fr; }
  .audience-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 768px) {
  .nav-links { display: none; }
  .mobile-menu-btn { display: flex; }
  .hero-cta-group { flex-direction: column; }
}
```

**Why**: Mobile-first progressive enhancement. Grid columns collapse (4 → 2 → 1), nav switches to hamburger, CTAs stack vertically.

---

## 16. Scroll-Driven Reveal Animations (CSS + JS)

```css
.reveal {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1),
              transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}

.reveal-delay-1 { transition-delay: 0.1s; }
.reveal-delay-2 { transition-delay: 0.2s; }
```

**Why**: Elements slide up and fade in as they enter the viewport. `cubic-bezier(0.16, 1, 0.3, 1)` is an "ease-out-expo" curve — fast deceleration that feels polished. Triggered by `IntersectionObserver` in JS.

---

## 17. `inset` Shorthand

```css
.hero-bg { position: absolute; inset: 0; }
.hero-overlay { position: absolute; inset: 0; }
```

**Why**: `inset: 0` replaces `top: 0; right: 0; bottom: 0; left: 0;` — cleaner and more readable for full-bleed overlays.

---

## 18. Screen Reader Utility

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
```

**Why**: Visually hides content while keeping it accessible to screen readers. Essential for ARIA labels and skip links.

---

## 19. Text Anti-Aliasing

```css
html {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```

**Why**: Forces subpixel anti-aliasing on macOS/WebKit and Firefox. Makes thin fonts (especially Barlow Light 300) render crisply instead of appearing heavy.

---

## 20. Overflow Control

```css
body { overflow-x: hidden; }

.about-image-wrap {
  max-height: 500px;
  overflow: hidden;
}
```

**Why**: `overflow-x: hidden` on body prevents horizontal scroll from animations. `overflow: hidden` on image wraps creates clean crops.

---

## 21. Interactive States & Box Shadows

```css
.audience-card:hover {
  border-color: var(--color-accent);
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.08);
}

.btn-whatsapp:hover {
  box-shadow: 0 8px 25px rgba(37, 211, 102, 0.3);
}
```

**Why**: Lift effect (translateY + shadow) on hover gives cards and buttons a tactile, physical feel. Color-tinted shadows (green for WhatsApp, blue for primary) feel more natural than neutral gray shadows.

---

## 22. Scroll Behavior

```css
html { scroll-behavior: smooth; }
```

**Why**: Native smooth scrolling for anchor links (`#about`, `#method`, etc.) without JavaScript. JS `scrollIntoView` is added as a progressive enhancement.

---

## Summary Table

| Category | Techniques |
|----------|-----------|
| **Layout** | CSS Grid, Flexbox, `inset` shorthand |
| **Typography** | `clamp()` fluid type, Google Fonts, anti-aliasing |
| **Color** | Custom properties, RGBA layering, CSS filters |
| **Animation** | Keyframes, transitions, cubic-bezier easing, staggered delays |
| **Responsive** | Media queries, grid collapse, show/hide elements |
| **Visual** | Backdrop blur, gradients, box-shadows, pseudo-elements |
| **Images** | `object-fit`, `aspect-ratio`, opacity overlays |
| **Accessibility** | `.sr-only`, semantic HTML, `aria-*` attributes |
