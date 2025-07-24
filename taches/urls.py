from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('accueil/', views.home_view, name='home'),
    path('ajouter/', views.ajouter_tache, name='ajouter_tache'),
    path('logout/', views.logout_view, name='logout'),
    path('modifier/<int:tache_id>', views.modifier_tache, name='modifier_tache'),
    path('supprimer/<int:tache_id>', views.supprimer_tache, name='supprimer_tache')
]
