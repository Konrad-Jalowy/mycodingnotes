-- Pobranie użytkowników i ich zamówień z danego przedziału czasowego
SELECT users.first_name, users.last_name, orders.total_price, orders.created_at
FROM users
JOIN orders ON users.id = orders.user_id
WHERE orders.created_at BETWEEN '2025-02-01' AND '2025-02-28'
ORDER BY orders.created_at DESC;
