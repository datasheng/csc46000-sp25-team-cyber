 CREATE TABLE IF NOT EXISTS market_share (
   quarter TEXT,           -- e.g., "Q1"
   year INTEGER,           -- e.g., 2023
   apple INTEGER,               -- Apple's market share (%)
   samsung INTEGER,             -- Samsung's market share (%)
   PRIMARY KEY (quarter, year)  -- Composite key to avoid duplicate entries
);

SELECT  -- Market share where Apple > Samsung
    quarter || ' ' || year AS period,
    apple AS apple_market_share,
    samsung AS samsung_market_share,
    (apple - samsung) AS difference
FROM market_share
WHERE apple > samsung
ORDER BY year, quarter;

 CREATE TABLE IF NOT EXISTS revenue (
   year INTEGER,           -- e.g., 2023
   revenue REAL,             -- Apple or Samsung revenue ($)
   PRIMARY KEY (year)
);

-- DROP TABLE revenue;

-- Show all entries
SELECT 
    year,
    printf("$%,.0f", apple_revenue) AS apple_revenue,
    printf("$%,.0f", samsung_revenue) AS samsung_revenue
FROM revenue
ORDER BY year DESC;