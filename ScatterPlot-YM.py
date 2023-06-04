import plotly.express as px
import pandas as pd
#import numpy as np
#import datetime

df = pd.read_csv('c:/00 RUG/Year 1 Term 2a/IRT/Data/00 Data/PAR/Python/solanderseye_weatherdata - PAR1.csv')

# Convert PAR column to float and replace NaN values with 0
df['PAR'] = pd.to_numeric(df['PAR'], errors='coerce').fillna(0)

# Convert 'day' column to datetime format
df['day'] = pd.to_datetime(df['day'], format='%m/%d/%Y')

# Create a scatter plot with Plotly Express
fig = px.scatter(df, x='day', y='hour', size='PAR', color='PAR', 
                 color_discrete_sequence='PAR', template='plotly_dark')

fig.update_traces(
    marker_line=dict(width=0,color='black')
)

fig.update_layout(title='Photosynthetically Active Radiation per 15 mins')

fig.show()
#fig.write_html("c:/00 RUG/Year 1 Term 2a/IRT/Data/00 Data/PAR/Python/plotly.html")
