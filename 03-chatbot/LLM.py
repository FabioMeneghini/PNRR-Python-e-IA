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
    

    def answer(self, question, context="NON DISPONIBILE"):
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": f"""Sei un assistente virtuale che risponde a domande in italiano.
                                    Di seguito ti verrà fornita una domanda dall'utente e possibilmente un contesto
                                    su cui ti dovrai basare.
                                    Rispondi in modo chiaro e conciso, senza ripetere la domanda e il contesto.
                                    Se un contesto è fornito, la risposta deve essere basata UNICAMENTE su di esso.
                                    Nella risposta non menzionare il contesto, ma utilizza le informazioni in esso contenute.
                                    Se non hai informazioni sufficienti per rispondere, dì che non hai informazioni a riguardo.
                                    Questo è il contesto:\n{context}""",
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
