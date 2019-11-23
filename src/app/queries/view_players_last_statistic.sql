-- (VIEW) 2) "players_last_statistic" - содержит столбцы со всеми игроками, их основной статистикой относительно последнего обновления информации

CREATE OR REPLACE VIEW players_last_statistic
    AS (
    WITH latest_players_attr AS
             (
                 SELECT player_api_id as "ID", MAX(date) as last_ts
                 FROM players_attributes
                 GROUP BY player_api_id
             )
    SELECT player_api_id       as "ID",
           date                as "LastTimestamp",
           overall_rating      as rating,
           preferred_foot      as foot,
           attacking_work_rate as attack,
           defensive_work_rate as defence
    FROM players_attributes,
         latest_players_attr
    WHERE players_attributes.player_api_id = latest_players_attr."ID"
      AND players_attributes.date = latest_players_attr.last_ts
      AND players_attributes.overall_rating IS NOT NULL
      AND players_attributes.preferred_foot IS NOT NULL
);

SELECT * FROM players_last_statistic
LIMIT 100;