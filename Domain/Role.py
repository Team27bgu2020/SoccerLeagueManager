from abc import ABC, abstractmethod


class Role(ABC):
    """ Default constructor for Role class"""

    def __init__(self, name):
        self.__role_name = name

    """ Abstract method to define role name"""

    def set_role_name(self, name):
        self.__role_name = name

    """ Abstract method to get role name"""

    def get_role_name(self):
        return self.__role_name

    """ Abstract method to string"""
    """need to be changed"""
    @abstractmethod
    def to_string(self):
        pass


def type_check(obj):
    if not issubclass(type(obj), Role):
        raise TypeError
