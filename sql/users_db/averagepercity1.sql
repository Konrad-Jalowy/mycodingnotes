SELECT COALESCE(a.city, 'Nieznane miasto') AS city, AVG(order_count) AS avg_orders_per_city
FROM (
    SELECT u.id AS user_id, COUNT(o.id) AS order_count
    FROM users u
    LEFT JOIN orders o ON u.id = o.user_id
    GROUP BY u.id
) AS order_stats
LEFT JOIN addresses a ON order_stats.user_id = a.user_id
GROUP BY city;
