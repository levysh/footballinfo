-- (WINDOW) 4) Для каждой команды считает количество забитых и пропущенных голов

SELECT
    team_name,
    SUM(scored_goals) as scored_goals,
    SUM(missed_goals) AS missed_goals
FROM (
         SELECT teams."LongName"                                        AS team_name,
                SUM(matches."AwayGoals") OVER (PARTITION BY teams."ID") as scored_goals,
                SUM(matches."HomeGoals") OVER (PARTITION BY teams."ID") as missed_goals
         FROM "Matches" as matches
                  INNER JOIN
              "Teams" as teams ON matches."AwayTeamId" = teams."ID"
        UNION ALL
        SELECT teams."LongName"                                        AS team_name,
               SUM(matches."AwayGoals") OVER (PARTITION BY teams."ID") as missed_goals,
               SUM(matches."HomeGoals") OVER (PARTITION BY teams."ID") as scored_goals
         FROM "Matches" as matches
                  INNER JOIN
              "Teams" as teams ON matches."HomeGoals" = teams."ID"
     ) AS team_scores
GROUP BY
    team_name
ORDER BY
    scored_goals DESC