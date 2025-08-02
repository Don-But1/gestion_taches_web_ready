from django import forms
from django.contrib.auth.models import User
from .models import UserProfile # Importez le modèle UserProfile
from .models import Tache

class FormulaireInscription(forms.Form):
    # Les champs que vous voulez afficher sur la page
    username = forms.CharField(label="Nom d'utilisateur")
    email = forms.EmailField(label="Adresse e-mail")
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmer le mot de passe")
    
    # Le champ pour la photo de profil
    photo = forms.ImageField(required=False, label="Photo de profil")

    class Meta:
        model = User
        fields = ['username', 'email']

def clean(self):
        # ... (Votre logique de validation des mots de passe reste la même)
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")
        return cleaned_data

class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ['titre', 'description', 'statut', 'date_debut', 'date_fin']

