import pandas as pd



def medals_total(df):
    medals=df
    medals=medals.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold', ascending=False).reset_index()
    medals['Total'] = medals['Gold'] + medals['Silver'] + medals['Bronze']
    return medals