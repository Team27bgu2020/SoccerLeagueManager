import datetime as date
from Domain.Team import Team

# from Domain.ClassesTypeCheckImports import *
""" Dor """


class Game:

    def __init__(self, game_id, home_team, away_team, match_time:  date.datetime, field: str):

        if home_team == away_team:
            raise ValueError("Team cannot play against herself")

        self.__game_id = game_id
        self.__home_team = home_team
        self.__away_team = away_team
        self.__match_time = match_time
        self.__field = field

        self.__home_score = 0
        self.__away_score = 0
        self.__main_referee = None
        self.__referees = []
        self.__events = []

        self.__is_game_on = False
        self.__is_game_finished = False

        self.fan_following = []

    @property
    def game_id(self):
        return self.__game_id

    @game_id.setter
    def game_id(self, value):
        self.__game_id = value

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

    """ Getter for events """

    @property
    def events(self):
        return self.__events

    @events.setter
    def events(self, value):
        self.__events = value

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

    @referees.setter
    def referees(self, value):
        self.__referees = value

    """ Getter for Field """

    @property
    def score(self):

        return {
            'home': self.__home_score,
            'away': self.__away_score
        }

    @property
    def home_score(self):
        return self.__home_score

    @home_score.setter
    def home_score(self, value):
        self.__home_score = value

    @property
    def away_score(self):
        return self.__away_score

    @away_score.setter
    def away_score(self, value):
        self.__away_score = value

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

    """ Add follower to the game"""
    def add_follower(self, fan):
        if fan in self.fan_following:
            raise ValueError('User is already following this game')
        self.fan_following.append(fan)

    """ Remove follower from the game"""
    def remove_follower(self, fan):
        if fan not in self.fan_following:
            raise ValueError("Fan is not following the game")
        self.fan_following.remove(fan)

    """ This method adds a referee to the game """

    def add_referee(self, referee):

        if referee in self.__referees or referee == self.__main_referee:
            raise ValueError("referee already defined for this game")

        self.__referees.append(referee)

    """ This method remove the given referee from the game """

    def remove_referee(self, referee):

        if referee in self.__referees:
            self.__referees.remove(referee)

    """ This method adds a game event to the event list """

    def add_event(self, event):

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
