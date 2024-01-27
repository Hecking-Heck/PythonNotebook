# Import
from pywebio.output import put_html
import plotly.graph_objects as go

import pandas as pd
from datetime import datetime

# Create a DataFrame from public CSV data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

# Create a Figure using the DataFrame data
fig = go.Figure(data=[go.Candlestick(x=df['Date'], open=df['AAPL.Open'], high=df['AAPL.High'], low=df['AAPL.Low'], close=df['AAPL.Close'])])

# Create a HTML object based on the Figure and display it
html = fig.to_html(include_plotlyjs="require", full_html=False)
put_html(html)