from pydantic import BaseModel
from datetime import date


class GameResponse(BaseModel):
    date: date
    result: str
    total_goals: int
    total_cards: int
    total_fouls: int
    total_corners: int


