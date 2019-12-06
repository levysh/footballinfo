DELETE FROM "LeaguePlayers" WHERE "PlayerId" = (SELECT "ID" FROM "Players" where "Name" = '{name}');
COMMIT;
SELECT 'DONE';