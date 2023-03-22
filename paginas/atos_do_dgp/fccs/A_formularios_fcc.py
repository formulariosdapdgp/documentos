import streamlit as st
from funcoes.variaveis import *
import funcoes.functions


# Formulários FCC
def formularios_fcc(doc_a_ser_gerado, eh_substituicao, nome_do_ato):
    '''
    Recebe: (nome da função que irá determinar o tipo de ato, bool para dizer se é substuição ou não, nome do ato par o título)
    '''
    st.subheader(f'Ato de {nome_do_ato}')
    dados_fcc = {}
    with st.form(key="fcc", clear_on_submit=True):
        col_numero_ato, col_ano_ato = st.columns(2)
        with col_numero_ato:
            dados_fcc['numero_ato'] = st.text_input("Informe o número do ato:", max_chars=4)
        with col_ano_ato:
            dados_fcc['ano_ato']= st.text_input("Informe o ano do ato:", value=str(ano_atual), max_chars=4)
        dados_fcc['nome_designado'] = st.text_input("Nome do Designado: ")
        col_substituicao_1, col_substituicao_2 = st.columns(2)
        if eh_substituicao:
         with col_substituicao_1:
               dados_fcc['nome_titular_substituido'] = st.text_input("Nome do Titular a ser substituído: ")
               dados_fcc['inicio_substituicao'] = st.date_input("Início da Substituição: ")
         with col_substituicao_2:
               dados_fcc['motivo_substituicao'] = st.text_input("Durante o período de: ")
               dados_fcc['fim_substituicao'] = st.date_input("Término da Substituição: ")
        col_genero, col_coord = st.columns(2)
        with col_genero:
            dados_fcc['genero_coordenador'] = st.radio("Genero:",("Masculino", "Feminino"))
        with col_coord:
            dados_fcc['nome_coordenacao'] = st.radio("Tipo de Coordenação:",("Curso de Pós-graduação", "Curso de Graduação"))
        dados_fcc['descricao_funcao'] = st.text_input("Curso de graduação ou pós-graduação em: ")
        dados_fcc['numero_sei'] = st.text_input("Número do processo SEI:")
        dados_fcc['decana'] = st.radio("Assinatura:",("Decana titular", "Decana em exercício"))
        pos_btn_1, pos_btn_2, pos_btn_3 = st.columns([3,3,1])
        with pos_btn_1:
            pass
        with pos_btn_2:
            btn_gravar = st.form_submit_button("Gravar dados")
        with pos_btn_3:
            pass
    if btn_gravar:
        ato_gerado = doc_a_ser_gerado(dados_fcc)
        st.success("Ato gerado com sucesso! Clique em 'BAIXAR DOCUMENTO'")
        funcoes.functions.baixar_formulario(ato_gerado)
