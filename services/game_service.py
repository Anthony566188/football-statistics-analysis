from typing import List, Optional

from dtos.game_response import GameResponse
from models.game import Game


class GameService:
    def calculate(self, games: list[Game]) -> List[GameResponse]:

        data_games = []
        id = 0

        for g in games:
            id += 1

            calculated_data = GameResponse(
                id=id,
                date=g.date,
                result=self._result_from_goals(g),
                total_goals=self._sum_optional(g.home_goals, g.away_goals),
                total_cards=self._sum_optional(g.yellow_cards_home, g.yellow_cards_away),
                total_fouls=self._sum_optional(g.home_fouls, g.away_fouls),
                total_corners=self._sum_optional(g.home_corners, g.away_corners),
            )
            data_games.append(calculated_data)
        return data_games


    def _sum_optional(self, a: Optional[int], b: Optional[int]) -> Optional[int]:
        if a is None or b is None:
            return None
        return a + b



    def _result_from_goals(self, g: Game) -> Optional[str]:
        if g.home_goals is None or g.away_goals is None:
            return None
        if g.home_goals > g.away_goals:
            return g.home_team.upper()
        if g.away_goals > g.home_goals:
            return g.away_team.upper()
        return "DRAW"
