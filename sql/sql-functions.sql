--average
SELECT AVG(items.price) FROM items

-- join + columns + group by + count
SELECT customers.last_name, COUNT(purchases.id) 
FROM customers 
LEFT JOIN purchases ON customers.id = purchases.item_id
GROUP BY customers.id;

-- join (x2) + columns + group by + sum
SELECT customers.last_name, SUM(items.price)
FROM items
INNER JOIN purchases ON purchases.item_id = items.id
INNER JOIN customers ON customers.id = purchases.customer_id
GROUP BY customers.id;

-- join (x2) + columns + group by + sum + rename + order by + limit
SELECT customers.last_name, SUM(items.price) AS  "Total spent"
FROM items
INNER JOIN purchases ON purchases.item_id = items.id
INNER JOIN customers ON customers.id = purchases.customer_id
GROUP BY customers.id
ORDER BY "Total spent" DESC
LIMIT 2;

-- join + columns + count + rename + having clause
SELECT customers.first_name, COUNT(purchases.id) as "Number of purchases"
FROM customers
INNER JOIN purchases ON purchases.customer_id = customers.id
GROUP BY customers.id
HAVING COUNT(purchases.id) > 2