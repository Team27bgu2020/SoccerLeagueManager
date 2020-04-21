from enum import Enum


""" Enum for possible policies for assigning the stadium for the games """


class GameAssigningPolicies(Enum):
    RANDOM = 'Random'
    EQUAL_HOME_AWAY = 'Equal'


""" Enum for possible policies for assigning the stadium for the games """


class RefereeQualification(Enum):
    MAIN = 'Main'
    REGULAR = 'Regular'


def type_check(obj):

    if not issubclass(Enum, obj):
        raise TypeError


def referee_qualification_type_check(obj):

    if type(obj) is not RefereeQualification:
        raise TypeError


def game_assigning_policies_type_check(obj):
    if type(obj) is not GameAssigningPolicies:
        raise TypeError
