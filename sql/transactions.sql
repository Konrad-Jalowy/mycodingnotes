-- Transakcje i blokady w MySQL
USE my_database;

-- 1. Przykład transakcji: Dodanie zamówienia i produktów do niego
START TRANSACTION;

INSERT INTO orders (user_id, total_price, status) 
VALUES (1, 100.00, 'pending');

SET @order_id = LAST_INSERT_ID();

INSERT INTO order_products (order_id, product_id, quantity) 
VALUES (@order_id, 2, 1), (@order_id, 3, 2);

COMMIT;

-- 2. Cofnięcie transakcji w razie błędu
START TRANSACTION;

UPDATE orders SET status = 'completed' WHERE id = @order_id;

-- Jeśli coś pójdzie nie tak, cofamy zmiany
IF (SELECT COUNT(*) FROM orders WHERE id = @order_id AND status = 'completed') = 0 THEN
    ROLLBACK;
ELSE
    COMMIT;
END IF;

-- 3. Ustawienie blokady na rekordy dla uniknięcia konfliktów
START TRANSACTION;
SELECT * FROM orders WHERE id = 1 FOR UPDATE;
UPDATE orders SET status = 'cancelled' WHERE id = 1;
COMMIT;
