-- Tworzenie nowej bazy danych
CREATE DATABASE IF NOT EXISTS users_db;
USE users_db;

-- Tabela użytkowników (nadrzędna - jeden użytkownik może mieć wiele zamówień)
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Tabela adresów (relacja 1:1 z użytkownikami)
CREATE TABLE addresses (
    user_id INT PRIMARY KEY,
    street VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(100) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Tabela zamówień (relacja 1:N - jeden użytkownik może mieć wiele zamówień)
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Wstawianie przykładowych użytkowników
INSERT INTO users (first_name, last_name) VALUES
('Jan', 'Kowalski'),
('Anna', 'Nowak'),
('Piotr', 'Zieliński'),
('Katarzyna', 'Wiśniewska'),
('Marek', 'Dąbrowski');

-- Wstawianie przykładowych adresów (nie każdy użytkownik ma adres)
INSERT INTO addresses (user_id, street, city, postal_code, country) VALUES
(1, 'ul. Polna 12', 'Warszawa', '00-001', 'Polska'),
(2, 'ul. Leśna 5', 'Kraków', '30-001', 'Polska'),
(4, 'ul. Słoneczna 8', 'Gdańsk', '80-001', 'Polska');

-- Wstawianie przykładowych zamówień (jeden użytkownik może mieć wiele zamówień)
INSERT INTO orders (user_id, total_price) VALUES
(1, 250.00),  -- Jan Kowalski
(1, 100.00),  -- Jan Kowalski
(2, 300.00),  -- Anna Nowak
(3, 150.00),  -- Piotr Zieliński
(3, 500.00);  -- Piotr Zieliński

-- Pobranie wszystkich użytkowników i ich zamówień (INNER JOIN - tylko użytkownicy z zamówieniami)
SELECT users.id, users.first_name, users.last_name, orders.id AS order_id, orders.total_price
FROM users
INNER JOIN orders ON users.id = orders.user_id;

-- Pobranie wszystkich użytkowników, nawet tych bez zamówienia (LEFT JOIN)
SELECT users.id, users.first_name, users.last_name, 
       COALESCE(orders.id, 'Brak zamówienia') AS order_id, 
       COALESCE(orders.total_price, 0) AS total_price
FROM users
LEFT JOIN orders ON users.id = orders.user_id;

-- Pobranie tylko użytkowników, którzy nie mają zamówienia (LEFT JOIN + WHERE)
SELECT users.id, users.first_name, users.last_name
FROM users
LEFT JOIN orders ON users.id = orders.user_id
WHERE orders.user_id IS NULL;

-- Pobranie użytkownika z jego zamówieniami posortowane po wartości zamówienia
SELECT users.first_name, users.last_name, orders.total_price
FROM users
JOIN orders ON users.id = orders.user_id
ORDER BY orders.total_price DESC;

-- Zliczenie liczby zamówień dla każdego użytkownika
SELECT users.first_name, users.last_name, COUNT(orders.id) AS order_count
FROM users
LEFT JOIN orders ON users.id = orders.user_id
GROUP BY users.id, users.first_name, users.last_name
ORDER BY order_count DESC;

-- Pobranie sumy wydatków użytkowników (pokazuje 0 dla tych, którzy nie mają zamówienia)
SELECT users.first_name, users.last_name, COALESCE(SUM(orders.total_price), 0) AS total_spent
FROM users
LEFT JOIN orders ON users.id = orders.user_id
GROUP BY users.id, users.first_name, users.last_name;

-- Pobranie sumy wydatków użytkowników (pokazuje tylko tych, którzy mają zamówienia)
SELECT users.first_name, users.last_name, SUM(orders.total_price) AS total_spent
FROM users
INNER JOIN orders ON users.id = orders.user_id
GROUP BY users.id, users.first_name, users.last_name;

-- Pobranie użytkowników, którzy wydali więcej niż 200
SELECT users.first_name, users.last_name, SUM(orders.total_price) AS total_spent
FROM users
INNER JOIN orders ON users.id = orders.user_id
GROUP BY users.id, users.first_name, users.last_name
HAVING SUM(orders.total_price) > 200;

-- Pobranie użytkowników, którzy wydali mniej niż 200 (łącznie z tymi, którzy nie mają zamówień)
SELECT users.first_name, users.last_name, COALESCE(SUM(orders.total_price), 0) AS total_spent
FROM users
LEFT JOIN orders ON users.id = orders.user_id
GROUP BY users.id, users.first_name, users.last_name
HAVING COALESCE(SUM(orders.total_price), 0) < 200;
