from Domain.SignedUser import SignedUser
from Enums.RefereeQualificationEnum import RefereeQualificationEnum
import copy
""" Dor """


class Referee(SignedUser):

    def __init__(self, qualification: RefereeQualificationEnum, user_name, password, name, birth_date, ip_address, user_id):
        self.__events = []
        self.__referee_in_games = []
        self.qualification = qualification
        super().__init__(user_name, password, name, birth_date, ip_address, user_id)

    """ This method adds new game """

    def add_game(self, game):

        self.__referee_in_games.append(game)

    """ This method removes game """

    def remove_game(self, game):
        if game in self.__referee_in_games:
            self.__referee_in_games.remove(game)

    """ events getter """

    @property
    def events(self):
        return copy.copy(self.__events)

    """ games getter """

    @property
    def referee_in_games(self):
        return copy.copy(self.__referee_in_games)

    """ This method adds new game event """

    def add_event(self, event):

        self.__events.append(event)

    """ This method removes game event """

    def remove_event(self, event):

        if event in self.__events:
            self.__events.remove(event)

    """ Getter for referee qualification """

    @property
    def qualification(self):

        return self.__qualification

    """ Setter for referee qualification """

    @qualification.setter
    def qualification(self, qualification: RefereeQualificationEnum):

        self.__qualification = qualification

    def show_games_by_referee(self):

        result = []
        for game in self.__referee_in_games:
            if (self in game.referees and not game.is_game_finished) or self == game.main_referee:
                result.append(game)
        return result

    def show_ongoing_games_by_referee(self):
        referee_games = self.show_games_by_referee()
        result = []
        for game in referee_games:
            if game.is_game_on:
                result.append(game)
        return result

