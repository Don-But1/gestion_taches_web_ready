from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import TacheForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .models import Tache

from django.shortcuts import render, redirect, get_object_or_404

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = "Nom d'utilisateur ou mot de passe incorrect!!!"
            return render(request, 'login.html', {'error': error})
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        
        form = FormulaireInscription(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            photo = form.cleaned_data.get('photo')

            user = User.objects.create_user(username=username, email=email, password=password)
            UserProfile.objects.create(user=user, photo=photo)

            return redirect('login')
    else:
        form = FormulaireInscription()
    
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def home_view(request):
    taches = Tache.objects.filter(utilisateur=request.user , is_archived=False)
    return render(request, 'home.html',{'taches': taches})

def logout_view(request):
    logout(request)
    return redirect('login')

def ajouter_tache(request):
    if request.method == 'POST':
        form = TacheForm(request.POST)
        if form.is_valid():
            tache = form.save(commit=False)
            tache.utilisateur = request.user
            tache.save()
            return redirect('home')
    else:
        form = TacheForm()
    return render(request, 'ajouter_tache.html', {'form': form})

# Modifier une tâche
@login_required
def modifier_tache(request, tache_id):
    tache = get_object_or_404(Tache, id=tache_id, utilisateur=request.user)
    if request.method == 'POST':
        form = TacheForm(request.POST, instance=tache)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TacheForm(instance=tache)
    return render(request, 'modifier_tache.html', {'form': form})

# Supprimer une tâche
@login_required
def supprimer_tache(request, tache_id):
    tache = get_object_or_404(Tache, id=tache_id, utilisateur=request.user)
    if request.method == 'POST':
        tache.is_archived = True
        tache.save()
        return redirect('home')
    return render(request, 'supprimer_tache.html', {'tache': tache})

@login_required
def liste_taches_archivees(request):
    """
    Affiche toutes les tâches archivées de l'utilisateur connecté.
    """
    # Filtrez les tâches par l'utilisateur et par l'état archivé
    taches_archivees = Tache.objects.filter(utilisateur=request.user, is_archived=True).order_by('-date_fin')
    
    # Renvoyez-les au template
    return render(request, 'taches/liste_taches_archivees.html', {'taches_archivees': taches_archivees})
    
@login_required
def supprimer_tache_definitivement(request, id):
    tache = get_object_or_404(Tache, id=id, utilisateur=request.user)
    tache.delete()
    return redirect('archives')