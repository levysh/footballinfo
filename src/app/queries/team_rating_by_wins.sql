-- (ANALYTICAL) 1) Для каждой команды выводит количество побед и её перцентиль в рейтинге по количеству побед среди всех команд

SELECT
    "Teams"."LongName" as team_name,
    teams_stats.wins_count,
    CUME_DIST() OVER (ORDER BY teams_stats.wins_count) as percentile
FROM (
         SELECT team_id,
                SUM(wins_count) AS wins_count
         FROM (
                  SELECT "HomeTeamId" AS team_id,
                         COUNT("ID")  as wins_count
                  FROM "Matches"
                  WHERE "HomeGoals" > "AwayGoals"
                  GROUP BY "HomeTeamId"

                  UNION ALL

                  SELECT "AwayTeamId" AS team_id,
                         COUNT("ID")  as wins_count
                  FROM "Matches"
                  WHERE "AwayGoals" > "HomeGoals"
                  GROUP BY "AwayTeamId"
              ) as united
         GROUP BY team_id
     ) as teams_stats
INNER JOIN "Teams" ON teams_stats.team_id = "Teams"."ID"
ORDER BY
    teams_stats.wins_count DESC