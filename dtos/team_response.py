from pydantic import BaseModel

from dtos.statistics_by_market_response import StatisticsByMarketResponse


class TeamResponse(BaseModel):
    matchs: int
    wins: int
    draws: int
    losses: int
    win_percentage: float
    analysis_goals: StatisticsByMarketResponse
    #analysis_cards: StatisticsByMarketResponse
    #analysis_fouls: StatisticsByMarketResponse
    #analysis_corners: StatisticsByMarketResponse