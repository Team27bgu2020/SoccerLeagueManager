import Domain.TeamUser as TeamUser
import Domain.Game as Game
import Domain.League as League
import Domain.Season as Season


class Team:

    def __init__(self, name, team_members=[]):

        if type(name) is not str:
            raise TypeError

        self.__team_members = []
        self.add_team_members(team_members)
        self.__name = name
        self.__upcoming_games = []
        self.__past_games = {}
        self.__leagues = {}

        self.open_team()

    """ This method adds a new season """

    def add_league(self, league):

        League.type_check(league)
        if league.get_season().get_year() in self.__leagues.keys():
            self.__leagues[league.get_season().get_year()] = []

        self.__leagues[league.get_season().get_year()].append(league)

    """ This method transfer the given game to the past games """

    def game_over(self, game):

        raise NotImplementedError

    """ This method adds all the given games to the team games list """

    def add_games(self, games):

        if type(games) is not list:
            raise TypeError

        for game in games:
            self.add_game(game)

    """ This method adds a game to the team games list """

    def add_game(self, game):

        Game.type_check(game)
        if self.collision_game_check(game):
            self.__upcoming_games.append(game)
            return True
        return False

    """ This method check if the given game collides with the team games """

    def collision_game_check(self, game):

        raise NotImplementedError

    """ This method adds all the given team members """

    def add_team_members(self, team_members):

        if type(team_members) is not list:
            raise TypeError

        for team_member in team_members:
            self.add_team_member(team_member)

    """ This method adds a new team member """

    def add_team_member(self, team_member):

        TeamUser.type_check(team_member)
        if team_member in self.__team_members:
            raise ValueError

        self.__team_members.append(team_member)

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
        TeamUser.type_check(team_member)
        if team_member not in self.__team_members:
            raise ValueError

        self.__team_members.remove(team_member)

    """ This method closes the team """

    def close_team(self):

        self.__is_open = False

    """ This method opens the team """

    def open_team(self):

        self.__is_open = True

    """ This method checks if the teams are equal """

    def __eq__(self, obj):

        return isinstance(obj, Team) and obj.__name == self.__name


def type_check(obj):

    if type(obj) is not Team:
        raise TypeError
