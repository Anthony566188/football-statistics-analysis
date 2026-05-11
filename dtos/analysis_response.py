from typing import List

from pydantic import BaseModel

from dtos.analysis_by_team_response import AnalysisByTeamResponse
from dtos.game_response import GameResponse
from dtos.general_analysis_response import GeneralAnalysisResponse


class AnalysisResponse(BaseModel):

    games: List[GameResponse]
    general_analysis: GeneralAnalysisResponse
    analysis_by_team: AnalysisByTeamResponse


'''   @staticmethod
    def from_entity(teste):
        return AnalysisResponse(
            games=teste.games
        )
 '''