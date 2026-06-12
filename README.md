# Lexitechsolutions — Portfolio Website

A full-stack personal portfolio website for a Python Developer & ML Engineer, built with Django. Features a dynamic project showcase, skills management, contact form with rate limiting, a custom admin dashboard, and Cloudinary-powered image hosting.

---

## Tech Stack

- **Backend:** Python / Django
- **Database:** PostgreSQL (via `dj-database-url`)
- **Media Storage:** Cloudinary
- **Static Files:** WhiteNoise + Django staticfiles
- **Cache / Rate Limiting:** Redis (`django-redis`)
- **Admin UI:** Jazzmin (custom-themed)
- **Maintenance Mode:** `django-maintenance-mode`
- **Frontend:** Bootstrap 5, Font Awesome, Devicons, Google Fonts

---

## Features

- **Portfolio Home** — Hero, About, Skills, Projects, Services, and Contact sections in a single-page layout
- **Skills Management** — Categorised skills (Languages, Frameworks, ML/Data Science, Tools) with proficiency percentages and animated bars
- **Projects Showcase** — Web, ML, Data Analysis, and Computer Vision categories; featured pinning; tech stack tags; GitHub & live links
- **Contact Form** — IP-based rate limiting (3 submissions / hour via Redis cache), flash message feedback
- **Custom Admin Dashboard** — Jazzmin-powered admin with a bespoke dashboard showing project stats, unread messages, top skills, and quick actions
- **Cloudinary Image Hosting** — Project images served via Cloudinary CDN
- **Maintenance Mode** — Toggle site-wide maintenance page while keeping admin accessible

---

## Project Structure

```
portfoliosite/          # Django project root
├── portfolioApp/
│   ├── models.py       # Skill, Project, ContactMessage
│   ├── views.py        # home view + contact view with rate limiting
│   ├── admin.py        # Custom LexiAdminSite with dashboard context
│   └── forms.py        # ContactForm
├── templates/
│   ├── base.html       # Base layout (navbar, footer, shared JS)
│   ├── home.html       # Main portfolio page
│   └── admin/
│       └── index.html  # Custom admin dashboard
├── static/
│   ├── css/
│   │   ├── styles.css
│   │   └── admin_custom.css
│   └── img/
├── settings.py
└── manage.py
```

---

## Models

**Skill** — `name`, `category` (language / framework / ml / tool), `icon_class`, `proficiency` (0–100), `order`

**Project** — `title`, `category` (web / ml / data / cv), `description`, `short_description`, `tech_stack` (comma-separated), `github_url`, `live_url`, `image` (Cloudinary), `featured`, `order`

**ContactMessage** — `name`, `email`, `subject`, `message`, `ip_address`, `is_read`

---

## Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL
- Redis
- A [Cloudinary](https://cloudinary.com) account

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/lexicooporation/lexitechsolutions.git
cd lexitechsolutions

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Fill in the values below in your .env file

# 5. Run migrations
python manage.py migrate

# 6. Collect static files
python manage.py collectstatic

# 7. Create a superuser
python manage.py createsuperuser

# 8. Start the development server
python manage.py runserver
```

---

## Environment Variables

Create a `.env` file in the project root with the following:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True

DATABASE_URL=postgres://user:password@localhost:5432/lexitech_db

CLOUDINARY_URL=cloudinary://api_key:api_secret@cloud_name
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret

REDIS_URL=redis://127.0.0.1:6379/1
```

> **Never commit your `.env` file.** Add it to `.gitignore`.

---

## Admin Panel

Access the custom admin dashboard at `/admin/`. It displays:

- Total projects, featured count, recent projects
- Unread and total contact messages
- Top skills by proficiency
- Quick-action shortcuts

The admin uses a red-accented Jazzmin theme branded as **LEXI.**.

---

## Deployment

This project is ready for deployment on platforms like **Render** or **Railway**.

- `DEBUG=False` in production
- `SECURE_SSL_REDIRECT`, `SECURE_HSTS_SECONDS`, and secure cookie settings are pre-configured in `settings.py`
- WhiteNoise handles static file serving
- Cloudinary handles all media uploads

---

## Contact

- **GitHub:** [github.com/lexicooporation](https://github.com/lexicooporation)
- **LinkedIn:** [nwankwo-ifeanyi](https://linkedin.com/in/nwankwo-ifeanyi-5014a8227)
- **Email:** lexicorporation22@gmail.com

---

© 2026 Lexitechsolutions. Built with Django & ❤️