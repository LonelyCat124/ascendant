CREATE TABLE IF NOT EXISTS teams(
    team VARCHAR(1023)
);

CREATE TABLE IF NOT EXISTS parsed_replays(
    match_id BIGINT NOT NULL PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS matches(
    match_id BIGINT NOT NULL,
    time_uploaded TIMESTAMP,
    match_date DATE,
    radiant_team VARCHAR(1023),
    dire_team VARCHAR(1023),
    winner VARCHAR(1023),
    loser VARCHAR(1023),
    radiant_kills INT,
    dire_kills INT,
    duration INT,
    first_blood_time TIMESTAMP,
    radiant_hero_1 VARCHAR(1023),
    radiant_hero_2 VARCHAR(1023),
    radiant_hero_3 VARCHAR(1023),
    radiant_hero_4 VARCHAR(1023),
    radiant_hero_5 VARCHAR(1023),
    dire_hero_1 VARCHAR(1023),
    dire_hero_2 VARCHAR(1023),
    dire_hero_3 VARCHAR(1023),
    dire_hero_4 VARCHAR(1023),
    dire_hero_5 VARCHAR(1023),
    radiant_ban_1 VARCHAR(1023),
    radiant_ban_2 VARCHAR(1023),
    radiant_ban_3 VARCHAR(1023),
    radiant_ban_4 VARCHAR(1023),
    radiant_ban_5 VARCHAR(1023),
    dire_ban_1 VARCHAR(1023),
    dire_ban_2 VARCHAR(1023),
    dire_ban_3 VARCHAR(1023),
    dire_ban_4 VARCHAR(1023),
    dire_ban_5 VARCHAR(1023),
    PRIMARY KEY (match_id)
);

CREATE TABLE IF NOT EXISTS player_matches(
    match_id BIGINT REFERENCES matches(match_id) ON DELETE CASCADE,
    hero VARCHAR(1023),
    player VARCHAR(1023) NOT NULL,
    team VARCHAR(1023),
    won BOOLEAN,
    kills INT,
    deaths INT,
    assists INT,
    side VARCHAR(255),
    net_worth INT,
    level INT,
    gpm INT,
    xpm INT,
    bounty_runes INT,
    hero_damage INT,
    building_damage INT,
    damage_taken INT,
    last_hits INT,
    denies INT,
    biggest_kill_streak INT,
    camps_stacked INT,
    item_1 VARCHAR(1023),
    item_2 VARCHAR(1023),
    item_3 VARCHAR(1023),
    item_4 VARCHAR(1023),
    item_5 VARCHAR(1023),
    item_6 VARCHAR(1023),
    item_1_time INT,
    item_2_time INT,
    item_3_time INT,
    item_4_time INT,
    item_5_time INT,
    item_6_time INT,
    backpack_1 VARCHAR(1023),
    backpack_2 VARCHAR(1023),
    backpack_3 VARCHAR(1023),
    backpack_1_time INT,
    backpack_2_time INT,
    backpack_3_time INT,
    PRIMARY KEY(match_id, player)
);