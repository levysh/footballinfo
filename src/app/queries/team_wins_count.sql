-- (SELECT) 2) Количество побед каждой из команд в каждой лиге
SELECT leauge_name, team_name, COUNT(*) as wins_count
FROM (
SELECT league."Name" AS leauge_name, team."LongName" AS team_name
FROM "Leagues" as league
INNER JOIN "Matches" as match on league."ID" = match."LeagueId"
INNER JOIN "Teams" as team on match."HomeTeamId" = team."ID"
WHERE match."HomeGoals" > match."AwayGoals"
UNION ALL
SELECT league."Name" AS leauge_name, team."LongName" AS team_name
FROM "Leagues" as league
INNER JOIN "Matches" as match on league."ID" = match."LeagueId"
INNER JOIN "Teams" as team on match."AwayTeamId" = team."ID"
WHERE match."AwayGoals" > match."HomeGoals"
) as winners_table
GROUP BY leauge_name, team_name
ORDER BY wins_count DESC;