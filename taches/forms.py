from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Tache

class FormulaireInscription(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None  # Supprime les textes "Requis. 150 caractères..." etc.
            class Meta:
                model = User
                fields = ['username', 'password1', 'password2']
                labels = {
                    'username': 'Nom d’utilisateur',
                    'password1': 'Mot de passe',
                    'password2': 'Confirmer le mot de passe',
                    }

class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ['titre', 'description', 'statut']
