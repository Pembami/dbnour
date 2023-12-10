import pandas as pd
import streamlit as st
from utils import dataprocessing, get_metrics
import numpy as np
import matplotlib.pyplot as plt

df_raw = pd.read_excel('./data/IndicateurCondi.xlsx', header = 4)
df = dataprocessing(df_raw)

# Display the dataframe in wide mode
st.set_page_config(layout="wide")

# Define a Streamlit layout for data reporting
st.title('Rapport sur les performances de l\'entreprise')

st.write('')
st.write('')


selected_year = st.selectbox('Sélectionner une année pour le rapport:', df['Année'].unique(),index=3)

st.write('')
st.write('')

columns_to_display  = ['Tps Ouverture (min)', 'Cadence (Sac/min)', 'TRS de la ligne ensachage']

st.write(f'## Performance Globales En {selected_year}')

st.write('')
st.write('')

columns = st.columns(4)


for ind, column in enumerate(columns):
    if ind == 0:
        with column:
            st.write("")
            st.write("")
            st.write("#### Moyenne :")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("#### Max : ")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("#### Min : ")
        
    else:
        with column:
            if selected_year-1 in df['Année'].unique():
                st.metric(columns_to_display[ind-1],round(df[df['Année']==selected_year][columns_to_display[ind-1]].mean(),2), round(df[df['Année']==selected_year][columns_to_display[ind-1]].mean()-df[df['Année']==selected_year-1][columns_to_display[ind-1]].mean(),2))
                st.write("")
                st.metric(columns_to_display[ind-1],round(df[df['Année']==selected_year][columns_to_display[ind-1]].max(),2), round(df[df['Année']==selected_year][columns_to_display[ind-1]].max()-df[df['Année']==selected_year-1][columns_to_display[ind-1]].max(),2))
                st.write("")
                st.metric(columns_to_display[ind-1],round(df[df['Année']==selected_year][columns_to_display[ind-1]].min(),2), round(df[df['Année']==selected_year][columns_to_display[ind-1]].min()-df[df['Année']==selected_year-1][columns_to_display[ind-1]].min(),2))
            else:
                st.metric(columns_to_display[ind-1],round(df[df['Année']==selected_year][columns_to_display[ind-1]].mean(),2), round(df[df['Année']==selected_year][columns_to_display[ind-1]].mean(),2)-0)
                st.write("")
                st.metric(columns_to_display[ind-1],round(df[df['Année']==selected_year][columns_to_display[ind-1]].max(),2), round(df[df['Année']==selected_year][columns_to_display[ind-1]].max(),2)-0)
                st.write("")
                st.metric(columns_to_display[ind-1],round(df[df['Année']==selected_year][columns_to_display[ind-1]].min(),2), round(df[df['Année']==selected_year][columns_to_display[ind-1]].min(),2)-0)


st.write('')
st.write('')
st.write('')
st.write('')
df['Mois'] = df['Date'].dt.month    

df_selected = df[df['Année']==selected_year]

df_by_month = df_selected.groupby('Mois')[columns_to_display].mean() 

df_by_month.reset_index(inplace=True)

for column in columns_to_display:
    a,b,c = st.columns([0.4,0.5,0.1])
    with b:
        st.write(f"#### {column} par mois")
    st.line_chart(df_by_month, x='Mois', y=column)

st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')

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

