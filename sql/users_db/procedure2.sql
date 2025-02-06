DELIMITER $$

CREATE PROCEDURE GetUserOrderCount(IN userId INT, OUT orderCount INT)
BEGIN
    SELECT COUNT(*) INTO orderCount FROM orders WHERE user_id = userId;
END $$

DELIMITER ;

CALL GetUserOrderCount(1, @orderCount);
SELECT @orderCount;
