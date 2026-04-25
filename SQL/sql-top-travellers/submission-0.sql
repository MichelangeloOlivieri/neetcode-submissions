-- Write your query below

/*
1) No duplicates as there is a primary key
2) JOIN and GROUP BY
*/

SELECT
    u.name,
    SUM(COALESCE(r.distance, 0)) AS travelled_distance
FROM users AS u
LEFT JOIN rides AS r
ON u.id = r.user_id 
GROUP BY u.id
ORDER BY travelled_distance DESC, u.name ASC;