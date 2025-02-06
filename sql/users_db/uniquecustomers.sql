SELECT addresses.city, COUNT(DISTINCT orders.user_id) AS unique_customers
FROM orders
JOIN users ON orders.user_id = users.id
JOIN addresses ON users.id = addresses.user_id
GROUP BY addresses.city;
