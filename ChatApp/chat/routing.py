from django.urls import path , include
from chat.consumers import ChatConsumer

# Definisce le rotte WebSocket per l'applicazione chat.
# Simile a urls.py ma per le connessioni WebSocket.
websocket_urlpatterns = [
    # Mappa l'URL radice ("") al consumer ChatConsumer
    path("" , ChatConsumer.as_asgi()) , 
]
