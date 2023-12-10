import pandas as pd
import streamlit as st
from dataprocessing import dataprocessing
import numpy as np

df_raw = pd.read_excel('./data/IndicateurCondi.xlsm', header = 4)
df = dataprocessing(df_raw)

# Define a Streamlit layout for data reporting
st.title('Data Reporting')
st.header('Overview')
st.write('This report provides an overview of the dataset.')

# Display the first few records of the DataFrame
st.subheader('Data Preview:')
st.dataframe(df.head())

# Show summary statistics
st.subheader('Summary Statistics:')
st.write(df.describe())

# Create an option to select columns
st.subheader('Select Columns to Display:')
options = st.multiselect('Select columns:', df.columns.tolist(), default=df.columns.tolist())

# Display the dataframe with selected columns
st.dataframe(df[options])

# Add a download button to allow users to download the data
st.download_button(label='Download Data as CSV',
                   data=df.to_csv(index=False).encode('utf-8'),
                   file_name='data_report.csv',
                   mime='text/csv')

# Add interactive plots using Streamlit widgets, if applicable

st.subheader('Interactive Plot')
selected_column = st.selectbox('Select a column to visualize:', df.select_dtypes(include=[np.number]).columns.tolist())
st.bar_chart(df[selected_column].value_counts())

