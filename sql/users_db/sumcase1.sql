-- Zliczenie użytkowników z adresami i bez
SELECT 
    SUM(CASE WHEN addresses.user_id IS NOT NULL THEN 1 ELSE 0 END) AS users_with_addresses,
    SUM(CASE WHEN addresses.user_id IS NULL THEN 1 ELSE 0 END) AS users_without_addresses
FROM users
LEFT JOIN addresses ON users.id = addresses.user_id;
