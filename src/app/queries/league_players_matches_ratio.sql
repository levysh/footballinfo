-- (WINDOW) 3) Для каждого игрока выбранной лиги выводит долю сыгранных им матчей в данной лиге среди всех его игр

SELECT
    player_name,
    league_id,
    played_by_player,
    CAST(COUNT(*) AS float) / played_by_player AS ratio_played_in_league
FROM (
         SELECT players."Name"                              AS player_name,
                league_players."LeagueId"                   as league_id,
                COUNT(*) OVER (PARTITION BY players."Name") AS played_by_player
         FROM "Players" AS players
                  INNER JOIN
              "LeaguePlayers" AS league_players on players."ID" = league_players."PlayerId"
     ) AS league_played_info
WHERE
    league_id = {league_id}
GROUP BY
    player_name, league_id, played_by_player