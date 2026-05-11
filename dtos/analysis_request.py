from pydantic import BaseModel, ConfigDict

from models.game import Game

class AnalysisRequest(BaseModel):
    model_config = ConfigDict(extra='forbid')  # Isso fará a API retornar erro 422 se houver campos extras
    games: list[Game]

'''    def to_entity(self):

        return Analysis(
            games=self.games,
            
        )
'''
