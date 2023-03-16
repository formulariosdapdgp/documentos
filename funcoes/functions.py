import streamlit as st
from funcoes.variaveis import *


def menu_opcoes_docs(doc_selecionado):
    
    # ATOS DA REITORIA
    if doc_selecionado == tipo_de_documento[1]:
       tipo_de_ato_reitoria = st.sidebar.selectbox("Informe o tipo de ato", atos_reitoria)
       if tipo_de_ato_reitoria == atos_reitoria[1] or tipo_de_ato_reitoria == atos_reitoria[2] or tipo_de_ato_reitoria == atos_reitoria[3]:
          cd_escolhida = st.sidebar.selectbox("Informe a CD", lista_cds)
       elif tipo_de_ato_reitoria == atos_reitoria[4] or tipo_de_ato_reitoria == atos_reitoria[5]:
          fg_escolhida = st.sidebar.selectbox("Informe a FG", lista_fgs)

    # ATOS DO DGP
    if doc_selecionado == tipo_de_documento[2]:
       tipo_de_ato_dgp = st.sidebar.selectbox("Informe o tipo de ato", atos_dgp)
       if tipo_de_ato_dgp == atos_dgp[1] or tipo_de_ato_dgp == atos_dgp[2] or tipo_de_ato_dgp == atos_dgp[3]:
          fcc_escolhida = st.sidebar.selectbox("Informe a FCC", lista_fcc)
       elif tipo_de_ato_dgp == atos_dgp[4]:
          opcao_fg = st.sidebar.selectbox("Informe a FG", lista_fgs)
            
