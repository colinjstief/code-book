-- group by
SELECT * FROM customers 
GROUP BY customers.id

-- join
SELECT * 
FROM customers 
INNER JOIN purchases ON customers.id = purchases.item_id;

-- join + columns
SELECT customers.first_name, customers.last_name 
FROM customers 
INNER JOIN purchases ON customers.id = purchases.item_id;

-- join (x2)
SELECT * 
FROM items 
INNER JOIN purchases ON items.id = purchases.item_id
INNER JOIN customers ON purchases.customer_id = customers.id;

-- join (x2) + columns
SELECT customers.last_name, items.name 
FROM items 
INNER JOIN purchases ON items.id = purchases.item_id
INNER JOIN customers ON purchases.customer_id = customers.id;
