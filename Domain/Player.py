from abc import ABC

from Domain.Role import Role


class Player(Role):

    def __init__(self, role_name):
        super().__init__(role_name)
        pass

    def set_role_name(self):

        pass


def type_check(obj):
    if type(obj) is not Player:
        raise TypeError
