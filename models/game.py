from typing import Optional

from pydantic import BaseModel
from datetime import date

class Game(BaseModel):
    date: Optional[date]
    home_team: str
    away_team: str
    home_goals: int
    away_goals: int
    yellow_cards_home: int
    yellow_cards_away: int
    home_fouls: int
    away_fouls: int
    home_corners: int
    away_corners: int

