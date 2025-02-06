SELECT 
    SUM(CASE WHEN orders.status = 'completed' THEN orders.total_price ELSE 0 END) AS total_completed,
    SUM(CASE WHEN orders.status = 'pending' THEN orders.total_price ELSE 0 END) AS total_pending
FROM orders;
