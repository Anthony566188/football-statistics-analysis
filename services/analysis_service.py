from statistics import mean
from typing import List

from numpy.ma.extras import median

from dtos.analysis_by_market_response import AnalysisByMarketResponse
from dtos.analysis_by_team_response import AnalysisByTeamResponse
from dtos.analysis_response import AnalysisResponse
from dtos.analysis_results_response import AnalysisResultsResponse
from dtos.game_response import GameResponse
from dtos.general_analysis_response import GeneralAnalysisResponse
from dtos.statistical_measure_response import StatisticalMeasuresResponse

from dtos.team_response import TeamResponse
from models.game import Game


class AnalysisService:

    def general_analysis(self, game_responses: List[GameResponse], games: List[Game])\
            -> AnalysisResponse:

        # 1. Gera as estatísticas gerais de todo os jogos
        general_match_statistics = self._calculate_general_metrics(game_responses)

        # 2. Pega os times presentes nos jogos
        teams = list(set(
            team.upper()
            for game in games
            for team in (game.home_team, game.away_team)
        ))

        # 3. Analisa as estatísticas por time
        teams_dicionaly = {}
        for team in teams:
            teams_dicionaly[team] = self._analyze_team(team, games, game_responses)

        # 4. Retorna o DTO final montado
        return AnalysisResponse(
            games=game_responses,
            general_analysis=general_match_statistics,
            analysis_by_team=AnalysisByTeamResponse(teams=teams_dicionaly)

        )



    def _calculate_statistical_measures(self, values: List[int]) -> StatisticalMeasuresResponse:
        """Calcula média, mediana, mínimo e máximo para uma lista de valores."""
        if not values:
            return StatisticalMeasuresResponse(average=0, median=0, minimum=0, maximum=0)

        return StatisticalMeasuresResponse(
            average=mean(values),
            median=median(values),
            minimum=min(values),
            maximum=max(values)
        )

    def _calculate_general_metrics(self, game_respponses: List[GameResponse]) -> GeneralAnalysisResponse:
        """Gera as estatísticas gerais de todos os jogos."""
        goals = [game.total_goals for game in game_respponses]
        cards = [game.total_cards for game in game_respponses]
        fouls = [game.total_fouls for game in game_respponses]
        corners = [game.total_corners for game in game_respponses]

        return GeneralAnalysisResponse(
            goals=self._calculate_statistical_measures(goals),
            cards=self._calculate_statistical_measures(cards),
            fouls=self._calculate_statistical_measures(fouls),
            corners=self._calculate_statistical_measures(corners)
        )

    def _create_market_response(self, matches: int, wins: int, draws: int, losses: int,
                                goals: List[int], cards: List[int], fouls: List[int],
                                corners: List[int]) -> AnalysisByMarketResponse:
        """Cria o objeto AnalysisByMarketResponse reaproveitando a lógica de estatísticas."""

        win_pct = self._win_percentage(matches, wins, draws) if matches > 0 else 0.0

        results_response = AnalysisResultsResponse(
            matches=matches, wins=wins, draws=draws, losses=losses, win_percentage=win_pct
        )

        return AnalysisByMarketResponse(
            results=results_response,
            goals=self._calculate_statistical_measures(goals),
            cards=self._calculate_statistical_measures(cards),
            fouls=self._calculate_statistical_measures(fouls),
            corners=self._calculate_statistical_measures(corners)
        )

    def _analyze_team(self, team: str, games: List[Game], game_responses: List[GameResponse]) -> TeamResponse:
        """Analisa todas as partidas de um único time e retorna o seu TeamResponse."""
        home_matches = home_wins = home_draws = home_losses = 0
        away_matches = away_wins = away_draws = away_losses = 0

        home_goals, home_cards, home_fouls, home_corners = [], [], [], []
        away_goals, away_cards, away_fouls, away_corners = [], [], [], []

        for game, game_response in zip(games, game_responses):
            home_team = game.home_team.upper()
            away_team = game.away_team.upper()

            if team not in (home_team, away_team):
                continue

            if team == home_team:
                home_matches += 1
                home_goals.append(game.home_goals)
                home_cards.append(game.yellow_cards_home)
                home_fouls.append(game.home_fouls)
                home_corners.append(game.home_corners)

                if game_response.result == team:
                    home_wins += 1
                elif game_response.result == "DRAW":
                    home_draws += 1
                else:
                    home_losses += 1

            else:  # team == away_team
                away_matches += 1
                away_goals.append(game.away_goals)
                away_cards.append(game.yellow_cards_away)
                away_fouls.append(game.away_fouls)
                away_corners.append(game.away_corners)

                if game_response.result == team:
                    away_wins += 1
                elif game_response.result == "DRAW":
                    away_draws += 1
                else:
                    away_losses += 1

        # O GERAL é simplesmente a união das listas e soma dos contadores de Casa e Fora
        general_matches = home_matches + away_matches
        general_wins = home_wins + away_wins
        general_draws = home_draws + away_draws
        general_losses = home_losses + away_losses

        return TeamResponse(
            general_analysis=self._create_market_response(
                general_matches, general_wins, general_draws, general_losses,
                home_goals + away_goals, home_cards + away_cards, home_fouls + away_fouls, home_corners + away_corners
            ),
            home_analysis=self._create_market_response(
                home_matches, home_wins, home_draws, home_losses,
                home_goals, home_cards, home_fouls, home_corners
            ),
            away_analysis=self._create_market_response(
                away_matches, away_wins, away_draws, away_losses,
                away_goals, away_cards, away_fouls, away_corners
            )
        )


    def _win_percentage(self, matches: int, wins: int, draws: int) -> float:
        if matches == 0: return 0.0
        points = wins * 3 + draws
        max_points = matches * 3
        return points / max_points * 100