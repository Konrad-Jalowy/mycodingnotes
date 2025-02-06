SELECT e1.name AS employee, COALESCE(e2.name, 'top-level-manager') AS manager
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.id;
