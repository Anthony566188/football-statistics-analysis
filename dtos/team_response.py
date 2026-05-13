from pydantic import BaseModel

from dtos.analysis_by_market_response import AnalysisByMarketResponse

class TeamResponse(BaseModel):
    # general
    general_analysis: AnalysisByMarketResponse
    # home
    home_analysis: AnalysisByMarketResponse
    # away
    away_analysis: AnalysisByMarketResponse

'''    analysis_goals: StatisticalMeasuresResponse
    analysis_cards: StatisticalMeasuresResponse
    analysis_fouls: StatisticalMeasuresResponse
    analysis_corners: StatisticalMeasuresResponse'''