-- (SELECT) 6) Средний рост/вес/возраст игроков по стране
SELECT
"Countries"."Name" as "Country",
SUM("Height") / COUNT(*) as "MeanHeigh",
SUM("Weight") / COUNT(*) as "MeanWeight",
SUM(extract(YEAR from now()) - extract(YEAR from "Birthday"::timestamp)) / COUNT(*) as "MeanAge"
FROM "Players"
INNER JOIN "LeaguePlayers" ON "Players"."ID" = "LeaguePlayers"."PlayerId"
INNER JOIN "Leagues" on "LeaguePlayers"."LeagueId" = "Leagues"."ID"
INNER JOIN "Countries" on "Leagues"."Country_id" = "Countries"."ID"
GROUP BY "Countries"."Name"
ORDER BY "Countries"."Name" ASC