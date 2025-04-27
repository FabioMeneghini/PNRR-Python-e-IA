# Scrivere un programma che permette di chattare con un assistente virtuale.
# Il programma deve utilizzare un modello LLM (Large Language Model) per generare le risposte.

from llm_adapter import LLM

llm = LLM("llama-3.1-8b-instant") # inizializza il modello LLM

print("Benvenuto! Sono un assistente virtuale. Posso aiutarti con le tue domande.")
print("Scrivi 'exit' per uscire.\n")

while True:
    question = input("USER: ")
    if question.lower() == "exit":
        break # esci dal ciclo se l'utente digita 'exit'
    
    answer = llm.answer(question) # ottieni la risposta dal modello LLM
    print(f"\nCHATBOT: {answer}\n")

print("Grazie per aver utilizzato il nostro assistente virtuale! Arrivederci!")