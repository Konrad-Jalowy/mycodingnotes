SELECT users.first_name, users.last_name, COALESCE(SUM(orders.total_price), 0) AS total_spent
FROM users
LEFT JOIN orders ON users.id = orders.user_id
GROUP BY users.id, users.first_name, users.last_name
HAVING COALESCE(SUM(orders.total_price), 0) < 200;
