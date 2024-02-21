from pywebio.output import *
import plotly.express as px
import pandas as pd

population_year = []
population_number = []

file = open('newcastle_population.csv', 'r')

for line in file:
   population_year.append(int(line.split(",")[0]))
   population_number.append(int(line.split(",")[1].rstrip()))

file.close()

print(population_year)
print(population_number)

df = pd.DataFrame({'Year': population_year, 'Population': population_number})

fig = px.line(df, x='Year', y='Population', title="Newcastle poplulation 1950-2024", height=525, markers=True)

html = fig.to_html(include_plotlyjs="require", full_html=False)

put_html(html)