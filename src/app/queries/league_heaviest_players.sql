-- (ANALYTICAL) 2) Выводит топ игроков заданной лиги по их весу с указанием процента игроков, которые легче

SELECT
    DISTINCT players."Name" as player_name,
    players."Weight" as weight,
    PERCENT_RANK() OVER (ORDER BY players."Weight") as heavy_percentile
FROM
    "Players" as players
INNER JOIN "LeaguePlayers" as league_players on players."ID" = league_players."PlayerId"
WHERE
    league_players."LeagueId" = {league_id}
ORDER BY
    weight DESC