"""
Gráfico da razão de gols feitos por gols tomados pelas seleções
"""

import pandas as pd
import plotly.express as px
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

df = pd.read_csv(
    "https://raw.githubusercontent.com/Marycota/projeto_apc/main/Fifa_world_cup_matches.csv")
valores = df.values.tolist()

"""
Criação de funções
"""


def selecoes(valores: list) -> list:
    """
    Args:
      valores: list com os dados do dataset da copa do mundo
    Return:
      selecoes: list com todas as seleções que jogaram a copa do mundo
    """
    times = []
    for jogos in valores:
        times.append(jogos[0])
        times.append(jogos[1])
    set_times = set(times)
    selecoes = list(set_times)
    return selecoes


def razoes_gols(valores: list, team: str) -> float:
    """
    Args:
        valores: list com os dados do dataset da copa do mundo
        team: string com o nome de uma selecao
    Return:
        razao: float com a razao entre gols feitos e tomados por essa selecao
    """
    gols_feitos = 0
    gols_tomados = 0
    time1 = []
    time2 = []
    gols1 = []
    gols2 = []
    for jogos in valores:
        time1.append(jogos[0])  # índice das seleções da primeira coluna
        time2.append(jogos[1])  # índice das seleções da segunda coluna
        gols1.append(jogos[5])  # índice dos gols da primeira seleção
        gols2.append(jogos[6])  # "    "     " "  segunda seleção
    for i in range(len(time1)):
        if time1[i] == team:
            gols_feitos += gols1[i]
            gols_tomados += gols2[i]
        elif time2[i] == team:
            gols_feitos += gols2[i]
            gols_tomados += gols1[i]
    if gols_tomados == 0:
        return gols_feitos
    razao = gols_feitos / gols_tomados
    return razao


def razoes_gols_selecoes(valores: list, selecoes: list) -> list:
    """
    Args:
        valores: list com os dados do dataset da copa do mundo
        selecoes: lista com os nomes de todas as selecoes
    Return:
        razoes: lista com a razao entre gols feitos e tomados das selecoes contidas na lista informada
    """
    razoes = []
    for selecao in selecoes:
        razoes.append(razoes_gols(valores, selecao))
    return razoes


def ordenar_lista(lista: list) -> list:
    """
    Função para ordenar a lista com as tuplas contendo as seleções e suas razões de gols
    """
    tamanho = len(lista)
    for i in range(tamanho):
        for j in range(i, tamanho):
            if lista[i][1] > lista[j][1]:
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar
    return lista


"""
Quantidade de jogos por grupo: 6
Quantidade de grupos: 8
Quantidade de jogos total na fase de grupos: 6*8 = 48
"""
fase_grupos = valores[0:48]
oitavas = valores[48:56]  # 48 + 8 jogos das oitavas de final = 56
quartas = valores[56:60]  # 56 + 4 jogos das quartas de final = 60
semi = valores[60:62]  # 60 + 2 jogos da semi final
terceiro_lugar = valores[62:63]  # 62 + 1 jogo da disputa de terceiro colocado
final = valores[63:64]  # último jogo da copa do mundo

fases_copa = [
    fase_grupos,
    oitavas,
    quartas,
    semi,
    terceiro_lugar,
    final
]

parametros = ["Fase de grupos",
              "Oitavas de final",
              "Quartas de final",
              "Semi finais",
              "Disputa de terceiro lugar",
              "Final"
              ]
