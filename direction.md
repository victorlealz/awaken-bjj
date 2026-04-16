# Direction — Prompt Strategy & Deployment Guide

This document explains the prompt architecture used to build the Awaken BJJ landing page, and provides step-by-step instructions for deploying it online using GitHub and Cloudflare Pages.

---

## Part 1: The Prompt That Built This Website

### Framework Used: BLAST

The entire website was generated from a single, structured prompt following the **BLAST** framework:

| Letter | Section | Purpose |
|--------|---------|---------|
| **B** | Blueprint | Define the goal, audience, value proposition, and deliverables |
| **L** | Link | Specify integrations (WhatsApp, future Supabase, SEO metadata) |
| **A** | Architect | Tech stack, structure, SEO keywords |
| **S** | Style | Colors, typography, design principles, buttons, inspiration |
| **T** | Trigger | Deployment requirements and output format |

### Prompt Breakdown

#### B — BLUEPRINT

The **Northstar** defined the product vision in one sentence:
> "Create a premium, minimalist, high-conversion landing page that positions the instructor as an elite, internationally experienced Jiu-Jitsu coach offering personalized, concept-driven private training starting at $80/hour."

Key elements specified:
- **Target audience** — 4 segments (enthusiasts, professionals, parents of neurodivergent kids, travelers)
- **Core value proposition** — "Artisanal, individualized Jiu-Jitsu training"
- **Delivery payload** — responsive, mobile-first, bilingual toggle, fast loading, SEO-optimized
- **Behavior rules** — prioritize clarity/hierarchy/conversion, no visual clutter, premium aesthetic
- **Required sections** — 8 sections explicitly listed (Hero through Language Toggle)

#### L — LINK

Specified all external integrations:
- **WhatsApp API** as the primary conversion channel with the exact phone number
- **Future Supabase** integration for leads and scheduling
- **SEO/OpenGraph metadata** requirements

#### A — ARCHITECT

Defined the technical constraints:
- HTML5 + CSS + minimal JS (no frameworks)
- Component-based sections with reusable CTA buttons
- Semantic HTML for SEO
- Specific keywords to target

#### S — STYLE (Critical Section)

The most detailed section — provided the exact design system:
- **Hex color codes** for every token (primary, secondary, accent, background, text)
- **Typography** stack (Helvetica, Arial, sans-serif)
- **Design principles** — high contrast, generous whitespace, grid-based, sharp edges
- **Button styling** — black background, white text, strong CTA emphasis
- **Inspiration** — Art of Jiu Jitsu (minimal, elite, disciplined)

#### Content Section

Provided **exact instructor data** with no room for AI invention:
- Age, belt rank, Muay Thai rank
- Complete teaching history with gym names and years
- All competition titles listed individually
- International experience with specific cities/countries
- Certifications
- Teaching philosophy broken into 4 pillars
- Copywriting tone, key messages, pricing, CTA text

#### Output Format

Explicit constraints on what to deliver and what NOT to do:
- ✅ Full single-page website code, production-ready, language toggle working
- ❌ No unnecessary frameworks, no overcomplicated animations, no generic clichés

### Why This Prompt Worked

1. **Specificity** — No ambiguity. Colors were hex codes, not "blue-ish." Content was exact quotes, not "write something about..."
2. **Structure** — BLAST framework organized concerns so nothing was missed
3. **Constraints** — Explicit "do NOT" rules prevented over-engineering
4. **Real data** — Providing exact instructor credentials meant no hallucinated content
5. **Aesthetic reference** — "Art of Jiu Jitsu" as inspiration gave a concrete design direction

---

## Part 2: Deploying with GitHub + Cloudflare Pages

### Prerequisites

