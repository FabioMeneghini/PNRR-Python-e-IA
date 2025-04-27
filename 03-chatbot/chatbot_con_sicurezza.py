from Chatbot import Chatbot, LLM, ZeroShot

llm = LLM("llama-3.1-8b-instant")
zero_shot = ZeroShot("MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7", "pericoloso", "sicuro")
chatbot = Chatbot(llm, zero_shot)

print("Benvenuto! Sono un assistente virtuale che risponde solo a domande sicure.")
print("(scrivi 'exit' per uscire)\n")

while True:
    question = input("USER: ")
    if question.lower() == "exit":
        break # esci dal ciclo se l'utente digita 'exit'
    
    answer = chatbot.answer(question, ["sicuro"]) # ottieni la risposta dal modello LLM
    print(f"\nCHATBOT: {answer}\n")

print("Grazie per aver utilizzato il nostro assistente virtuale! Arrivederci!")
