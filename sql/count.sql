SELECT user_id, COUNT(product_name) AS total_products
FROM orders
GROUP BY user_id;
