import pandas as pd
import numpy as np
import plotly.express as px

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