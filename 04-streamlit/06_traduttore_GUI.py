# Modifiche apportate ai file precedentemente scritti:
# - LLMTranslator: aggiunto al metodo `answer` il parametro `language` per specificare la lingua di traduzione
# - TextToSpeech: aggiunto il metodo `set_voice` per cambiare la voce di sintesi vocale

import streamlit as st
from LLMTranslator import LLMTranslator
from TextToSpeech import TextToSpeech
import time

def response_generator(response):
    for chunk in response.split():
        yield chunk+" "
        time.sleep(0.04)

st.set_page_config(page_title="Traduttore", page_icon="🌐")

# INIZIALIZZAZIONE -----------------------------------------
with st.spinner("Inizializzazione modelli..."):
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "model_name" not in st.session_state:
        st.session_state.model_name = "llama-3.1-8b-instant"
    
    if "llm" not in st.session_state:
        st.session_state.llm = LLMTranslator("llama-3.1-8b-instant")
    
    if "tts" not in st.session_state:
        st.session_state.tts = TextToSpeech("Fritz")
    
    if "last_translation" not in st.session_state:
        st.session_state.last_translation = ""
    
    if "voice" not in st.session_state:
        st.session_state.voice = "Fritz"
# ----------------------------------------------------------

st.title("Traduttore")

# SIDEBAR --------------------------------------------------
st.sidebar.title("Impostazioni")

# Selezione del modello LLM da utilizzare
model_name = st.sidebar.selectbox(
    "Seleziona il modello LLM da utilizzare",
    options=st.session_state.llm.names,
    index=st.session_state.llm.names.index(st.session_state.model_name)
)
# Se l'utente ha cambiato il modello LLM, aggiorna il chatbot
if model_name != st.session_state.model_name:
    st.session_state.model_name = model_name
    st.session_state.llm.set_model_name(model_name)

# Selezione della lingua di traduzione
language = st.sidebar.selectbox(
    "Seleziona la lingua di traduzione",
    options=["inglese", "francese", "spagnolo", "tedesco"],
    index=0
)

# Se l'utente ha impostato l'inglese, allora può impostare la voce e generare l'audio
voice = st.sidebar.selectbox(
    "Seleziona la voce per l'audio",
    options=st.session_state.tts.voices,
    index=st.session_state.tts.voices.index(st.session_state.voice),
    disabled=language != "inglese",
    help="Seleziona la voce da utilizzare per la sintesi vocale (disponibile solo per l'inglese)."
)
# Se l'utente ha cambiato la voce, aggiorna il TextToSpeech
if voice != st.session_state.voice:
    st.session_state.tts.set_voice(voice)

generate_audio = st.sidebar.button("Genera audio",
                                   help="Genera l'audio dell'ultima traduzione effettuata (disponibile solo per l'inglese).",
                                   disabled=language != "inglese")
if generate_audio:
    if st.session_state.last_translation != "":
        st.session_state.tts.speech(st.session_state.last_translation, "traduttore.wav")
        st.sidebar.audio("traduttore.wav", format="audio/wav")
        st.sidebar.success("Audio generato con successo!")
    else:
        st.sidebar.error("Nessuna traduzione disponibile per generare l'audio.")
# ----------------------------------------------------------

# Quando l'applicazione "rerunna", stampa tutti i messaggi precedenti
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


prompt = st.chat_input(f"Scrivi un testo da tradurre in {language}") # L'invio dell'utente causa un "rerun"
# se l'utente ha inviato un messaggio...
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    #Aggiorna la cronologia dei messaggi
    st.session_state.messages.append({"role": "user", "content": prompt})

    # ottieni la risposta dal modello LLM
    response = st.session_state.llm.answer(prompt, language=language)

    # Se è stata tradotta una frase in inglese, salvala come ultima traduzione
    if language == "inglese":
        st.session_state.last_translation = response
    
    # Mostra la risposta del modello
    with st.chat_message("assistant"):
        st.write_stream(response_generator(response))
    # Aggiorna la cronologia dei messaggi
    st.session_state.messages.append({"role": "assistant", "content": response})