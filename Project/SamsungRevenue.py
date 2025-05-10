import requests
import pandas as pd

url = "https://companiesmarketcap.com/samsung/revenue/"

# Send GET request
response = requests.get(url)

# Read tables from HTML
tables = pd.read_html(response.text)

# Assume first table is the one we want
revenue_table = tables[0]

# Clean 'Revenue' column: remove '$' and 'B', convert to float
revenue_table['Revenue'] = revenue_table['Revenue'].replace('[\$,B]', '', regex=True).astype(float)

# Filter for years between 2007 and 2024
revenue_table = revenue_table[revenue_table['Year'].between(2007, 2024)]

# Calculate estimated smartphone revenue (45% of total)
revenue_table['Estimated Smartphone Revenue'] = revenue_table['Revenue'] * 0.45

# Format the revenue with 'B' suffix
revenue_table['Estimated Smartphone Revenue'] = revenue_table['Estimated Smartphone Revenue'].map(lambda x: f"${x:.2f} B")

# Drop the original 'Revenue' column if not needed
revenue_table.drop(columns=['Revenue'], inplace=True)

# Reset index and print result
revenue_table.reset_index(drop=True, inplace=True)
print(revenue_table)
revenue_table.to_csv("samsung_estimated_smartphone_revenue.csv", index=False)



