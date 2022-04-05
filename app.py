from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from plots import load_percent_education
from components import get_navbar
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
figs = [load_percent_education(), load_percent_education()] 
tabs = [ dbc.Tab(
        dbc.Container(children=[
            dcc.Graph(
                id=str(i),
                figure=fig
            )
        ]), label='Test'
    ) for i, fig in enumerate(figs) ]

app.layout = html.Div(children=[
    get_navbar(),
    dbc.Container(children=[
        html.H1(
            'Test Graph',
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
