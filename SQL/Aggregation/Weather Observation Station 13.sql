SELECT
    ROUND(SUM(LAT_N), 4)
FROM
    STATION
WHERE
    LAT_N BETWEEN 38.7800 AND 137.2345
;