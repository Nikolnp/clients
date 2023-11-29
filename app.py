import streamlit as st
import pandas as pd


# Load your dataset
df = pd.read_csv('C:/Users/Nikoleta/Source/Repos/clients/data.csv')

# Streamlit app
st.title('Data Visualization with Streamlit')

# Show the raw data
st.subheader('Raw Data')
st.table(df)

