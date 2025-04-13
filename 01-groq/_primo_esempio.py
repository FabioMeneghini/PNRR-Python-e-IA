from groq import Groq # importazione libreria API Groq

import os # importazione libreria per la gestione delle variabili d'ambiente
from dotenv import load_dotenv

load_dotenv() # carica le variabili d'ambiente dal file .env
key = os.getenv("GROQ_API_KEY") # recupera la chiave API da una variabile d'ambiente

model_name = "llama-3.1-8b-instant" # nome del modello LLM da utilizzare
# (i nomi disponibili sono elencati nella documentazione di Groq: https://console.groq.com/docs/models)

question = "Ciao come stai?" # domanda dell'utente
answer = "" # inizializza la variabile per la risposta

try:
    client = Groq(api_key=key) # si collega al servizio Groq usando la chiave API

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system", # messaggio di sistema: dobbiamo dire al LLM come comportarsi e che tipi di messaggi aspettarsi
                "content": """Sei un assistente virtuale che risponde a domande in italiano."""
            },
            {
                "role": "user", # messaggio dell'utente
                "content": f"{question}",
            }
        ],
        model = model_name # specifica il modello da utilizzare
    )
    answer = chat_completion.choices[0].message.content # risposta alla domanda
except Exception as e:
    answer = f"Si è verificato un errore: \n {e}" # gestione degli errori
finally:
    print(answer)

