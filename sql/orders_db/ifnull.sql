SELECT IFNULL(users.id, 'NO USER!!!') AS user_id, IFNULL(users.name, 'NO USER!!!') AS name, orders.id AS order_id, orders.total_price
FROM users
RIGHT JOIN orders ON users.id = orders.user_id
ORDER BY orders.id;