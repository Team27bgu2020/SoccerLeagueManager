from abc import ABC


class Role(ABC):

    """ Default constructor for Role class """

    def __init__(self, name):
        self.__role_name = name

    """ Abstract method to define role name """

    def set_role_name(self, name):
        self.__role_name = name

    """ Abstract method to get role name """

    def get_role_name(self):
        return self.__role_name


def type_check(obj):
    if not issubclass(type(obj), Role):
        raise TypeError
