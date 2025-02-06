SELECT first_name, last_name, DATEDIFF(NOW(), created_at) AS days_since_registration 
FROM users;
