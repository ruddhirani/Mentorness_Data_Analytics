import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate

# Load the data from the Excel file
file_path = 'cost-of-living.xlsx'
df = pd.read_excel(file_path)

# Display the first few rows of the dataframe
df.head()

# Check for missing values
missing_values = df.isnull().sum()

# Display missing values
print("Missing values in each column:\n", missing_values)

# Drop rows with missing values for simplicity
df = df.dropna()

# Define the path for the new Excel file
new_file_path = 'cost_of_living_data_no_null.xlsx'

# Save the DataFrame to a new Excel file without null values
df.to_excel(new_file_path, index=False)

# Ensure numerical columns are of correct data type
for col in df.columns[2:]:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Display the cleaned dataframe info
df.info()

# Calculate the total cost of living as a sum of all relevant columns
cost_columns = df.columns[2:]
df['Total_Cost'] = df[cost_columns].sum(axis=1)

# Find cities with highest and lowest total costs of living
highest_cost_city = df.loc[df['Total_Cost'].idxmax()]
lowest_cost_city = df.loc[df['Total_Cost'].idxmin()]

print("City with highest cost of living:\n",
      highest_cost_city[['city', 'country', 'Total_Cost']])
print("City with lowest cost of living:\n",
      lowest_cost_city[['city', 'country', 'Total_Cost']])

# Calculate mean cost for each component
mean_costs = df[cost_columns].mean().sort_values(ascending=False)

# Display the top 5 major cost components
print("Top 5 major cost components contributing to the overall cost of living:\n", mean_costs.head())


correlation_matrix = df.corr()

# Correlation of each factor with the total cost of living
correlation_with_total_cost = correlation_matrix['Total_Cost'].sort_values(
    ascending=False)

# Save the correlation data to a text file in a table format
with open('correlation_with_total_cost.txt', 'w') as f:
    f.write(tabulate(correlation_with_total_cost.reset_index(), headers=[
            'Factor', 'Correlation with Total Cost'], tablefmt='grid'))

# Display correlation with total cost
print("Correlation of each factor with the total cost of living:\n",
      correlation_with_total_cost)


# Visualize the correlation matrix as a heatmap
# plt.figure(figsize=(16, 12))  # Increase the size for better readability
# sns.heatmap(correlation_matrix, annot=False, fmt='.2f',
#             cmap='coolwarm', cbar=True, linewidths=0.5)
# plt.title('Correlation Matrix of Cost of Living Factors', fontsize=18)
# plt.xticks(rotation=45, ha='right')
# plt.yticks(rotation=0)
# plt.tight_layout()  # Ensure the layout fits well
# plt.show()

# Plot average salary vs. total cost of living
# plt.figure(figsize=(10, 6))
# sns.scatterplot(
#     data=df, x='Average Monthly Net Salary (After Tax) (USD)', y='Total_Cost')
# plt.title('Average Salary vs. Total Cost of Living')
# plt.xlabel('Average Monthly Net Salary (USD)')
# plt.ylabel('Total Cost of Living (USD)')
# plt.show()
