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

        teams_dicionaly = {}

        for team in teams:
            matches = 0
            home_matches = 0
            away_matches = 0
            wins = 0
            home_wins = 0
            away_wins = 0
            draws = 0
            home_draws = 0
            away_draws = 0
            losses = 0
            home_losses = 0
            away_losses = 0
            goals_by_match_team = []
            home_goals = []
            away_goals = []
            cards_by_match_team = []
            home_cards = []
            away_cards = []
            fouls_by_match_team = []
            home_fouls = []
            away_fouls = []
            corners_by_match_team = []
            home_corners = []
            away_corners = []




            for game, game_response in zip(games, game_responses):

                home_team = game.home_team.upper()
                away_team = game.away_team.upper()

                # Pula para a próxima iteração se o time não estiver presente na partida
                if team != home_team and team != away_team:
                    continue

                matches += 1



                # Calcula vitórias, empates e derrotas usando o DTO de resposta
                if game_response.result == team:
                    wins += 1
                elif game_response.result == "DRAW":
                    draws += 1
                else:
                    losses += 1

                # Separa os gols do time de Fora na lista
                if away_team == team:
                    goals_by_match_team.append(game.away_goals)
                    away_goals.append(game.away_goals)
                    away_cards.append(game.yellow_cards_away)
                    away_fouls.append(game.away_fouls)
                    away_corners.append(game.away_corners)

                    cards_by_match_team.append(game.yellow_cards_away)
                    fouls_by_match_team.append(game.away_fouls)
                    corners_by_match_team.append(game.away_corners)

                    away_matches += 1

                    # Verifica se o time venceu
                    if away_team == game_response.result:
                        away_wins += 1

                    # Verifica se o time EMPATOU
                    if game_response.result == "DRAW":
                        away_draws += 1

                    # Verifica se time PERDEU
                    if game_response.result != away_team and game_response.result != "DRAW":
                        away_losses += 1

                # Verfica se o time jogou em CASA
                if home_team == team:
                    # Separa os gols do time na lista
                    goals_by_match_team.append(game.home_goals)
                    # Adiciona na lista de gols em CASA
                    home_goals.append(game.home_goals)
                    # Adiciona na lista de cartões em CASA
                    home_cards.append(game.yellow_cards_home)
                    # Adiciona na lista de faltas em CASA
                    home_fouls.append(game.home_fouls)
                    # Adiciona na lista de escanteios em CASA
                    home_corners.append(game.home_corners)

                    cards_by_match_team.append(game.yellow_cards_home)
                    fouls_by_match_team.append(game.home_fouls)
                    corners_by_match_team.append(game.home_corners)
                    home_matches += 1

                    # Verifica se o time venceu
                    if home_team == game_response.result:
                        home_wins += 1

                    # Verifica se o time EMPATOU
                    if game_response.result == "DRAW":
                        home_draws += 1

                    # Verifica se time PERDEU
                    if game_response.result != home_team and game_response.result != "DRAW":
                        home_losses += 1



            # Calcula o aproveitamento do time no GERAL
            win_percentage_general = self._win_percentage(matches, wins, draws)

            # Calcula o aproveitamento do time em CASA
            win_percentage_home = self._win_percentage(home_matches, home_wins, home_draws)

            # Calcula o aproveitamento do time jogando FORA
            win_percentage_away = self._win_percentage(away_matches, away_wins, away_draws)


            # Estatísticas de Gols do TIME GERAL
            average_goals = mean(goals_by_match_team) if goals_by_match_team else 0.0
            median_goals = median(goals_by_match_team) if goals_by_match_team else 0.0
            min_goals = min(goals_by_match_team) if goals_by_match_team else 0.0
            max_goals = max(goals_by_match_team) if goals_by_match_team else 0.0

            # Estatísticas de Gols do time em CASA
            home_goals_average = mean(home_goals) if home_goals else 0.0
            home_goals_median = median(home_goals) if home_goals else 0.0
            home_goals_min = min(home_goals) if home_goals else 0.0
            home_goals_max = max(home_goals) if home_goals else 0.0

            # Estatísticas de Gols do time FORA
            away_goals_average = mean(away_goals) if away_goals else 0.0
            away_goals_median = median(away_goals) if away_goals else 0.0
            away_goals_min = min(away_goals) if away_goals else 0.0
            away_goals_max = max(away_goals) if away_goals else 0.0


            # Estatísticas de Cartões do TIME GERAL
            average_cards = mean(cards_by_match_team) if cards_by_match_team else 0.0
            median_cards = median(cards_by_match_team) if cards_by_match_team else 0.0
            min_cards = min(cards_by_match_team) if cards_by_match_team else 0.0
            max_cards = max(cards_by_match_team) if cards_by_match_team else 0.0

            # Estatísticas de Cartões do time em CASA
            home_cards_average = mean(home_cards) if home_cards else 0.0
            home_cards_median = median(home_cards) if home_cards else 0.0
            home_cards_min = min(home_cards) if home_cards else 0.0
            home_cards_max = max(home_cards) if home_cards else 0.0

            # Estatísticas de Cartões do time FORA
            away_cards_average = mean(away_cards) if away_cards else 0.0
            away_cards_median = median(away_cards) if away_cards else 0.0
            away_cards_min = min(away_cards) if away_cards else 0.0
            away_cards_max = max(away_cards) if away_cards else 0.0

            # Estatísticas de Faltas do TIME GERAL
            average_fouls = mean(fouls_by_match_team) if fouls_by_match_team else 0.0
            median_fouls = median(fouls_by_match_team) if fouls_by_match_team else 0.0
            min_fouls = min(fouls_by_match_team) if fouls_by_match_team else 0.0
            max_fouls = max(fouls_by_match_team) if fouls_by_match_team else 0.0

            # Estatísticas de Faltas do time em CASA
            home_fouls_average = mean(home_fouls) if home_fouls else 0.0
            home_fouls_median = median(home_fouls) if home_fouls else 0.0
            home_fouls_min = min(home_fouls) if home_fouls else 0.0
            home_fouls_max = max(home_fouls) if home_fouls else 0.0

            # Estatísticas de Faltas do time FORA
            away_fouls_average = mean(away_fouls) if away_fouls else 0.0
            away_fouls_median = median(away_fouls) if away_fouls else 0.0
            away_fouls_min = min(away_fouls) if away_fouls else 0.0
            away_fouls_max = max(away_fouls) if away_fouls else 0.0



            # Estatísticas de Escanteios do TIME GERAL
            average_corners = mean(corners_by_match_team) if corners_by_match_team else 0.0
            median_corners = median(corners_by_match_team) if corners_by_match_team else 0.0
            min_corners = min(corners_by_match_team) if corners_by_match_team else 0.0
            max_corners = max(corners_by_match_team) if corners_by_match_team else 0.0

            # Estatísticas de Escanteios do time em CASA
            home_corners_average = mean(home_corners) if home_corners else 0.0
            home_corners_median = median(home_corners) if home_corners else 0.0
            home_corners_min = min(home_corners) if home_corners else 0.0
            home_corners_max = max(home_corners) if home_corners else 0.0

            # Estatísticas de Escanteios do time FORA
            away_corners_average = mean(away_corners) if away_corners else 0.0
            away_corners_median = median(away_corners) if away_corners else 0.0
            away_corners_min = min(away_corners) if away_corners else 0.0
            away_corners_max = max(away_corners) if away_corners else 0.0





            general_results_analysis_team = AnalysisResultsResponse(matches=matches, wins=wins, draws=draws, losses=losses,
                                                       win_percentage=win_percentage_general)

            general_goals_analysis_team = StatisticalMeasuresResponse(average=average_goals, median=median_goals, minimum=min_goals, maximum=max_goals)

            general_cards_analysis_team = StatisticalMeasuresResponse(average=average_cards, median=median_cards, minimum=min_cards, maximum=max_cards)

            general_fouls_analysis_team = StatisticalMeasuresResponse(average=average_fouls, median=median_fouls, minimum=min_fouls, maximum=max_fouls)

            general_corners_analysis_team = StatisticalMeasuresResponse(average=average_corners, median=median_corners, minimum=min_corners, maximum=max_corners)

            general_analysis = AnalysisByMarketResponse(results=general_results_analysis_team, goals=general_goals_analysis_team, cards=general_cards_analysis_team, fouls=general_fouls_analysis_team, corners=general_corners_analysis_team)

            # Análise em CASA
            home_results_analysis = AnalysisResultsResponse(matches=home_matches, wins=home_wins, draws=home_draws, losses=home_losses, win_percentage=win_percentage_home)

            home_goals_analysis = StatisticalMeasuresResponse(average=home_goals_average, median=home_goals_median, minimum=home_goals_min, maximum=home_goals_max)

            home_cards_analysis = StatisticalMeasuresResponse(average=home_cards_average, median=home_cards_median, minimum=home_cards_min, maximum=home_cards_max)

            home_fouls_analysis = StatisticalMeasuresResponse(average=home_fouls_average, median=home_fouls_median, minimum=home_fouls_min, maximum=home_fouls_max)

            home_corners_analysis = StatisticalMeasuresResponse(average=home_corners_average, median=home_corners_median, minimum=home_corners_min, maximum=home_corners_max)

            home_analysis = AnalysisByMarketResponse(results=home_results_analysis, goals=home_goals_analysis, cards=home_cards_analysis, fouls=home_fouls_analysis, corners=home_corners_analysis)

            # Análise FORA
            away_results_analysis = AnalysisResultsResponse(matches=away_matches, wins=away_wins, draws=away_draws, losses=away_losses, win_percentage=win_percentage_away)

            away_goals_analysis = StatisticalMeasuresResponse(average=away_goals_average, median=away_goals_median, minimum=away_goals_min, maximum=away_goals_max)

            away_cards_analysis = StatisticalMeasuresResponse(average=away_cards_average, median=away_cards_median, minimum=away_cards_min, maximum=away_cards_max)

            away_fouls_analysis = StatisticalMeasuresResponse(average=away_fouls_average, median=away_fouls_median, minimum=away_fouls_min, maximum=away_fouls_max)

            away_corners_analysis = StatisticalMeasuresResponse(average=away_corners_average, median=away_corners_median, minimum=away_corners_min, maximum=away_corners_max)

            away_analysis = AnalysisByMarketResponse(results=away_results_analysis, goals=away_goals_analysis, cards=away_cards_analysis, fouls=away_fouls_analysis, corners=away_corners_analysis)

            # Passa as análises para o dicionário
            teams_dicionaly[team] = (
                TeamResponse(general_analysis=general_analysis, home_analysis=home_analysis,
                             away_analysis=away_analysis))




        return AnalysisResponse(
            games=game_responses,
            analysis_by_team=AnalysisByTeamResponse(teams=teams_dicionaly),
            general_analysis=general_match_statistics

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
        # Extraindo as listas de valores diretamente via list comprehension
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


    def _win_percentage(self, matches: int, wins: int, draws: int) -> float:
        points = wins * 3 + draws
        max_points = matches * 3
        return points / max_points * 100