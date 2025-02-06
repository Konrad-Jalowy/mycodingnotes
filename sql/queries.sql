-- Zaawansowane zapytania SQL
USE my_database;

-- 1. Pobranie wszystkich użytkowników z liczbą ich zamówień
SELECT users.id, users.name, COUNT(orders.id) AS total_orders
FROM users
LEFT JOIN orders ON users.id = orders.user_id
GROUP BY users.id, users.name
ORDER BY total_orders DESC;

-- 2. Pobranie wszystkich zamówień z informacją o użytkowniku
SELECT orders.id, users.name, orders.total_price, orders.status, orders.created_at
FROM orders
JOIN users ON orders.user_id = users.id
ORDER BY orders.created_at DESC;

-- 3. Pobranie najczęściej zamawianych produktów
SELECT products.name, COUNT(order_products.product_id) AS total_sold
FROM order_products
JOIN products ON order_products.product_id = products.id
GROUP BY products.name
ORDER BY total_sold DESC
LIMIT 10;

-- 4. Pobranie zamówień powyżej średniej wartości wszystkich zamówień
SELECT * FROM orders
WHERE total_price > (SELECT AVG(total_price) FROM orders);

-- 5. Pobranie użytkowników, którzy nie złożyli jeszcze żadnego zamówienia
SELECT users.* FROM users
LEFT JOIN orders ON users.id = orders.user_id
WHERE orders.id IS NULL;
