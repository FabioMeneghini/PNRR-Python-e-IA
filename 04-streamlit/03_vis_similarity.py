import streamlit as st
from Similarity import Similarity

st.set_page_config(page_title="Prova streamlit", page_icon="📊")

# INIZIALIZZAZIONE MODELLO --------------------------
data = [
    "Il gatto è sul tappeto",
    "Il cane gioca in giardino",
    "La pizza è deliziosa",
    "I gatti miagolano di notte",
    "Il sole splende nel cielo",
    "La luna brilla di notte",
    "Il mare è calmo"
]
if "similarity" not in st.session_state:
    st.session_state.similarity = Similarity()
    st.session_state.similarity.index(data)
# --------------------------------------------------

st.title('Visualizzazione sentence similarity')

# SIDEBAR --------------------------------------
st.sidebar.title('Barra laterale')
target = st.sidebar.text_input(label='Testo', label_visibility="hidden", placeholder='Scrivi qui la frase da confrontare')
threshold = st.sidebar.slider(label='Soglia di punteggio minima:', min_value=0.0, max_value=1.0, value=0.15, step=0.01)
limit = st.sidebar.slider(label='Limite massimo di risultati:', min_value=1, max_value=len(data), value=len(data)//2, step=1)
confronta = st.sidebar.button('Confronta')
# ---------------------------------------------

if confronta: # se l'utente ha cliccato "Confronta", mostra un grafico
    if not target:
        st.sidebar.error('La frase non può essere vuota!')
    else:
        results = st.session_state.similarity.search(target, threshold, limit)
        #results_sorted = sorted(results, key=lambda x: x['score'], reverse=True)
        st.bar_chart(
            data={
                "Punteggio": [result['score'] for result in results],
                "Frase": [result['text'] for result in results]
            },
            x="Frase",
            y="Punteggio",
            use_container_width=True,
            height=500
        )
else: # altrimenti, mostra una tabella con le frasi del dataset
    st.subheader('Dataset')
    tabella = {
        "Frasi": data
    }
    st.table(tabella)