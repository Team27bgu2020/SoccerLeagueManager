from Domain.League import League
from Domain.Season import Season
from Domain.PointsCalculationPolicy import PointsCalculationPolicy
from Domain.GameSchedulePolicy import GameSchedulePolicy
from Domain.TeamBudgetPolicy import TeamBudgetPolicy
from Log.Logger import *


class LeagueController:

    def __init__(self, league_db, season_db, user_db, policy_db):

        self.__league_DB = league_db
        self.__season_DB = season_db
        self.__user_db = user_db
        self.__policy_db = policy_db
        self.__league_id_counter = self.__league_DB.get_id_counter()
        self.__points_policy_id_counter = self.__policy_db.get_points_id_counter()
        self.__schedule_policy_id_counter = self.__policy_db.get_schedule_id_counter()
        self.__budget_policy_id_counter = self.__policy_db.get_budget_id_counter()
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

    def create_new_league(self, name: str, season_year, points_calculation_policy_id, games_schedule_policy_id,
                          team_budget_policy_id, user_id=""):
        try:
            season = self.__season_DB.get(season_year)

            self.__policy_db.get_points_policy(points_calculation_policy_id)
            self.__policy_db.get_schedule_policy(games_schedule_policy_id)
            self.__policy_db.get_budget_policy(team_budget_policy_id)

            league = League(name, season.year, points_calculation_policy_id, games_schedule_policy_id, team_budget_policy_id, self.__league_id_counter)
            self.update_league_counter()

            season.add_league(league.league_id)
            self.__league_DB.add(league)
            self.__season_DB.update(season)
            Logger.info_log("{0}: ".format(user_id) + "created {} league ".format(name))
            return league

        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def create_points_policy(self, win_points, tie_points, lose_points, user_id=""):

        try:
            self.__policy_db.add_point_policy(PointsCalculationPolicy(win_points, tie_points, lose_points, self.__points_policy_id_counter))
            self.update_points_policy_counter()
            Logger.info_log("{}: Created new points calculation policy".format(user_id))
        except Exception as err:
            Logger.error_log("{}:".format(user_id) + str(err))
            raise err

    def create_game_schedule_policy(self, team_games_num, games_per_week, games_stadium_assigning, user_id=""):

        try:
            self.__policy_db.add_schedule_policy(GameSchedulePolicy(team_games_num, games_per_week, games_stadium_assigning, self.__schedule_policy_id_counter))
            self.update_schedule_policy_counter()
            Logger.info_log("{}: Created new game schedule policy".format(user_id))
        except Exception as err:
            Logger.error_log("{}:".format(user_id) + str(err))
            raise err

    def create_team_budget_policy(self, min_amount, user_id=""):

        try:
            self.__policy_db.add_budget_policy(TeamBudgetPolicy(min_amount, self.__budget_policy_id_counter))
            self.update_budget_policy_counter()
            Logger.info_log("{}: Created new team budget policy".format(user_id))
        except Exception as err:
            Logger.error_log("{}:".format(user_id) + str(err))
            raise err

    def delete_points_calculation_policy(self, policy_id, user_id=""):

        try:
            self.__policy_db.delete_points_policy(policy_id)
            Logger.info_log("{}: Deleted points calculation policy {}".format(user_id, policy_id))
        except Exception as err:
            Logger.error_log("{}:".format(user_id) + str(err))
            raise err

    def delete_schedule_calculation_policy(self, policy_id, user_id=""):

        try:
            self.__policy_db.delete_schedule_policy(policy_id)
            Logger.info_log("{}: Deleted game schedule policy {}".format(user_id, policy_id))
        except Exception as err:
            Logger.error_log("{}:".format(user_id) + str(err))
            raise err

    def delete_budget_calculation_policy(self, policy_id, user_id=""):

        try:
            self.__policy_db.delete_budget_policy(policy_id)
            Logger.info_log("{}: Deleted team budget policy {}".format(user_id, policy_id))
        except Exception as err:
            Logger.error_log("{}:".format(user_id) + str(err))
            raise err

    def get_points_calculation_policy(self, policy_id, user_id=""):

        try:
            policy = self.__policy_db.get_points_policy(policy_id)
            Logger.info_log("{}: Retrived point calculation policy {}".format(user_id, policy_id))
            return policy
        except Exception as err:
            Logger.error_log("{}:".format(user_id) + str(err))
            raise err

    def get_schedule_calculation_policy(self, policy_id, user_id=""):

        try:
            policy = self.__policy_db.get_schedule_policy(policy_id)
            Logger.info_log("{}: Retrived game schedule policy {}".format(user_id, policy_id))
            return policy
        except Exception as err:
            Logger.error_log("{}:".format(user_id) + str(err))
            raise err

    def get_budget_calculation_policy(self, policy_id, user_id=""):

        try:
            policy = self.__policy_db.get_budget_policy(policy_id)
            Logger.info_log("{}: Retrived team budget policy {}".format(user_id, policy_id))
            return policy
        except Exception as err:
            Logger.error_log("{}:".format(user_id) + str(err))
            raise err

    def get_all_points_policies(self):

        return self.__policy_db.get_all_points_policy()

    def get_all_schedule_policies(self):

        return self.__policy_db.get_all_schedule_policy()

    def get_all_budget_policies(self):

        return self.__policy_db.get_all_budget_policy()

    """ This method updates the points calculation policy """

    def update_points_calculation_policy_in_league(self, league_id, policy_id, user_id=""):
        try:
            league = self.__league_DB.get(league_id)
            policy = self.__policy_db.get_points_policy(policy_id)
            league.points_calculation_policy = policy.policy_id
            self.__league_DB.update(league)
            Logger.info_log("{0}: ".format(user_id) + "update calculation policy ")
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ This method updates the game schedule policy """

    def update_game_schedule_policy_in_league(self, league_id, policy_id, user_id=""):

        try:
            league = self.__league_DB.get(league_id)
            policy = self.__policy_db.get_schedule_policy(policy_id)
            league.game_schedule_policy = policy.policy_id
            self.__league_DB.update(league)
            Logger.info_log("{0}: ".format(user_id) + "update game schedule policy ")
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ This method updates the team budget policy """

    def update_team_budget_policy_in_league(self, league_id, policy_id, user_id=""):

        try:
            league = self.__league_DB.get(league_id)
            policy = self.__policy_db.get_budget_policy(policy_id)
            league.team_budget_policy = policy.policy_id
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

    def update_league_counter(self):
        self.__league_id_counter += 1
        self.__league_DB.update_id_counter(self.__league_id_counter)

    def update_points_policy_counter(self):
        self.__points_policy_id_counter += 1
        self.__policy_db.update_points_id_counter(self.__points_policy_id_counter)

    def update_schedule_policy_counter(self):
        self.__schedule_policy_id_counter += 1
        self.__policy_db.update_schedule_id_counter(self.__schedule_policy_id_counter)

    def update_budget_policy_counter(self):
        self.__budget_policy_id_counter += 1
        self.__policy_db.update_budget_id_counter(self.__budget_policy_id_counter)

    """ This method create a new points calculation policy """
