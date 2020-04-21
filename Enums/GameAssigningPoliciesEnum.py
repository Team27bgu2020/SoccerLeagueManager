from enum import Enum


""" Enum for possible policies for assigning the stadium for the games """


class GameAssigningPoliciesEnum(Enum):
    RANDOM = 'Random'
    EQUAL_HOME_AWAY = 'Equal'


def type_check(obj):

    if not isinstance(obj, GameAssigningPoliciesEnum):
        raise TypeError