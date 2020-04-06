import datetime as date
from Domain.Referee import Referee
from Domain.Team import Team


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

        self._home_score = 0
        self._away_score = 0
        self._referees = []

    """ Setter for main referee object """

    def set_main_referee(self, main_referee):

        if type(main_referee) is not Referee:
            raise TypeError

        self._main_referee = main_referee

    """ Setter for match time """

    def set_match_time(self, match_time):

        if type(match_time) is not date.datetime:
            raise TypeError

        self._match_time = match_time

    """ Setter for game field """

    def set_field(self, field):

        if type(field) is not str:
            raise TypeError

        self._field = field

    """ Setter for home team """

    def set_home_team(self, home_team):

        if type(home_team) is not Team:
            raise TypeError

        self._home_team = home_team

    """ Setter for away team """

    def set_away_team(self, away_team):

        if type(away_team) is not Team:
            raise TypeError

        self._away_team = away_team

    """ Getter for home team """

    def get_home_team(self):

        return self._home_team

    """ Getter for away team """

    def get_away_team(self):

        return self._away_team

    """ Getter for match time """

    def get_match_time(self):

        return self._match_time

    """ Getter for Field """

    def get_field(self):

        return self._field

    """ Getter for referees 
        This method returns 2 values:
        1. main referee
        2. referees list """

    def get_referees(self):

        return self._main_referee, self._referees

    """ Getter for Field """

    def get_score(self):

        return {
                'home': self._home_score,
                'away': self._away_score
                }

    """ This method adds a referee to the game """

    def add_referee(self, referee):

        if type(referee) is not Referee:
            raise TypeError
        if referee in self._referees or referee == self._main_referee:
            raise ValueError

        self._referees.append(referee)

    """ This method remove the given referee from the game """

    def remove_referee(self, referee):

        if referee in self._referees:
            self._referees.remove(referee)

    """ This method increase by 1 the home team score """

    def home_team_goal(self):

        self._home_score += 1

    """ This method increase by 2 the home team score """

    def away_team_goal(self):

        self._away_score += 1
