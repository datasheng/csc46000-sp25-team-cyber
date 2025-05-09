import pandas as pd
import sqlite3

# Load your scraped CSV
csv_path = 'apple_vs_samsung_market_share.csv'
df = pd.read_csv(csv_path)

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect('smartphone_market_sales.db')

# Insert data into SQLite table
df.to_sql(
    name='market_share',  # Table name
    con=conn,
    if_exists='replace',  # Options: 'fail', 'replace', 'append'
    index=False,
    dtype={
        'quarter': 'TEXT',
        'year': 'INTEGER',
        'Apple': 'INTEGER',
        'Samsung': 'INTEGER'
    }
)

# Verify insertion
print("Data inserted successfully!")
print(pd.read_sql_query("SELECT * FROM market_share LIMIT 5", conn))

conn.close()  # Close connection