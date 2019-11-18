-- (ANALYTICAL) 5) Для каждой лиги выводит медианое число забитых голов обоими командами в рамках матчей данной лиги

SELECT
    league_name,
    percentile_cont(0.5) WITHIN GROUP ( ORDER BY  total_goals) as median_goals
FROM (
         SELECT leagues."Name"                            as league_name,
                matches."HomeGoals" + matches."AwayGoals" AS total_goals
         FROM "Leagues" as leagues
                  INNER JOIN "Matches" as matches ON leagues."ID" = matches."LeagueId"
     ) as match_results
GROUP BY
    league_name