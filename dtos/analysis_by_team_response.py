from pydantic import BaseModel

from dtos.team_response import TeamResponse


class AnalysisByTeamResponse(BaseModel):
    teams: dict[str, TeamResponse]