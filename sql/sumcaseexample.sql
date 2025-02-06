SELECT 
    SUM(CASE WHEN addresses.city = 'Warszawa' THEN 1 ELSE 0 END) AS warszawa_users,
    SUM(CASE WHEN addresses.city = 'Kraków' THEN 1 ELSE 0 END) AS krakow_users
FROM users
LEFT JOIN addresses ON users.id = addresses.user_id;
