
import pandas as pd
import matplotlib.pyplot as plt

# Reading an Excel file
df = pd.read_excel("./Python/data.xlsx")


# Convert column names to strings
df.columns = df.columns.map(str)

# Ensure numeric values
df[['2004', '2022']] = df[['2004', '2022']].apply(pd.to_numeric)

# plot --------------

# Plot horizontal bars
plt.barh(y=df['Country'], width=df['2004'], color='#33608C', label='2004')
plt.barh(y=df['Country'], width=df['2022'], left=df['2004'], color='#BE2641', label='2022')

# Add labels and title
plt.xlabel('Count')
plt.ylabel('Country')
plt.title('Comparison of Counts in 2004 and 2022')
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()