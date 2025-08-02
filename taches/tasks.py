# Fichier : taches/tasks.py
from celery import shared_task
from datetime import datetime, timedelta
from .notificator import send_task_notification
from .models import Tache

@shared_task
def check_and_send_notifications():
    """
    Vérifie les tâches et envoie les notifications si l'heure est venue.
    Cette tâche sera exécutée régulièrement par Celery Beat.
    """
    now = datetime.now()
    
    # Récupérer les tâches qui commencent dans 2 minutes
    tasks_to_start_soon = Tache.objects.filter(
        date_debut__range=[now + timedelta(minutes=1, seconds=59), now + timedelta(minutes=2, seconds=1)]
    )
    for tache in tasks_to_start_soon:
        send_task_notification(tache.titre, tache.utilisateur.email, "avant")
        
    # Récupérer les tâches qui ont commencé il y a 2 minutes
    tasks_started = Tache.objects.filter(
        date_debut__range=[now - timedelta(minutes=2, seconds=1), now - timedelta(minutes=1, seconds=59)]
    )
    for tache in tasks_started:
        send_task_notification(tache.titre, tache.utilisateur.email, "apres")

