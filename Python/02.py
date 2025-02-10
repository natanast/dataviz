import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as mlines

# Reading the Excel file
df = pd.read_excel("./Python/data.xlsx")

# Convert the numeric columns into strings
df.columns = df.columns.astype(str)

# Assign numerical positions for each country
x_pos = np.arange(len(df))

# Define colors for each country (ensure you have as many colors as countries)
colors = ['#33608C', '#BE2641', '#2CA02C']  # Add more colors if needed

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 5))

# Plot each country with its corresponding color for the year 2022
for i, (country, value) in enumerate(zip(df['Country'], df['2022'])):
    # Plot the line (lollipop stick) for 2022
    ax.plot([x_pos[i], x_pos[i]], [0, value], color=colors[i], lw=2)
    # Plot the marker (the round part of the lollipop) for 2022
    ax.scatter(x_pos[i], value, color=colors[i], s=100, zorder=5)

# Plot each country with its corresponding color for the year 2004, shifting x_pos slightly
shift = 0.2  # Amount to shift for 2004 lollipop
for i, (country, value) in enumerate(zip(df['Country'], df['2004'])):
    # Plot the line (lollipop stick) for 2004
    ax.plot([x_pos[i] - shift, x_pos[i] - shift], [0, value], color=colors[i], linestyle='--', lw=2)
    # Plot the marker (the round part of the lollipop) for 2004
    ax.scatter(x_pos[i] - shift, value, color=colors[i], s=100, zorder=5)

# Set x-axis labels
ax.set_xticks(x_pos)
ax.set_xticklabels(df['Country'], rotation=45, ha="right")

# Set y-axis limits
ax.set_ylim(0, max(df['2004'].max(), df['2022'].max()) * 1.2)

# Add labels and title
plt.xlabel("Country")
plt.ylabel("Value")
plt.title("Lollipop Chart for 2004 and 2022")

# Create custom legend handles
line_2022 = mlines.Line2D([], [], color='black', lw=2, label='2022')
line_2004 = mlines.Line2D([], [], color='black', lw=2, linestyle='--', label='2004')

# Add custom legend to the plot
ax.legend(handles=[line_2022, line_2004], loc="upper left", title="", frameon=False)

# Show the plot
plt.tight_layout()  # Optional: To adjust layout
plt.show()
