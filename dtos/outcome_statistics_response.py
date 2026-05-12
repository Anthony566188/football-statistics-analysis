from pydantic import BaseModel


class OutcomeStatisticsResponse(BaseModel):
    matches: int
    wins: int
    draws: int
    losses: int
    win_percentage: float