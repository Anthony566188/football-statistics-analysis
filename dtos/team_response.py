from pydantic import BaseModel

from dtos.statistics_by_market_response import StatisticsByMarketResponse


class TeamResponse(BaseModel):
    matchs: int
    wins: int
    draws: int
    losses: int
    home_wins: int
    home_draws: int
    home_losses: int
    away_wins: int
    away_draws: int
    away_losses: int
    win_percentage_general: float
    win_percentage_home: float
    win_percentage_away: float
    analysis_goals: StatisticsByMarketResponse
    analysis_cards: StatisticsByMarketResponse
    analysis_fouls: StatisticsByMarketResponse
    analysis_corners: StatisticsByMarketResponse