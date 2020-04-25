import datetime as date
from Domain.Team import Team
# from Domain.ClassesTypeCheckImports import *
""" Dor """


class Game:

    def __init__(self, home_team: Team, away_team: Team, match_time:  date.datetime, field: str):

        if home_team == away_team:
            raise ValueError

        self.home_team = home_team
        self.away_team = away_team
        self.match_time = match_time
        self.field = field

        self.__home_score = 0
        self.__away_score = 0
        self.__main_referee = None
        self.__referees = []
        self.__events = []

        self.__is_game_on = False
        self.__is_game_finished = False

    @property
    def is_game_finished(self):
        return self.__is_game_finished

    @is_game_finished.setter
    def is_game_finished(self, is_game_finished):
        if not self.__is_game_on:
            self.__is_game_finished = is_game_finished

    @property
    def is_game_on(self):
        return self.__is_game_on

    @is_game_on.setter
    def is_game_on(self, is_game_on: bool):
        self.__is_game_on = is_game_on

    """ Getter for home team """

    @property
    def home_team(self):

        return self.__home_team

    """ Getter for away team """

    @property
    def away_team(self):

        return self.__away_team

    """ Getter for match time """

    @property
    def match_time(self):

        return self.__match_time

    """ Getter for Field """

    @property
    def field(self):

        return self.__field

    """ Getter for main referee """

    @property
    def main_referee(self):

        return self.__main_referee

    """ Getter for referees list (without main referee) """

    @property
    def referees(self):

        return self.__referees

    """ Getter for Field """

    @property
    def score(self):

        return {
            'home': self.__home_score,
            'away': self.__away_score
        }

    """ Setter for main referee object """

    @main_referee.setter
    def main_referee(self, main_referee):

        self.__main_referee = main_referee

    """ Setter for match time """

    @match_time.setter
    def match_time(self, match_time):

        if type(match_time) is not date.datetime:
            raise TypeError

        self.__match_time = match_time

    """ Setter for game field """

    @field.setter
    def field(self, field):

        if type(field) is not str:
            raise TypeError

        self.__field = field

    """ Setter for home team """

    @home_team.setter
    def home_team(self, home_team):

        self.__home_team = home_team

    """ Setter for away team """

    @away_team.setter
    def away_team(self, away_team):

        self.__away_team = away_team

    """ This method adds a referee to the game """

    def add_referee(self, referee):

        if referee in self.__referees or referee == self.__main_referee:
            raise ValueError

        self.__referees.append(referee)

    """ This method remove the given referee from the game """

    def remove_referee(self, referee):

        if referee in self.__referees:
            self.__referees.remove(referee)

    """ This method adds a game event to the event list """

    def add_event(self, event):

        ref = event.referee
        if ref not in self.__referees and ref != self.__main_referee:
            raise ValueError

        if event in self.__events:
            raise ValueError

        self.__events.append(event)

    """ This method removes a game event from the event list """

    def remove_event(self, event):

        if event in self.__events:
            self.__events.remove(event)

    """ This method increase by 1 the home team score """

    def home_team_goal(self):

        self.__home_score += 1

    """ This method increase by 2 the home team score """

    def away_team_goal(self):

        self.__away_score += 1
