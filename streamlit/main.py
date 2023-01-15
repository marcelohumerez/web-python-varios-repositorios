import pandas as pd
import streamlit as st

st.write("""
# Hola Lucianita My first app
Hello World #
""")

df = pd.read_csv(r'data.csv')
st.line_chart(df['Rank'])