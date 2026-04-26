-- Write your query below

/*
1) No duplicates; possible NULLs in the first table; output format?
2) A join would do
*/

SELECT 
    left_operand, 
    operator, 
    right_operand,
    CASE
        WHEN operator = '<' AND v1.value < v2.value THEN True
        WHEN operator = '=' AND v1.value = v2.value THEN True
        WHEN operator = '>' AND v1.value > v2.value THEN True
        ELSE False
    END AS value
FROM expressions AS e
INNER JOIN variables AS v1
ON e.left_operand = v1.name
INNER JOIN variables AS v2
ON e.right_operand = v2.name;