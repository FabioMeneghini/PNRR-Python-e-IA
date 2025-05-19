from LLM import LLM

class LLMLibrary(LLM):
    def __init__(self, model_name):
        super().__init__(model_name)
    

    def answer(self, question, context="NON DISPONIBILE"):
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": f"""Sei un assistente virtuale che risponde a domande in italiano relative ad una libreria.
                                    Parla come se fossi il proprietario della libreria e rispondi in modo amichevole e professionale.
                                    Di seguito ti verrà fornita una domanda dall'utente e un contesto su cui ti dovrai basare.
                                    Il contesto conterrà informazioni su alcuni libri, autori, generi e altri dettagli pertinenti.
                                    Rispondi in modo chiaro e conciso, senza ripetere la domanda e il contesto.
                                    Se la domanda dell'utente fa riferimento a un libro non presente nel contesto, dì che non hai informazioni a riguardo.
                                    Non includere informazioni non pertinenti con il contesto o non richieste.
                                    Nella risposta non menzionare il contesto, ma utilizza le informazioni in esso contenute.
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
