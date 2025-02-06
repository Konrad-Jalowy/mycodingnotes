-- Pobranie listy użytkowników i ich zamówień (LEFT JOIN z N/A zamiast NULL)
SELECT users.id, users.name, COALESCE(orders.id, 'N/A') AS order_id, COALESCE(orders.total_price, 'N/A') AS total_price
FROM users
LEFT JOIN orders ON users.id = orders.user_id
ORDER BY users.id;