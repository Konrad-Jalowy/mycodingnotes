SELECT user_id, GROUP_CONCAT(product_name SEPARATOR ', ') AS products_list
FROM orders
GROUP BY user_id;
