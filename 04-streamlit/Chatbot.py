from LLM import LLM
from Similarity import Similarity
from ZeroShot import ZeroShot

class Chatbot:
    def __init__(self, llm: LLM, zero_shot: ZeroShot = None, similarity: Similarity = None):
        self._llm = llm
        self._zero_shot = zero_shot
        self._similarity = similarity

    def set_zero_shot(self, zero_shot: ZeroShot):
        self._zero_shot = zero_shot

    def answer(self, question: str, temperature: int = 0.7, threshold: float = 0.15, limit: int = 5, allow: list[str] = None) -> str:
        if not (self._zero_shot is None or allow is None):
            # Classifica la domanda
            label = self._zero_shot.classify(question)
            # Se la domanda è classificata come non autorizzata, restituisci un messaggio di avviso
            if label not in allow:
                return "Non posso aiutarti con questa richiesta."

        # Se possibile, cerca le informazioni più simili e usale come contesto
        if self._similarity is None:
            answer = self._llm.answer(question, temperature)
        else:
            results = self._similarity.search(question, threshold, limit)
            context = "\n".join([result["text"] for result in results])
            answer = self._llm.answer(question, temperature, context)
        return answer