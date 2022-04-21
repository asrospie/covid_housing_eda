import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def load_percent_education():
    df = pd.read_csv('data/covid_housing_latest.csv')
    ch_df = df.drop(['survey_producer', 'survey_link', 'last_updated', 'row_id'], axis=1)
    fin_df = ch_df.drop(['region', 'country'], axis=1)
    
    area_df = fin_df[['indicator', 'indicator_val', 'urban_rural']]

    # Statment #12
    area_df = area_df[area_df['indicator'].str.contains('Demo_educ')]

    area_pt = pd.pivot_table(area_df, values=['indicator_val'], index=['urban_rural', 'indicator'], aggfunc=np.mean).reset_index()
    educ_mapper = {'Demo_educ1': 'No Education',
                'Demo_educ2': 'Any Primary',
                'Demo_educ3': 'Any Secondary',
                'Demo_educ4': 'Any Post Secondary'}
    area_pt['indicator'] = area_pt['indicator'].apply(lambda x: educ_mapper[x])

    return px.bar(area_pt, x='urban_rural', y='indicator_val', color='indicator', barmode="group", title='Percentage of Respondents per Education Level in Differing Areas')

def load_prev_measures():
    df = pd.read_csv('data/covid_housing_latest.csv')

    gdp_df = df[['indicator', 'indicator_val', 'GDP_pc']]
    gdp_df = gdp_df.rename(columns={'indicator_val': 'Preventative Measure', 'GDP_pc': 'GDP / Capita'})
    gdp_df = gdp_df[gdp_df['indicator'] == 'Prev_AP_other']

    return px.density_heatmap(gdp_df, x='GDP / Capita', y='Preventative Measure', title='Distribution of Preventative Measures per GDP / Capita')

def load_violin():
    df = pd.read_csv('data/covid_housing_latest.csv')

    vac_df = df[['indicator_val', 'indicator', 'income_group']]
    vac_df = vac_df[(vac_df['indicator'] == 'Vac_done') | (vac_df['indicator'] == 'Know_any')]
    vac_df['indicator'] = vac_df['indicator'].apply(lambda x: 'Known Gov. Intv.' if x == 'Know_any' else 'Vaccinated')

    return px.violin(vac_df, x='income_group', y='indicator_val', color='indicator', title='% of Respondents Per Income Group Vaccinated and Know of any Gov. Intervention')

def load_region_graph():
    df = pd.read_csv('data/covid_housing_latest.csv')

    frame_count = df[['region_code', 'region']]\
                .groupby('region_code')\
                .agg({'region' : 'count'})\
                .reset_index()
    frame_count.rename(columns={"region": "region_count"})
    frame_plot = df[['region', 'region_code']]
    frame_plot_graph = frame_count.join(frame_plot.set_index('region_code'),\
                                        on='region_code', how='inner', lsuffix='_count')\
                                        .sort_values(by='region_count', ascending=False)

    return px.histogram(frame_plot_graph, x='region_code', color='region', title='# of Surveyed People per Region')