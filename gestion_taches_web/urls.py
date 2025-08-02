from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.shortcuts import redirect
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', lambda request: redirect('login')),
    path('', include('taches.urls')),
]

# Ces lignes sont cruciales pour servir les fichiers médias en mode développement.
# Elles doivent être placées en dehors de la liste urlpatterns.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




    
   