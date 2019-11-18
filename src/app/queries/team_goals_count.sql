-- (SELECT) 5) Количество забитых мячей у каждой команды с учтом количества сыгранных ею матчей
SELECT "LongName" as "TeamName", SUM(goals) as "TotalGoals", COUNT(*) as "MatchesPlayed"
FROM (
SELECT "Teams"."LongName", "HomeGoals" AS goals
FROM "Matches"
INNER JOIN "Teams" ON "Matches"."HomeTeamId" = "Teams"."ID"
UNION ALL
SELECT "Teams"."LongName", "AwayGoals" AS goals
FROM "Matches"
INNER JOIN "Teams" ON "Matches"."AwayTeamId" = "Teams"."ID"
) AS goals_scored
GROUP BY "LongName"
ORDER BY "TotalGoals" DESC;