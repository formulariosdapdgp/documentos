import streamlit as st
from funcoes.variaveis import *
from funcoes.functions import *


def form_designacao_fcc():
    dados_fcc = {}
    with st.form(key="fcc", clear_on_submit=True):
        dados_fcc['nome_designado'] = st.text_input("Nome do Designado: ")
        col_genero, col_coord = st.columns(2)
        with col_genero:
            dados_fcc['genero_coordenador'] = st.radio("Genero:",("Masculino", "Feminino"))
        with col_coord:
            dados_fcc['nome_coordenacao'] = st.radio("Tipo de Coordenação:",("curso de pós-graduação", "curso de graduação"))
        dados_fcc['descricao_funcao'] = st.text_input("Curso de graduação ou pós-graduação em: ")
        dados_fcc['numero_sei'] = st.text_input("Número do processo SEI:")
        pos_btn_1, pos_btn_2, pos_btn_3 = st.columns([3,3,1])
        with pos_btn_1:
            pass
        with pos_btn_2:
            btn_gravar = st.form_submit_button("Gravar dados")
            if btn_gravar:
                st.write(dados_fcc)
        with pos_btn_3:
            pass


