from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class Game(BaseModel):
    date: Optional[date]# = None
    home_team: str = Field(..., min_length=1)
    away_team: str = Field(..., min_length=1)
    home_goals: Optional[int]# = None
    away_goals: Optional[int]# = None
    yellow_cards_home: Optional[int]# = None
    yellow_cards_away: Optional[int]# = None
    home_fouls: Optional[int]# = None
    away_fouls: Optional[int]# = None
    home_corners: Optional[int]# = None
    away_corners: Optional[int]# = None

