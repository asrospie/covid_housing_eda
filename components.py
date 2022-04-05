import dash_bootstrap_components as dbc

def get_navbar():
    return dbc.NavbarSimple(
        children=[],
        brand='Covid Housing EDA', 
        brand_href='#',
        color='primary',
        dark=True,
    )