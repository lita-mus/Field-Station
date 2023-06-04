import pandas as pd
import plotly.express as px

# Load CSV file into a pandas dataframe temperature every 1 hour
df = pd.read_csv('c:/00 RUG/Year 1 Term 2a/IRT/Data/00 Data/Temperature/Temperature.csv')

# Convert 'day' column to datetime format
df['day'] = pd.to_datetime(df['day'], format='%m/%d/%Y')

# Create a scatter plot with Plotly Express - FS
fig = px.scatter(df, x='day', y='hour', color='Temperature_FS', 
                 color_discrete_sequence='Temperature_FS', template='plotly_dark')

# Add vertical lines between each month
last_month = None
for i in range(1, len(df)):
    if df['day'][i].month != df['day'][i-1].month:
        if last_month is not None:
            fig.add_shape(type='line',
                          x0=pd.Timestamp(year=df['day'][i-1].year, month=last_month, day=1).date(),
                          y0=0,
                          x1=pd.Timestamp(year=df['day'][i-1].year, month=last_month, day=1).date(),
                          y1=24,
                          line=dict(color='black', width=2))
        last_month = df['day'][i].month

fig.update_traces(
    marker_line=dict(width=0,color='black'),
    marker_symbol='square',
    # Set the marker opacity to 0.7
    marker_opacity=0.7
)

# Set the title and width
fig.update_layout(
    title='Temperature per hour at Solander Field Station',
    height=300
)

# Show the plot
fig.show()
fig.write_html("c:/00 RUG/Year 1 Term 2a/IRT/Data/00 Data/PAR/Python/TemperatureWithLine.html")
