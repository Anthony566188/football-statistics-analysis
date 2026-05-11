from statistics import mean
from typing import List

from numpy.ma.extras import median

from dtos.analysis_by_team_response import AnalysisByTeamResponse
from dtos.analysis_response import AnalysisResponse
from dtos.game_response import GameResponse
from dtos.general_analysis_response import GeneralAnalysisResponse
from dtos.statistics_by_market_response import StatisticsByMarketResponse
from dtos.team_response import TeamResponse
from models.game import Game


class AnalysisService:

    def general_analysis(self, game_responses: List[GameResponse], games: List[Game])\
            -> AnalysisResponse:

        total_goals_games = 0
        teams_dicionaly = {}
        goals_by_match = []
        cards_by_match = []
        fouls_by_match = []
        corners_by_match = []


        for game in game_responses:
            # Pega o total de gols de todas as partidas
            total_goals_games += game.total_goals

            # Adiciona na lista o total gols por partida
            goals_by_match.append(game.total_goals)

            # Adiciona na lista o total de cartões por jogo
            cards_by_match.append(game.total_cards)

            # Adiciona na lista o total de faltas por jogo
            fouls_by_match.append(game.total_fouls)

            # Adiciona na lista o total de escanteios por jogo
            corners_by_match.append(game.total_corners)




        # Estatísticas de gols GERAL
        average_goals = total_goals_games / len(game_responses)
        median_goals = median(goals_by_match)
        min_goals = min(goals_by_match)
        max_goals = max(goals_by_match)

        # Estatísticas de cartões GERAL
        average_cards = mean(cards_by_match)
        median_cards = median(cards_by_match)
        min_cards = min(cards_by_match)
        max_cards = max(cards_by_match)

        # Estatísticas de faltas GERAL
        average_fouls = mean(fouls_by_match)
        median_fouls = median(fouls_by_match)
        min_fouls = min(fouls_by_match)
        max_fouls = max(fouls_by_match)

        # Estatísticas de escanteios GERAL
        average_corners = mean(corners_by_match)
        median_corners = median(corners_by_match)
        min_corners = min(corners_by_match)
        max_corners = max(corners_by_match)

        # Loop para pegar os times presentes nos jogos
        teams = list(set(
            team.upper()
            for game in games
            for team in (game.home_team, game.away_team)
        ))

        for team in teams:
            matchs = 0
            home_matchs = 0
            away_matchs = 0
            wins = 0
            draws = 0
            losses = 0
            goals_by_match_team = []
            cards_by_match_team = []
            fouls_by_match_team = []
            corners_by_match_team = []




            for game, game_response in zip(games, game_responses):

                home_team = game.home_team.upper()
                away_team = game.away_team.upper()

                # Pula para a próxima iteração se o time não estiver presente na partida
                if team != home_team and team != away_team:
                    continue

                matchs += 1



                # Calcula vitórias, empates e derrotas usando o DTO de resposta
                if game_response.result == team:
                    wins += 1
                elif game_response.result == "DRAW":
                    draws += 1
                else:
                    losses += 1

                # Separa os gols do time na lista
                if home_team == team:
                    goals_by_match_team.append(game.home_goals)
                    home_matchs += 1
                if away_team == team:
                    goals_by_match_team.append(game.away_goals)
                    away_matchs += 1

                # Separa os cartões do time na lista
                if home_team == team: cards_by_match_team.append(game.yellow_cards_home)
                if away_team == team: cards_by_match_team.append(game.yellow_cards_away)

                # Separa as faltas do time na lista
                if home_team == team: fouls_by_match_team.append(game.fouls_home)
                if away_team == team: fouls_by_match_team.append(game.fouls_away)

                # Separa os Escanteios do TIME na lista
                if home_team == team: corners_by_match_team.append(game.corners_home)
                if away_team == team: corners_by_match_team.append(game.corners_away)

            # Calcula o aproveitamento do time no GERAL
            win_percentage_general = self.win_percentage(matchs, wins, draws)

            #win_percentage_home = self.win_percentage(home_matchs, )

            # Estatísticas de Gols do TIME
            average_goals = mean(goals_by_match_team) if goals_by_match_team else 0.0
            median_goals = median(goals_by_match_team) if goals_by_match_team else 0.0
            min_goals = min(goals_by_match_team) if goals_by_match_team else 0.0
            max_goals = max(goals_by_match_team) if goals_by_match_team else 0.0

            analysis_goals_by_team = StatisticsByMarketResponse(
                average=average_goals, median=median_goals, minimum=min_goals, maximum=max_goals
            )


            # Estatísticas de Cartões do TIME
            average_cards = mean(cards_by_match_team) if cards_by_match_team else 0.0
            median_cards = median(cards_by_match_team) if cards_by_match_team else 0.0
            min_cards = min(cards_by_match_team) if cards_by_match_team else 0.0
            max_cards = max(cards_by_match_team) if cards_by_match_team else 0.0

            analysis_cards_by_team = StatisticsByMarketResponse(
                average=average_cards, median=median_cards, minimum=min_cards, maximum=max_cards
            )


            # Estatísticas de Faltas do TIME
            average_fouls = mean(fouls_by_match_team) if fouls_by_match_team else 0.0
            median_fouls = median(fouls_by_match_team) if fouls_by_match_team else 0.0
            min_fouls = min(fouls_by_match_team) if fouls_by_match_team else 0.0
            max_fouls = max(fouls_by_match_team) if fouls_by_match_team else 0.0

            analysis_fouls_by_team = StatisticsByMarketResponse(
                average=average_fouls, median=median_fouls, minimum=min_fouls, maximum=max_fouls
            )


            # Estatísticas de Escanteios do TIME
            average_corners = mean(corners_by_match_team) if corners_by_match_team else 0.0
            median_corners = median(corners_by_match_team) if corners_by_match_team else 0.0
            min_corners = min(corners_by_match_team) if corners_by_match_team else 0.0
            max_corners = max(corners_by_match_team) if corners_by_match_team else 0.0

            analysis_corners_by_team = StatisticsByMarketResponse(
                average=average_corners, median=median_corners, minimum=min_corners, maximum=max_corners
            )



            teams_dicionaly[team] = (
                TeamResponse(matchs=matchs, wins=wins, draws=draws, losses=losses, home_wins=, home_draws=,
                             home_losses=, away_wins=, away_draws=, away_losses=,
                             win_percentage_general=win_percentage_general, win_percentage_home=,
                             win_percentage_away=, analysis_goals=analysis_goals_by_team,
                             analysis_cards=analysis_cards_by_team, analysis_fouls=analysis_fouls_by_team,
                             analysis_corners=analysis_corners_by_team
                )
            )





        # Estatísticas de gols
        statistics_goals = (
            StatisticsByMarketResponse(
                average=average_goals, median=median_goals, minimum=min_goals,
                maximum=max_goals
            )
        )


        # Estatísticas de cartões
        statistics_cards = (
            StatisticsByMarketResponse(
                average=average_cards, median=median_cards, minimum=min_cards,
                maximum=max_cards

            )
        )


        # Estatísticas de faltas
        statistics_fouls = (
           StatisticsByMarketResponse(
               average=average_fouls, median=median_fouls, minimum=min_fouls,
               maximum=max_fouls

           )
        )


       # Estatísticas de escanteios
        statistics_corners = (
            StatisticsByMarketResponse(
                average=average_corners, median=median_corners, minimum=min_corners,
                maximum=max_corners

            )
        )



        # Análise GERAL com todos os mercados
        general_analysis = (
            GeneralAnalysisResponse(
                goals=statistics_goals, cards=statistics_cards, fouls=statistics_fouls,
                corners=statistics_corners

            )
        )


        return AnalysisResponse(
            games=game_responses,
            analysis_by_team=AnalysisByTeamResponse(teams=teams_dicionaly),
            general_analysis=general_analysis

        )






    def win_percentage(self, matchs: int, wins: int, draws: int) -> float:
        points = wins * 3 + draws
        max_points = matchs * 3
        return points / max_points * 100