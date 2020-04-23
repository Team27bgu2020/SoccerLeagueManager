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
        self.__owner = None
        self.__manager = None
        self.__is_open = True
        self.__budget_manager = TeamBudget()

    """ This method adds a new season """

    def add_league(self, league):

        if league.season.year not in self.__leagues.keys():
            self.__leagues[league.season.year] = []

        self.__leagues[league.season.year].append(league)

    """ This method transfer the given game to the past games """

    def game_over(self, game):

        if game not in self.__upcoming_games or game in self.__past_games:
            raise ValueError

        self.__upcoming_games.remove(game)
        self.__past_games.append(game)

    """ This method adds all the given games to the team games list """

    def add_games(self, games):

        if type(games) is not list:
            raise TypeError

        for game in games:
            self.add_game(game)

    """ This method adds a game to the team games list """

    def add_game(self, game):

        if not self.collision_game_check(game):
            self.__upcoming_games.append(game)
            return True
        return False

    """ This method removes a game from the team games list """

    def remove_upcoming_game(self, game):

        if game in self.__upcoming_games:
            self.__upcoming_games.remove(game)

    """ This method check if the given game collides with the team games (same day) """

    def collision_game_check(self, new_game):

        for game in self.__upcoming_games:
            if game.match_time.date() == new_game.match_time.date():
                return True
        return False

    """ This method adds all the given team members """

    def add_team_members(self, team_members):

        if type(team_members) is not list:
            raise TypeError

        for team_member in team_members:
            self.add_team_member(team_member)

    """ This method adds a new team member """

    def add_team_member(self, team_member):

        if team_member in self.__team_members:
            raise ValueError

        self.__team_members.append(team_member)
        team_member.set_team(self)

    """ This method removes all the given team members """

    def remove_team_members(self, team_members):
        # who can use it?
        if type(team_members) is not list:
            raise TypeError

        for team_member in team_members:
            self.remove_team_member(team_member)

    """ This method removes a team member """

    def remove_team_member(self, team_member):
        # who can use it?
        if team_member in self.__team_members:
            self.__team_members.remove(team_member)

    """ This method closes the team """

    def close_team(self):

        self.__is_open = False

    """ This method opens the team """

    def open_team(self):

        self.__is_open = True

    """ Add expanse"""

    def add_expanse(self, amount, description):
        self.__budget_manager.add_expanse(amount, description)

    """ Add income"""

    def add_income(self, amount, description):
        self.__budget_manager.add_income(amount, description)

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
    def current_budget(self):
        return self.__budget_manager.current_budget

    """ name getter """

    @property
    def name(self):

        return self.__name

    """ team members getter """

    @property
    def team_members(self):

        return self.__team_members

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

    """ Team Owner getter"""

    @property
    def owner(self):

        return self.__owner

    """ Team Manager getter"""

    @property
    def manager(self):

        return self.__manager

    """ Budget Controller getter"""

    @property
    def budget_controller(self):

        return self.__budget_manager

    """ stadium getter """

    @property
    def stadium(self):

        return self.__stadium

    """ stadium setter """

    @stadium.setter
    def stadium(self, stadium):

        self.__stadium = stadium

    """ Manger setter """

    @manager.setter
    def manager(self, manager):

        self.__manager = manager

    """ Manger setter """

    @manager.setter
    def owner(self, owner):

        self.owner = owner

    """ This method checks if the teams are equal """

    def __eq__(self, obj):

        return isinstance(obj, Team) and obj.__name == self.__name
