SELECT user_id, JSON_ARRAYAGG(product_name) AS products_list
FROM orders
GROUP BY user_id;
