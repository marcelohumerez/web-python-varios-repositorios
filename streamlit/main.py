import pandas as pd
import streamlit as st
import plotly_express as px

st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide"
)


st.write("""
# Hola Lu Pupi y Tato Mouse My first app
Marcelo Humerez #

Colons can be used to align columns.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the 
raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3
""")

df = pd.read_csv(r'data.csv')
st.line_chart(df['Rank'])


st.dataframe(df)