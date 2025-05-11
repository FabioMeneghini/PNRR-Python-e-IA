from groq import Groq
import time
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=key)

model_name = "deepseek-r1-distill-llama-70b" # ad oggi, solo due modelli supportano il reasoning: deepseek-r1-distill-llama-70b e qwen-qwq-32b
question = "Qual è il risultato di (2+(7*3)-12)+16-9 ?"

completion = client.chat.completions.create(
    model=model_name,
    messages=[
        {
            "role": "user",
            "content": question
        }
    ],
    temperature=0.1, # temperatura: valore tra 0 e 2 che controlla la casualità e la creatività della risposta
    max_completion_tokens=2048, # numero massimo di token nella risposta
    stream=True, # ricevere i risultati come stream
    reasoning_format="raw" 
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="") # end="": al post di inserire un a capo dopo la stringa da stampare, non fa nulla
                                                        # utile per stampare a video il risultato in tempo reale dallo stream
    time.sleep(0.025)

# con stream=False...
"""
answer = completion.choices[0].message.content or "" # risposta alla domanda
print(answer) # stampa la risposta
"""