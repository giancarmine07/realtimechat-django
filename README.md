# Realtime Chat con Django Channels

Un'applicazione di chat in tempo reale semplice e performante, costruita con Django e WebSockets (Django Channels).

## Funzionalità
*   **Autenticazione Utente:** Login e Logout gestiti da Django.
*   **Chat Realtime:** Scambio messaggi istantaneo tramite WebSocket.
*   **Offline Support:** I messaggi vengono salvati localmente e inviati automaticamente al ritorno della connessione.

## Requisiti
*   Python 3.9+
*   Redis (opzionale in sviluppo, raccomandato in produzione)

## Installazione e Avvio

1.  **Clona il repository:**
    ```bash
    git clone <URL_DEL_TUO_REPO>
    cd realtimechat-django
    ```

2.  **Crea e attiva il virtual environment:**
    ```bash
    python3 -m venv my_env
    source my_env/bin/activate  # Su Windows: my_env\Scripts\activate
    ```

3.  **Installa le dipendenze:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Applica le migrazioni:**
    ```bash
    python ChatApp/manage.py migrate
    ```

5.  **Avvia il server:**
    ```bash
    python ChatApp/manage.py runserver
    ```

Visita `http://127.0.0.1:8000/` per iniziare a chattare!
