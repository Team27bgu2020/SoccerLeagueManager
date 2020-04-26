from abc import ABC

from Domain.Role import Role


class Player(Role):

    def __init__(self, assigned_by=None, position:  str = None, number=0):
        super().__init__(assigned_by)
        self.__position = position
        self.__number = number

    """  method to get position"""
    @property
    def position(self):
        return self.__position

    """  method to set position """

    @position.setter
    def position(self, position):
        self.__position = position

    """  method to get position"""

    @property
    def number(self):
        return self.__number

    """  method to set position """

    @number.setter
    def number(self, number):
        self.__number = number
