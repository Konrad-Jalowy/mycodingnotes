-- Tworzenie nowej bazy danych
CREATE DATABASE IF NOT EXISTS users_db;
USE users_db;

-- Tabela użytkowników
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

-- Wstawianie przykładowych użytkowników (niektórzy nie mają adresów)
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

-- Pobranie wszystkich użytkowników i ich adresów (INNER JOIN - tylko użytkownicy z adresami)
SELECT users.id, users.first_name, users.last_name, addresses.street, addresses.city
FROM users
INNER JOIN addresses ON users.id = addresses.user_id;

-- Pobranie wszystkich użytkowników, nawet tych bez adresu (LEFT JOIN)
SELECT users.id, users.first_name, users.last_name, 
       COALESCE(addresses.street, 'N/A') AS street, 
       COALESCE(addresses.city, 'N/A') AS city
FROM users
LEFT JOIN addresses ON users.id = addresses.user_id;

-- Pobranie tylko użytkowników, którzy nie mają adresu (LEFT JOIN + WHERE)
SELECT users.id, users.first_name, users.last_name
FROM users
LEFT JOIN addresses ON users.id = addresses.user_id
WHERE addresses.user_id IS NULL;

-- Pobranie wszystkich adresów wraz z użytkownikami (RIGHT JOIN)
SELECT COALESCE(users.first_name, 'NO USER!!!') AS first_name, 
       COALESCE(users.last_name, 'NO USER!!!') AS last_name, 
       addresses.street, addresses.city
FROM users
RIGHT JOIN addresses ON users.id = addresses.user_id;

-- Zliczenie użytkowników z adresami i bez
SELECT 
    SUM(CASE WHEN addresses.user_id IS NOT NULL THEN 1 ELSE 0 END) AS users_with_addresses,
    SUM(CASE WHEN addresses.user_id IS NULL THEN 1 ELSE 0 END) AS users_without_addresses
FROM users
LEFT JOIN addresses ON users.id = addresses.user_id;
