from txtai.pipeline import Labels

class ZeroShot:
    def __init__(self, model: str = "MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7", *labels):
        self._zs = Labels(model)  # Inizializza il modello di zero-shot classification
        self._labels = list(labels)  # Salva le etichette fornite

    def classify(self, text: str) -> str:
        results = self._zs(text, self._labels)  # Esegui la classificazione
        label = self._labels[results[0][0]]  # Ottieni l'etichetta con il punteggio più alto
        return label  # Restituisci l'etichetta classificata




if __name__ == "__main__":
    # Esempio di utilizzo
    zero_shot = ZeroShot("MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7", "pericoloso", "sicuro")
    text = "i gatti sono i miei animali preferiti"
    label = zero_shot.classify(text)
    print(label)  # Stampa l'etichetta classificata