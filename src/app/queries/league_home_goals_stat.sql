-- (ANALYTICAL) 4) Для каждой команды считает минимум, максимум, а также 25, 50, 75 перцентили забитых голов в домашних матчах

SELECT
    teams."LongName" as team_name,
    MIN(matches."HomeGoals") as min_home_goals,
    percentile_disc(0.25) WITHIN GROUP (ORDER BY matches."HomeGoals") as percentile_25_home_goals,
    percentile_disc(0.5) WITHIN GROUP (ORDER BY matches."HomeGoals") as percentile_50_home_goals,
    percentile_disc(0.75) WITHIN GROUP (ORDER BY matches."HomeGoals") as percentile_75_home_goals,
    MAX(matches."HomeGoals") as max_home_goals
FROM "Teams" as teams
INNER JOIN "Matches" as matches ON teams."ID" = matches."AwayTeamId"
GROUP BY
    team_name
ORDER BY
    max_home_goals DESC