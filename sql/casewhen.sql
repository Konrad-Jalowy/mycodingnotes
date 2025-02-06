SELECT first_name, last_name, 
    CASE 
        WHEN age < 18 THEN 'Niepełnoletni'
        WHEN age BETWEEN 18 AND 65 THEN 'Dorosły'
        ELSE 'Senior'
    END AS user_category
FROM users;
