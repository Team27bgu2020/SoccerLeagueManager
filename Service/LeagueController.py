from Domain.League import League
from Domain.Season import Season
from Domain.PointsCalculationPolicy import PointsCalculationPolicy
from Domain.GameSchedulePolicy import GameSchedulePolicy
from Domain.TeamBudgetPolicy import TeamBudgetPolicy
from Log.Logger import *


class LeagueController:

    def __init__(self, league_db, season_db, user_db):

        self.__league_DB = league_db
        self.__season_DB = season_db
        self.__user_db = user_db
        self.__league_id_counter = self.__league_DB.get_id_counter()
        Logger.start_logger()

    """ This method creates new season """

    def create_new_season(self, year: int, user_id=""):
        try:
            season = Season(year)
            self.__season_DB.add(season)
            Logger.info_log("{0}: ".format(user_id) + "created {} season ".format(year))
            return season
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ This method creates a new league and adds it to the league data base """

    def create_new_league(self, name: str, season_year, points_calculation_policy_dict, games_schedule_policy_dict,
                          team_budget_policy_dict, user_id=""):
        try:
            season = self.__season_DB.get(season_year)

            policy = self.create_policy_objects(points_calculation_policy_dict, games_schedule_policy_dict, team_budget_policy_dict)

            league = League(name, season.year, policy[0], policy[1], policy[2], self.__league_id_counter)
            self.update_counter()

            season.add_league(league.league_id)
            self.__league_DB.add(league)
            self.__season_DB.update(season)
            Logger.info_log("{0}: ".format(user_id) + "created {} league ".format(name))
            return league

        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def create_policy_objects(
            self, points_calculation_policy_dict, games_schedule_policy_dict, team_budget_policy_dict
    ):

        points_calculation_policy = self.create_points_policy(points_calculation_policy_dict)
        games_schedule_policy = self.create_game_schedule_policy(games_schedule_policy_dict)
        team_budget_policy = self.create_team_budget_policy(team_budget_policy_dict)

        return points_calculation_policy, games_schedule_policy, team_budget_policy

    def create_points_policy(self, points_calculation_policy_dict):

        return PointsCalculationPolicy(points_calculation_policy_dict['win_points'],
                                       points_calculation_policy_dict['tie_points'],
                                       points_calculation_policy_dict['lose_points'])

    def create_game_schedule_policy(self, games_schedule_policy_dict):

        return GameSchedulePolicy(games_schedule_policy_dict['team_games_num'],
                                  games_schedule_policy_dict['games_per_week'],
                                  games_schedule_policy_dict['chosen_days'],
                                  games_schedule_policy_dict['games_stadium_assigning'])

    def create_team_budget_policy(self, team_budget_policy_dict):

        return TeamBudgetPolicy(team_budget_policy_dict['min_amount'])

    """ This method updates the points calculation policy """

    def update_points_calculation_policy(self, league_id, points_calculation_policy_dict, user_id=""):
        try:
            league = self.__league_DB.get(league_id)
            league.points_calculation_policy = self.create_points_policy(points_calculation_policy_dict)
            self.__league_DB.update(league)
            Logger.info_log("{0}: ".format(user_id) + "update calculation policy ")
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ This method updates the game schedule policy """

    def update_game_schedule_policy(self, league_id, game_schedule_policy_dict, user_id=""):

        try:
            league = self.__league_DB.get(league_id)
            league.game_schedule_policy = self.create_game_schedule_policy(game_schedule_policy_dict)
            self.__league_DB.update(league)
            Logger.info_log("{0}: ".format(user_id) + "update game schedule policy ")
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ This method updates the team budget policy """

    def update_team_budget_policy(self, league_id, team_budget_policy_dict, user_id=""):

        try:
            league = self.__league_DB.get(league_id)
            league.team_budget_policy = self.create_team_budget_policy(team_budget_policy_dict)
            self.__league_DB.update(league)
            Logger.info_log(
                "{0}: ".format(user_id) + "Update budget policy in league {0}".format(league.name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def add_referee_to_league(self, league_id, referee_id, user_id=""):
        try:
            league = self.__league_DB.get(league_id)
            referee = self.__user_db.get_signed_user(referee_id)
            league.add_referee(referee.user_id)
            self.__league_DB.update(league)
            Logger.info_log(
                "{0}: ".format(user_id) + "Add to league {0} referee {1}".format(league.name, referee_id))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ This method adds new teams to a season """

    def add_teams_to_league(self, league_id, teams, user_id=""):

        try:
            league = self.__league_DB.get(league_id)
            league.add_teams(teams)
            for team in teams:
                Logger.info_log(
                    "{0}: ".format(user_id) + "Added {0} to league".format(team))
            self.__league_DB.update(league)

        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ This method adds leagues to season """

    def add_leagues_to_season(self, season_year, leagues, user_id=""):

        try:
            season = self.__season_DB.get(season_year)
            season.add_leagues(leagues)
            for league in leagues:
                Logger.info_log(
                    "{0}: ".format(user_id) + "Added {0} league to season".format(league.name))
            self.__season_DB.update(season)

        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ This method returns the season of the given year """

    def get_season(self, year: int, user_id=""):
        try:
            return self.__season_DB.get(year)
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ This method returns the league in the given year with the same given name """

    def get_league(self, league_id, user_id=""):
        try:
            return self.__league_DB.get(league_id)
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ This method returns the all the leagues in the given year (season) """

    def get_league_by_season(self, year: int, user_id=""):
        try:
            res = []
            for league in self.__season_DB.get(year).leagues:
                res.append(self.__league_DB.get(league))
            return res
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def get_all_leagues(self):
        return self.__league_DB.get_all_leagues()

    def get_all_seasons(self):
        return self.__season_DB.get_all_seasons()

    def update_counter(self):
        self.__league_id_counter += 1
        self.__league_DB.update_id_counter(self.__league_id_counter)

    """ This method create a new points calculation policy """
