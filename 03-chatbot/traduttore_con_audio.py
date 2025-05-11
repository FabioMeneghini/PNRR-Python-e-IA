from LLMTranslator import LLMTranslator
from TextToSpeech import TextToSpeech

llm = LLMTranslator("llama-3.1-8b-instant")
tts = TextToSpeech("Fritz")

print("Benvenuto! Sono un assistente virtuale che traduce frasi da italiano a inglese.")
print("(scrivi 'exit' per uscire)\n")

while True:
    text = input("USER: ")
    if text.lower() == "exit":
        break # esci dal ciclo se l'utente digita 'exit'
    
    answer = llm.translate(text) # ottieni la risposta dal modello LLM
    tts.speech(answer, "traduttore.wav") # genera l'audio della risposta
    print(f"\nCHATBOT: {answer}\n")

print("Grazie per aver utilizzato il nostro traduttore! Arrivederci!")