DELIMITER $$

CREATE TRIGGER after_order_update
AFTER UPDATE ON orders
FOR EACH ROW
BEGIN
    INSERT INTO order_logs (order_id, old_total, new_total, changed_at)
    VALUES (OLD.id, OLD.total_price, NEW.total_price, NOW());
END $$

DELIMITER ;
