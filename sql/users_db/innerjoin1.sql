-- Pobranie wszystkich użytkowników i ich adresów (INNER JOIN - tylko użytkownicy z adresami)
SELECT users.id, users.first_name, users.last_name, addresses.street, addresses.city
FROM users
INNER JOIN addresses ON users.id = addresses.user_id;