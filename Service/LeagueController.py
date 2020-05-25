from Domain.League import League
from Domain.Season import Season
from Domain.PointsCalculationPolicy import PointsCalculationPolicy
from Domain.GameSchedulePolicy import GameSchedulePolicy
from Domain.TeamBudgetPolicy import TeamBudgetPolicy
from Log.Logger import *


class LeagueController:

    def __init__(self, league_db, season_db, policy_db):

        self.__league_DB = league_db
        self.__season_DB = season_db
        self.__policies_DB = policy_db
        Logger.start_logger()

    """ This method creates new season """

    def create_new_season(self, year: int, user_id=""):
        try:
            if self.__season_DB.get(year) is not None:
                raise ValueError("Season with the same year exists inn the System already")
            season = Season(year)
            self.__season_DB.add(season)
            Logger.info_log("{0}: ".format(user_id) + "created {} season ".format(year))
            return season
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ This method creates a new league and adds it to the league data base """

    def create_new_league(self, name: str, season, points_calculation_policy, games_schedule_policy,
                          team_budget_policy, user_id=""):
        try:
            if self.__league_DB.get(name, season.year) is not None:
                raise ValueError("League with that name already exists in the given season")
            league = League(name, season, points_calculation_policy, games_schedule_policy, team_budget_policy)
            self.__league_DB.add(league)
            Logger.info_log("{0}: ".format(user_id) + "created {} league ".format(name))
            return league

        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ This method updates the points calculation policy """

    def update_points_calculation_policy(self, league, points_calculation_policy, user_id=""):
        try:
            league.points_calculation_policy = points_calculation_policy
            Logger.info_log("{0}: ".format(user_id) + "update calculation policy ")
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ This method updates the game schedule policy """

    def update_game_schedule_policy(self, league, game_schedule_policy, user_id=""):

        try:
            league.game_schedule_policy = game_schedule_policy
            Logger.info_log("{0}: ".format(user_id) + "update game schedule policy ")
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ This method updates the team budget policy """

    def update_team_budget_policy(self, league, team_budget_policy, user_id=""):

        try:
            league.team_budget_policy = team_budget_policy
            Logger.info_log(
                "{0}: ".format(user_id) + "Update budget policy in league {0}".format(league.name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def add_referee_to_league(self, league, referee, user_id=""):
        try:
            league.add_referee(referee)
            Logger.info_log(
                "{0}: ".format(user_id) + "Add to league {0} referee {1}".format(league.name, referee.user_id))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ This method adds new teams to a season """

    def add_teams_to_league(self, league, teams, user_id=""):

        try:
            league.add_teams(teams)
            for team in teams:
                Logger.info_log(
                    "{0}: ".format(user_id) + "Added {0} to league".format(team.name))
            Logger.info_log(
                "{0}: ".format(user_id) + "Added list of teams to league")
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ This method adds leagues to season """

    def add_leagues_to_season(self, season, leagues, user_id=""):

        try:
            season.add_leagues(leagues)
            for league in leagues:
                Logger.info_log(
                    "{0}: ".format(user_id) + "Added {0} league to season".format(league.name))
            Logger.info_log(
                "{0}: ".format(user_id) + "Added list of leagues to season")
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

    def get_league(self, name: str, year: int, user_id=""):
        try:
            return self.__league_DB.get(name, year)
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err
    """ This method returns the all the leagues in the given year (season) """

    def get_league(self, year: int, user_id=""):
        try:
            return self.__league_DB.get_leagues_by_season(year)
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ This method create a new points calculation policy """

    def create_points_calculation_policy(self, win_points: int, tie_points: int, lose_points: int, user_id=""):
        try:
            policy = PointsCalculationPolicy(win_points, tie_points, lose_points)
            self.__policies_DB.add(policy)
            Logger.info_log("{0}: ".format(user_id) + "created new calculation policy")
            return policy
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ This method create a new game schedule policy """

    def create_game_schedule_policy(self, team_games_num: int, games_per_week: int, chosen_days,
                                    games_stadium_assigning, user_id=""):
        try:
            policy = GameSchedulePolicy(team_games_num, games_per_week, chosen_days, games_stadium_assigning)
            self.__policies_DB.add(policy)
            Logger.info_log("{0}: ".format(user_id) + "created new game schedule policy")
            return policy
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ This method create a new team budget policy """

    def create_team_budget_policy(self, min_amount: int, user_id=""):

        try:
            policy = TeamBudgetPolicy(min_amount)
            self.__policies_DB.add(policy)
            Logger.info_log("{0}: ".format(user_id) + "created new budget policy")
            return policy
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ This method create a new points calculation policy """

    @property
    def points_calculation_policies(self):

        return self.__policies_DB.points_calculation_policies

    """ This method create a new game schedule policy """

    @property
    def game_schedule_policy(self):

        return self.__policies_DB.game_schedule_policies

    """ This method create a new team budget policy """

    @property
    def team_budget_policy(self):

        return self.__policies_DB.team_budget_policies
