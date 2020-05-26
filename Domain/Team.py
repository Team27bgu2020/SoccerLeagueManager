from Domain.TeamBudget import TeamBudget

""" Dor """


class Team:

    def __init__(self, name, team_members=[], stadium=None):

        if type(name) is not str:
            raise TypeError

        self.__team_members = []
        self.add_team_members(team_members)
        self.__name = name
        self.__upcoming_games = []
        self.__past_games = []
        self.__leagues = {}
        self.__stadium = stadium
        self.__owners = []
        self.__managers = []
        self.__is_open = True
        self.__budget_manager = TeamBudget()

    """ This method adds a new season """

    def add_league(self, league):

        if league.season.year not in self.__leagues.keys():
            self.__leagues[league.season.year] = []

        if league not in self.__leagues[league.season.year]:
            self.__leagues[league.season.year].append(league)
        else:
            raise ValueError('team is already in this league')

    """ This method transfer the given game to the past games """

    def game_over(self, game):

        if game not in self.__upcoming_games or game in self.__past_games:
            raise ValueError('Team {} is not participating in this game'.format(self.name))

        self.__upcoming_games.remove(game)
        self.__past_games.append(game)

    """ This method adds all the given games to the team games list """

    def add_games(self, games):

        if type(games) is not list:
            raise TypeError('Expected list of game, recieved {}'.format(games))

        exception = ''

        for game in games:
            try:
                self.add_game(game)
            except ValueError as err:
                exception = exception + err + '\n'

        if exception is not '':
            raise ValueError(exception)

    """ This method adds a game to the team games list """

    def add_game(self, game):

        if not self.collision_game_check(game):
            self.__upcoming_games.append(game)
        else:
            raise ValueError('The {}-{} game has collision with another team game'
                             .format(game.home_team.name, game.away_team.name))

    """ This method removes a game from the team games list """

    def remove_upcoming_game(self, game):

        if game in self.__upcoming_games:
            self.__upcoming_games.remove(game)
        else:
            raise ValueError('The team is not in this game')

    """ This method check if the given game collides with the team games (same day) """

    def collision_game_check(self, new_game):

        for game in self.__upcoming_games:
            if game.match_time.date() == new_game.match_time.date():
                return True
        return False

    """ This method adds all the given team members """

    def add_team_members(self, team_members):

        if type(team_members) is not list:
            raise TypeError('Expected list, received {}'.format(team_members))

        exception = ''

        for team_member in team_members:
            try:
                self.__team_members.append(team_member)
                team_member.team = self
            except ValueError as err:
                exception = exception + err + '\n'

        if exception is not '':
            raise ValueError(exception)

    """ This method adds a new team member """

    def add_team_member(self, team_member):

        if team_member in self.__team_members:
            raise ValueError('User {} already in this team'.format(team_member.user_name))
        if team_member.team is not None:
            raise ValueError('User {} already have a team'.format(team_member.user_name))
        self.__team_members.append(team_member)
        team_member.team = self

    """ This method removes all the given team members """

    def remove_team_members(self, team_members):
        if type(team_members) is not list:
            raise TypeError('Expected a list, received {}'.format(team_members))

        exception = ''

        for team_member in team_members:
            try:
                self.remove_team_member(team_member)
            except ValueError as err:
                exception = exception + err + '\n'

        if exception is not '':
            raise ValueError(exception)

    """ This method removes a team member """

    def remove_team_member(self, team_member):
        if team_member in self.__team_members:
            self.__team_members.remove(team_member)
            team_member.team = None
        else:
            raise ValueError('User {} is not a player or a coach in this team'.format(team_member.user_name))

    """ This method adds a new team owner """

    def add_team_owner(self, team_member):

        if team_member in self.owners:
            raise ValueError('User {} is already a owner in this team'.format(team_member.user_name))
        if team_member.team is not None:
            raise ValueError('User {} already in a team'.format(team_member.user_name))
        self.__owners.append(team_member)
        team_member.team = self

    """ This method removes a team owner """

    def remove_team_owner(self, team_member):
        if len(self.__owners) == 1:
            raise Exception("Team must have at least one Team Owner")

        if team_member in self.owners:
            self.__owners.remove(team_member)
            team_member.team = None
            self.cascade_remove(team_member)
        else:
            raise ValueError('User {} is not a team owner in this team'.format(team_member.user_name))

    """ Remove all team members assigned by given team member"""

    def cascade_remove(self, team_member):

        exception = ''

        for player in self.team_members:
            if player.role.assigned_by == team_member:
                try:
                    self.remove_team_member(player)
                except ValueError as err:
                    exception = exception + err + '\n'
        for manager in self.managers:
            if manager.role.assigned_by == team_member:
                try:
                    self.remove_team_member(manager)
                except ValueError as err:
                    exception = exception + err + '\n'
        for owner in self.owners:
            if owner.role.assigned_by == team_member:
                try:
                    self.remove_team_member(owner)
                except ValueError as err:
                    exception = exception + err + '\n'

        if exception is not '':
            raise Exception(exception)

    """ This method adds a new team manager """

    def add_team_manager(self, team_member):

        if team_member in self.managers:
            raise ValueError('User {} is already a manager in the team'.format(team_member.user_name))
        if team_member.team is not None:
            raise ValueError('User {} is already in another team'.format(team_member.user_name))
        self.__managers.append(team_member)
        team_member.team = self

    """ This method removes a team manager """

    def remove_team_manager(self, team_member):
        if team_member in self.__managers:
            self.__managers.remove(team_member)
            team_member.team = None
        else:
            raise ValueError('User {} is not a manager in the team'.format(team_member.user_name))

    """ This method set the assigned by value"""

    def set_assigned_by(self, team_member, assigning_user):
        team_member.role.assigned_by = assigning_user

    """ This method closes the team """

    def close_team(self):

        if self.__is_open:
            self.__is_open = False
            self.notify_team_members("Team {} is now closed".format(self.name))
        else:
            raise Exception('Team is already closed')

    """ This method opens the team """

    def open_team(self):

        if not self.__is_open:
            self.__is_open = True
            self.notify_team_members("Team {} is now reopened".format(self.name))
        else:
            raise Exception('Team is already open')

    """ Add expanse"""

    def add_expanse(self, amount, description):
        if amount <= 0:
            raise ValueError("expanse can't be a negative number")
        return self.__budget_manager.add_expanse(amount, description)

    """ Add income"""

    def add_income(self, amount, description):
        if amount <= 0:
            raise ValueError("income can't be a negative number")
        self.__budget_manager.add_income(amount, description)

    """ Notify team members with a certain notification """
    def notify_team_members(self, notification):
        for team_member in self.team_members:
            team_member.notify(notification)
        for team_manager in self.managers:
            team_manager.notify(notification)
        for team_owner in self.owners:
            team_owner.notify(notification)

    """ Get expanses"""

    @property
    def expanses(self):
        return self.__budget_manager.expanses

    """ Get expanses"""

    @property
    def incomes(self):
        return self.__budget_manager.incomes

    """ Get transactions"""

    @property
    def transactions(self):
        return self.__budget_manager.transactions

    """ Get Current"""

    @property
    def budget(self):
        return self.__budget_manager.current_budget

    """ name getter """

    @property
    def name(self):

        return self.__name

    """ team members getter """

    @property
    def team_members(self):

        return self.__team_members

    """ team members getter """

    @property
    def owners(self):

        return self.__owners

    """ team members getter """

    @property
    def managers(self):

        return self.__managers

    """ upcoming games getter """

    @property
    def upcoming_games(self):

        return self.__upcoming_games

    """ past games getter """

    @property
    def past_games(self):

        return self.__past_games

    """ leagues getter """

    @property
    def leagues(self):

        return self.__leagues

    """ is open getter """

    @property
    def is_open(self):

        return self.__is_open

    """ Budget Controller getter"""

    @property
    def budget_manager(self):

        return self.__budget_manager

    """ stadium getter """

    @property
    def stadium(self):

        return self.__stadium

    """ stadium setter """

    @stadium.setter
    def stadium(self, stadium):

        self.__stadium = stadium

    """ This method checks if the teams are equal """

    def __eq__(self, obj):

        return isinstance(obj, Team) and obj.__name == self.__name
