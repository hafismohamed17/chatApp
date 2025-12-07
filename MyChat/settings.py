from pathlib import Path
import os

# -----------------------
# BASE DIRECTORY
# -----------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------
# SECURITY SETTINGS
# -----------------------
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-default-secret-key')
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

# Hosts your app can serve
ALLOWED_HOSTS = ['chatapp-l0mb.onrender.com', 'localhost', '127.0.0.1']

# CSRF trusted origins (no trailing slashes!)
CSRF_TRUSTED_ORIGINS = [
    "https://chatapp-l0mb.onrender.com",
    "http://chatapp-l0mb.onrender.com",  # optional if HTTP is used
]

# -----------------------
# APPLICATIONS
# -----------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Channels & Chat app
    'channels',
    'freeChat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MyChat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Add templates folder if you have one
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # required for auth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# -----------------------
# WSGI / ASGI
# -----------------------
WSGI_APPLICATION = 'MyChat.wsgi.application'
ASGI_APPLICATION = 'MyChat.asgi.application'

# -----------------------
# DATABASE
# -----------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # simple for Render free tier
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -----------------------
# CHANNEL LAYERS
# -----------------------
# For single-worker setups, InMemoryChannelLayer works. For multiple workers, use Redis.
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}

# -----------------------
# PASSWORD VALIDATION
# -----------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# -----------------------
# INTERNATIONALIZATION
# -----------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -----------------------
# STATIC FILES
# -----------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # for deployment

# -----------------------
# DEFAULT AUTO FIELD
# -----------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
