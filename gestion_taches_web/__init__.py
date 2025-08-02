# fichier: gestion_taches_web_ready/__init__.py

# Ce code assure que l'application Celery est toujours importée
# au démarrage de Django, pour que les tâches soient reconnues.
from .celery import app as celery_app

