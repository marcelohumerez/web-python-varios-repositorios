import pandas as pd
import streamlit as st
import plotly_express as px

st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide"
)


st.write("""
# Hola Lu Pupi y Tato Mouse My first app
Marcelo Humerez 
test2 #


1 | 2 | 3
""")

df = pd.read_csv(r'data.csv')
st.line_chart(df['Rank'])


st.dataframe(df)