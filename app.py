from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from plots import load_prev_measures, load_percent_education, load_violin, load_region_graph 
from components import get_navbar
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
figs = [load_percent_education(), load_prev_measures(), load_violin(), load_region_graph()] 
tabs = [ dbc.Tab(
        dbc.Container(children=[
            dcc.Graph(
                id=str(i),
                figure=fig
            )
        ]), label=f'Graph {i + 1}'
    ) for i, fig in enumerate(figs) ]

app.layout = html.Div(children=[
    get_navbar(),
    dbc.Container(children=[
        html.H1(
            'Dashboard',
            className='page-title'
        ),
        # dcc.Graph(
        #     id='example-graph',
        #     figure=fig
        # )
        dbc.Tabs(tabs)
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)
