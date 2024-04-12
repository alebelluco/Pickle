# test development streamlit persistence

import streamlit as st
import pandas as pd
import persistence_ab as p

# Dati di accesso a GitHub-------------------------------------------

repository_name = 'storage_exera'
file_path  = 'pickled_df2.pickle'
#username = "alebelluco"
#token  = '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'
#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
# --------------------------------------------------------------------

st.set_page_config(page_title="Test", layout='wide')
st.title('Script write and retrieve')

st.write('Test1. Caricamento file excel')
path = st.file_uploader('carica il file excel')
if not path:
    st.stop()

df = pd.read_excel(path)

if st.button('Aggiorna'):
    p.upload_file(df, repository_name, file_path)

if st.button('Rerieve'):
    file = p.retrieve_file(repository_name, file_path)

    st.write(file)