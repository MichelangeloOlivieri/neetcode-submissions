-- Write your query below

/*
1) No duplicates as there are primary keys; there could be NULLs
2) LEFT JOIN as we are not interested in individuals with NULL names
*/

SELECT
    p.first_name, 
    p.last_name,
    a.city,
    a.state
FROM person AS p
LEFT JOIN address AS a
ON p.person_id = a.person_id


