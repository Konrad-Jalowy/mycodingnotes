SELECT AVG(users_count) AS avg_users_with_addresses
FROM (SELECT user_id, COUNT(*) AS users_count FROM addresses GROUP BY user_id) AS subquery;
