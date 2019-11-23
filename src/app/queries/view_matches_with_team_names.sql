-- (VIEW) 3) "matches_with_team_names" - содержит столбцы с читабельной информацией касаемо сыгранных матчей

CREATE OR REPLACE VIEW "matches_with_team_names" AS (
    SELECT L."Name"             as "League",
           C."Name"             as "Country",
           home_team."LongName" as "HomeTeam",
           away_team."LongName" as "AwayTeam",
           "HomeGoals",
           "AwayGoals",
           "Matches"."Date"
    FROM "Matches"
             JOIN "Leagues" L
                  ON "Matches"."LeagueId" = L."ID"
             JOIN "Countries" C
                  ON "Matches"."CountryId" = C."ID"
             JOIN "Teams" as away_team
                  ON "Matches"."HomeTeamId" = away_team."ID"
             JOIN "Teams" as home_team
                  ON "Matches"."AwayTeamId" = home_team."ID"
);

SELECT *
FROM matches_with_team_names
LIMIT 100;