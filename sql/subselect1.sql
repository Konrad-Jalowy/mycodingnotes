SELECT * FROM users
WHERE id = (SELECT MAX(id) FROM users);