- A [GitHub account](https://github.com)
- A [Cloudflare account](https://dash.cloudflare.com/sign-up) (free tier works)
- [Git installed](https://git-scm.com/downloads) on your computer
- (Optional) A custom domain

---

### Step 1: Create a GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. **Repository name**: `awaken-bjj`
3. **Visibility**: Public (required for free GitHub Pages, optional for Cloudflare)
4. **Do NOT** initialize with README (we already have one)
5. Click **Create repository**

---

### Step 2: Push Your Code to GitHub

Open a terminal in the `awaken-bjj` folder and run:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "feat: launch Awaken BJJ landing page"

# Add your GitHub repo as remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/awaken-bjj.git

# Push to GitHub
git branch -M main
git push -u origin main
```

After this, your code will be live on GitHub at `https://github.com/YOUR_USERNAME/awaken-bjj`.

---

### Step 3: Connect to Cloudflare Pages

1. Log in to [Cloudflare Dashboard](https://dash.cloudflare.com)
2. In the left sidebar, click **Workers & Pages**
3. Click **Create** → **Pages** → **Connect to Git**
4. Authorize Cloudflare to access your GitHub account
5. Select the **awaken-bjj** repository
6. Configure the build settings:

| Setting | Value |
|---------|-------|
| **Project name** | `awaken-bjj` |
| **Production branch** | `main` |
| **Framework preset** | None |
| **Build command** | *(leave empty)* |
| **Build output directory** | `/` |

7. Click **Save and Deploy**

> **Important**: Since this is a static HTML site, there is NO build command and the output directory is just `/` (the root). Cloudflare will serve `index.html` directly.

---

### Step 4: Your Site Is Live

After ~1 minute, Cloudflare will assign a free subdomain:

```
https://awaken-bjj.pages.dev
```

Every time you push to `main` on GitHub, Cloudflare automatically redeploys.

---

### Step 5 (Optional): Custom Domain

If you own a domain (e.g., `awakenbjj.com`):

1. In Cloudflare Pages → your project → **Custom domains**
2. Click **Set up a custom domain**
3. Enter your domain: `awakenbjj.com`
4. Cloudflare will show DNS instructions:

**If your domain's DNS is on Cloudflare:**
- It auto-creates the CNAME record. Just click **Activate domain**.

**If your domain's DNS is elsewhere (e.g., Hostinger, GoDaddy):**
- Add a **CNAME record**:
  - **Name**: `@` or `www`
  - **Target**: `awaken-bjj.pages.dev`
- Wait for DNS propagation (usually 5–30 minutes)

5. Cloudflare automatically provisions a **free SSL certificate** — your site will be HTTPS by default.

---

### Step 6 (Optional): Add `www` Redirect

To make `www.awakenbjj.com` redirect to `awakenbjj.com`:

1. In Cloudflare Pages → Custom domains
2. Add `www.awakenbjj.com` as a second custom domain
3. Cloudflare handles the redirect automatically

---

### Updating the Site

After making changes locally:

```bash
git add .
git commit -m "update: description of what changed"
git push
```

Cloudflare detects the push and redeploys within ~30 seconds.

---

### Recommended `.gitignore`

Create a `.gitignore` file to keep the repo clean:

```
# OS files
.DS_Store
Thumbs.db
desktop.ini

# Editor files
.vscode/
*.swp
*.swo

# Misc
*.log
```

---

## Architecture Diagram

```
┌──────────────┐       git push       ┌──────────────┐
│              │ ───────────────────▶  │              │
│  Your Local  │                       │    GitHub     │
│   Machine    │                       │  Repository  │
│              │                       │              │
└──────────────┘                       └──────┬───────┘
                                              │
                                     webhook trigger
                                              │
                                              ▼
                                       ┌──────────────┐
                                       │  Cloudflare   │
                                       │    Pages      │
                                       │              │
                                       │  Serves site  │
                                       │  at .pages.dev│
                                       │  + custom     │
                                       │    domain     │
                                       │  + free SSL   │
                                       └──────────────┘
                                              │
                                              ▼
                                       ┌──────────────┐
                                       │   Visitors    │
                                       │ (global CDN)  │
                                       └──────────────┘
```

---

## Summary

| Step | Action | Time |
|------|--------|------|
| 1 | Create GitHub repo | 1 min |
| 2 | Push code | 2 min |
| 3 | Connect Cloudflare Pages | 3 min |
| 4 | Site live at `.pages.dev` | 1 min |
| 5 | Custom domain (optional) | 5–30 min (DNS) |

**Total time to go live: ~7 minutes.**
