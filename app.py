import streamlit as st
from funcoes.variaveis import *
from funcoes.functions import *

# Título da página
col_titulo_1, col_titulo_2, col_titulo_3 = st.columns([1, 3, 1])
with col_titulo_1:
    pass
with col_titulo_2:
    st.subheader("Criador de documentos da COREF")
with col_titulo_3:
    pass

# barra lateral
with st.sidebar:
    st.title("MENU DE OPÇÕES")
    documento_escolhido = st.selectbox("Escolha o tipo de documento: ", tipo_de_documento)

# Chamando menu de opções
menu_opcoes_docs(documento_escolhido)    