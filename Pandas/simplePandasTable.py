import pandas as pd

# Sample raw data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Creating a DataFrame from the raw data
df = pd.DataFrame(data)

# Displaying the DataFrame
df.style