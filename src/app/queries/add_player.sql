INSERT INTO "Players" ("Name", "Birthday", "Height", "Weight", "OverallRating", "Potential", "Balance", "CountryID")
VALUES ('{name}',
        '{birthday}',
        {height},
        {weight} * 2.2,
        {rating},
        {potential},
        {balance},
        (SELECT "ID" from "Countries" where "Countries"."Name" = '{country}')
);
COMMIT;

SELECT "Players"."ID", "Players"."Name", "Birthday", "Height", "Weight" as "Weight(lbs)", "OverallRating", "Potential", "Balance", "Countries"."Name"
    FROM "Players" join "Countries" on "Players"."CountryID" = "Countries"."ID" where "Players"."Name" = '{name}';