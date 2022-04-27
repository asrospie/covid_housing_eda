from dash import Dash, html, dcc, callback, Input, Output
from components import get_navbar, dashboard_page
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


app.layout = html.Div(children=[
    get_navbar(),
    dcc.Location(id='url', refresh=False),
    dbc.Container(id='page-content')
])

# ROUTER
@callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return dashboard_page()
    else:
        return dashboard_page()



if __name__ == '__main__':
    app.run_server(debug=True)
