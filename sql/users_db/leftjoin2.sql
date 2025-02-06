-- Pobranie tylko użytkowników, którzy nie mają adresu (LEFT JOIN + WHERE)
SELECT users.id, users.first_name, users.last_name
FROM users
LEFT JOIN addresses ON users.id = addresses.user_id
WHERE addresses.user_id IS NULL;