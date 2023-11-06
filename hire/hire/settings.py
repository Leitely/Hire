import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-9s(u2!gjvtqoap9yrr2g2m@88v=301%hih$bhc%6+=6+(hi!sh"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# ALL AUTH CONFIGURATION
SITE_ID = 1
AUTHENTICATION_BACKENDS = [
    # DJANGO LOGIN
    'django.contrib.auth.backends.ModelBackend',

    # ALL AUTH LOGIN
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",

    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.github",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.instagram",

    "system.home.apps.HomeConfig",

    'crispy_forms',
    'crispy_tailwind',
    'tailwind',
    'theme',
    'django_browser_reload'
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "hire.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request"
            ],
        },
    },
]

SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'APP': {
            'client_id': '5d598c20517447a3e6d5',
            'secret': 'bba6c863ecc53202362393e678559a6a36bc9202',
            'key': '',
        }
    },
    'google': {
        'APP': {
            'client_id': '25765846986-ov5on17qop8vciaicrt6vgmfpqslli9o.apps.googleusercontent.com',
            'secret': '25765846986-ov5on17qop8vciaicrt6vgmfpqslli9o.apps.googleusercontent.com'
        }
    },
}


WSGI_APPLICATION = "hire.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/images/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# path to user uploaded images.
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
# path to upload images in production.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

TAILWIND_APP_NAME = 'theme'
TAILWIND_ALLOWED_TEMPLATE_PACKS = 'tailwind'
CRISPY_TEMPLATE_PACK = 'tailwind'

INTERNAL_IPS = [
    "127.0.0.1",
]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'login'

NPM_BIN_PATH = os.getenv("NPM_BIN_PATH", None)

if NPM_BIN_PATH:
    NPM_RUN = os.path.join(NPM_BIN_PATH, "npm")
