import pandas as pd
import sqlite3

# Load scraped CSV
csv_path = 'apple_vs_samsung_market_share.csv'
df = pd.read_csv(csv_path)

# Revenue data
smartphone_revenue = pd.read_csv('smartphone_revenue.csv')
# Remove commas from numbers and convert to float
smartphone_revenue["Apple's Revenue"] = smartphone_revenue["Apple's Revenue"].str.replace(',', '').astype(float)
smartphone_revenue["Samsung's Revenue"] = smartphone_revenue["Samsung's Revenue"].str.replace(',', '').astype(float)

# Connect to SQLite database
conn = sqlite3.connect('smartphone_market_sales.db')

# Insert data into SQLite table
# df.to_sql(
#     name='market_share', 
#     con=conn,
#     if_exists='replace',
#     index=False,
#     dtype={
#         'quarter': 'TEXT',
#         'year': 'INTEGER',
#         'Apple': 'INTEGER',
#         'Samsung': 'INTEGER'
#     }
# )

# Insert data
smartphone_revenue.rename(columns={
    "Year": "year",
    "Apple's Revenue": "apple_revenue",
    "Samsung's Revenue": "samsung_revenue"
})[['year', 'apple_revenue', 'samsung_revenue']].to_sql(
    name='revenue',
    con=conn,
    if_exists='replace',
    index=False
)

# Verify insertion
# print(pd.read_sql_query("SELECT * FROM market_share LIMIT 5", conn))

conn.close()  # Close connection