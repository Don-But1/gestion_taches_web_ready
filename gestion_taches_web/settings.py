from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-fake-key-for-dev'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'taches',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gestion_taches_web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gestion_taches_web.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'


STATICSFILES_DIRS = [os.path.join(BASE_DIR, 'taches/static')]
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/accueil/'
# Configuration de l'envoi d'emails
# Pour le développement, les emails seront affichés dans la console.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Pour une configuration réelle avec un serveur SMTP (par exemple, Gmail)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'dondedieuirenge@gmail.com'
EMAIL_HOST_PASSWORD = '366529Don'

# -----------------------------------------------------------------------------
# Celery
# -----------------------------------------------------------------------------
# Celery nécessite un "broker" (un courtier) pour envoyer des messages entre les tâches.
# Redis est le choix le plus courant et le plus performant.
# Assurez-vous que Redis est installé et démarré sur votre machine.
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Celery Beat est le planificateur qui exécute les tâches à des intervalles réguliers.
CELERY_BEAT_SCHEDULE = {
    'check-and-send-notifications': {
        'task': 'taches.tasks.check_and_send_notifications',
        'schedule': 60.0,  # Exécuter cette tâche toutes les 60 secondes
        'args': (),
    },
    'archive-old-tasks': {
        'task': 'taches.tasks.archive_old_tasks',
        'schedule': 3600.0,  # Exécuter cette tâche toutes les heures
        'args': (),
    }
}

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
