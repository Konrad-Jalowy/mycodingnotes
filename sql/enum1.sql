CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    status ENUM('pending', 'completed', 'cancelled') DEFAULT 'pending'
);

INSERT INTO orders (user_id, status) VALUES 
(1, 'pending'),
(2, 'completed'),
(3, 'cancelled'),
(4, DEFAULT); -- Tu zostanie ustawiony 'pending'

SELECT * FROM orders;
