# grafico de desempenho
df4 = df.values.tolist()  # transformando os valores do dataframe em matriz

# insere jogo em df_filtrado
# return df_filtrado


def pais_df(pais1, pais2):

    posicao_time1 = []  # Criando uma lista vazia de posições

    time1 = []
    time2 = []
    for i in df4:                # ta percorrendo as listas da lista principal e pegando os valores da primeira coluna
        time1.append(i[0])
    for i in df4:                # ta percorrendo as listas da lista principal e pegando os valores da segunda coluna
        time2.append(i[1])

    # for que percorre todo o dataframe, e pega os times e suas posições onde se encontra
    for i in range(len(time1)):
        if time1[i] == pais1:
            posicao_time1.append(i)
    for j in posicao_time1:
        if time2[j] == pais2:
            jogo_time1_time2 = j
            break  # pra acabar com o loop
    return jogo_time1_time2


def posicao(pais1, pais2):
    pais1 = pais1.upper()  # Deixar a string maiuscula
    pais2 = pais2.upper()

    posicao_p1_time1 = []
    posicao_p1_time2 = []
    posicao_p2_time1 = []
    posicao_p2_time2 = []
    time1 = []
    time2 = []
    for i in df4:
        time1.append(i[0])
    for i in df4:
        time2.append(i[1])

    for i in range(len(time1)):
        if time1[i] == pais1:
            posicao_p1_time1.append(i)
    for i in range(len(time2)):
        if time2[i] == pais1:
            posicao_p1_time2.append(i)
    for i in range(len(time1)):
        if time1[i] == pais2:
            posicao_p2_time1.append(i)
    for i in range(len(time2)):
        if time2[i] == pais2:
            posicao_p2_time2.append(i)

    posicoes_pais1 = sorted(posicao_p1_time1 + posicao_p1_time2)
    posicoes_pais2 = sorted(posicao_p2_time1 + posicao_p2_time2)

    return posicoes_pais1, posicoes_pais2


def posse_bola(pais1, pais2):
    pais1 = pais1.upper()  # Deixar a string maiuscula
    pais2 = pais2.upper()

    # posicao
    pos_pais1, pos_pais2 = posicao(pais1, pais2)

    posse_pais1 = []  # posses em si
    posse_pais2 = []

    possession_team1 = []
    for i in df4:
        possession_team1.append(i[2])
    possession_team2 = []
    for i in df4:
        possession_team2.append(i[3])

    for i in pos_pais1:  # pegando as posses do time
        if i in pos_pais1:
            # entra no valor 0 e percorre até o ultimo valor. Por isso usamos o [:-1]
            posse_pais1.append(int(possession_team1[i][:-1]))
        if i in pos_pais1:
            posse_pais1.append(int(possession_team2[i][:-1]))
    for i in pos_pais2:
        if i in pos_pais2:
            posse_pais2.append(int(possession_team1[i][:-1]))
        if i in pos_pais2:
            posse_pais2.append(int(possession_team2[i][:-1]))

    return posse_pais1, posse_pais2, pais1, pais2


def gols(pais1, pais2):  # gols e a posição
    pais1 = pais1.upper()  # Deixar a string maiuscula
    pais2 = pais2.upper()

    # posicao
    gols_pais1, gols_pais2 = posicao(pais1, pais2)

    gol_pais1 = []  # gols em si
    gol_pais2 = []

    number_of_goals_team1 = []
    for i in df4:
        number_of_goals_team1.append(i[5])
    number_of_goals_team2 = []
    for i in df4:
        number_of_goals_team2.append(i[6])

    for i in gols_pais1:  # pegando os gols
        if i in gols_pais1:
            gol_pais1.append(int(number_of_goals_team1[i]))
        if i in gols_pais1:
            gol_pais1.append(int(number_of_goals_team2[i]))
    for i in gols_pais2:
        if i in gols_pais2:
            gol_pais2.append(int(number_of_goals_team1[i]))
        if i in gols_pais2:
            gol_pais2.append(int(number_of_goals_team2[i]))

    return gol_pais1, gol_pais2, pais1, pais2


# Grafico dos gols
# comparar tamanho das listas, plora
def grafico_gols(pais1, pais2):
    gol_p1, gol_p2, time1, time2 = gols(pais1, pais2)

    if len(gol_p1) > len(gol_p2):
        indice = len(gol_p1)
    else:
        indice = len(gol_p2)

    jogos = []
    for i in range(indice):
        jogos.append(f'Jogo {i}')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=jogos,
        y=gol_p1,
        name='GOL ' + time1,
        marker_color='red'
    ))
    fig.add_trace(go.Bar(
        x=jogos,
        y=gol_p2,
        name='GOL ' + time2,
        marker_color='blue'
    ))

    fig.update_layout(barmode='group', xaxis_tickangle=-45,
                      title=f'Desempenho dos gols {pais1} e {pais2}')

    return fig


# fig.show()

# Grafico do posse de bola
def grafico_posse(pais1, pais2):

    gol_p1, gol_p2, time1, time2 = gols(pais1, pais2)

    if len(gol_p1) > len(gol_p2):
        indice = len(gol_p1)
    else:
        indice = len(gol_p2)

    posse_p1, posse_p2, pais1, pais2 = posse_bola(pais1, pais2)
    jogos = []
    for i in range(indice):
        jogos.append(f'Jogo {i}')

    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        x=jogos,
        y=posse_p1,
        name='Posse de Bola ' + pais1,
        marker_color='indianred'
    ))
    fig2.add_trace(go.Bar(
        x=jogos,
        y=posse_p2,
        name='Posse de bola ' + pais2,
        marker_color='lightsalmon'
    ))

    fig2.update_layout(barmode='group', xaxis_tickangle=-
                       45,  title=' Posse de bola ')

    return fig2


fig = grafico_gols('ARGENTINA', 'FRANCE')
fig2 = grafico_posse('ARGENTINA', 'FRANCE')

time1 = []
time2 = []
partidas = []

for i in df4:                # ta percorrendo as listas da lista principal e pegando os valores da primeira coluna
    time1.append(i[0])
for i in df4:                # ta percorrendo as listas da lista principal e pegando os valores da segunda coluna
    time2.append(i[1])

for n1, n2 in zip(time1, time2):  # for para juntar as listas de times1 e times2
    # adicionando os times e separando por ' X '
    partidas.append((str(n1) + ' x '+str(n2)))
