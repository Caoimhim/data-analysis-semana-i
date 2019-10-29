import dash
import dash_core_components as dcc
import dash_html_components as html

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

app = dash.Dash()
app.layout = html.Div([
    html.Div([
        html.Div([
            html.H3('Histograma'),
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
        ])

    ])])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(debug=True)
