from Chatbot import Chatbot, LLM, ZeroShot, Similarity

llm = LLM("llama-3.1-8b-instant")
zero_shot = ZeroShot("MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7", "pericoloso", "sicuro")
similarity = Similarity("MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7")

knowledge = []
with open("./03-chatbot/knowledge.txt", "r", encoding="utf-8") as file:
    knowledge = [line.strip() for line in file]

similarity.index(knowledge) # indicizza le informazioni
similarity.save("knowledge_index") # salva l'indice delle informazioni

chatbot = Chatbot(llm, zero_shot, similarity)

print("Benvenuto! Sono l'assistente virtuale della libreria. Come posso aiutarti?")
print("(scrivi 'exit' per uscire)\n")

while True:
    question = input("USER: ")
    if question.lower() == "exit":
        break # esci dal ciclo se l'utente digita 'exit'
    
    answer = chatbot.answer(question, ["sicuro"]) # ottieni la risposta dal modello LLM
    print(f"\nCHATBOT: {answer}\n")

print("Grazie per aver utilizzato il nostro assistente virtuale! Arrivederci!")