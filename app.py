# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Load your dataset
df = pd.read_csv('data.csv')

# Streamlit app
st.title('Data Visualization with Streamlit')

# Show the raw data
st.subheader('Raw Data')
st.write(df)

# Visualization: Bar Chart
st.subheader('Bar Chart - Number of Projects by Client')
bar_data = df['Client'].value_counts()
bar_chart = go.Figure(go.Bar(x=bar_data.index, y=bar_data.values))
bar_chart.update_layout(title='Number of Projects by Client', xaxis_title='Client', yaxis_title='Number of Projects')
st.plotly_chart(bar_chart)

# Visualization: Pie Chart
st.subheader('Pie Chart - Distribution of Implementation Types')
pie_data = df['Implementation Type'].value_counts()
pie_chart = go.Figure(go.Pie(labels=pie_data.index, values=pie_data.values))
pie_chart.update_layout(title='Distribution of Implementation Types')
st.plotly_chart(pie_chart)
