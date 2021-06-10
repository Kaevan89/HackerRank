SELECT
    DISTINCT CITY
FROM
    STATION
WHERE
    MOD(ID, 2) = 0
ORDER BY
    CITY
;