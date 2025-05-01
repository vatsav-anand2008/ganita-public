import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('/home/venkat/Projects/workbook/AnaadiAI/lilavati/1_square_calculation_results.csv')

# Filter out rows with errors
df = df[df['Mean Time'].notna()]

# Convert Mean Time to float, ignoring any non-numeric values
df['Mean Time'] = pd.to_numeric(df['Mean Time'], errors='coerce')

# Drop any rows where conversion to float failed
df = df.dropna(subset=['Mean Time'])

# Get unique methods
methods = df['Method'].unique()

# Create the plot
plt.figure(figsize=(12, 8))

# Plot each method
for method in methods:
    data = df[df['Method'] == method]
    plt.plot(data['Digits'], data['Mean Time'], label=method, marker='o')

plt.xlabel('Number of Digits')
plt.ylabel('Mean Time (seconds)')
plt.title('Performance of Different Square Calculation Methods')
plt.legend()
plt.xscale('log')  # Use log scale for x-axis due to large range
plt.yscale('log')  # Use log scale for y-axis due to large range of times
plt.grid(True, which="both", ls="-", alpha=0.2)

# Show the plot
plt.tight_layout()
plt.show()
