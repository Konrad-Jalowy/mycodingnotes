SELECT users.id, users.name, orders.id AS order_id, orders.total_price
FROM users
LEFT JOIN orders ON users.id = orders.user_id
ORDER BY users.id;
