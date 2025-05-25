# Modifiche apportate ai file precedentemente scritti:
# - LLM: aggiunto il metodo `set_model_name` per cambiare il modello LLM da utilizzare.
# - Chatbot: aggiunto il metodo `set_zero_shot` per cambiare il classificatore zero-shot da utilizzare.
# - Chatbot: modificato il metodo `answer` in modo da supportare l'assenza di un modello zero-shot
# - Chatbot: modificato il metodo `answer` in modo da avere controllo sul threshold e sul limit della ricerca di similarità
# - Chatbot, LLM, LLMLibrary: aggiunto al metodo `answer` il parametro `temperature`

import streamlit as st
from Chatbot import Chatbot, Similarity, ZeroShot
from LLMLibrary import LLMLibrary
import time

def response_generator(response):
    for chunk in response.split():
        yield chunk+" "
        time.sleep(0.04)  # Simula un ritardo per mostrare il caricamento della risposta

st.set_page_config(page_title="Chatbot libreria", page_icon="📚")

# INIZIALIZZAZIONE -----------------------------------------
with st.spinner("Inizializzazione modelli..."):
    if "messages" not in st.session_state:
        st.session_state.messages = [] # messages è una lista di dizionari del tipo {"role": "user" o "assistant", "content": "testo del messaggio"}

    if "zero_shot" not in st.session_state:
        st.session_state.zero_shot = ZeroShot("MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7", "pericoloso", "sicuro")

    if "similarity" not in st.session_state:
        st.session_state.similarity = Similarity("nickprock/sentence-bert-base-italian-xxl-uncased")
        knowledge = []
        with open("./04-streamlit/knowledge.txt", "r", encoding="utf-8") as file:
            knowledge = [line.strip() for line in file]
        st.session_state.similarity.index(knowledge)

    if "llm" not in st.session_state:
        st.session_state.llm = LLMLibrary("llama-3.1-8b-instant")

    if "chatbot" not in st.session_state:
        st.session_state.chatbot = Chatbot(
            st.session_state.llm,
            st.session_state.zero_shot,
            st.session_state.similarity
        )
    if "model_name" not in st.session_state:
        st.session_state.model_name = "llama-3.1-8b-instant" # Modello LLM da utilizzare

    if "use_zero_shot" not in st.session_state:
        st.session_state.use_zero_shot = True # Flag che indica se utilizzare il classificatore zero-shot o meno
# ----------------------------------------------------------

st.title("Chatbot")

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
    st.session_state.chatbot = Chatbot(
        st.session_state.llm,
        st.session_state.zero_shot,
        st.session_state.similarity
    )

# Selezione della temperatura per il modello LLM
temperature = st.sidebar.slider(
    "Temperatura del LLM",
    min_value=0.0,
    max_value=2.0,
    value=0.7,
    step=0.1
)

# Selezione se utilizzare il classificatore zero-shot
use_zero_shot = st.sidebar.checkbox(
    "Utilizza il classificatore zero-shot",
    value=st.session_state.zero_shot is not None
)
# Se l'utente ha cambiato il flag, aggiorna il chatbot
if use_zero_shot != st.session_state.use_zero_shot:
    st.session_state.use_zero_shot = use_zero_shot
    if use_zero_shot:
        st.session_state.chatbot.set_zero_shot(st.session_state.zero_shot)
    else:
        st.session_state.chatbot.set_zero_shot(None)

# Selezione della soglia di similarità per la ricerca delle informazioni
threshold = st.sidebar.slider(
    "Soglia di similarità per la ricerca delle informazioni",
    min_value=0.0,
    max_value=1.0,
    value=0.15,
    step=0.01
)

# Selezione del numero massimo di risultati da considerare nella ricerca delle informazioni
limit = st.sidebar.number_input(
    "Numero massimo di risultati da considerare nella ricerca delle informazioni",
    min_value=5,
    max_value=50,
    value=10,
    step=1,
    placeholder="Inserisci un numero..."
)
# ----------------------------------------------------------


# Quando l'applicazione "rerunna", stampa tutti i messaggi precedenti
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


prompt = st.chat_input("Scrivi un messaggio") # L'invio dell'utente causa un "rerun"
# se l'utente ha inviato un messaggio...
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # ottieni la risposta dal modello LLM
    response = st.session_state.chatbot.answer(prompt,
                                               temperature,
                                               threshold,
                                               limit,
                                               ["sicuro"])
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.write_stream(response_generator(response))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})