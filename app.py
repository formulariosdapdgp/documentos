import streamlit as st
from funcoes.variaveis import *
import funcoes.functions
import paginas.pagina_inicial



# barra lateral
with st.sidebar:
    st.title("MENU DE OPÇÕES")
    documento_escolhido = st.selectbox("Escolha o tipo de documento: ", tipo_de_documento)

# Chamando menu de opções
funcoes.functions.menu_opcoes_docs(documento_escolhido)    