import streamlit as st

st.set_page_config(page_title="Prova streamlit", page_icon="🧪")

if "text" not in st.session_state:
    st.session_state.text = ""
if "rerun" not in st.session_state:
    st.session_state.rerun = False

st.title('Pagina interattiva')
st.write(f'Testo inviato: {st.session_state.text}')

st.sidebar.title('Barra laterale')
text = st.sidebar.text_input('Scrivi qui il tuo testo')
button = st.sidebar.button('Invia')
check = st.sidebar.checkbox('Spunta prima di inviare')

 # se la pagina è stata rerunnata significa che l'utente ha inviato il testo, quindi mostra un messaggio di successo
if st.session_state.rerun:
    st.session_state.rerun = False
    st.sidebar.success('Testo inviato con successo!')
    st.balloons()
    st.snow()

if button:
    if not text:
        st.sidebar.error('Devi scrivere qualcosa prima di inviare!')
    elif not check:
        st.sidebar.error('Devi spuntare la casella prima di inviare!')
    else: # se il testo viene inviato, rerunno la pagina
        st.session_state.text = text
        st.session_state.rerun = True
        st.rerun()
        
