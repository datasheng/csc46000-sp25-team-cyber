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