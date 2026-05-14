from typing import Optional
from pydantic import BaseModel
from datetime import date


class GameResponse(BaseModel):
    id: int
    date: Optional[date]
    result: Optional[str]
    total_goals: Optional[int]
    total_cards: Optional[int]
    total_fouls: Optional[int]
    total_corners: Optional[int]


