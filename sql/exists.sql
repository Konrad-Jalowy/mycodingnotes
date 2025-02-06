SELECT * FROM users u
WHERE EXISTS (SELECT 1 FROM addresses a WHERE a.user_id = u.id);
