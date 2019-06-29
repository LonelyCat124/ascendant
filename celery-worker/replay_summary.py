from typing import Dict, List, Any

Replay = Dict[Any, Any]
Summary = Dict[str, Any]

class ReplaySummariser():

    def __init__(self, parsed_replay: Replay)-> None:
        self.parsed_replay = parsed_replay
        self.summarise()

    def summarise(self) -> None:
        raise NotImplementedError

    def match_summary(self) -> Summary:
        raise NotImplementedError
    
    def hero_summary(self) -> List[Summary]:
        raise NotImplementedError

    def item_summary(self) -> List[Summary]:
        raise NotImplementedError