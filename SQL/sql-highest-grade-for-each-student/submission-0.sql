-- Write your query below

/*
1) No NULL problems and no duplicate problems (there is a primary key)
2) Use ranking function such as RANK()
*/

WITH rank_cte AS 
(
    SELECT
        student_id, 
        exam_id,
        score,
        ROW_NUMBER() OVER(PARTITION BY student_id ORDER BY score DESC, exam_id ASC) 
        AS grade_rank
    FROM exam_results
)

SELECT 
    student_id, 
    exam_id, 
    score
FROM rank_cte
WHERE grade_rank = 1
ORDER BY student_id ASC;

/*
3) Ok
4) Ok
*/

