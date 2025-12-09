from django.urls import path, include
from chat import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    # Rotta per la pagina principale della chat
    path("", chat_views.chatPage, name="chat-page"),

    # Sezione Login/Logout
    # Usa le viste integrate di Django per il login e logout
    path("auth/login/", LoginView.as_view(template_name="chat/loginPage.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
]
