from fastapi import APIRouter

from dtos.analysis_request import AnalysisRequest
from dtos.analysis_response import AnalysisResponse
from services.analysis_service import AnalysisService
from services.game_service import GameService

router = APIRouter()

game_service = GameService()
analysis_service = AnalysisService()

@router.post("/analysis", response_model=AnalysisResponse)
def return_analysis(analysis_request: AnalysisRequest):

    calculated_games = game_service.calculate(analysis_request.games)

    analysis_response = analysis_service.general_analysis(calculated_games, games=analysis_request.games)

    # Retorna a DTO de resposta
    return analysis_response