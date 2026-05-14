from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class Game(BaseModel):
    date: Optional[date]
    home_team: str = Field(..., min_length=1)
    away_team: str = Field(..., min_length=1)
    home_goals: Optional[int]
    away_goals: Optional[int]
    yellow_cards_home: Optional[int]
    yellow_cards_away: Optional[int]
    home_fouls: Optional[int]
    away_fouls: Optional[int]
    home_corners: Optional[int]
    away_corners: Optional[int]

