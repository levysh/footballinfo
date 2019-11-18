-- (WINDOW) 5) Для всех команд выбранной лиги считает количество забитых голов в матчах лиги и отставание от следующей команды (в забитых голах)
SELECT
    total_scores.team_id,
    total_scores.scored_goals,
    COALESCE(LEAD(total_scores.scored_goals) OVER (ORDER BY total_scores.scored_goals) - total_scores.scored_goals, 0) as next_team_gap
FROM (
    SELECT
        team_id,
        SUM(scored_goals) as scored_goals
    FROM (
        SELECT
            "HomeTeamId" as team_id,
            SUM("HomeGoals") as scored_goals
        FROM
            "Matches"
        WHERE
            "LeagueId" = {league_id}
        GROUP BY
            team_id
        UNION ALL
        SELECT
            "AwayTeamId" as team_id,
            SUM("AwayGoals") as scored_goals
        FROM
            "Matches"
        WHERE
            "LeagueId" = {league_id}
        GROUP BY
            team_id
    ) as home_away_scores
    GROUP BY
        team_id
) as total_scores
ORDER BY
    total_scores.scored_goals DESC