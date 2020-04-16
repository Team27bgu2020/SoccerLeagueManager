import Domain.Season as Season
import Domain.Team as Team
import Domain.Referee as Referee
import Domain.PointsCalculationPolicy as PointsCalculationPolicy
import Domain.GameSchedulePolicy as GameSchedulePolicy


class League:

    def __init__(self, name, season, points_calculation_policy, games_schedule_policy):

        if type(name) is not str:
            raise TypeError
        Season.type_check(season)

        self.__name = name
        self.__referees = []
        self.__teams = []
        self.__policies = {}
        self.set_points_calculation_policy(points_calculation_policy)
        self.set_game_schedule_policy(games_schedule_policy)
        self.__season = season
        # adds the created league to the season (connection)
        self.__season.add_league(self)

    """ This method adds a new team to the league """

    def add_team(self, team):

        Team.type_check(team)
        self.__teams.append(team)

    """ This method removes the given team from the league """

    def remove_team(self, team):

        Team.type_check(team)
        self.__teams.remove(team)

    """ This method adds a new referee to the league """

    def add_referee(self, referee):

        Referee.type_check(referee)
        self.__referees.append(referee)

    """ This method removes the given referee from the league """

    def remove_referee(self, referee):

        Referee.type_check(referee)
        self.__referees.remove(referee)

    """ This method returns the league teams """

    def get_teams(self):

        return self.__teams

    """ This method returns the league referees """

    def get_referees(self):

        return self.__referees

    """ This method returns the league points calculation policy """

    def get_points_calculation_policy(self):

        return self.__policies["Points"]

    """ This method returns the league game schedule policy """

    def get_game_schedule_policy(self):

        return self.__policies["Schedule"]

    """ This method returns the league season """

    def get_season(self):

        return self.__season

    """ This method returns the league name """

    def get_season(self):

        return self.__name

    """ This method sets new point calculation policy """

    def set_points_calculation_policy(self, policy):

        PointsCalculationPolicy.type_check(policy)
        self.__policies["Points"] = policy

    """ This method sets new game schedule policy """

    def set_game_schedule_policy(self, policy):

        GameSchedulePolicy.type_check(policy)
        self.__policies["Schedule"] = policy


def type_check(obj):
    if type(obj) is not League:
        raise TypeError