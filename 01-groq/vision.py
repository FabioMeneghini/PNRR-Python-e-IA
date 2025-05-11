from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("GROQ_API_KEY")

# solo due modelli supportano le immagini: "llama-4-scout-17b-16e-instruct" e "meta-llama/llama-4-maverick-17b-128e-instruct"
model_name = "meta-llama/llama-4-scout-17b-16e-instruct"

question = "Descrivi questa immagine" # domanda dell'utente
img_url = "https://neewa.it/img/leoblog/b/1/13/lg-b-neewa-cover-cani-sport-accessori-pettorine-imbraghi-cani-sportivi-blog-cane-di-razza.jpg" # URL dell'immagine da inviare al LLM

client = Groq(api_key=key)

completion = client.chat.completions.create(
    model=model_name,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": question
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": img_url
                    }
                }
            ]
        },
#        { # multi-turn conversation
#            "role": "user",
#            "content": "Dimmi di più su questa razza di cane"
#        }
    ],
    temperature=0.6,
    max_completion_tokens=2048,
    stream=False
)

answer = completion.choices[0].message.content
print(answer)