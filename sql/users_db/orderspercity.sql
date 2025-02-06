SELECT addresses.city, COUNT(orders.id) AS total_orders
FROM orders
JOIN users ON orders.user_id = users.id
JOIN addresses ON users.id = addresses.user_id
GROUP BY addresses.city;