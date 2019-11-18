-- (WINDOW) 1) ТОП-k самых высоких игроков с указанием того, скольких человек они выше

SELECT
    "Name", "Height", COUNT("ID") OVER(ORDER BY "Height") AS "Taller_than"
FROM
    "Players"
ORDER BY
    "Height" DESC
LIMIT
    {count};