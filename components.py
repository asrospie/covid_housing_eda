from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd
from plots import load_prev_measures, load_percent_education, load_violin, load_region_graph, load_income_distribution
import dash_bootstrap_components as dbc

def get_navbar():
    return dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink('Home', href='/')),
            dbc.NavItem(dbc.NavLink('Correlations', href='/correlations')),
        ],
        brand='Covid Housing EDA', 
        brand_href='#',
        color='primary',
        dark=True,
    )

def dashboard_page():
    hypothesis = [
        'Due to the lower income status of many of these countries I expect to see a higher level of respondents in the “No Education” and the “Any Primary” categories in the National perspective. I would expect to see the same trend in the Rural perspective, with a more balanced response in the Urban perspective. ',
        'We would\'ve expected that an increase in GDP/Capita would be highly correlated to a larger amount of preventative measures.',
        'Our hypothesis is that the higher the income, the greater the percentage of individuals who both know about the Government Intervention and the Vaccination rates. ',
        'I would\'ve expected that Europe (ECA) would have the highest surveying rate, followed by the Middle East (MNA), Latin America (LAC), East Asia (EAP), South Asia (SAR), and finally Sub-Saharan Africa (SSA) at the end.',
        'The assumption that would be made here would be that areas with lower income are going to be reported more on the high income would be a smaller portion of the statistic. This would be due to the majority of people in various countries residing at the middle of the income distribution plot.'
    ]
    conclusions = [
        'The final result of having higher responses in the Secondary and Post Secondary was a bit surprising to me. My hypothesis of having lower responses of “No Education” and “Any Primary” and greater levels in the “Any Post Secondary” responses in the Urban perspective when compared to Rural was correct. This could be correct perspectives, or it could be incomplete Data as the surveys were all done by phone and access to cell phone or land line phones could skew the Data.',
        'While the predicted observation was proven by this data, we also saw how skewed the distribution of GDP per capita is in this dataset.',
        'This Data mostly reinforces the hypothesis in regard to the Vaccinated response. I was surprised to see a lower response of known Government Intervention in the High Income response group.',
        'While we don\'t know what proportion of the populations was represented by the survey\'s sample size, it was incredibly surprising to see SSA (a lower-developed region) significantly higher than ECA. Additionally, seeing SAR much lower than the rest of the groups didn\'t make sense considering how large of a population base is present.',
        'The summary supports the hypothesis by High Income representing roughly 5% of the total data while the others make up nearly equally.'
    ]

    figs = [load_percent_education(), load_prev_measures(), load_violin(), load_region_graph(), load_income_distribution()] 

    tabs = [ dbc.Tab(
        dbc.Container(children=[
            html.H2('Hypothesis'),
            html.Div(hypothesis[i]),
            dcc.Graph(
                id=str(i),
                figure=fig[1]
            ),
            html.H2('Conclusion'),
            html.Div(conclusions[i])
        ]), label=fig[0]
    ) for i, fig in enumerate(figs) ]

    return html.Div(children=[
        html.H1(
            'Dashboard',
            className='page-title'
        ),
        dbc.Tabs(tabs)
    ]) 

def correlations_page():
    return html.Div(children=[
        html.H1('Correlations', className='page-title'),
        html.Div('More coming soon I promise...')
    ])