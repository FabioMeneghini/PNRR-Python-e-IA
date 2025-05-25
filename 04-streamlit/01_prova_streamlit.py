import streamlit as st

# PAGINA PRINCIPALE

st.set_page_config(page_title="Prova streamlit", page_icon="🧪")
st.title('Titolo della pagina')
st.write('Testo')

st.subheader('Sottotitolo')
st.write('Testo')

st.text_input('Scrivi qui il tuo testo')
st.text_area('Scrivi qui il tuo testo')
st.button('Invia')

st.checkbox('Accetta i termini e le condizioni')
st.radio('Scegli una opzione', ('Opzione 1', 'Opzione 2'))
st.selectbox('Scegli una opzione', ('Opzione 1', 'Opzione 2'))
st.multiselect('Scegli più opzioni', ('Opzione 1', 'Opzione 2'))

st.slider('Scegli un numero', 0, 100, 50)
st.date_input('Scegli una data')
st.time_input('Scegli un orario')
st.file_uploader('Carica un file')
st.color_picker('Scegli un colore')

st.progress(50)

st.success('Operazione completata con successo!')
st.error('Si è verificato un errore!')
st.warning('Attenzione! Questo è un avviso!')
st.info('Informazioni utili!')


# SIDEBAR

st.sidebar.title('Barra laterale')
st.sidebar.write('Testo nella barra laterale')
st.sidebar.text_input('Scrivi qui il tuo testo')
st.sidebar.text_area('Scrivi qui il tuo testo')
st.sidebar.button('Invia')
st.sidebar.checkbox('Accetta i termini e le condizioni')
st.sidebar.radio('Scegli una opzione nella barra laterale', ('Opzione 1', 'Opzione 2'))
st.sidebar.selectbox('Scegli una opzione nella barra laterale', ('Opzione 1', 'Opzione 2'))
