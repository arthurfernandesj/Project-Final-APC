# grafico de prevencao de gols
import plotly.graph_objects as go


# lista com os valores numéricos de cada jogo
df = pd.read_csv(
    "https://github.com/Marycota/projeto_apc/raw/main/Fifa_world_cup_matches.csv")
df2 = df.values.tolist()

# função cria uma lista com todos os times


def nomes_times():
    nome_times = set()
    for coluna in df2:
        nome_times.add(coluna[0])
        nome_times.add(coluna[1])
    return nome_times


# função cria uma lista com todas as defesas(colna 80, 81)
def defesas_times(time):
    defesas = 0
    for coluna in df2:
        if coluna[0] == time:
            defesas += (coluna[80])
        if coluna[1] == time:
            defesas += (coluna[81])
    return defesas

# função junta todos os países com suas respectivas desesas


def total_defesas():
    paises = nomes_times()
    lista_def = []
    lista_pais = []
    for time in paises:
        soma = defesas_times(time)
        lista_def.append(soma)
        lista_pais.append(time)
    return lista_def, lista_pais


# função cria uma lista com os gols sofridos por cada time (coluna 6, 5 )
# o correto seria fazer a coluna 5 antes da 6, mas como são os gols levados elas são invertidas
def gols_levados_times(time):
    gols_levados = 0
    for coluna in df2:
        if coluna[0] == time:
            gols_levados += (coluna[6])
        if coluna[1] == time:
            gols_levados += (coluna[5])
    return gols_levados

# função junta todos os países com os respectivos gols levados


def total_gols():
    paises = nomes_times()
    lista_gols = []
    lista_pais = []
    for time in paises:
        soma = gols_levados_times(time)
        lista_gols.append(soma)
        lista_pais.append(time)
    return lista_gols, lista_pais


# Aqui nós estamos atribuindo o valor que as funções nos dão a gols, times e defesas
gols, times = total_gols()
# __________________________________________________________________________________
defesas, times = total_defesas()

graf = go.Figure(data=[go.Bar(name='Defesas de gol', x=times, y=defesas), go.Bar(
    name='Gols levados', x=times, y=gols)])  # Esse é o gráfico com todos os países da Copa

# Aqui nós estamos criando esse termo "opções" que vai receber uma lista com o nome de todos os países da copa
opções = list(nomes_times())
