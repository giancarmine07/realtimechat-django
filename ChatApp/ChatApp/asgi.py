import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChatApp.settings')

# Inizializza l'applicazione ASGI di Django in anticipo per assicurarsi che l'AppRegistry
# sia popolato prima di importare codice che potrebbe importare modelli ORM.
django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter , URLRouter

# Configurazione principale dell'applicazione ASGI
# ProtocolTypeRouter instrada le richieste in base al tipo di protocollo (http o websocket)
application = ProtocolTypeRouter(
    {
        "http" : django_asgi_app , 
    }
)

from chat import routing

# Aggiunge il routing per i WebSocket
# AuthMiddlewareStack gestisce l'autenticazione per i WebSocket (es. accesso a request.user)
application.application_mapping["websocket"] = AuthMiddlewareStack(
    URLRouter(
        routing.websocket_urlpatterns
    )
)
