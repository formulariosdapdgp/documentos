import streamlit as st
from funcoes.variaveis import *
import funcoes.functions
        

def gerar_ato_fcc(dados_ato, tipo_ato):
    nome_arquivo = f'Ato de {tipo_ato}.html'
    with open(nome_arquivo, "w", encoding='UTF-8') as ato:
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
            </style>''')
        ato.write(f'''        
            <title>{tipo_ato}</title>
            </head>
        
            <body>
            <p class="Texto_Centralizado_Maiusculas">ATO DO DECANATO DE GEST&Atilde;O DE PESSOAS&nbsp;n&ordm; {dados_ato['numero_ato']}/{dados_ato['ano_ato']}</p>

            <p>&nbsp;</p>
            <table align="center" border="0" cellpadding="20" cellspacing="2" style="width: 98%;">
                <tbody>
                    <tr>
                        <td style="padding-right: 25px; width: 224px; text-align: left;" valign="middle">&nbsp;&nbsp;</td>
                        <td style="width: 384px;">''')
        nome = dados_ato['nome_designado'].title().replace(" Da ", " da ").replace(" Do ", " do ").replace(" De ", " de ").replace(" Di ", " di ").replace(" Du ", " du" )
        if tipo_ato == "Designação de FCC":
            ato.write(f'''
                            <p class="Texto_Justificado" style="font-size:12pt;font-family:Calibri;text-align:justify;word-wrap:normal;text-indent:0;margin:6pt;">
                            Designa {"o Professor do Magistério Superior" if dados_ato['genero_coordenador'] == "Masculino" else "a Professora do Magistério Superior"} {nome} 
                            para exercer a função de {"Coordenador" if dados_ato['genero_coordenador'] == "Masculino" else "Coordenadora"} do {dados_ato['nome_coordenacao']} em 
                            {dados_ato['descricao_funcao'].title().replace(" Da ", " da ").replace(" Do ", " do ").replace(" De ", " de ").replace(" Di ", " di ").replace(" Du ", " du" )} (FCC).</p>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <p class="Texto_Justificado_Recuo_Primeira_Linha" style="font-size:12pt;font-family:Calibri;text-indent:25mm;text-align:justify;word-wrap:normal;margin:6pt;">A DECANA&nbsp;DE GEST&Atilde;O DE PESSOAS DA UNIVERSIDADE DE BRAS&Iacute;LIA, no uso de suas atribui&ccedil;&otilde;es legais, conferidas pelo Ato da Reitoria n&ordm; 72, publicado no DOU n. 13, de 20 de janeiro&nbsp;de 2021, se&ccedil;&atilde;o 2, p&aacute;gina 24, e de acordo com a compet&ecirc;ncia que lhe foi delegada por meio do Ato da Reitoria n. 304, de 23 de mar&ccedil;o de 2017, publicado no&nbsp;<em>DOU</em>&nbsp;
                n. 58, de 24 de mar&ccedil;o de 2017 e &agrave; vista do constante no Processo Eletr&ocirc;nico n&ordm; {dados_ato['numero_sei']},</p>

                <p class="Texto_Justificado_Recuo_Primeira_Linha">&nbsp;</p>

                <p class="Texto_Justificado_Recuo_Primeira_Linha">R E S O L V E:</p>

                <p class="Texto_Justificado_Recuo_Primeira_Linha">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</p>

                <p class="Texto_Justificado_Recuo_Primeira_Linha" style="font-size:12pt;font-family:Calibri;text-indent:25mm;text-align:justify;word-wrap:normal;margin:6pt;">Designar, para mandato de 2 (dois) anos, {"o Professor do Magistério Superior" if dados_ato['genero_coordenador'] == "Masculino" else "a Professora do Magistério Superior"} {nome}
                para exercer a fun&ccedil;&atilde;o de&nbsp;{"Coordenador" if dados_ato['genero_coordenador'] == "Masculino" else "Coordenadora"} do
                {dados_ato['nome_coordenacao']} em {dados_ato['descricao_funcao'].title().replace(" Da ", " da ").replace(" Do ", " do ").replace(" De ", " de ").replace(" Di ", " di ").replace(" Du ", " du" )} (FCC).</p>

                <p class="Texto_Justificado_Recuo_Primeira_Linha">&nbsp;</p>

                <p class="Texto_Justificado_Recuo_Primeira_Linha">&nbsp;</p>

                <p class="Tabela_Texto_Centralizado">
                {decana_titular  if dados_ato['decana'] == "Decana titular" else decana_em_exercicio }
                </p>
                
                </body>
                </html>''')
        elif tipo_ato == "Dispensa de FCC":
            ato.write(f'''
                            <p class="Texto_Justificado" style="font-size:12pt;font-family:Calibri;text-align:justify;word-wrap:normal;text-indent:0;margin:6pt;">
                            Dispensa {"o Professor do Magistério Superior" if dados_ato['genero_coordenador'] == "Masculino" else "a Professora do Magistério Superior"} {nome} 
                            da função de {"Coordenador" if dados_ato['genero_coordenador'] == "Masculino" else "Coordenadora"} do {dados_ato['nome_coordenacao']} em 
                            {dados_ato['descricao_funcao'].title().replace(" Da ", " da ").replace(" Do ", " do ").replace(" De ", " de ").replace(" Di ", " di ").replace(" Du ", " du" )} (FCC).</p>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <p class="Texto_Justificado_Recuo_Primeira_Linha" style="font-size:12pt;font-family:Calibri;text-indent:25mm;text-align:justify;word-wrap:normal;margin:6pt;">A DECANA&nbsp;DE GEST&Atilde;O DE PESSOAS DA UNIVERSIDADE DE BRAS&Iacute;LIA, no uso de suas atribui&ccedil;&otilde;es legais, conferidas pelo Ato da Reitoria n&ordm; 72, publicado no DOU n. 13, de 20 de janeiro&nbsp;de 2021, se&ccedil;&atilde;o 2, p&aacute;gina 24, e de acordo com a compet&ecirc;ncia que lhe foi delegada por meio do Ato da Reitoria n. 304, de 23 de mar&ccedil;o de 2017, publicado no&nbsp;<em>DOU</em>&nbsp;
                n. 58, de 24 de mar&ccedil;o de 2017 e &agrave; vista do constante no Processo Eletr&ocirc;nico n&ordm; {dados_ato['numero_sei']},</p>

                <p class="Texto_Justificado_Recuo_Primeira_Linha">&nbsp;</p>

                <p class="Texto_Justificado_Recuo_Primeira_Linha">R E S O L V E:</p>

                <p class="Texto_Justificado_Recuo_Primeira_Linha">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</p>

                <p class="Texto_Justificado_Recuo_Primeira_Linha" style="font-size:12pt;font-family:Calibri;text-indent:25mm;text-align:justify;word-wrap:normal;margin:6pt;">Dispensar, por término de mandato, {"o Professor do Magistério Superior" if dados_ato['genero_coordenador'] == "Masculino" else "a Professora do Magistério Superior"} {nome}
                da fun&ccedil;&atilde;o de&nbsp;{"Coordenador" if dados_ato['genero_coordenador'] == "Masculino" else "Coordenadora"} do
                {dados_ato['nome_coordenacao']} em {dados_ato['descricao_funcao'].title().replace(" Da ", " da ").replace(" Do ", " do ").replace(" De ", " de ").replace(" Di ", " di ").replace(" Du ", " du" )} (FCC).</p>

                <p class="Texto_Justificado_Recuo_Primeira_Linha">&nbsp;</p>

                <p class="Texto_Justificado_Recuo_Primeira_Linha">&nbsp;</p>

                <p class="Tabela_Texto_Centralizado">
                {decana_titular  if dados_ato['decana'] == "Decana titular" else decana_em_exercicio }
                </p>
                
                </body>
                </html>''')    
        elif tipo_ato == "Substituição de FCC":
            ato.write(f'''
                            <p class="Texto_Justificado" style="font-size:12pt;font-family:Calibri;text-align:justify;word-wrap:normal;text-indent:0;margin:6pt;">
                            Designa {"o Professor do Magistério Superior" if dados_ato['genero_coordenador'] == "Masculino" else "a Professora do Magistério Superior"} {nome} 
                            para substituir {"o Coordenador" if dados_ato['genero_titular_substituido'] == "Masculino" else " a Coordenadora"} do {dados_ato['nome_coordenacao']} em 
                            {dados_ato['descricao_funcao'].title().replace(" Da ", " da ").replace(" Do ", " do ").replace(" De ", " de ").replace(" Di ", " di ").replace(" Du ", " du" )} (FCC).</p>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <p class="Texto_Justificado_Recuo_Primeira_Linha" style="font-size:12pt;font-family:Calibri;text-indent:25mm;text-align:justify;word-wrap:normal;margin:6pt;">A DECANA&nbsp;DE GEST&Atilde;O DE PESSOAS DA UNIVERSIDADE DE BRAS&Iacute;LIA, no uso de suas atribui&ccedil;&otilde;es legais, conferidas pelo Ato da Reitoria n&ordm; 72, publicado no DOU n. 13, de 20 de janeiro&nbsp;de 2021, se&ccedil;&atilde;o 2, p&aacute;gina 24, e de acordo com a compet&ecirc;ncia que lhe foi delegada por meio do Ato da Reitoria n. 304, de 23 de mar&ccedil;o de 2017, publicado no&nbsp;<em>DOU</em>&nbsp;
                n. 58, de 24 de mar&ccedil;o de 2017 e &agrave; vista do constante no Processo Eletr&ocirc;nico n&ordm; {dados_ato['numero_sei']},</p>

                <p class="Texto_Justificado_Recuo_Primeira_Linha">&nbsp;</p>

                <p class="Texto_Justificado_Recuo_Primeira_Linha">R E S O L V E:</p>

                <p class="Texto_Justificado_Recuo_Primeira_Linha">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</p>

                <p class="Texto_Justificado_Recuo_Primeira_Linha" style="font-size:12pt;font-family:Calibri;text-indent:25mm;text-align:justify;word-wrap:normal;margin:6pt;">Designar {"o Professor do Magistério Superior" if dados_ato['genero_coordenador'] == "Masculino" else "a Professora do Magistério Superior"} {nome}
                para substituir {"o Coordenador" if dados_ato['genero_titular_substituido'] == "Masculino" else " a Coordenadora"} do
                {dados_ato['nome_coordenacao'].title().replace(" Da ", " da ").replace(" Do ", " do ").replace(" De ", " de ").replace(" Di ", " di ").replace(" Du ", " du" )} 
                em {dados_ato['descricao_funcao'].title().replace(" Da ", " da ").replace(" Do ", " do ").replace(" De ", " de ").replace(" Di ", " di ").replace(" Du ", " du" )} 
                (FCC), durante o período de {dados_ato['motivo_substituicao'].title().replace(" Da ", " da ").replace(" Do ", " do ").replace(" De ", " de ").replace(" Di ", " di ").replace(" Du ", " du" )}, 
                de {funcoes.functions.data_convertida_br(str(dados_ato['inicio_substituicao']))} a {funcoes.functions.data_convertida_br(str(dados_ato['fim_substituicao']))}, 
                {'do titular' if dados_ato['genero_titular_substituido'] == "Masculino" else 'da titular'} {dados_ato['nome_titular_substituido'].title().replace(" Da ", " da ").replace(" Do ", " do ").replace(" De ", " de ").replace(" Di ", " di ").replace(" Du ", " du" )}.</p>

                <p class="Texto_Justificado_Recuo_Primeira_Linha">&nbsp;</p>

                <p class="Texto_Justificado_Recuo_Primeira_Linha">&nbsp;</p>

                <p class="Tabela_Texto_Centralizado">
                {decana_titular  if dados_ato['decana'] == "Decana titular" else decana_em_exercicio }
                </p>
                
                </body>
                </html>''')
            
    return [ato.name, ato]
