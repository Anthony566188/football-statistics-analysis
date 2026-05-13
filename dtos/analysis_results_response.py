from pydantic import BaseModel


class AnalysisResultsResponse(BaseModel):
    matches: int
    wins: int
    draws: int
    losses: int
    win_percentage: float