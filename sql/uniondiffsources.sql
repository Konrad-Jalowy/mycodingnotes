SELECT first_name, last_name, 'USER' AS type FROM users
UNION
SELECT name AS first_name, '' AS last_name, 'EMPLOYEE' AS type FROM employees;
