from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=key)

speech_file_path = "speech.wav" 
model = "playai-tts"
voice = "Fritz-PlayAI"
text = "These are short, famous texts in English from classic sources like the Bible or Shakespeare. Some texts have word definitions and explanations to help you. Some of these texts are written in an old style of English. Try to understand them, because the English that we speak today is based on what our great, great, great, great grandparents spoke before! Of course, not all these texts were originally written in English. The Bible, for example, is a translation. But they are all well known in English today, and many of them express beautiful thoughts. "
response_format = "wav"


response = client.audio.speech.create(
    model=model,
    voice=voice,
    input=text,
    response_format=response_format
)

response.write_to_file(speech_file_path)