from txtai.pipeline import Labels

zs = Labels("MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7")
candidate_labels = ["positivo", "negativo"]

results = zs("oggi è una bella giornata", candidate_labels)
# è un po' strano: zs viene utilizzato come se fosse una funzione,
# grazie a metodo speciale __call__ definito all'interno della classe Labels

# il risultato è una lista di coppie (indice_label, score), ordinate per score decrescente
# il punteggio è la probabilità che la frase appartenga a quella classe

label = candidate_labels[results[0][0]] # la label con punteggio più alto

print(label)