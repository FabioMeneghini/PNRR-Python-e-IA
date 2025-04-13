from llm_adapter import LLM

llm = LLM("llama-3.1-8b-instant") # inizializza il modello LLM

counter = 1 # inizializza il contatore delle domande
chat_history = [] # inizializza la storia della chat
context = "" # inizializza il contesto vuoto
context_length = 5 # inizializza la lunghezza del contesto a 5 domande e relative 5 risposte

print("Benvenuto! Sono un assistente virtuale. Posso aiutarti con le tue domande.")
print("Scrivi 'exit' per uscire.\n")

while True:
    question = input("USER: ")
    if question.lower() == "exit":
        break # esci dal ciclo se l'utente digita 'exit'

    context = "".join(chat_history[-2*context_length:]) # prendi le ultime 10 domande e risposte come contesto
    
    answer = llm.answer(question, context) # ottieni la risposta dal modello LLM
    chat_history.append(f"DOMANDA {counter}: {question}\n") # aggiungi la domanda alla storia della chat
    chat_history.append(f"RISPOSTA {counter}: {answer}\n") # aggiungi la risposta alla storia della chat
    counter += 1
    print(f"\nCHATBOT: {answer}\n")

print("Grazie per aver utilizzato il nostro assistente virtuale! Arrivederci!")