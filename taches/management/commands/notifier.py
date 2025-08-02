# Fichier taches/notifier.py

from django.core.mail import send_mail
from django.conf import settings

def send_task_notification(task_name, user_email, notification_type):
    # Logique pour définir le sujet et le message
    if notification_type == "avant":
        subject = f"Rappel : Votre tâche '{task_name}' commence dans 2 minutes."
        message = f"Bonjour, la tâche '{task_name}' va commencer dans 2 minutes."
    elif notification_type == "apres":
        subject = f"Notification : Votre tâche '{task_name}' est terminée."
        message = f"Bonjour, la tâche '{task_name}' a commencé il y a 2 minutes."
    else:
        # Gérer le cas où le type de notification est inconnu
        print(f"Type de notification inconnu : {notification_type}")
        return # Ne rien faire et quitter la fonction

    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]

    try:
        # Ajout de fail_silently=False pour que l'erreur remonte
        send_mail(
            subject,
            message,
            email_from,
            recipient_list,
            fail_silently=False  # C'est la ligne la plus importante à ajouter
        )
        print(f"Notification envoyée à {user_email} pour la tâche '{task_name}'.")
    except Exception as e:
        print(f"Erreur lors de l'envoi de la notification: {e}")

