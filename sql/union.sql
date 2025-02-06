SELECT first_name, last_name, city FROM users u
JOIN addresses a ON u.id = a.user_id WHERE a.city = 'Warszawa'
UNION
SELECT first_name, last_name, city FROM users u
JOIN addresses a ON u.id = a.user_id WHERE a.city = 'Kraków';
