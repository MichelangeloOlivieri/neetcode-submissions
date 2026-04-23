-- Write your query below

/*
1) No duplicates as there is a primary key; there could be NULLs
2) Maybe even without JOINs
*/

SELECT 
    seller_name
FROM seller
WHERE seller_id NOT IN
(
    SELECT 
        seller_id
    FROM orders
    WHERE EXTRACT(YEAR FROM sale_date) = 2020
)
ORDER BY seller_name ASC