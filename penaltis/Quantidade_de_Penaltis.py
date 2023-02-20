# grafico de quantidade de penaltis

dados = df.values.tolist()
# função para separar os times em uma lista em ordem alfabetica


def list_nome_dos_paises():
    lista_nome_dos_paises = set()  # pegar um set vazio

    for coluna in dados:  # varredura do dataset de todas as disputas
        # adiciona os países sem repetir por conta do "Set()"
        lista_nome_dos_paises.add(coluna[0])
        lista_nome_dos_paises.add(coluna[1])  # mesma coisa da coluna 0.

    return list(lista_nome_dos_paises)  # retorna uma lista

# função para fazer a soma total de penaltes


# parametro com o nome do país em questão, ex. França
def lista_total_penalt_pais(nomedepais):
    qtdpenalts = 0  # definir o ponto de partida como 0

    for coluna in dados:  # varreção do dataset
        if coluna[0] == nomedepais:  # na coluna 0 comparamos se o país é o mesmo da linha da coluna[0]
            # somamos a quantidade de penaltis dele da coluna com a variável que foi definida acima(qtdpenalts)
            qtdpenalts += (coluna[78])

        if coluna[1] == nomedepais:  # mesma coisa da coluna 0 para somar
            qtdpenalts += (coluna[79])

    return qtdpenalts  # soma todos e retorna a quantidade de penaltis


def soma_penalts():
    paises = list_nome_dos_paises()  # chamamos a função list_nome_dos_paises
    lista_penalts = []  # depois definir duas listas vazias para guardar os valores
    lista_pais = []

    for pais in paises:  # percorrer toda a lista de paises, então adiciona cada país na função que busca os penaltis
        soma = lista_total_penalt_pais(pais)
        lista_penalts.append(soma)  # adiciona os penaltis em uma lista
        lista_pais.append(pais)

    return lista_penalts, lista_pais


def interacao(numerodepenaltis):  # definimos uma função para a interação
    numerodepenaltis = int(numerodepenaltis)
    pen = []  # criamos duas listas vazias para penaltis (pen) e países (pai)
    pai = []

    # duas variaveis para chamar a função de soma de penaltes e as suas listas
    listpenaltis, listpais = soma_penalts()
    cont = 0  # definimos um contador q começa em zero e toda vez que passar pelo looping somará mais 1

    for penaltis in listpenaltis:
        if penaltis == numerodepenaltis:
            # adicionará os países à lista 'pai' de acordo com o respectivo número do contador
            pai.append(listpais[cont])
            pen.append(penaltis)
        cont += 1
    return pen, pai  # retorna a lista pen (penaltis) e pai (países)


# duas variaveis para chamar a função de soma de penaltes e as suas listas
penalts, paises = soma_penalts()

# grafico
fig = px.bar(labels={'x': 'Países', 'y': 'Total de Penaltis'}, x=paises, y=penalts, width=1000,
             height=500, title='Total de penaltis por país', color_discrete_sequence=px.colors.qualitative.Vivid)
