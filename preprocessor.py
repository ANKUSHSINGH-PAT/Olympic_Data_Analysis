import pandas as pd
import numpy as np

df=pd.read_csv('athlete_events.csv')
region_df=pd.read_csv('noc_regions.csv')

def preprocess(df,region_df):
    # filtering for summer olympics
    df = df[df['Season'] == 'Summer']
    # merge with region_df
    df = df.merge(region_df, on='NOC', how='left')
    # dropping duplicates
    df.drop_duplicates(inplace=True)

    #Filling Empty Values
    mean_age=df['Age'].mean()
    mean_height=df['Height'].mean()
    mean_weight=df['Weight'].mean()

    df['Age']=df['Age'].fillna(mean_age)
    df['Height']=df['Height'].fillna(mean_height)
    df['Weight']=df['Weight'].fillna(mean_weight)

    df=pd.DataFrame(df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal']))

    # one hot encoding medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df