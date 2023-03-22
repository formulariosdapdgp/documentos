import streamlit as st
from funcoes.variaveis import *
import paginas.pagina_inicial 
import paginas.atos_do_dgp.fccs.designacao_fcc, paginas.atos_do_dgp.fccs.dispensa_fcc, paginas.atos_do_dgp.fccs.substituicao_fcc, paginas.atos_do_dgp.fccs.A_formularios_fcc, paginas.atos_do_dgp.fccs.ato_generio_fcc
import os

   
def menu_opcoes_docs(doc_selecionado):
    
    pagina_inicial = True
    # ATOS DA REITORIA
    if doc_selecionado == tipo_de_documento[1]:
       tipo_de_ato_reitoria = st.sidebar.selectbox("Informe o tipo de ato", atos_reitoria)
       if tipo_de_ato_reitoria == atos_reitoria[1] or tipo_de_ato_reitoria == atos_reitoria[2] or tipo_de_ato_reitoria == atos_reitoria[3]:
          cd_escolhida = st.sidebar.selectbox("Informe a CD", lista_cds)
          if cd_escolhida != "":
              pagina_inicial = False
       elif tipo_de_ato_reitoria == atos_reitoria[4] or tipo_de_ato_reitoria == atos_reitoria[5]:
          fg_escolhida = st.sidebar.selectbox("Informe a FG", lista_fgs)
          if fg_escolhida != "":
              pagina_inicial = False
    

    # ATOS DO DGP
    if doc_selecionado == tipo_de_documento[2]:
       tipo_de_ato_dgp = st.sidebar.selectbox("Informe o tipo de ato", atos_dgp)
       if tipo_de_ato_dgp == atos_dgp[1] or tipo_de_ato_dgp == atos_dgp[2] or tipo_de_ato_dgp == atos_dgp[3]:
          fcc_escolhida = st.sidebar.selectbox("Informe a FCC", lista_fcc)
          if fcc_escolhida != "":
              pagina_inicial = False

          # Designação para FCC
          if fcc_escolhida == lista_fcc[1] and tipo_de_ato_dgp == atos_dgp[1]:
             paginas.atos_do_dgp.fccs.A_formularios_fcc.formularios_fcc(paginas.atos_do_dgp.fccs.ato_generio_fcc.gerar_ato_fcc, False, "Designação de FCC")
             #paginas.atos_do_dgp.fccs.A_formularios_fcc.formularios_fcc(paginas.atos_do_dgp.fccs.designacao_fcc.gerar_ato_designa_fcc, False, "Designação de FCC")
             st.sidebar.write(modelo_ato_em_branco)
          
          # Dispensa para FCC
          if fcc_escolhida == lista_fcc[1] and tipo_de_ato_dgp == atos_dgp[2]:
             paginas.atos_do_dgp.fccs.A_formularios_fcc.formularios_fcc(paginas.atos_do_dgp.fccs.ato_generio_fcc.gerar_ato_fcc, False, "Dispensa de FCC")
             #paginas.atos_do_dgp.fccs.A_formularios_fcc.formularios_fcc(paginas.atos_do_dgp.fccs.dispensa_fcc.gerar_ato_dispensa_fcc, False, "Dispensa de FCC")
             st.sidebar.write(modelo_ato_em_branco)
          
          # Substituição para FCC
          if fcc_escolhida == lista_fcc[1] and tipo_de_ato_dgp == atos_dgp[3]:
             paginas.atos_do_dgp.fccs.A_formularios_fcc.formularios_fcc(paginas.atos_do_dgp.fccs.ato_generio_fcc.gerar_ato_fcc, True, "Substituição de FCC")
             #paginas.atos_do_dgp.fccs.A_formularios_fcc.formularios_fcc(paginas.atos_do_dgp.fccs.substituicao_fcc.gerar_ato_substituicao_fcc, True, "Substituição de FCC")
             st.sidebar.write(modelo_ato_em_branco)


       elif tipo_de_ato_dgp == atos_dgp[4]:
          opcao_fg = st.sidebar.selectbox("Informe a FG", lista_fgs)
          if opcao_fg != "":
              pagina_inicial = False
       
       
    # Pagina inicial
    if pagina_inicial:
      paginas.pagina_inicial.home()

            



#Baixar Arquivo
def baixar_formulario(form_gerado):
    pos_btn_1, pos_btn_2, pos_btn_3 = st.columns([3,3,1])
    with pos_btn_1:
        pass
    with pos_btn_2:
       try:
            with open(str(form_gerado[0]), "rb") as file:
                st.download_button(
                    label="BAIXAR DOCUMENTO",
                    data=file,
                    file_name=form_gerado[0],
                    mime="text/html")
       except:
            st.error("ARQUIVO NÃO LOCALIZADO! REPITA O PROCESSO.")
    with pos_btn_3:
        pass
    os.remove(form_gerado[0])
    

# função para deixar data recebida no formato necessário
def data_convertida_br(dt): # recebe uma String
  dia = dt[8:]
  mes = dt[5:7]
  ano = dt[0:4]
  if dia == "":
    return ""
  else:
    return f'{dia}/{mes}/{ano}' # retorna uma String
