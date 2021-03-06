from Domain.SignedUser import SignedUser
from Enums.RefereeQualificationEnum import RefereeQualificationEnum
import copy
""" Dor """


class Referee(SignedUser):

    def __init__(self, qualification: RefereeQualificationEnum, user_name, password, name, birth_date, user_id):
        self.__events = []
        self.__referee_in_games = []
        self.qualification = qualification
        super().__init__(user_name, password, name, birth_date, user_id)

    """ This method adds new game """

    def add_game(self, game):

        if game in self.referee_in_games:
            raise ValueError('game is already tracked by this referee')

        self.__referee_in_games.append(game)

    """ This method removes game """

    def remove_game(self, game):
        if game in self.__referee_in_games:
            self.__referee_in_games.remove(game)
        else:
            raise ValueError('Game is not refereed by this referee')

    """ events getter """

    @property
    def events(self):
        return copy.copy(self.__events)

    """ games getter """

    @property
    def referee_in_games(self):
        return copy.copy(self.__referee_in_games)

    @referee_in_games.setter
    def referee_in_games(self, value):
        self.__referee_in_games = value

    @events.setter
    def events(self, value):
        self.__events = value

    """ This method adds new game event """

    def add_event(self, event):

        if event in self.__events:
            raise ValueError('event is already in this game')

        self.__events.append(event)

    """ This method removes game event """

    def remove_event(self, event):

        if event in self.__events:
            self.__events.remove(event)
        else:
            raise ValueError('event is not created by this referee')

    """ Getter for referee qualification """

    @property
    def qualification(self):

        return self.__qualification

    """ Setter for referee qualification """

    @qualification.setter
    def qualification(self, qualification: RefereeQualificationEnum):

        self.__qualification = qualification

