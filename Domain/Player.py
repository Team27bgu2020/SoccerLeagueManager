from abc import ABC

from Domain.Role import Role


class Player(Role):

    def __init__(self, position):
        super().__init__("Player")
        self.__position = position

    """  method to set position """

    def set_position_name(self, position):
        self.__position = position

    """  method to get position"""

    def get_position_name(self):
        return self.__position

    def to_string(self):
        print("I am a " + self.get_role_name(), "playing as " + self.get_position_name())


def type_check(obj):
    if type(obj) is not Player:
        raise TypeError
