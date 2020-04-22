from Domain.Season import Season
import Domain.Season as Season
from Domain.PointsCalculationPolicy import PointsCalculationPolicy
import Domain.PointsCalculationPolicy as PointsCalculationPolicy
from Domain.GameSchedulePolicy import GameSchedulePolicy
# from Domain.ClassesTypeCheckImports import *

""" Dor """


class League:

    TEAM_INDEX = 0
    SCORE_INDEX = 1

    def __init__(self, name: str, season, points_calculation_policy, games_schedule_policy, team_budget_policy):

        if type(name) is not str:
            raise TypeError

        self.__name = name
        self.__referees = []
        self.__teams = {}
        self.__policies = {}
        self.points_calculation_policy = points_calculation_policy
        self.game_schedule_policy = games_schedule_policy
        self.team_budget_policy = team_budget_policy
        self.__season = season
        # adds the created league to the season (connection)
        self.__season.add_league(self)

    """ This method adds a new team to the league """

    def add_team(self, team):

        self.__teams[team.name] = [team, 0]

    """ This method removes the given team from the league """

    def remove_team(self, team_name):

        self.__teams.remove(team_name)

    """ This method updates the teams score if the team won the game """

    def won(self, team_name):

        self.__teams[team_name][self.SCORE_INDEX] += self.points_calculation_policy.win_points

    """ This method updates the teams score if the team tied the game """

    def tied(self, team_name):

        self.__teams[team_name][self.SCORE_INDEX] += self.points_calculation_policy.tie_points

    """ This method updates the teams score if the team lost the game """

    def lost(self, team_name):

        self.__teams[team_name][self.SCORE_INDEX] += self.points_calculation_policy.lose_points

    """ This method adds a new referee to the league """

    def add_referee(self, referee):

        self.__referees.append(referee)

    """ This method removes the given referee from the league """

    def remove_referee(self, referee):

        self.__referees.remove(referee)


    """ This method returns the league teams """

    @property
    def teams(self):
        return self.__teams

    """ This method returns the league referees """

    @property
    def referees(self):
        return self.__referees

    """ This method returns the league points calculation policy """

    @property
    def points_calculation_policy(self):
        return self.__policies["Points"]

    """ This method returns the league game schedule policy """

    @property
    def game_schedule_policy(self):
        return self.__policies["Schedule"]

    """ This method returns the league game schedule policy """

    @property
    def team_budget_policy(self):
        return self.__policies["Schedule"]

    """ This method returns the league season """

    @property
    def season(self):
        return self.__season

    """ This method returns the league name """

    @property
    def name(self):
        return self.__name

    """ This method sets new point calculation policy """

    @points_calculation_policy.setter
    def points_calculation_policy(self, policy):

        self.__policies["Points"] = policy

    """ This method sets new game schedule policy """

    @game_schedule_policy.setter
    def game_schedule_policy(self, policy):

        self.__policies["Schedule"] = policy

    """ This method sets new game schedule policy """

    @game_schedule_policy.setter
    def game_team_budget_policy(self, policy):

        self.__policies["budget"] = policy


