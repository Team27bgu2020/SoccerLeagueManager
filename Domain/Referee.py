from Domain.ClassesTypeCheckImports import *
from Domain.SignedUser import SignedUser


""" Dor """


class Referee(SignedUser):

    def __init__(self, qualification):

        self.__events = []
        self.qualification = qualification

    """ This method adds new game event """

    def add_event(self, event):

        GameEvent.type_check(event)

        self.__events.append(event)

    """ Getter for referee qualification """

    @property
    def qualification(self):

        return self.__qualification

    """ Setter for referee qualification """

    @qualification.setter
    def qualification(self, qualification):

        Enums.referee_qualification_type_check(qualification)

        self.__qualification = qualification


def type_check(obj):

    if type(obj) is not Referee:
        raise TypeError
