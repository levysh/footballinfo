-- (SELECT) 1) Топ команд по количеству игравших в них игроков
SELECT "LongName" as "Team", "players_cnt" as "Players_played_for_team" FROM (
SELECT team."LongName", COUNT(DISTINCT team_players."PlayerId") as players_cnt
FROM "Teams" AS team
INNER JOIN "TeamsPlayers" AS team_players on team."ID" = team_players."TeamId"
GROUP BY team."ID"
) AS team_players_total
ORDER BY players_cnt DESC
LIMIT {count};
