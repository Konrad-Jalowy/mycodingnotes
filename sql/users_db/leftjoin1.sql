
-- Pobranie wszystkich użytkowników, nawet tych bez adresu (LEFT JOIN)
SELECT users.id, users.first_name, users.last_name, 
       COALESCE(addresses.street, 'N/A') AS street, 
       COALESCE(addresses.city, 'N/A') AS city
FROM users
LEFT JOIN addresses ON users.id = addresses.user_id;