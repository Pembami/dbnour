import pandas as pd
import streamlit as st

def dataprocessing(df):
    """
    Convert the date column in the given dataframe to datetime format.
    Convert the observations column in the given dataframe to string format.
    
    Parameters:
    - df: pandas DataFrame object containing the data to be processed
    
    Returns:
    - df: pandas DataFrame object with the modified date and observations columns
    """
    
    # convert date column to datetime
    df.Date = pd.to_datetime(df.Date)
    
    # convert observations column to string
    df.Observations = df.Observations.astype(str)
    
     # convert année column to int
    df['Année'] =  df['Année'].astype(int)
    
    return df

def get_metrics(df, column,func, year):
    df_filter = df[df['année']==year]
    last_year = year -1
    
    if last_year in df['Année']:
        st.metric(column,round(df[df['Année']==year][column].func(),1))
    else:
        st.metric(column,round(df[df['Année']==year][column].func(),1))
    
    