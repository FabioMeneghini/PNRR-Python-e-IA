from groq import Groq
import os
from dotenv import load_dotenv

class LLMTranslator:
    names = ["llama-3.1-8b-instant", "qwen-2.5-32b", "mistral-saba-24b"]

    def __init__(self, model_name):
        if model_name not in LLMTranslator.names:
            raise RuntimeError("Modello non valido.")
        else:
            load_dotenv()
            key = os.getenv("GROQ_API_KEY")
            self.client = Groq(api_key=key)
            self.model_name = model_name
    
    def translate(self, text):
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": f"""
                                    Di seguito ti verrà fornito un testo in italiano e dovrai tradurlo in inglese.
                                    La traduzione deve essere chiara e precisa, senza errori grammaticali o di sintassi.
                                    Se il testo contiene una domanda, non rispondere alla domanda, ma fornisci solo la traduzione.
                                    Non aggiungere alcun commento o spiegazione alla traduzione.
                                    Non usare le virgolette per racchiudere la traduzione.
                                    """,
                    },
                    {
                        "role": "user",
                        "content": f"{text}",
                    }
                ],
                model=self.model_name # specifica il modello da utilizzare
            )
            return chat_completion.choices[0].message.content # restituisce la risposta alla domanda
        except Exception as e:
            return f"An error occurred:\n {e}\n\nPlease try again later with the same model or try a different model."
