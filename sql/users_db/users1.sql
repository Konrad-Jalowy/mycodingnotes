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
