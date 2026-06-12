from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG','False')=='True'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "portfolioApp",
    "cloudinary_storage",
    "cloudinary", 
    "maintenance_mode",

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "maintenance_mode.middleware.MaintenanceModeMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "portfoliosite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / os.path.join("templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "portfoliosite.wsgi.application"


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600,
    )
}

# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / os.path.join("static"),]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import cloudinary

cloudinary.config(
    cloudinary_url=os.getenv('CLOUDINARY_URL')
)

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
    'API_KEY':    os.getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET'),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'




MAINTENANCE_MODE = False
MAINTENANCE_MODE_IGNORE_ADMIN_SITE = True   
MAINTENANCE_MODE_IGNORE_SUPERUSER = True   
MAINTENANCE_MODE_TEMPLATE = '503.html'   



CACHES = {
    "default": {
        "BACKEND":  "django_redis.cache.RedisCache",
        "LOCATION": os.getenv("REDIS_URL", "redis://127.0.0.1:6379/1"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}


default_theme_mode='light'

# ══════════════════════════════════════════════════════════════
#  JAZZMIN SETTINGS — lexitechsolutions admin panel
# ══════════════════════════════════════════════════════════════

JAZZMIN_SETTINGS = {
    "site_title": "Lexitech Admin",
    "site_header": "LEXI.",
    "site_brand": "Lexitech Solutions",
    "site_logo": "img/browser-icon.png",
    "login_logo": "img/login-icon.png",
    "site_logo_classes": "img-circle",
    "site_icon": "img/browser.png",
    "welcome_sign": "Welcome Bruh, 😤.",
    "copyright": "lexitechsolutions © 2026",
    "search_model": ["portfolioApp.ContactMessage"],
    "topmenu_links": [
        {"name": "Dashboard", "url": "admin:index"},
        {"name": "View Site", "url": "/", "new_window": True},
        {"name": "Messages", "url": "/admin/portfolioApp/contactmessage/"},
        {"app": "portfolioApp"},
    ],
    "usermenu_links": [
        {"name": "View Site", "url": "/", "new_window": True, "icon": "fas fa-globe"},
    ],
    "hide_apps": ["auth"],
    "order_with_respect_to": ["portfolioApp"],
    "icons": {
        "portfolioApp.project": "fas fa-folder-open",
        "portfolioApp.skill": "fas fa-code",
        "portfolioApp.contactmessage": "fas fa-envelope",
    },
    "related_modal_active": True,
    "custom_css": "css/admin_custom.css",
    "changeform_format": "horizontal_tabs",
}


# ── Jazzmin UI tweaks (colours, fonts, skin) ─────────────────
JAZZMIN_UI_TWEAKS = {
    "brand_colour": "navbar-danger",
    "accent": "accent-danger",
    "navbar": "navbar-dark navbar-danger",
    "no_navbar_border": True,
    "navbar_fixed": True,
    "sidebar": "sidebar-light-danger",
    "sidebar_disable_expand": True,
    "sidebar_nav_child_indent": True,
    "theme": "simplex"
}




# ── Security ──────────────────────────────────────────────────
SECURE_SSL_REDIRECT          = False  # redirect HTTP to HTTPS in production
SECURE_HSTS_SECONDS          = 31536000   # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD          = True
SESSION_COOKIE_SECURE        = not DEBUG  # HTTPS-only session cookie
CSRF_COOKIE_SECURE           = not DEBUG  # HTTPS-only CSRF cookie
SECURE_BROWSER_XSS_FILTER    = True
SECURE_CONTENT_TYPE_NOSNIFF  = True
X_FRAME_OPTIONS              = 'DENY'