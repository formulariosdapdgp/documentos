import streamlit as st
from funcoes.variaveis import *
from funcoes.functions import *

st.subheader("Criador de documentos para o SEI")

# barra lateral
with st.sidebar:
    st.title("MENU DE OPÇÕES")
    documento_escolhido = st.selectbox("Escolha o tipo de documento: ", tipo_de_documento)

menu_opcoes_docs(documento_escolhido)    