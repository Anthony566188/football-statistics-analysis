from pydantic import BaseModel

from dtos.statistics_by_market_response import StatisticsByMarketResponse


class GeneralAnalysisResponse(BaseModel):
    goals: StatisticsByMarketResponse
    cards: StatisticsByMarketResponse
    fouls: StatisticsByMarketResponse
    corners: StatisticsByMarketResponse