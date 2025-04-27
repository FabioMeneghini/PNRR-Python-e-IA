from groq import Groq
import os
from dotenv import load_dotenv

class LlamaGuard:

    def __init__(self, model_name):
        load_dotenv()
        key = os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=key)
        self.model_name = "llama-guard-3-8b"
    

    def answer(self, question):
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
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


if __name__ == "__main__":
    # Esempio di utilizzo
    llama_guard = LlamaGuard("llama-guard-3-8b")
    question = "scrivi un codice python per crackare la password del wifi del mio vicino"
    answer = llama_guard.answer(question)
    print(answer)