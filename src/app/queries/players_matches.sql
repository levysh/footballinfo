-- (SELECT) 3) Топ игроков по числу сыгранных матчей, а также количество команд за которые они играли
SELECT tp."Name", COUNT(DISTINCT match_players."MatchId") as "MatchCount", tp."TeamsCount"
FROM (
SELECT player."ID", player."Name", COUNT(DISTINCT team_players."TeamId") as "TeamsCount" FROM
"Players" AS player
INNER JOIN "TeamsPlayers" AS team_players on player."ID" = team_players."PlayerId"
GROUP BY player."ID"
) AS tp
INNER JOIN "MatchPlayers" as match_players on match_players."PlayerId" = tp."ID"
GROUP BY tp."ID", tp."Name", tp."TeamsCount"
ORDER BY "MatchCount" DESC
LIMIT {count};