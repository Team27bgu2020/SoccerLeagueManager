from abc import ABC, abstractmethod


class Role(ABC):

    """ Default constructor for Role class"""
    def __init__(self):

        self.__role_name = ''

    """ Abstract method to define role name"""
    @abstractmethod
    def set_role_name(self):
        pass


def type_check(obj):

    if not issubclass(type(obj), Role):
        raise TypeError
