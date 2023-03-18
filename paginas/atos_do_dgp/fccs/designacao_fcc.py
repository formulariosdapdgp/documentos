import streamlit as st
from funcoes.variaveis import *
import funcoes.functions
 


def form_designacao_fcc():
    dados_fcc = {}
    with st.form(key="fcc", clear_on_submit=True):
        col_numero_ato, col_ano_ato = st.columns(2)
        with col_numero_ato:
            dados_fcc['numero_ato'] = st.text_input("Informe o número do ato:", max_chars=4)
        with col_ano_ato:
            dados_fcc['ano_ato']= st.text_input("Informe o ano do ato:", value=str(ano_atual), max_chars=4)
        dados_fcc['nome_designado'] = st.text_input("Nome do Designado: ")
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
        ato_gerado = gerar_ato_designa_fcc(dados_fcc)
        st.success("Ato gerado com sucesso! Clique em 'BAIXAR DOCUMENTO'")
        funcoes.functions.baixar_formulario(ato_gerado)
        

def gerar_ato_designa_fcc(dados_designacao):
    with open("Ato_designacao_fcc.html", "w", encoding='UTF-8') as ato:
        ato.write('''
        <!DOCTYPE html>
        <html lang="pt-br" >
            <head>
            <!--
            <meta http-equiv="Pragma" content="no-cache" />
            <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">-->
            <meta charset="UTF-8">
            <style type="text/css">
            p.Citacao {font-size:10pt;font-family:Calibri;word-wrap:normal;margin:4pt 0 4pt 160px;text-align:justify;} p.Fonte_10 {font-size:10pt;} p.Item_Alinea_Letra {font-size:12pt;font-family:Calibri;text-indent:0mm;text-align:justify;word-wrap:normal;margin:6pt 6pt 6pt 120px;counter-increment:letra_minuscula;} p.Item_Alinea_Letra:before {content:counter(letra_minuscula, lower-latin) ") ";display:inline-block;width:5mm;font-weight:normal;} p.Item_Inciso_Romano {font-size:12pt;font-family:Calibri;text-align:justify;word-wrap:normal;text-indent:0mm;margin:6pt 6pt 6pt 120px;counter-increment:romano_maiusculo;counter-reset:letra_minuscula;} p.Item_Inciso_Romano:before {content:counter(romano_maiusculo, upper-roman) " - ";display:inline-block;width:15mm;font-weight:normal;} p.Item_Nivel1 {text-transform:uppercase;font-weight:bold;background-color:#e6e6e6;font-size:12pt;font-family:Calibri;text-align:justify;word-wrap:normal;text-indent:0;margin:6pt;counter-increment:item-n1;counter-reset:item-n2 item-n3 item-n4 romano_maiusculo letra_minuscula;} p.Item_Nivel1:before {content:counter(item-n1) ".";display:inline-block;width:25mm;font-weight:normal;} p.Item_Nivel2 {font-size:12pt;font-family:Calibri;text-indent:0mm;text-align:justify;word-wrap:normal;margin:6pt;counter-increment:item-n2;counter-reset:item-n3 item-n4 romano_maiusculo letra_minuscula;} p.Item_Nivel2:before {content:counter(item-n1) "." counter(item-n2) ".";display:inline-block;width:25mm;font-weight:normal;} p.Item_Nivel3 {font-size:12pt;font-family:Calibri;text-indent:0mm;text-align:justify;word-wrap:normal;margin:6pt;counter-increment:item-n3;counter-reset:item-n4 romano_maiusculo letra_minuscula;} p.Item_Nivel3:before {content:counter(item-n1) "." counter(item-n2) "." counter(item-n3) ".";display:inline-block;width:25mm;font-weight:normal;} p.Item_Nivel4 {font-size:12pt;font-family:Calibri;text-indent:0mm;text-align:justify;word-wrap:normal;margin:6pt;counter-increment:item-n4;counter-reset:romano_maiusculo letra_minuscula;} p.Item_Nivel4:before {content:counter(item-n1) "." counter(item-n2) "." counter(item-n3) "."  counter(item-n4) ".";display:inline-block;width:25mm;font-weight:normal;} p.Paragrafo_Numerado_Nivel1 {font-size:12pt;font-family:Calibri;text-align:justify;word-wrap:normal;text-indent:0mm;margin:6pt;counter-increment:paragrafo-n1;counter-reset:paragrafo-n2 paragrafo-n3 paragrafo-n4 romano_maiusculo letra_minuscula;} p.Paragrafo_Numerado_Nivel1:before {content:counter(paragrafo-n1) ".";display:inline-block;width:25mm;font-weight:normal;} p.Paragrafo_Numerado_Nivel2 {font-size:12pt;font-family:Calibri;text-indent:0mm;text-align:justify;word-wrap:normal;margin:6pt;counter-increment:paragrafo-n2;counter-reset:paragrafo-n3 paragrafo-n4 romano_maiusculo letra_minuscula;} p.Paragrafo_Numerado_Nivel2:before {content:counter(paragrafo-n1) "." counter(paragrafo-n2) ".";display:inline-block;width:25mm;font-weight:normal;} p.Paragrafo_Numerado_Nivel3 {font-size:12pt;font-family:Calibri;text-indent:0mm;text-align:justify;word-wrap:normal;margin:6pt;counter-increment:paragrafo-n3;counter-reset:paragrafo-n4 romano_maiusculo letra_minuscula;} p.Paragrafo_Numerado_Nivel3:before {content:counter(paragrafo-n1) "." counter(paragrafo-n2) "." counter(paragrafo-n3) ".";display:inline-block;width:25mm;font-weight:normal;} p.Paragrafo_Numerado_Nivel4 {font-size:12pt;font-family:Calibri;text-indent:0mm;text-align:justify;word-wrap:normal;margin:6pt;counter-increment:paragrafo-n4;counter-reset:romano_maiusculo letra_minuscula;} p.Paragrafo_Numerado_Nivel4:before {content:counter(paragrafo-n1) "." counter(paragrafo-n2) "." counter(paragrafo-n3) "." counter(paragrafo-n4) ".";display:inline-block;width:25mm;font-weight:normal;} p.Tabela_texto_6 {font-size:6pt;font-family:Calibri;text-align:left;word-wrap:normal;margin:0 3pt 0 3pt;} p.Tabela_Texto_8 {font-size:8pt;font-family:Calibri;text-align:left;word-wrap:normal;margin:0 3pt 0 3pt;} p.Tabela_Texto_8_Alinhado_Direita_UnB {font-size:8pt;font-family:Calibri;text-align:rigth;word-wrap:normal;margin:0 3pt 0 3pt;} p.Tabela_Texto_8_Centralizado_UnB {font-size:8pt;font-family:Calibri;text-align:center;word-wrap:normal;margin:0 3pt 0 3pt;} p.Tabela_Texto_Alinhado_Direita {font-size:11pt;font-family:Calibri;text-align:right;word-wrap:normal;margin:0 3pt 0 3pt;} p.Tabela_Texto_Alinhado_Esquerda {font-size:11pt;font-family:Calibri;text-align:left;word-wrap:normal;margin:0 3pt 0 3pt;} p.Tabela_Texto_Centralizado {font-size:11pt;font-family:Calibri;text-align:center;word-wrap:normal;margin:0 3pt 0;} p.Tachado {font-size:11pt;font-family:Calibri;text-indent:1.18in;text-align:justify;word-wrap:normal;text-decoration:line-through;} p.Texto_Alinhado_Direita {font-size:12pt;font-family:Calibri;text-align:right;word-wrap:normal;margin:6pt;} p.Texto_Alinhado_Esquerda {font-size:12pt;font-family:Calibri;text-align:left;word-wrap:normal;margin:6pt;} p.Texto_Alinhado_Esquerda_Espacamento_Simples {font-size:12pt;font-family:Calibri;text-align:left;word-wrap:normal;margin:0;} p.Texto_Alinhado_Esquerda_Espacamento_Simples_Maiusc {font-size:12pt;font-family:Calibri;text-align:left;text-transform:uppercase;word-wrap:normal;margin:0;} p.Texto_Centralizado {font-size:12pt;font-family:Calibri;text-align:center;word-wrap:normal;margin:6pt;} p.Texto_Centralizado_Maiusculas {font-size:13pt;font-family:Calibri;text-align:center;text-transform:uppercase;word-wrap:normal;} p.Texto_Centralizado_Maiusculas_Negrito {font-weight:bold;font-size:13pt;font-family:Calibri;text-align:center;text-transform:uppercase;word-wrap:normal;} p.Texto_Espaco_Duplo_Recuo_Primeira_Linha {letter-spacing:0.2em;font-weight:bold;font-size:12pt;font-family:Calibri;text-indent:25mm;text-align:justify;word-wrap:normal;margin:6pt;} p.Texto_Fundo_Cinza_Maiusculas_Negrito {text-transform:uppercase;font-weight:bold;background-color:#e6e6e6;font-size:12pt;font-family:Calibri;text-align:justify;word-wrap:normal;text-indent:0;margin:6pt;} p.Texto_Fundo_Cinza_Negrito {font-weight:bold;background-color:#e6e6e6;font-size:12pt;font-family:Calibri;text-align:justify;word-wrap:normal;text-indent:0;margin:6pt;} p.Texto_Justificado {font-size:12pt;font-family:Calibri;text-align:justify;word-wrap:normal;text-indent:0;margin:6pt;} p.Texto_Justificado_Maiusculas {font-size:12pt;font-family:Calibri;text-align:justify;word-wrap:normal;text-indent:0;margin:6pt;text-transform:uppercase;} p.Texto_Justificado_Recuo_Primeira_Linha {font-size:12pt;font-family:Calibri;text-indent:25mm;text-align:justify;word-wrap:normal;margin:6pt;} p.Texto_Mono_Espacado {font-size:8pt;font-family:Calibri;text-align:left;white-space:pre;word-wrap:normal;margin:2pt;} 
            </style><title>Designação FCC</title>
            </head>''')
        ato.write(f'''
            <body>
            <p class="Texto_Centralizado_Maiusculas">ATO DO DECANATO DE GEST&Atilde;O DE PESSOAS&nbsp;n&ordm; {dados_designacao['numero_ato']}/{dados_designacao['ano_ato']}</p>

            <p>&nbsp;</p>
            <table align="center" border="0" cellpadding="20" cellspacing="2" style="width: 98%;">
                <tbody>
                    <tr>
                        <td style="padding-right: 25px; width: 224px; text-align: left;" valign="middle">&nbsp;&nbsp;</td>
                        <td style="width: 384px;">''')
        nome_designado = dados_designacao['nome_designado'].title().replace(" Da ", " da ").replace(" Do ", " do ").replace(" De ", " de ").replace(" Di ", " di ").replace(" Du ", " du" )
        ato.write(f'''
                        <p class="Texto_Justificado" style="font-size:12pt;font-family:Calibri;text-align:justify;word-wrap:normal;text-indent:0;margin:6pt;">
                        Designa {"o Professor do Magistério Superior" if dados_designacao['genero_coordenador'] == "Masculino" else "a Professora do Magistério Superior"} {nome_designado} 
                        para exercer a função de {"Coordenador" if dados_designacao['genero_coordenador'] == "Masculino" else "Coordenadora"} do {dados_designacao['nome_coordenacao']} em 
                        {dados_designacao['descricao_funcao'].title().replace(" Da ", " da ").replace(" Do ", " do ").replace(" De ", " de ").replace(" Di ", " di ").replace(" Du ", " du" )} (FCC).</p>
                        </td>
                    </tr>
                </tbody>
            </table>
            <p class="Texto_Justificado_Recuo_Primeira_Linha" style="font-size:12pt;font-family:Calibri;text-indent:25mm;text-align:justify;word-wrap:normal;margin:6pt;">A DECANA&nbsp;DE GEST&Atilde;O DE PESSOAS DA UNIVERSIDADE DE BRAS&Iacute;LIA, no uso de suas atribui&ccedil;&otilde;es legais, conferidas pelo Ato da Reitoria n&ordm; 72, publicado no DOU n. 13, de 20 de janeiro&nbsp;de 2021, se&ccedil;&atilde;o 2, p&aacute;gina 24, e de acordo com a compet&ecirc;ncia que lhe foi delegada por meio do Ato da Reitoria n. 304, de 23 de mar&ccedil;o de 2017, publicado no&nbsp;<em>DOU</em>&nbsp;
            n. 58, de 24 de mar&ccedil;o de 2017 e &agrave; vista do constante no Processo Eletr&ocirc;nico n&ordm; {dados_designacao['numero_sei']},</p>

            <p class="Texto_Justificado_Recuo_Primeira_Linha">&nbsp;</p>

            <p class="Texto_Justificado_Recuo_Primeira_Linha">R E S O L V E:</p>

            <p class="Texto_Justificado_Recuo_Primeira_Linha">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</p>

            <p class="Texto_Justificado_Recuo_Primeira_Linha" style="font-size:12pt;font-family:Calibri;text-indent:25mm;text-align:justify;word-wrap:normal;margin:6pt;">Designar, para mandato de 2 (dois) anos, {"o Professor do Magistério Superior" if dados_designacao['genero_coordenador'] == "Masculino" else "a Professora do Magistério Superior"} {nome_designado}
              para exercer a fun&ccedil;&atilde;o de&nbsp;{"Coordenador" if dados_designacao['genero_coordenador'] == "Masculino" else "Coordenadora"} do
              {dados_designacao['nome_coordenacao']} em {dados_designacao['descricao_funcao'].title().replace(" Da ", " da ").replace(" Do ", " do ").replace(" De ", " de ").replace(" Di ", " di ").replace(" Du ", " du" )} (FCC).</p>

            <p class="Texto_Justificado_Recuo_Primeira_Linha">&nbsp;</p>

            <p class="Texto_Justificado_Recuo_Primeira_Linha">&nbsp;</p>

            <p class="Tabela_Texto_Centralizado">
            {decana_titular  if dados_designacao['decana'] == "Decana titular" else decana_em_exercicio }
            </p>
            
            </body>
            </html>''')
    return [ato.name, ato]
          
        



    
    