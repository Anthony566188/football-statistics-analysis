from pydantic import BaseModel
from datetime import date

class Game(BaseModel):
    date: date
    home_team: str
    away_team: str
    home_goals: int
    away_goals: int
    yellow_cards_home: int
    yellow_cards_away: int
    fouls_home: int
    fouls_away: int
    corners_home: int
    corners_away: int

