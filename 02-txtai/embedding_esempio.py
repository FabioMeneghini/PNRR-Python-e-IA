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

# specifica il percorso del modello: si trovano su Hugging Face
# content = True significa che i dati che gli passeremo saranno testuali
embeddings = Embeddings(path="nickprock/sentence-bert-base-italian-xxl-uncased", content=True)

# CARICA gli embedding dal percorso specificato, **se salvati in precedenza**
#embeddings.load("./embeddings")

# CREA GLI EMBEDDING E LI SALVA IN UN INDICE
entries = [(i, text, None) for i, text in enumerate(data)] # crea una lista di tuple (id, testo, None) per ogni elemento del dataset
# il None è un placeholder per metadati aggiuntivi, che non ci interessano in questo caso
embeddings.index(entries) # indicizza i dati (crea gli embedding e li salva in un indice)

# i dati nell'indice ora possono essere ricercati tramite ricerca semantica (cosine similarity)

# SALVA gli embedding in una cartella al percorso specificato (opzionale)
embeddings.save("./embeddings")

target = "cosa posso mangiare per cena?" # frase da cercare
# results = embeddings.search(target, 5) # ricerca semantica
query = f"""SELECT score, text FROM txtai
            WHERE similar('{target}')
            AND score > 0.15
            ORDER BY score desc
            LIMIT 5""" # query SQL-like per cercare i dati indicizzati
results = embeddings.search(query) # ricerca semantica

# la ricerca calcola il vettore di embedding della frase target e lo confronta
# con i vettori di embedding dei dati indicizzati tramite cosine similarity

for result in results: # stampa i risultati
    print(f"SCORE: {result['score']:.4f} | TEXT: {result['text']}")