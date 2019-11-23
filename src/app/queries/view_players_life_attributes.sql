-- (VIEW) 4) "players_life_attributes" - содержит характеристику игроков с определенным весом и ростом.
-- На VIEW установлены check option, так что изменить данные неподходящие под фильтр нельзя

CREATE OR REPLACE VIEW "players_life_attributes" AS (
    SELECT "Name", "Birthday", "Height", "Weight"
    FROM "Players"
    WHERE "Height" > {height}
      AND "Weight" < {weight} * 2.2
) WITH CASCADED CHECK OPTION;

SELECT * from players_life_attributes
LIMIT 100;

-- UPDATE players_life_attributes SET "Height"={height} WHERE "Name"='{name}';