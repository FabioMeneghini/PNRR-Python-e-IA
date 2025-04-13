from txtai import Embeddings

data = [ # dataset di esempio (potrebbe essere prelevato da un CSV, JSON, database, ecc...)
    "Il gatto è sul tappeto",
    "Il cane gioca in giardino",
    "La pizza è deliziosa",
    "I gatti miagolano di notte",
    "Il sole splende nel cielo",
    "La luna brilla di notte",
    "Il mare è calmo"
]

# Carica gli embedding
# embeddings.load("path")

embeddings = Embeddings(path="nickprock/sentence-bert-base-italian-xxl-uncased", content=True) 

entries = [(i, text, None) for i, text in enumerate(data)]
embeddings.index(entries)
# i dati nell'indice ora possono essere ricercati tramite ricerca semantica (cosine similarity)

# Salva gli embedding (opzionale)
# embeddings.save("path")

target = "cosa posso mangiare per cena?" # frase da cercare
query = f"""select score, text from txtai
            where similar('{target}')
            and score > 0.15
            order by score desc
            limit 5"""
results = embeddings.search(query) # ricerca semantica
# la ricerca calcola il vettore di embedding della frase target e lo confronta
# con i vettori di embedding dei dati indicizzati

for result in results: # stampa i risultati
    print(f"SCORE: {result['score']:.4f}, TEXT: {result['text']}")
            


