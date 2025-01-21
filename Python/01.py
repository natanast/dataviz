import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# Reading an Excel file

df = pd.read_excel(r"scripts\data.xlsx")

df = pd.read_csv("data.csv")


# Plot horizontal bars for 2004 and 2022
plt.barh(y=df['Country'], width=df['2004'], color='#33608C', label='2004')
plt.barh(y=df['Country'], width=df['2022'], left=df['2004'], color='#BE2641', label='2022')

# Add labels and title
plt.xlabel('Count')
plt.title('Comparison of Counts in 2004 and 2022')
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()











