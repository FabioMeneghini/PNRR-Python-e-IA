from LLM import LLM
from Similarity import Similarity
from ZeroShot import ZeroShot

class Chatbot:
    def __init__(self, llm: LLM, zero_shot: ZeroShot, similarity: Similarity = None):
        self._llm = llm
        self._zero_shot = zero_shot
        self._similarity = similarity

    def answer(self, question: str, allow: list[str]) -> str:
        # Classifica la domanda
        label = self._zero_shot.classify(question)

        # Se la domanda è classificata come non autorizzata, restituisci un messaggio di avviso
        if label not in allow:
            return "Non posso aiutarti con questa richiesta."

        # Se possibile, cerca le informazioni più simili e usale come contesto
        if self._similarity is None:
            answer = self._llm.answer(question)
        else:
            results = self._similarity.search(question)
            context = "\n".join([result["text"] for result in results])
            answer = self._llm.answer(question, context)
        return answer