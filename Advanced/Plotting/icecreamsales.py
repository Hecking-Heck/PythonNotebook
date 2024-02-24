# Imports
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Datset
temperature = [14.2, 16.4, 11.9, 12.5, 18.9]
sales = [215.20, 325.00, 185.20, 330.20, 418.60]

# Plotting
plt.title('Ice-cream Sales vs. Temperature')
plt.xlabel('Sales')
plt.ylabel('Temperature')
plt.scatter(temperature, sales, color='red')
plt.show()