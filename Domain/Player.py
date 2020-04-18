from abc import ABC

from Domain.Role import Role


class Player(Role):

    def __init__(self):

        pass

    def set_role_name(self):

        pass


def type_check(obj):
    if type(obj) is not Player:
        raise TypeError