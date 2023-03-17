import streamlit as st
from funcoes.variaveis import *
from paginas.atos_do_dgp.fccs import designacao_fcc


#Baixar Arquivo
def baixar_formulario(form_gerado):
    pos_btn_1, pos_btn_2, pos_btn_3 = st.columns([3,3,1])
    with pos_btn_1:
        pass
    with pos_btn_2:
       try:
            with open(str(form_gerado[0]), "rb") as file:
                st.download_button(
                    label="BAIXAR ATO",
                    data=file,
                    file_name=form_gerado[0],
                    mime="text/html")
       except:
            st.error("ARQUIVO NÃO LOCALIZADO! REPITA O PROCESSO.")
    with pos_btn_3:
        pass
    
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
          # Designação para FCC
          if fcc_escolhida == lista_fcc[1] and tipo_de_ato_dgp == atos_dgp[1]:
             designacao_fcc.form_designacao_fcc()
             st.sidebar.write(modelo_ato_em_brando)
       elif tipo_de_ato_dgp == atos_dgp[4]:
          opcao_fg = st.sidebar.selectbox("Informe a FG", lista_fgs)
            
