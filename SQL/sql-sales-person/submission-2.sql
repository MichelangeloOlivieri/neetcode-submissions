-- Write your query below

/*
1) No duplicates; output format?
2) Subquery solution
*/

SELECT name
FROM sales_person AS s
WHERE NOT EXISTS
(
    SELECT 1
    FROM orders AS o
    INNER JOIN company AS c
    ON o.com_id = c.com_id
    WHERE c.name = 'CRIMSON' AND s.sales_id = o.sales_id
)

