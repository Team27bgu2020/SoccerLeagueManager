from abc import ABC

from Domain.Role import Role


class Player(Role):

    def __init__(self, assigned_by=None, position:  str = None):
        super().__init__(assigned_by)
        self.__position = position

    """  method to set position """

    def set_position_name(self, position):
        self.__position = position

    """  method to get position"""

    def get_position_name(self):
        return self.__position


