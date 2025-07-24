from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import FormulaireInscription
from django.contrib.auth.decorators import login_required
from .forms import TacheForm
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
        form = FormulaireInscription(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = FormulaireInscription()
    return render(request, 'register.html', {'form': form})

def home_view(request):
    taches = Tache.objects.filter(utilisateur=request.user)
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
        tache.delete()
        return redirect('home')
    return render(request, 'supprimer_tache.html', {'tache': tache})

