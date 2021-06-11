SELECT
    salary * months AS TOTAL,
    COUNT(employee_id)
FROM
    Employee
GROUP BY
    TOTAL
ORDER BY
    TOTAL DESC
LIMIT 1
;