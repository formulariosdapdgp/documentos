import datetime

tipo_de_documento = ["", "ATOS DA REITORIA", "ATOS DO DGP", "NOTA TÉCNICA"]

atos_reitoria = ["", "Nomeação de CD", "Exoneração de CD", "Substitução de CD", "Recondução de CD", "Designação de FG", "Dispensa de FG"]

atos_dgp = ["", "Designação de FCC", "Dispensa de FCC", "Substitução de FCC", "Substitução de FG"]

lista_fgs = ["", "FG-01", "FG-02", "FG-03"]

lista_cds = ["", "CD-01", "CD-02", "CD-03", "CD-04"]

lista_fcc = ["", "FCC", "Função não remunerada"]

lista_nota_tecnica = ["", "PPP"]

decana_titular = "Maria do Socorro Mendes Gomes<br>Decana de Gestão de Pessoas"

decana_em_exercicio = "Sheila Perla Maria de Andrade da Silva<br>Decana de Gestão de Pessoas em exercício"

modelo_ato_em_branco = {"Número SEI do modelo de ato": 9449709}

# capturando ano
data_atual = datetime.date.today()
ano_atual = data_atual.year