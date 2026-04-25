-- Write your query below

/*
1) No duplicates; output format?
2) Subquery solution
*/

WITH cte AS
(
    SELECT 
        c.com_id, 
        o.sales_id
    FROM company AS c
    INNER JOIN orders AS o
    ON c.com_id = o.com_id
    WHERE c.name = 'CRIMSON'
)

SELECT name
FROM sales_person AS s
WHERE NOT EXISTS 
(
    SELECT 1
    FROM cte
    WHERE s.sales_id = cte.sales_id
)

