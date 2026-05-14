from typing import Union, Optional

from pydantic import BaseModel
from datetime import date


class GameResponse(BaseModel):
    id: int
    date: Optional[date]
    result: str
    total_goals: int
    total_cards: int
    total_fouls: int
    total_corners: int


