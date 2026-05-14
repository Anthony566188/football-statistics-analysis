from typing import List

from dtos.game_response import GameResponse
from models.game import Game


class GameService:
    def calculate(self, games: list[Game]) -> List[GameResponse]:

        data_games = []
        id = 0

        for g in games:
            id += 1
            result = g.home_team if g.home_goals > g.away_goals else g.away_team
            if g.home_goals == g.away_goals:
                result = "DRAW"

            calculated_data = GameResponse(
                id=id,
                date=g.date,
                result=result.upper(),
                total_goals=g.home_goals + g.away_goals,
                total_cards=g.yellow_cards_home + g.yellow_cards_away,
                total_fouls=g.home_fouls + g.away_fouls,
                total_corners=g.home_corners + g.away_corners
            )
            data_games.append(calculated_data)
        return data_games