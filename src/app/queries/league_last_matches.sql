-- (ANALYTICAL) 3) Для выбранной лиги выводит последние сыгранные матчи с указанием его порядкового номера

SELECT
    matches."ID" as match_id,
    teams."LongName" as home_team,
    sub_query.away_name as away_team,
    matches."Date" as match_date,
    RANK() OVER(ORDER BY matches."Date") as match_number
FROM "Matches" as matches
INNER JOIN "Teams" as teams ON matches."HomeTeamId" = teams."ID"
INNER JOIN (
        SELECT
            matches."ID" as match_id,
            teams."LongName" as away_name
        FROM
            "Matches" as matches
        INNER JOIN "Teams" as teams ON matches."AwayTeamId" = teams."ID"
        WHERE
            matches."LeagueId" = {league_id}
     ) as sub_query ON matches."ID" = sub_query.match_id
ORDER BY
    match_date DESC
LIMIT
    {count}