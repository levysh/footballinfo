INSERT INTO "Players" ("Name", "Birthday", "Height", "Weight") VALUES ('{name}', '{birthday}', {height}, {weight});
COMMIT;

SELECT * from "Players" WHERE "Name" = '{name}';