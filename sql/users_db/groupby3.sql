SELECT users.first_name, users.last_name, SUM(orders.total_price) AS total_spent
FROM users
INNER JOIN orders ON users.id = orders.user_id
GROUP BY users.id, users.first_name, users.last_name;
