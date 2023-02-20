# grafico de cartoes amarelos e vermelhos
# leitura do banco de dados em csv
df = pd.read_csv(
    "https://github.com/Marycota/projeto_apc/raw/main/Fifa_world_cup_matches.csv")
Data = df.values.tolist()  # variavel para ler o grafico


def times() -> list:  # função para separar os times em uma lista em ordem alfabetica
    times = []  # lista para colocar os times

    for i in Data:  # for para juntar os times por colunas
        times.append(i[0])  # adicionar lista dos times 1
        times.append(i[1])  # adicionar lista dos times 2
    # lista para colocar os times sem repetições, total são 32
    lista_times = set(times)
    # lista em ordem alfabetica #a função sorted ordena numeros do menor para o maior e as letras em ordem alfabetica(a-z)
    lista_total = sorted(lista_times)
    return lista_total

# Função que retorna as posições de um time específico nas duas colunas no csv


def posicao_time(opcoes_lista_times):
    posicao_p1_time = []  # lista para guarda a posição doa coluna 0
    posicao_p2_time = []  # lista para guarda a posição doa coluna 1

    time1 = []  # lista de times da coluna 0
    time2 = []  # lista de times da coluna 0

    for i in Data:
        time1.append(i[0])  # lista de times coluna 0
        time2.append(i[1])  # lista de times coluna 1

    for i in range(len(time1)):  # varrer as posições em que o time se encontra em cada lista
        if time1[i] == opcoes_lista_times:  # adicionar a posição 1 do time em uma lista
            posicao_p1_time.append(i)
        if time2[i] == opcoes_lista_times:  # adicionar a posição 2 do time em uma lista
            posicao_p2_time.append(i)

    # lista com as posições do time nas duas colunas em ordem crescente
    posicoes_time = sorted(posicao_p1_time + posicao_p2_time)
    return posicoes_time

# Função que retorna as partidas de um time (time1 x time2)


def partidas(opcoes_lista_times):
    times1 = []  # variavel para receber os times1 por partidas
    times2 = []  # variavel para receber os times2 por partidas
    partidas = []  # variavel para receber as partidas (time1 x time2)

    posicao_partidas = posicao_time(opcoes_lista_times)
    posicao_cada_partida = []  # lista com todas as posições

    for i in Data:  # for para juntar os times por colunas
        times1.append(str(i[0]))  # lista dos times 1
        times2.append(str(i[1]))  # lista dos times 2

    for n1, n2 in zip(times1, times2):  # for para juntar as listas de times1 e times2
        # adicionando os times e separando por ' X '
        partidas.append((str(n1)+' x '+str(n2)))

    for i in partidas:  # for para varrer a lista de partidas
        for i in posicao_partidas:  # for para varrer a lista de posições
            # adicionar as posições em que o time aparece nas partidas em uma lista das suas partidas
            posicao_cada_partida.append(partidas[i])
        break  # parar o for quando a lista de posições acabar
    return posicao_cada_partida  # retorna as partidas do time

# Função que retorna a soma dos cartões amarelos de uma partida


def cartao_amarelo(opcoes_lista_times):
    cartao_amarelo1 = []  # Variavel de cartões amarelos time 1
    cartao_amarelo2 = []  # Variavel de cartões amarelos time 2
    soma_ca = []  # variavel para a soma

    posicao_partidas = posicao_time(opcoes_lista_times)
    posicao_ca = []  # lista com todas as posições

    for i in Data:
        cartao_amarelo1.append(int(i[56]))  # lista de cartões amarelos time 1
        cartao_amarelo2.append(int(i[57]))  # lista de cartões amarelos time 2

    # Percorre o Array a enumerando suas posições
    for x, y in enumerate(cartao_amarelo1):
        # somando elemento do array a com o elemento de mesma posição no array cartao_amarelo2
        soma_ca.append(y+cartao_amarelo2[x])

    for i in soma_ca:  # for para varrer a lista de soma de soma dos cartões amarelos
        for i in posicao_partidas:  # for para varrer a lista de posições das partidas do time
            # adicionar os valores dos cartões amarelos de cada partida do time
            posicao_ca.append(soma_ca[i])
        break
    return posicao_ca

# Função que retorna a soma dos cartões vermelhos de uma partida


def cartao_vermelho(opcoes_lista_times):
    cartao_vermelho1 = []  # Variavel de cartões vermelhos time 1
    cartao_vermelho2 = []  # Variavel de cartões vermelhos time 2
    soma_cv = []  # variavel para a soma

    posicao_partidas = posicao_time(opcoes_lista_times)
    posicao_cv = []  # lista com todas as posições

    for i in Data:
        # lista de cartões vermelhos time 1
        cartao_vermelho1.append(int(i[58]))
        # lista de cartões vermelhos time 2
        cartao_vermelho2.append(int(i[59]))

    # Percorre o Array a enumerando suas posições
    for x, y in enumerate(cartao_vermelho1):
        # somando elemento do array a com o elemento de mesma posição no array cartao_vermelho2
        soma_cv.append(y+cartao_vermelho2[x])

    for i in soma_cv:  # for para varrer a lista de soma de soma dos cartões vermelhos
        for i in posicao_partidas:  # for para varrer a lista de posições das partidas do time
            # adicionar os valores dos cartões vermelhos de cada partida do time
            posicao_cv.append(soma_cv[i])
        break
    return posicao_cv


opcoes_lista_times = times()  # variavel para dar a lista de times no botão

# variavel para substituir a função no dicionario
partidas = partidas(opcoes_lista_times)
# variavel para substituir a função no dicionario
ca = cartao_amarelo(opcoes_lista_times)
# variavel para substituir a função no dicionario
cv = cartao_vermelho(opcoes_lista_times)
legenda_cv_ca = {"Partidas": partidas,  # criando a legenda no grafico com as novas variaveis do dicionario
                 # criando a legenda no grafico com as novas variaveis do dicionario
                 "Cartões vermelhos": cv,
                 # criando a legenda no grafico com as novas variaveis do dicionario
                 "Cartôes amarelos": ca
                 }

legenda_completa = pd.DataFrame(legenda_cv_ca)  # dicionario para a legenda

# grafico:
fig = px.bar(legenda_completa, x='Partidas', y=['Cartôes amarelos', 'Cartões vermelhos'], title=(
    f'Cartões Vermelhos e Amarelos por partidas'), labels={'x': 'Partidas', 'y': 'Total'}, color_discrete_sequence=["gold", "firebrick"],)
# esconder titulo da legenda do grafico
fig.update_layout(legend_title_text='')

opcoes_lista_times = times()  # variavel para dar a lista de times no botão
