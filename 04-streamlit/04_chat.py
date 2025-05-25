import streamlit as st

st.set_page_config(page_title="Prova streamlit", page_icon="💬")

# INIZIALIZZAZIONE -----------------------------------------
# Inizializza la variabile di sessione "messages" per gestire la cronologia dei messaggi
if "messages" not in st.session_state:
    st.session_state.messages = [] # messages è una lista di dizionari del tipo {"role": "user" o "assistant", "content": "testo del messaggio"}
# ----------------------------------------------------------

st.title("Chat")

# Quando l'applicazione "rerunna", stampa tutti i messaggi precedenti
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Scrivi un messaggio") # L'invio dell'utente causa un "rerun"
# se l'utente ha inviato un messaggio...
if prompt:
    #st.write(f"L'utente ha scritto: {prompt}") # lo stampa come "testo semplice"
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})