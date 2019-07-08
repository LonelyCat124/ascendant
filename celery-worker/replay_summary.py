from typing import Dict, List, Any

Summary = Dict[str, Any]

class ReplaySummariser():

    def __init__(self, parsed_replay_file: str, replay_meta_file: str) -> None:
        """
        Summarises replays. Takes the parsed replay file and a metadata file.
        :param parsed_replay_file: The filename of the parsed replay.
        :param replay_meta_file: The filename of the replay metadata file.
            {
                "replay_id": 123345,
                "radiant_team": "Radiant team name",
                "dire_team": "Dire team name",
                "timestamp": 1562598006 # timestamp of upload
            }
        """
        self.parsed_replay_file = parsed_replay_file
        self.replay_meta_file = replay_meta_file
        self.summarise()

    def summarise(self) -> None:
        """
        Reads the supplied replay and meta files and builds
        the hero and match summaries.
        :return: None
        """
        with open(self.parsed_replay_file, "r") as f:
            self.parsed_replay = [line for line in f]

        # Some parsing stuff here

        self.match_summary = {
            "match_id": 123345,
            "match_date": "2019-07-07", #If we can get it, otherwise upload timestamp from the meta file
            "radiant": "Radiant team name",
            "dire": "Dire team name",
            "radiant_won": True,
            "radiant_kills": 22,
            "dire_kills": 3,
            "duration": 3600, # Time in seconds,
            "first_blood_time": 120, # Time in seconds
            "first_blood_hero": "Hero name",
            "picks": {
                "radiant": {
                    "pick_1": "Hero name",
                    "pick_2": "Hero name"
                    # etc
                },
                "dire": {
                    "pick_1": "Hero name",
                    "pick_2": "Hero name"
                }
            },
            "bans": {
                "radiant": {
                    "ban_1": "Hero name",
                    "ban_2": "Hero name"
                },
                "dire": {
                    "ban_1": "Hero name",
                    "ban_2": "Hero name"
                }
            }
        }

        # A list of player summaries
        self.player_summaries = [
            {
                "match_id": 123345,
                "hero": "Hero name",
                "player": "Player name",
                "team": "Team name",
                "side": "Radiant",
                "won": True,
                "kills": 30,
                "deaths": 5,
                "assists": 6,
                "net_worth": 31493, # At end of game
                "level": 25,
                "gpm": 800,
                "xpm": 400,
                "last_hits": 200,
                "denies": 30,
                "hero_damage": 10000,
                "building_damage": 20000,
                "damage_taken": 5000,
                "biggest_kill_streak": 4,
                "bounty_runes": 4,
                "wards_placed": 5,
                "items": { # Not sure on this data structure
                    "slot_1": {
                        "name": "BKB",
                        "time": 900 # Game time item bought in seconds
                    } # repeat for other item slots and backpack
                },
                "timings": {
                    "gold": {
                        0: 600,
                        1: 800
                        # per minute net worth total
                    },
                    "xp": {
                        0: 0,
                        1: 150
                        # per minute xp total
                    }
                }

            }
        ]