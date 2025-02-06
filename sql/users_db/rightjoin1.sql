-- Pobranie wszystkich adresów wraz z użytkownikami (RIGHT JOIN)
SELECT COALESCE(users.first_name, 'NO USER!!!') AS first_name, 
       COALESCE(users.last_name, 'NO USER!!!') AS last_name, 
       addresses.street, addresses.city
FROM users
RIGHT JOIN addresses ON users.id = addresses.user_id;