from django.db import models
from django.contrib.auth.models import User

class Tache(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('terminee', 'Terminée'),
    ]
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')

def __str__(self):
    return f"{self.titre}({self.get_statut_display()})"