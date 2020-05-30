""" Dor """


class League:

    def __init__(self, name: str, season, points_calculation_policy, games_schedule_policy, team_budget_policy, league_id):

        if type(name) is not str:
            raise TypeError

        self.__league_id = league_id
        self.__name = name
        self.__referees = []
        self.__teams = {}
        self.__policies = {
            'Points': points_calculation_policy,
            'Schedule': games_schedule_policy,
            'Budget': team_budget_policy
        }
        self.__season = season

    """ This method adds teams to the league """

    def add_teams(self, teams):

        exception = ''

        for team in teams:
            try:
                self.add_team(team)
            except ValueError as err:
                exception = exception + str(err) + '\n'

        if exception is not '':
            raise ValueError(exception)

    """ This method adds a new team to the league """

    def add_team(self, team_name):

        if team_name in self.__teams:
            raise ValueError('Team {} already in this league'.format(team_name.name))

        self.__teams[team_name] = 0

    """ This method removes the given team from the league """

    def remove_team(self, team_name):

        if team_name not in self.__teams:
            raise ValueError('{} team is not in this league'.format(team_name))

        del self.__teams[team_name]

    """ This method updates the teams score if the team won the game """

    def won(self, team_name):

        if team_name not in self.__teams:
            raise ValueError('{} team is not in this league')

        self.__teams[team_name] += self.points_calculation_policy.win_points

    """ This method updates the teams score if the team tied the game """

    def tied(self, team_name):

        if team_name not in self.__teams:
            raise ValueError('{} team is not in this league')

        self.__teams[team_name] += self.points_calculation_policy.tie_points

    """ This method updates the teams score if the team lost the game """

    def lost(self, team_name):

        if team_name not in self.__teams:
            raise ValueError('{} team is not in this league')

        self.__teams[team_name] += self.points_calculation_policy.lose_points

    """ This method adds a new referee to the league """

    def add_referee(self, referee):

        if referee in self.__referees:
            raise ValueError('referee is already in this league')

        self.__referees.append(referee)

    """ This method removes the given referee from the league """

    def remove_referee(self, referee):

        if referee not in self.__referees:
            raise ValueError('referee is not in this league')

        self.__referees.remove(referee)

    """ This method returns the league teams """

    @property
    def teams(self):
        return self.__teams

    @teams.setter
    def teams(self, value):
        self.__teams = value

    """ This method returns the league referees """

    @property
    def referees(self):
        return self.__referees

    @referees.setter
    def referees(self, value):
        self.__referees = value

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
        return self.__policies["Budget"]

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

    @team_budget_policy.setter
    def team_budget_policy(self, policy):

        self.__policies["Budget"] = policy

    @property
    def league_id(self):
        return self.__league_id

    @league_id.setter
    def league_id(self, value):
        self.__league_id = value


