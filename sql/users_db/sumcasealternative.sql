SELECT 
    COUNT(addresses.user_id) AS users_with_addresses, 
    COUNT(*) - COUNT(addresses.user_id) AS users_without_addresses
FROM users
LEFT JOIN addresses ON users.id = addresses.user_id;
