from api_test import *
import streamlit as st
import pandas as pd

def get_data():
    with st.spinner('crawling data...'):
        crawl_data()
    st.success('data is up to date!')

st.button("Refresh")
st.button("Crawl data", on_click=get_data)


st.title('akaSwap 收益畫圖')
df = pd.read_csv("Income_tz1WCYsbPyHTBcnj4saWG6SRFHECCj2TTzC6.csv", index_col=0)
#st.write("Here's our first attempt at using data to create a table:")
#st.write(df)

import plotly.express as px
fig = px.line(df, x="Date", y="Amount", title='Time vs. Amount')
st.plotly_chart(fig, use_container_width=True)


df


