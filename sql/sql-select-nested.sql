-- nested select to get items with higher than average price
SELECT * 
FROM items
WHERE items.price >
(
  SELECT AVG(items.price)
  FROM items
)

-- nested select to say how much items are below or above the average price
SELECT items.name, items.price
- (
  SELECT AVG(items.price)
  FROM items 
)
FROM items

-- nested select using view to find how much luxury items (>100) are below or above the average price of luxury items
CREATE VIEW luxury_items AS
SELECT *
FROM items
WHERE items.price > 100

SELECT luxury_items.name, luxury_items.price
- (
  SELECT AVG(luxury_items.price)
  FROM luxury_items 
)
FROM luxury_items