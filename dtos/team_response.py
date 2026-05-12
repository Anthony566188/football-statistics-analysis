from pydantic import BaseModel

from dtos.outcome_statistics_response import OutcomeStatisticsResponse
from dtos.statistics_by_market_response import StatisticsByMarketResponse


class TeamResponse(BaseModel):
    # general
    analysis_results_general: OutcomeStatisticsResponse
    # home
    home_analysis: OutcomeStatisticsResponse
    # away
    away_analysis: OutcomeStatisticsResponse

    analysis_goals: StatisticsByMarketResponse
    analysis_cards: StatisticsByMarketResponse
    analysis_fouls: StatisticsByMarketResponse
    analysis_corners: StatisticsByMarketResponse