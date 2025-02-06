-- Procedury składowane i triggery w MySQL
USE my_database;

-- 1. Procedura składowana: Dodanie nowego użytkownika
DELIMITER $$
CREATE PROCEDURE AddUser(
    IN p_name VARCHAR(100),
    IN p_email VARCHAR(100)
)
BEGIN
    INSERT INTO users (name, email) VALUES (p_name, p_email);
END $$
DELIMITER ;

-- 2. Procedura składowana: Pobranie sumy zamówień użytkownika
DELIMITER $$
CREATE PROCEDURE GetUserTotalOrders(
    IN p_user_id INT,
    OUT total DECIMAL(10,2)
)
BEGIN
    SELECT SUM(total_price) INTO total FROM orders WHERE user_id = p_user_id;
END $$
DELIMITER ;

-- 3. Trigger: Automatyczna zmiana statusu zamówienia po dodaniu produktu
DELIMITER $$
CREATE TRIGGER after_order_product_insert
AFTER INSERT ON order_products
FOR EACH ROW
BEGIN
    UPDATE orders SET status = 'pending' WHERE id = NEW.order_id;
END $$
DELIMITER ;
