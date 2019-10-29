import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.offline as pyo
import plotly_express as pyx
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app = dash.Dash()
app.layout = html.Div([
    html.Div([
        html.Div([
            html.H3('Grafica 1'),
            dcc.Graph(id='g1', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="six columns"),

        html.Div([
            html.H3('Grafica 2'),
            dcc.Graph(id='g2', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="six columns"),
        html.Div([
            html.H3('Grafica 3'),
            dcc.Graph(id='g3', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="six columns"),
        html.Div([
            html.H3('Grafica 4'),
            dcc.Graph(id='g4', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="six columns"),
    ], className="row")
])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(debug=True)


if __name__ == '__main__':
    app.run_server(debug=True)

    # input
    data = pd.read_csv("sample_semanai.csv")
