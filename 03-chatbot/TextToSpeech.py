from groq import Groq
import os
from dotenv import load_dotenv

class TextToSpeech:
    voices = ["Arista", "Atlas", "Basil", "Briggs", "Calum", "Celeste", "Cheyenne",
              "Chip", "Cillian", "Deedee", "Fritz", "Gail", "Indigo", "Mamaw",
              "Mason", "Mikail", "Mitch", "Quinn", "Thunder"]

    def __init__(self, voice="Fritz"):
        if voice not in TextToSpeech.voices:
            raise RuntimeError("Voce non valida.")
        else:
            load_dotenv()
            key = os.getenv("GROQ_API_KEY")
            self.client = Groq(api_key=key)
            self.voice = voice

    def speech(self, text, path="speech.wav"):
        try:
            response = self.client.audio.speech.create(
                model="playai-tts",
                voice=f"{self.voice}-PlayAI",
                input=text,
                response_format="wav"
            )
            response.write_to_file(path)
            return text
        except Exception as e:
            return f"Errore durante la sintesi vocale: \n{e}"
