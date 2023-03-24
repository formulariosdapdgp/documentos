import streamlit as st
import pandas as pd
import funcoes.functions


dados_nt_ppp = {}
uorg = []
dt_ini = []
dt_fim = []


def gerar_nt_ppp():
    dados_gerais, lotacao_exercicio, concessao_adcional, licencas_afastamentos, ficha_financeira = st.tabs(("Informações Gerais",
                                                                                                            "Lotação/Exercício",
                                                                                                            "Concessões de Adcionais",
                                                                                                            "Licenças/Afastamentos",
                                                                                                            "Ficha Financeira"))
    with dados_gerais:
        st.write("")
        with st.form(key="dados_gerais", clear_on_submit=True):

            # Informações do servidor
            col_1, col_2 = st.columns(2)
            with col_1:
                dados_nt_ppp['nome_servidor'] = st.text_input("Nome do Servidor(a): ")
                dados_nt_ppp['cargo_servidor'] = st.text_input("Cargo do Servidor(a): ")
            with col_2:
                dados_nt_ppp['matricula_siape_servidor'] = st.text_input("Matrícula SIAPE: ")
                dados_nt_ppp['ingresso_unb_servidor'] = st.date_input("Ingresso na UnB: ")
            dados_nt_ppp['genero_servidor'] = st.radio("Informe o Gênero:", ("Masculino", "Feminino"))
            
            # referências do SEI
            with st.expander("Clique para informar as referências do processo SEI", expanded=False):
                dados_nt_ppp['processo_SEI'] = st.text_input("Número do Processo SEI de Referência", placeholder="Caso seja mais de um, separar por vírgula. Ex.: 23106.025969/2023-13, 23106.025969/2023-14")
                dados_nt_ppp['SEI_dados_funcionais'] = st.text_input("Número SEI dos Dados Funcionais", placeholder="Caso seja mais de um, separar por vírgula. Ex.: 9422148, 9449709")
                dados_nt_ppp['SEI_atos_concessao'] = st.text_input("Número SEI dos Atos de Concessão", placeholder="Caso seja mais de um, separar por vírgula. Ex.: 9422148, 9449709")
                dados_nt_ppp['SEI_relatorio_afastamentos'] = st.text_input("Número SEI dos Relatórios de Afastamento", placeholder="Caso seja mais de um, separar por vírgula. Ex.: 9422148, 9449709")
                dados_nt_ppp['SEI_ficha_financeira'] = st.text_input("Número SEI da Ficha Financeira", placeholder="Caso seja mais de um, separar por vírgula. Ex.: 9422148, 9449709")
            col_1_btn_gerais, col_2_btn_gerais, col_3_btn_gerais = st.columns([2,3,1])
            with col_1_btn_gerais:
                pass
            with col_2_btn_gerais:
                st.write("")
                btn_dados_gerais = st.form_submit_button("GRAVAR DADOS GERAIS")
            with col_3_btn_gerais:
                pass
    
    with lotacao_exercicio:
        st.write("Lotação exercício")
    
    # concessões de adicionais
    with concessao_adcional:
        st.write("") 
                                                                                                            
        with st.form(key="atos_concessao", clear_on_submit=True):
            uorg_col, dt_ini_col, dt_fim_col, btn_salvar_col = st.columns(4)
            with uorg_col:
                dados_nt_ppp['uorg_concessao_adicional'] = st.text_input("Informe a UORG: ", max_chars=4)
            with dt_ini_col:
                dados_nt_ppp['data_inicial_concessao_adicional'] = st.date_input("Data Inicial da Concessão")
            with dt_fim_col:
                dados_nt_ppp['data_final_concessao_adicional'] = st.date_input("Data Final  da Concessão")
            with btn_salvar_col:
                st.text("")
                st.text("")
                btn_gravar_infos = st.form_submit_button("GRAVAR CONCESSÃO")
        if btn_gravar_infos:
            uorg.append(dados_nt_ppp['uorg_concessao_adicional'])
            dt_ini.append(dados_nt_ppp["data_inicial_concessao_adicional"])
            dt_fim.append(dados_nt_ppp["data_final_concessao_adicional"])
            df = pd.DataFrame(data={"UORG": uorg, "DATA INICIAL": dt_ini, "DATA FINAL": dt_fim})
            st.table(df)
    
    with licencas_afastamentos:
        st.write("Licenças - Afastamentos")
    
    with ficha_financeira:
        st.write("Ficha Financeira")
        