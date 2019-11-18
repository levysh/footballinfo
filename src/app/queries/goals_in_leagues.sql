-- (SELECT) 4) Количество забитых мячей во всех матчах лиги с учетом количества сыгранных матчей в лиге
SELECT "Name", SUM(total_goals_per_match) AS "TotalGoals", COUNT(*) as "MathesPlayed" FROM (
SELECT "Leagues"."Name", "HomeGoals" + "AwayGoals" AS total_goals_per_match
FROM "Matches"
INNER JOIN "Leagues" ON "Matches"."LeagueId" = "Leagues"."ID"
) AS match_goals
GROUP BY "Name"
ORDER BY "TotalGoals" DESC;