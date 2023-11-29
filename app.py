import streamlit as st
import pandas as pd
import plotly.express as px

# Load your dataset
df = pd.read_csv('C:/Users/Nikoleta/Source/Repos/clients/data.csv')

# Streamlit app
st.title('Data Visualization with Streamlit')

# Show the raw data
st.subheader('Raw Data')
st.table(df)

# Visualization: Bar Chart
st.subheader('Bar Chart - Number of Projects by Client')
bar_chart = px.bar(df, x='Client', title='Number of Projects by Client')
st.plotly_chart(bar_chart)

# Visualization: Pie Chart
st.subheader('Pie Chart - Distribution of Implementation Types')
pie_chart = px.pie(df, names='Implementation Type', title='Distribution of Implementation Types')
st.plotly_chart(pie_chart)
