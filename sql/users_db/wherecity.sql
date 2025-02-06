SELECT users.first_name, users.last_name, orders.total_price, addresses.city
FROM users
JOIN orders ON users.id = orders.user_id
JOIN addresses ON users.id = addresses.user_id
WHERE addresses.city = 'Warszawa'
ORDER BY orders.total_price DESC;
