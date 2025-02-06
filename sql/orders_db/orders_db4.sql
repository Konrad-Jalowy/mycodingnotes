-- Tworzenie bazy danych
CREATE DATABASE IF NOT EXISTS orders_db;
USE orders_db;

-- Tabela użytkowników
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Wstawianie przykładowych użytkowników
INSERT INTO users (name, email) VALUES
('Jan Kowalski', 'jan.kowalski@example.com'),
('Anna Nowak', 'anna.nowak@example.com'),
('Piotr Zieliński', 'piotr.zielinski@example.com');

-- Tabela produktów
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

-- Wstawianie przykładowych produktów
INSERT INTO products (name, price) VALUES
('Laptop Lenovo', 3500.00),
('Smartfon Samsung', 2500.00),
('Słuchawki Sony', 300.00);

-- Tabela zamówień
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Wstawianie przykładowych zamówień
INSERT INTO orders (user_id, total_price) VALUES
(1, 3800.00),
(2, 2500.00),
(3, 300.00);

-- Tabela produktów w zamówieniach
CREATE TABLE order_items (
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT DEFAULT 1,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Wstawianie przykładowych produktów do zamówień
INSERT INTO order_items (order_id, product_id, quantity) VALUES
(1, 1, 1),
(1, 3, 1),
(2, 2, 1),
(3, 3, 1);

-- Pobranie listy użytkowników i ich zamówień
SELECT users.id, users.name, orders.id AS order_id, orders.total_price
FROM users
LEFT JOIN orders ON users.id = orders.user_id
ORDER BY users.id;

-- Obliczenie łącznej wartości zamówień każdego użytkownika
SELECT users.id, users.name, SUM(orders.total_price) AS total_spent
FROM users
LEFT JOIN orders ON users.id = orders.user_id
GROUP BY users.id, users.name
ORDER BY total_spent DESC;

-- Pobranie najczęściej kupowanych produktów
SELECT products.id, products.name, SUM(order_items.quantity) AS total_sold
FROM products
JOIN order_items ON products.id = order_items.product_id
GROUP BY products.id, products.name
ORDER BY total_sold DESC;

-- Pobranie największych klientów (użytkowników z największą liczbą zamówień)
SELECT users.id, users.name, COUNT(orders.id) AS total_orders
FROM users
LEFT JOIN orders ON users.id = orders.user_id
GROUP BY users.id, users.name
ORDER BY total_orders DESC;

-- Pobranie najdroższego zamówienia
SELECT id, user_id, total_price
FROM orders
ORDER BY total_price DESC
LIMIT 1;

-- Pobranie produktów, których nikt jeszcze nie kupił
SELECT products.id, products.name
FROM products
LEFT JOIN order_items ON products.id = order_items.product_id
WHERE order_items.product_id IS NULL;

-- Obliczenie średniej wartości zamówienia
SELECT AVG(total_price) AS average_order_value FROM orders;
