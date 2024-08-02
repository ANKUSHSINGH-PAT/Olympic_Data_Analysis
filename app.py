import streamlit as st
import pandas as pd
import preprocessor
import helper

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')


df=preprocessor.preprocess(df,region_df)

option = st.sidebar.selectbox(
    '---------SELECT AN OPTION---------',
    ['Medal Tally', 'TotalMedals']  # Add other options if needed
)

if option=='Medal Tally':
    st.dataframe(df)



if option=='TotalMedals':
    medal_tally=helper.medals_total(df)
    st.dataframe(medal_tally)