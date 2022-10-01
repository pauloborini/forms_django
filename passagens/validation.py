# Verifica se origem e destino são iguais
def origem_destino_iguais(origem, destino, lista_de_erros):
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destino não podem ser iguais'


# Verifica se algum campo tem número
def campo_tem_numero(valor_campo, nome_campo, lista_de_erros):
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua números nesse campo'


# Verifica os campos de data
def data_volta_anterior_data_ida(data_ida, data_volta, lista_de_erros):
    if data_ida > data_volta:
        lista_de_erros['data_volta'] = 'Data de volta não pode ser anterior a data de ida'


# Verifica data da viagem com a pesquisa
def data_ida_anterior_hoje(data_ida, data_pesquisa, lista_de_erros):
    if data_ida < data_pesquisa:
        lista_de_erros['data_ida'] = 'Data de ida não é válida, pois já passou'
