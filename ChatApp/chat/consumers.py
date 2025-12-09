import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    """
    Questa classe gestisce le connessioni WebSocket per la chat.
    Eredita da AsyncWebsocketConsumer per gestire le connessioni in modo asincrono.
    """
    async def connect(self):
        """
        Metodo chiamato quando un client tenta di connettersi al WebSocket.
        """
        self.roomGroupName = "group_chat_gfg"
        # Aggiunge il canale corrente al gruppo della chat
        await self.channel_layer.group_add(
            self.roomGroupName ,
            self.channel_name
        )
        # Accetta la connessione WebSocket
        await self.accept()

    async def disconnect(self , close_code):
        """
        Metodo chiamato quando la connessione WebSocket viene chiusa.
        """
        # Rimuove il canale corrente dal gruppo della chat
        await self.channel_layer.group_discard(
            self.roomGroupName , 
            self.channel_name 
        )

    async def receive(self, text_data):
        """
        Metodo chiamato quando il server riceve un messaggio dal WebSocket.
        """
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        
        # Invia il messaggio a tutto il gruppo della chat
        await self.channel_layer.group_send(
            self.roomGroupName,{
                "type" : "sendMessage" ,
                "message" : message , 
                "username" : username ,
            })

    async def sendMessage(self , event) : 
        """
        Metodo helper per inviare il messaggio al client WebSocket.
        Viene chiamato dal channel layer quando c'è un evento di tipo 'sendMessage'.
        """
        message = event["message"]
        username = event["username"]
        # Invia i dati in formato JSON al client
        await self.send(text_data = json.dumps({"message":message ,"username":username}))
      