SELECT users.first_name, users.last_name, orders.total_price, orders.created_at, addresses.city
FROM users
JOIN orders ON users.id = orders.user_id
JOIN addresses ON users.id = addresses.user_id
WHERE addresses.city = 'Kraków' 
AND orders.created_at BETWEEN '2025-02-01' AND '2025-02-28'
ORDER BY orders.created_at DESC;
