-- (WINDOW) 2) Для игроков из выбранной лиги считает количество игроков, которые старше его

SELECT
    filtered_league.player_name,
    filtered_league.player_birthday,
    filtered_league.league_id,
    COUNT(player_id) OVER (PARTITION BY filtered_league.league_id ORDER BY filtered_league.player_birthday) AS younger_than
FROM (
         SELECT DISTINCT players."Name"            AS player_name,
                         players."ID"              AS player_id,
                         players."Birthday"        AS player_birthday,
                         league_players."LeagueId" AS league_id
         FROM "Players" AS players
                  INNER JOIN
              "LeaguePlayers" AS league_players on players."ID" = league_players."PlayerId"
         WHERE league_players."LeagueId" = {league_id}
     ) AS filtered_league
ORDER BY
    younger_than DESC
LIMIT
    {count}