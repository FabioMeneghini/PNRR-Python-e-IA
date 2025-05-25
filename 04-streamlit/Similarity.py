from txtai import Embeddings

class Similarity:
    def __init__(self, model: str = "nickprock/sentence-bert-base-italian-xxl-uncased"):
        self._embeddings = Embeddings(path=model, content=True)

    def load(self, path: str):
        self._embeddings.load(path)

    def save(self, path: str):
        self._embeddings.save(path)

    def index(self, data: list):
        entries = [(i, text, None) for i, text in enumerate(data)]
        self._embeddings.index(entries)

    def search(self, target: str, threshold = 0.15, limit: int = 5):
        query = f"""SELECT score, text FROM txtai
                    WHERE similar('{target}')
                    AND score > {threshold}
                    ORDER BY score DESC
                    LIMIT {limit}"""
        results = self._embeddings.search(query)
        return results


if __name__ == "__main__":
    # Esempio di utilizzo
    data = [
        "Il gatto è sul tappeto",
        "Il cane gioca in giardino",
        "La pizza è deliziosa",
        "I gatti miagolano di notte",
        "Il sole splende nel cielo",
        "La luna brilla di notte",
        "Il mare è calmo"
    ]

    similarity = Similarity()
    similarity.index(data)

    target = "cosa posso mangiare per cena?"
    results = similarity.search(target)

    for result in results:
        print(f"SCORE: {result['score']:.4f} | TEXT: {result['text']}")