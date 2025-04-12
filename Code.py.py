import pandas as pd

# Load the dataset

df = pd.read_csv(r"C:\B-Tech\SEM4\datascience.py\Electric_Vehicle_Population_Data.csv")

# Show basic info and first few rows to understand the dataset
df.info(), df.head()
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")

# Count of EVs by year
yearly_counts = df['Model Year'].value_counts().sort_index()

# Plot
plt.figure(figsize=(12, 6))
sns.lineplot(x=yearly_counts.index, y=yearly_counts.values, marker='o', color='green')
plt.title('EV Adoption Over the Years', fontsize=16)
plt.xlabel('Model Year')
plt.ylabel('Number of EVs Registered')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Top 10 cities with the most EVs
top_cities = df['City'].value_counts().head(10)

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(x=top_cities.values, y=top_cities.index, hue=top_cities.index, palette="viridis", dodge=False, legend=False)
plt.title('Top 10 Cities by Number of EVs', fontsize=16)
plt.xlabel('Number of EVs')
plt.ylabel('City')
plt.tight_layout()
plt.show()
# Top 10 makes
top_makes = df['Make'].value_counts().head(10)

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(x=top_cities.values, y=top_cities.index, hue=top_cities.index, palette="mako", dodge=False, legend=False)
plt.title('Top 10 EV Makes', fontsize=16)
plt.xlabel('Number of EVs')
plt.ylabel('Make')
plt.tight_layout()
plt.show()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data structure
# Assuming a DataFrame with columns: 'Vehicle Type' and 'Electric Range'
data = pd.DataFrame({
    'Vehicle Type': ['BEV'] * 50 + ['PHEV'] * 50,
    'Electric Range': (
        list(range(30, 330, 6)) +  # Simulated BEV ranges
        list(range(10, 60, 1))     # Simulated PHEV ranges
    )
})

# Set the plot style
sns.set(style="whitegrid")

# Create the boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x='Vehicle Type', y='Electric Range', hue='Vehicle Type', palette='pastel', legend=False)

# Customize labels and title
plt.title('Electric Range by Vehicle Type', fontsize=16)
plt.xlabel('Electric Vehicle Type', fontsize=12)
plt.ylabel('Electric Range (miles)', fontsize=12)

# Rotate x-axis labels for clarity
plt.xticks(rotation=20)

# Show the plot
plt.tight_layout()
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = pd.DataFrame({
    'ZIP Code': ['2951', '3052', '3166', '3382', '3391', '3459', '3644', '3825', '4457', '5824'],
    'Number of EVs': [98000, 98100, 98200, 98300, 98400, 98500, 98600, 98700, 98800, 98900]
})

# Normalize for color mapping
norm = plt.Normalize(data["Number of EVs"].min(), data["Number of EVs"].max())
colors = plt.cm.viridis(norm(data["Number of EVs"]))

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Scatter (dot) plot
scatter = ax.scatter(
    data["Number of EVs"],
    data["ZIP Code"],
    s=100,
    color=colors,
    edgecolor="green"
)

# Labels and title
ax.set_title("EV Count by ZIP Code – Gradient Dot Strip", fontsize=16, weight='bold')
ax.set_xlabel("Number of EVs", fontsize=12)
ax.set_ylabel("ZIP Code", fontsize=12)
ax.grid(axis='x', linestyle='--', alpha=0.5)

# Colorbar assigned to current axis
sm = plt.cm.ScalarMappable(cmap="viridis", norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax)
cbar.set_label("Number of EVs", fontsize=12)

plt.tight_layout()
plt.show()









