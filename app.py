import streamlit as st
import pandas as pd
st.button("Refresh")

st.title('akaSwap 收益畫圖')
df = pd.read_csv("data.csv", index_col=0)
#st.write("Here's our first attempt at using data to create a table:")
#st.write(df)

import plotly.express as px
fig = px.line(df, x="Date", y="Amount", title='Time vs. Amount')
st.plotly_chart(fig, use_container_width=True)


df


