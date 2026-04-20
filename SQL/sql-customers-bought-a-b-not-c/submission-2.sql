-- Write your query below

WITH A_buyers AS 
(
    SELECT DISTINCT
        customers.customer_id AS customer_id,
        customers.customer_name AS customer_name
    FROM customers
    INNER JOIN orders
    ON customers.customer_id = orders.customer_id
    WHERE product_name = 'A'
),

B_buyers AS 
(
    SELECT DISTINCT
        customers.customer_id AS customer_id,
        customers.customer_name AS customer_name
    FROM customers
    INNER JOIN orders
    ON customers.customer_id = orders.customer_id
    WHERE product_name = 'B'
)

SELECT
    t1.customer_id,
    t1.customer_name
FROM A_buyers AS t1
INNER JOIN B_buyers AS t2
ON t1.customer_id = t2.customer_id
WHERE t1.customer_id NOT IN 
(
    SELECT customer_id
    FROM orders
    WHERE product_name = 'C'
)
ORDER BY t1.customer_name