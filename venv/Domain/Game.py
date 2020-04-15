import datetime as date
import Domain.GameEvent as GameEvent
import Domain.Referee as Referee
import Domain.Team as Team


# noinspection PyAttributeOutsideInit
class Game:

    def __init__(self, home_team, away_team, match_time, field, main_referee=None):

        if home_team == away_team:
            raise ValueError

        self.set_home_team(home_team)
        self.set_away_team(away_team)
        self.set_match_time(match_time)
        self.set_field(field)
        self.set_main_referee(main_referee)

        self.__home_score = 0
        self.__away_score = 0
        self.__referees = []
        self.__events = []

    """ Setter for main referee object """

    def set_main_referee(self, main_referee):

        Referee.type_check(main_referee)

        self.__main_referee = main_referee

    """ Setter for match time """

    def set_match_time(self, match_time):

        if type(match_time) is not date.datetime:
            raise TypeError

        self.__match_time = match_time

    """ Setter for game field """

    def set_field(self, field):

        if type(field) is not str:
            raise TypeError

        self.__field = field

    """ Setter for home team """

    def set_home_team(self, home_team):

        Team.type_check(home_team)

        self.__home_team = home_team

    """ Setter for away team """

    def set_away_team(self, away_team):

        Team.type_check(away_team)

        self.__away_team = away_team

    """ Getter for home team """

    def get_home_team(self):

        return self.__home_team

    """ Getter for away team """

    def get_away_team(self):

        return self.__away_team

    """ Getter for match time """

    def get_match_time(self):

        return self.__match_time

    """ Getter for Field """

    def get_field(self):

        return self.__field

    """ Getter for referees 
        This method returns 2 values:
        1. main referee
        2. referees list """

    def get_referees(self):

        return self.__main_referee, self.__referees

    """ Getter for Field """

    def get_score(self):

        return {
            'home': self.___home_score,
            'away': self.__away_score
        }

    """ This method adds a referee to the game """

    def add_referee(self, referee):

        Referee.type_check(referee)

        if referee in self.__referees or referee == self.__main_referee:
            raise ValueError

        self.__referees.append(referee)

    """ This method remove the given referee from the game """

    def remove_referee(self, referee):

        if referee in self.__referees:
            self.__referees.remove(referee)

    """ This method adds a game event to the event list """

    def add_event(self, event):

        GameEvent.type_check(event)

        self.__events.append(event)

    """ This method removes a game event from the event list """

    def remove_event(self, event):

        if event in self.__events:
            self.__events.remove(event)

    """ This method increase by 1 the home team score """

    def home_team_goal(self):

        self.___home_score += 1

    """ This method increase by 2 the home team score """

    def away_team_goal(self):

        self.__away_score += 1


def type_check(obj):
    if type(obj) is not Game:
        raise TypeError
