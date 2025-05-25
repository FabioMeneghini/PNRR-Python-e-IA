from LLM import LLM

class LLMTranslator(LLM):
    def __init__(self, model_name):
        super().__init__(model_name)
    
    # override il metodo answer per la traduzione
    def answer(self, text, language="inglese"):
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": f"""
                                    Di seguito ti verrà fornito un testo in italiano e dovrai tradurlo in {language}.
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
            return f"An error occurred:\n{e}\n\nPlease try again later with the same model or try a different model."
