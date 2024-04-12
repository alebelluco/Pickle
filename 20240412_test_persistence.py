# test development streamlit persistence

import streamlit as st
import pandas as pd
import persistence_ab as p

st.set_page_config(page_title="Test", layout='wide')
st.title('Script write and retrieve')

# Dati di accesso a GitHub-------------------------------------------

repository_name = st.text_input('Inserire nome cartella')

file_path  = 'pickled_test.pickle'
username = "alebelluco"

token = st.text_input('Inserire totken')
#token  = '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'


# --------------------------------------------------------------------


st.write('Test1. Caricamento file excel')
path = st.file_uploader('carica il file excel')
if not path:
    st.stop()

df = pd.read_excel(path)

if st.button('Aggiorna'):
    p.upload_file(username,token,df, repository_name, file_path)

if st.button('Rerieve'):
    file = p.retrieve_file(username, token,repository_name, file_path)

    st.write(file)