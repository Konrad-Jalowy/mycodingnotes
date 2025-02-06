SELECT users.id, users.name, orders.id AS order_id, orders.total_price
FROM users
RIGHT JOIN orders ON users.id = orders.user_id
ORDER BY orders.id;
