from groq import Groq
import os
from dotenv import load_dotenv

class LLM:
    names = ["llama-3.1-8b-instant", "qwen-2.5-32b", "mistral-saba-24b"]

    def __init__(self, model_name):
        if model_name not in LLM.names:
            raise RuntimeError("Modello non valido.")
        else:
            load_dotenv()
            key = os.getenv("GROQ_API_KEY")
            self.client = Groq(api_key=key)
            self.model_name = model_name
    

    def answer(self, question, context=""):
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": f"""Sei un assistente virtuale che risponde a domande in italiano.
                                    Di seguito di verrà fornita una domanda dall'utente e possibilmente la storia della chat
                                    tra l'utente e l'assistente virtuale.
                                    Rispondi in modo chiaro e conciso, senza ripetere la domanda e la storia della chat.
                                    Rispondi soltanto all'ultima domanda dell'utente.
                                    Questi sono i messaggi precedenti: {context}"""
                    },
                    {
                        "role": "user",
                        "content": f"{question}",
                    }
                ],
                model=self.model_name # specifica il modello da utilizzare
            )
            return chat_completion.choices[0].message.content # restituisce la risposta alla domanda
        except Exception as e:
            return f"Si è verificato un errore:\n {e}\n\nRiprova più tardi con lo stesso modello oppure riprova con un modello diverso."
