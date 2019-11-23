-- (VIEW) 1) "teams_per_country" - содержит столбцы со всеми командами а также информацией о стране и лиге в которой они играют
CREATE OR REPLACE VIEW
teams_per_country
AS
(
    SELECT DISTINCT "Countries"."Name" as "Country", L."Name" as "League", T."LongName" as "TeamName"
    FROM
        "Countries"
        JOIN "Leagues" L
            on "Countries"."ID" = L."Country_id"
        JOIN "LeagueTeams" LT
            on L."ID" = LT."LeagueId"
        JOIN "Teams" T
            on LT."TeamId" = T."ID"
);

SELECT *
FROM teams_per_country;