-- (VIEW) 5) "average_match_players_rating" - информация о среднем рейтинге всех игроков, участвовавших в матче

CREATE OR REPLACE VIEW "average_match_players_rating" AS (
    SELECT "MatchId",
           "thome"."LongName" AS "HomeTeam",
           "taway"."LongName" AS "AwayTeam",
           "Matches"."Date",
           AVG(rating) as "AveragePlayersRating"
    FROM "Matches"
             JOIN "MatchPlayers" MP ON "Matches"."ID" = MP."MatchId"
             JOIN players_last_statistic ON players_last_statistic."ID" = MP."PlayerId"
             JOIN "Teams" taway on "Matches"."AwayTeamId" = taway."ID"
             JOIN "Teams" thome on "Matches"."HomeTeamId" = thome."ID"
    GROUP BY "MatchId", "taway"."LongName", "thome"."LongName", "Matches"."Date"
);

SELECT * FROM average_match_players_rating
LIMIT 100;