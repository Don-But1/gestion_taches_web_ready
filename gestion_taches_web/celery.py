# fichier: gestion_taches_web_ready/celery.py

import os
from celery import Celery

# Définir la variable d'environnement pour Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_taches_web_ready.settings')

# Créer l'application Celery
app = Celery('gestion_taches_web_ready')

# Charger les configurations à partir de Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Découvrir et charger automatiquement les tâches dans les applications
app.autodiscover_tasks()

