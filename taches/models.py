from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Tache(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('terminee', 'Terminée'),
    ]
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_debut = models.DateTimeField(default=timezone.now)
    date_fin = models.DateTimeField(default=timezone.now) 
    est_terminee = models.BooleanField(default=False)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    is_archived = models.BooleanField(default=False)

def __str__(self):
    return f"{self.titre}({self.get_statut_display()})"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profils_pics', blank=True, null=True)
def __str__(self):
    return f'{self.user.username} Profile'