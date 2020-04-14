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

        self._name = name
        self._referees = []
        self._teams = []
        self._policies = {}
        self.set_points_calculation_policy(points_calculation_policy)
        self.set_game_schedule_policy(games_schedule_policy)
        self._season = season
        # adds the created league to the season (connection)
        self._season.add_league(self)

    """ This method adds a new team to the league """

    def add_team(self, team):

        Team.type_check(team)
        self._teams.append(team)

    """ This method removes the given team from the league """

    def remove_team(self, team):

        Team.type_check(team)
        self._teams.remove(team)

    """ This method adds a new referee to the league """

    def add_referee(self, referee):

        Referee.type_check(referee)
        self._referees.append(referee)

    """ This method removes the given referee from the league """

    def remove_referee(self, referee):

        Referee.type_check(referee)
        self._referees.remove(referee)

    """ This method returns the league teams """

    def get_teams(self):

        return self._teams

    """ This method returns the league referees """

    def get_referees(self):

        return self._referees

    """ This method returns the league points calculation policy """

    def get_points_calculation_policy(self):

        return self._policies["Points"]

    """ This method returns the league game schedule policy """

    def get_game_schedule_policy(self):

        return self._policies["Schedule"]

    """ This method returns the league season """

    def get_season(self):

        return self._season

    """ This method returns the league name """

    def get_season(self):

        return self._name

    """ This method sets new point calculation policy """

    def set_points_calculation_policy(self, policy):

        PointsCalculationPolicy.type_check(policy)
        self._policies["Points"] = policy

    """ This method sets new game schedule policy """

    def set_game_schedule_policy(self, policy):

        GameSchedulePolicy.type_check(policy)
        self._policies["Schedule"] = policy


def type_check(obj):
    if type(obj) is not League:
        raise TypeError