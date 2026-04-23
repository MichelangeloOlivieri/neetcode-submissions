-- Write your query below

/*
1) No duplicates as there is a primary key; there could be NULLs
2) Maybe even without JOINs
*/

SELECT seller_name
FROM seller AS s
WHERE NOT EXISTS
(
    SELECT 1
    FROM orders AS o
    WHERE s.seller_id = o.seller_id AND EXTRACT(YEAR FROM o.sale_date) = 2020
)
ORDER BY seller_name ASC