
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import plotly.graph_objects as go
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = JupyterDash(__name__)

fig = px.funnel()

app.layout = html.Div(children=[
    html.H1(children='Dataset da Copa do Mundo 2022'),

    # Tabela da razao de gols
    dcc.Dropdown(parametros, value=[
                 "Fase de grupos"], id='dropdown', multi=True),
    html.Div(id='dd-output-container'),

    dcc.Graph(
        id='razao_gols',
        figure=fig
    ),

    # tabela da quantidade de penaltis
    dcc.Dropdown([0, 1, 2, 4], value="1", id="lista-penaltis"),  # botão
    dcc.Graph(
        id='grafico',  # grafico
        figure=fig),


    # Tabela de prevencao de gols e gols levados
    html.H1(children='Gráfico Prevenção de Gol e Gols levados'),

    # Criação do Botão para interação com o usuártio (multi é para poder escolher mais de um pais ao mesmo tempo)
    dcc.Dropdown(opcoes, value=(), id='Botão', multi=True),
    # lembrando que o valor do gráfico começa vazio

    dcc.Graph(
        id='gráfico_paises',
        figure=graf)


])

# dropwdown da razao de gols


@app.callback(
    Output('razao_gols', 'figure'),
    Input('dropdown', 'value')
)
def update_output(value):
    if value == []:
        return px.funnel()

    indices = []
    for i in value:
        indice = parametros.index(i)
        indices.append(indice)

    fase = []
    for i in indices:
        fase += fases_copa[i]

    times = selecoes(fase)
    razoes_times = razoes_gols_selecoes(fase, times)
    lista1 = zip(times, razoes_times)
    total = list(lista1)
    total = ordenar_lista(total)

    paises = []
    razoes = []
    for i in total:
        paises.append(i[0])
        razoes.append(i[1])

    fig = px.funnel(labels={"x": "Razões", "y": "Países"}, x=razoes, y=paises, width=1400,
                    height=900, title="Razões entre gols feitos e gols tomados por seleções")

    return fig

# dropdown da quantidade de penaltis


@app.callback(
    Output('grafico', 'figure'),
    Input("lista-penaltis", "value")
)
# função pra fazer a interação funcionar
def update_graph(value):  # criamos uma função que chama a função interação
    value = int(value)
    # duas variaveis para chamar as duas listas da função interacao
    penalts, paises = interacao(value)

    fig1 = px.bar(labels={'x': 'Países', 'y': 'Total de Penaltis'}, x=paises, y=penalts,
                  title='Total de penaltis por país', color_discrete_sequence=px.colors.qualitative.Vivid)
    return fig1

# dropwdown de prevencao de gols e gols levados


@app.callback(
    Output('gráfico_paises', 'figure'),
    Input('Botão', 'value')
)
def update_output(value):
    if value == []:  # se o valor do dropdown estiver vazio, o dash irá mostrar o gráfico original com os 32 países

        graf = go.Figure(data=[go.Bar(name='Defesas de gol', x=times, y=defesas), go.Bar(
            name='Gols levados', x=times, y=gols)])
        return graf

    else:
        # essa é a lista comprehension, que faz a função de um "for x in enumerate(times)" com a condição do "if x in value" --
        # -- com ela nós adicionamos o termo i, que será usado para filtrar os gols, defesas e os times --
        # -- essa lista comprehension vai verificar se o time que está no valor (no caso todos os times selecionados pelo usuário) também está na lista --
        # -- de times da copa, e vai enumerá-los com a função enumerate(), depois vai atribuir o número do time ao termo 'i'
        index = [i for i, x in enumerate(times) if x in value]
        times_filtrados = [times[i] for i in index]
        defesas_filtradas = [defesas[i] for i in index]
        gols_filtrados = [gols[i] for i in index]

        # gráfico com os times, gols e defesas já filtrados
        graf = go.Figure(data=[go.Bar(name='Defesas de gol', x=times_filtrados, y=defesas_filtradas), go.Bar(
            name='Gols levados', x=times_filtrados, y=gols_filtrados)])
        return graf


if __name__ == '__main__':
    app.run_server(debug=True)
