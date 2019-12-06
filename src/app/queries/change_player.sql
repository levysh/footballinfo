UPDATE "Players" SET
"Height" = {height},
"Weight" = {weight},
"OverallRating" = {rating},
"Potential" = {potential},
"Balance" = {balance}
WHERE "Name" = '{name}';

INSERT INTO "LeaguePlayers" ("Date", "PlayerId", "LeagueId") VALUES
(
date_trunc('seconds', now()),  (SELECT "ID" FROM "Players" where "Name" = '{name}'), (SELECT "ID" FROM "Leagues" where "Name" = '{league}')
);
COMMIT;

SELECT "Players"."ID",
       "Players"."Name",
       "Birthday",
       "Height",
       "Weight",
       "OverallRating",
       "Potential",
       "Balance",
       "Countries"."Name" as "CountryOfBirth",
       "Leagues"."Name" as "League",
       "Date"
    FROM "Players"
        join "Countries" on "Players"."CountryID" = "Countries"."ID"
        join "LeaguePlayers" on "Players"."ID" = "LeaguePlayers"."PlayerId"
        join "Leagues" on "LeaguePlayers"."LeagueId" = "Leagues"."ID"
where "Players"."Name" = '{name}'
ORDER BY "Date" DESC LIMIT 10;