from pydantic import BaseModel

from dtos.analysis_results_response import AnalysisResultsResponse
from dtos.statistical_measure_response import StatisticalMeasuresResponse


class AnalysisByMarketResponse(BaseModel):
    results: AnalysisResultsResponse
    goals: StatisticalMeasuresResponse
    cards: StatisticalMeasuresResponse
    fouls: StatisticalMeasuresResponse
    corners: StatisticalMeasuresResponse