import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.offline as pyo
import plotly_express as pyx
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
data = pd.read_csv("sample_semanai.csv")

data = data.drop_duplicates().iloc[:]
data_ham = data[data["Tipo de grupo"] == "Alimentos"]
ham_hist = pyx.histogram(data_ham, x="Clave platillo")

data_bebidas = data[data["Tipo de grupo"] == "Bebidas"]
bebidas_hist = pyx.histogram(data_bebidas, x="Clave platillo")
data_stacked_day = data.groupby(['Día', 'Grupo'])['Cantidad'].sum(
).reset_index().sort_values(['Día', 'Cantidad'], ascending=False)
data_stacked_group = data.groupby(['Clave platillo', 'Grupo'])['Cantidad'].sum(
).reset_index().sort_values(['Clave platillo', 'Cantidad'], ascending=False)

app = dash.Dash()
app.layout = html.Div([
    html.Div([
        html.Div([
            html.H3('Histograma alimentos'),
            dcc.Graph(
                id='hist_alimentos',
                figure={
                    'data': [
                        {
                            'x': data_ham['Clave platillo'],
                            #'text': data_ham['Platillo'],
                            #'customdata': df['storenum'],
                            #'name': 'Open Date',
                            'type': 'histogram'
                        },
                    ], 'layout': {}
                }
            )]),

        html.Div([
            html.H3('Histograma de Bebidas'),
            dcc.Graph(
                id='hist_bebidas',
                figure={
                    'data': [
                        {
                            'x': data_bebidas['Clave platillo'],
                            'type': 'histogram'
                        },
                    ],
                    'layout':{}
                }
            )
        ]),

        html.Div([
            html.H3('Stacked graph de días'),
            dcc.Graph(
                id='stacked_days',
                figure={
                    'data': [
                        {
                            'x': data_stacked_day['Día'],
                            'y': data_stacked_day['Cantidad'],
                            'color': data_stacked_day['Grupo'].to_list(),
                            'type': 'bar',
                        },
                    ],
                    'layout':{}
                }
            )
        ]),

        html.Div([
            html.H3('Stacked graph de ventas'),
            dcc.Graph(
                id='stacked_products',
                figure={
                    'data': [
                        {
                            'x': data_stacked_group['Grupo'],
                            'y': data_stacked_group['Cantidad'],
                            'color': data_stacked_group['Clave platillo'],
                            'type': 'bar',
                        },
                    ],
                    'layout':{}
                }
            )
        ])

    ])])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(debug=True)
