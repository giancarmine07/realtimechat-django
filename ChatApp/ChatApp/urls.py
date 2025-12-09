from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Rotta per l'interfaccia di amministrazione di Django
    path('admin/', admin.site.urls),
    # Include le URL definite nell'applicazione 'chat'
    path("", include("chat.urls")),
]
